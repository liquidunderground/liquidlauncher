import time
import requests
import os

from PySide6 import QtCore
from PySide6.QtCore import Signal

from packaging import version # for version checks

from networking import modsource
from networking.ms_query import Netgame
from networking.ms_query import get_server_list, query_ms_rooms

from parse import *

from packaging import version # for version checks

from ll_info import http_headers, version_check_url

class QueryLiquid(QtCore.QThread):
    # Emit latest version string for callback
    check_version_cb_sig = Signal(object)
    load_news_cb_sig = Signal(object)
    update_snitchmsg_sig = Signal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.query_news = False
        self.query_version = False
        self.snitch = False
        self.versionString = "v0.0a0"
        self.currentFeed = ""
        self.snitch_src = ""
        self.snitch_dest = ""
        print("QueryLiquid worker INIT\n")
        
    def on_check_version(self, versionString):
        print("on_check_version")
        self.versionString = versionString
        self.query_version = True

    def on_load_rss(self, feed):
        print("on_load_rss")
        self.currentFeed = feed
        self.query_news = True

    def on_snitch(self, src, dest):
        print('on_snitch({}, {})'.format(src, dest))
        self.snitch_src = src["url"]
        self.snitch_src_api = src["api"]
        self.snitch_dest = dest
        self.snitch = True

    def run(self):
        self.running = True
        while self.running:
            if self.query_news:
                print("query_news")
                try:
                    feed = requests.get(self.currentFeed, headers=http_headers)
                    feed.raise_for_status()
                    feed_parsed = feed.text
                    #print("FETCH RESULT: {}\n".format(feed_parsed))
                    #self.load_news_cb_sig.emit(feed_parsed, False)
                    alertArgs = {
                        "type" : "info",
                        "title" : f"RSS Fetch successful",
                        "message" :  "News feed successfully loaded." if len(feed_parsed) > 0  else  "No news found. Did you check the URL?",
                        "content": feed_parsed,
                    }
                    self.load_news_cb_sig.emit(alertArgs)
                except Exception as e:
                    print("News fetch error: ",e)
                    alertArgs = {
                        "type" : "warning",
                        "title" : f"Query Error ",
                        "message" : f'Unable to query <a href="{self.currentFeed}">{self.currentFeed}</a>',
                        "detailedText" : str(e),
                    }
                    self.load_news_cb_sig.emit(alertArgs)
                    #self.load_news_cb_sig.emit(str(e), True)
                self.query_news = False
            if self.query_version:
                print("check_version")
                
                latest = None

                for version_check_src in version_check_url:
                    print("Checking for updates at " + version_check_src + "...")

                    try:
                        f = requests.get(version_check_src, headers=http_headers, timeout=10).json()
                        feed.raise_for_status()

                        found = {
                            "url": version_check_src,
                            "version": f["tag_name"]
                        }
                        print("Found: " + found["version"])
                        print("Current: " + self.versionString)

                        if latest == None or version.parse(found["version"]) > version.parse(latest["version"]):
                            latest = found
                        
                        print("Latest: " + found["version"])

                    except Exception as e:
                        print("Version check error: ",e)

                self.check_version_cb_sig.emit(latest)

                self.query_version = False
            if self.snitch:
                #server_list = get_server_list(ms_url, "v1")
                # TODO: Pass API from user config
                try:
                    print('Snitching "{}" to "{}"'.format(self.snitch_src, self.snitch_dest))
                    if self.snitch_src == None:
                        raise Exception("Source URL not given. Please select a source.")
                    if self.snitch_dest == "":
                        raise Exception("Destination URL not given. Please select a source.")
                    print('Fetching "{}"...\n'.format(self.snitch_src))
                    self.update_snitchmsg_sig.emit('Fetching "{}"...'.format(self.snitch_src))
                    fetch = get_server_list(
                        self.snitch_src,
                        self.snitch_src_api
                        )
                    # Parse fetch into CSV
                    snitch_csv_txt = ""
                    for line in fetch:
                        # CSV-compliant quote escaping
                        tmp_ip = line['ip'].replace('"','""')
                        tmp_port = line['port'].replace('"','""')
                        tmp_name = line['name'].replace('"','""')
                        tmp_version = line['version'].replace('"','""')
                        tmp_room = line['room'].replace('"','""')
                        tmp_origin = line['origin'].replace('"','""')
                        snitch_csv_txt += '{ip},{port},{name},{version},{room},{origin}\n'.format(
                            # Escape fields with quotes, according to CSV
                            ip=tmp_ip if "," not in tmp_ip else "\"{}\"".format(tmp_ip),
                            port=tmp_port if "," not in tmp_port else "\"{}\"".format(tmp_port),
                            name=tmp_name if "," not in tmp_name else "\"{}\"".format(tmp_name),
                            version=tmp_version if "," not in tmp_version else "\"{}\"".format(tmp_version),
                            room=tmp_room if "," not in tmp_room else "\"{}\"".format(tmp_room),
                            origin=tmp_origin if "," not in tmp_origin else "\"{}\"".format(tmp_origin)
                        )
                    print('Snitching to "{}"...\n'.format(self.snitch_dest))
                    self.update_snitchmsg_sig.emit('Snitching to "{}"...'.format(self.snitch_dest))
                    snitch_csv_obj = {"file": ('snitch.csv', snitch_csv_txt) }
                    res = requests.post(self.snitch_dest.rstrip("/"), headers=http_headers, files=snitch_csv_obj) # Pass CSV to Snitch API
                    res.raise_for_status()
                    self.update_snitchmsg_sig.emit('Successfully snitched {} to {}.  Thank you.'.format(self.snitch_src, self.snitch_dest))
                except Exception as e:
                    print('Snitch error: {}\n'.format(e))
                    self.update_snitchmsg_sig.emit('Snitch error: {}'.format(e))
                self.snitch = False                    
            time.sleep(1)

class QueryMasterServer(QtCore.QThread):
    server_list_sig1 = Signal(list)
    server_list_sig2 = Signal(object)
    on_ms_rooms_sig = Signal(object)

    def __init__(self, host, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.query_ms = False
        self.query_ms_rooms = False
        self.hostMsUrl = "about:blank"
        self.running = True
        self.host = host
    
    def on_refresh(self):
        """Refresh button clicked
        """
        self.query_ms = True

    def on_query_ms_rooms(self, url):
        self.hostMsUrl = url
        self.query_ms_rooms = True
        
    def on_quit(self):
        self.running = False
        
    def run(self):
        while self.running:
            if self.query_ms:
                #server_list = get_server_list(ms_url, "v1")
                # TODO: Pass API from user config
                print("QThread.current_ms = ", self.host.global_settings["current_ms"])
                try:
                    server_list = get_server_list(
                        self.host.global_settings["current_ms"]["url"].rstrip(),
                        self.host.global_settings["current_ms"]["api"]
                        )
                    print("Successfully queried {}\n".format(self.host.global_settings["current_ms"]["url"]))
                    alertArgs = {
                        "type" : "info",
                        "title" : f"Query successful",
                        "message" : f"Successfully queried {self.host.global_settings['current_ms']['url']}",
                    }
                    self.server_list_sig2.emit(alertArgs)
                    self.server_list_sig1.emit(server_list)
                except Exception as e:
                    print("Query error: {}\n".format(e))
                    #self.server_list_sig2.emit("Query error: {}".format(e))
                    alertArgs = {
                        "type" : "warning",
                        "title" : f"Query Error ",
                        "message" : "Unable to query " \
                            f"{self.host.global_settings['current_ms']['url']} -" \
                            "Check details to see the exact error message.",
                        "detailedText" : str(e),
                    }
                    self.server_list_sig2.emit(alertArgs)
                    self.server_list_sig1.emit({})
                self.query_ms = False                    
            if self.query_ms_rooms:
                print("QThread.masterserver = ", self.host.global_settings["current_ms"])
                try:
                    rooms = query_ms_rooms(self.hostMsUrl)
                except Exception as e:
                    rooms = {}
                print("Queried rooms: {}".format(rooms) )
                self.on_ms_rooms_sig.emit(rooms)
                self.query_ms_rooms = False                    
            time.sleep(1)


class ModDownloader(QtCore.QThread):
    mod_filepath_sig1 = Signal(list)
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.download_url = None
        self.filepath = None
        self.running = True
        
    def on_download_button(self, download_url):
        self.download_url = download_url
        print("ModDownloader.download_url = ", self.download_url)
        
    def on_filepath_emit(self, filepath):
        self.filepath = filepath
        print("ModDownloader.filepath = ", self.filepath)

    def run(self):
        print("ModDownloader.download_url = ", self.download_url)
        print("ModDownloader.filepath = ", self.filepath)
        while self.running:
            if self.download_url and self.filepath:
                filepath = modsource.download_mod(self.filepath, self.download_url)
                # Extract files, get wads/pk3/etc to add.

                self.mod_filepath_sig1.emit([filepath])
                self.download_url = None
                self.filepath = None
            time.sleep(1)


class LqSignals(QtCore.QObject):
    """Global signals dict to keep things simple
    Treat Qt signals as essentially a global publisher-subscriber bus
    """
    
    # Launcher version
    version_check_finish = Signal(object)
    news_load_finish = Signal(object)
    snitchmsg_update = Signal(str)
    
    # MS server listings
    server_list_sig2 = Signal(object)
    on_ms_rooms_sig = Signal(object)
    
    # Mod browser
    ### Emits a string describing the mod
    mod_description_sig1 = Signal(object)
    ### Emits a list of mods
    mod_list_fetch_finish = Signal(object)
    mod_list_sig1 = Signal(dict, str)
    mod_statmsg_sig1 = Signal(str)
    # Mod downoader
    mod_download_finish = Signal(object, str)
    
    # Netgames
    netgame_update_finish = Signal(list)    # Emits List of Netgames to update
    netgame_list_fetch_finish = Signal(list)    # Emits new List of Netgames

    # Alert
    alert = Signal(object)

ll_signalbus = LqSignals()


class CheckLauncherversionThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus
    
    def __init__(self, current_version):
        super(CheckLauncherversionThread, self).__init__()
        self.current_version = current_version

    def run(self):

        latest = None

        # === Find latest versions across all version check sources === #
        for version_check_src in version_check_url:
            print("[CheckLauncherversionThread] Checking for updates at " + version_check_src + "...")

            try:
               f = requests.get(version_check_src, headers=http_headers, timeout=10)
               f.raise_for_status()

               # All fine -> just get the JSON data
               f = f.json()

               found = {
                   "url": version_check_src,
                   "version": f["tag_name"]
               }
               print("[CheckLauncherversionThread] Found: " + found["version"])
               print("[CheckLauncherversionThread] Current: " + self.current_version)

               if latest == None or version.parse(found["version"]) > version.parse(latest["version"]):
                   latest = found
                
               print("[CheckLauncherversionThread] Latest version: " + found["version"])

            except Exception as e:
               print("[CheckLauncherversionThread] Version check error: ",e)

        # === Check latest launcher version against current === #
        if version.parse(latest["version"]) > version.parse(self.current_version):
            alertArgs = {
               "type" : "question",
               "title" : f"Version {latest["version"]} available",
               "message" : f"Your version of LiquidLauncher seems to be " \
                           f"outdated. Please download <a href=\"{latest["url"]}\"> version {latest["version"]}</a>.",
               "detailedText" : f"Latest version of LiquidLauncher: " \
                   f"{latest["version"]}\nYou are currently running: " \
                   f"{self.current_version}",
            }
            self.signalbus.alert.emit(alertArgs)
        elif version.parse(latest["version"]) < version.parse(self.current_version):
            print("Greetings, time traveller.")
            alertArgs = {
               "type" : "info",
               "title" : "Greetings, time traveller.",
               "message" : f"<p>You seem to be using an in-development " \
                   "version of LiquidLauncher. Please note that some things " \
                   "might not be finished yet.</p><p>If you'd like to use our current release " \
                   f"version {latest["version"]},  please check " \
                   f'our <a href=\"{latest["url"]}\">repository</a>.</p>',
            }
            self.signalbus.alert.emit(alertArgs)
        else:
            print("[CheckLauncherversionThread] up-to-date (" + self.current_version + ")")

class QueryRSSThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus
    
    def __init__(self, url):
        super(QueryRSSThread, self).__init__()
        self.url = url

    def run(self):
        print(f"[QueryRSSThread]: Querying RSS feed {self.url}")
        try:
            feed = requests.get(self.url, headers=http_headers)
            feed.raise_for_status()
            feed_parsed = feed.text

            news = feedparser.parse(feed_parsed)["items"]

            self.signalbus.news_load_finish.emit(news)

            alertArgs = {
                "type" : "info",
                "title" : f"RSS Fetch successful",
                "message" :  "News feed successfully loaded." if len(feed_parsed) > 0  else  "No news found. Did you check the URL?",
            }
            self.signalbus.alert.emit(alertArgs)
        except Exception as e:
            print("News fetch error: ",e)
            alertArgs = {
                "type" : "warning",
                "title" : f"Query Error ",
                "message" : f'Unable to query <a href="{self.url}">{self.url}</a>',
                "detailedText" : str(e),
            }
            self.signalbus.alert.emit(alertArgs)

"""Types of netgame/master server-related threads:
1. NetgameThread: Queries individual netgames for live metadata through their UDP protocol
2. NetgameListThread: Retrieves lists of netgames from a Master Server
3. NetgameRoomlistThread: Retrieves the rooms of room-based Master Server protocols
"""

class NetgameThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus

    def __init__(self, netgames:list):
        super(NetgameThread,self).__init__()

        
        self.netgames = netgames
        print(f"Created thread for netgames {self.netgames}")
        
    @QtCore.Slot()
    def run(self):
        print(f"Running thread on netgames {self.netgames}")
        for netgame in self.netgames:
            print(f"[NETGAMETHREAD] querying {netgame}...")
            netgame.query()
            ll_signalbus.netgame_update_finish.emit([netgame])
        

class NetgameListThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus

    def __init__(self, ms_url, ms_api):
        super(NetgameListThread,self).__init__()
        self.ms_url = ms_url
        self.ms_api = ms_api
        
    @QtCore.Slot()
    def run(self):
        print(f"Running query thread for {self.ms_url} (API: {self.ms_api})")
        if self.query_ms:
            try:
                server_list = get_server_list(
                    self.ms_url.rstrip(),
                    self.ms_api
                    )
                print(f"Successfully queried {self.ms_url}\n")
                alertArgs = {
                    "type" : "info",
                    "title" : f"Query successful",
                    "message" : f"Successfully queried {self.ms_url}",
                }
                self.signalbus.alert.emit(alertArgs)
                self.signalbus.netgame_list_fetch_finish.emit(server_list)
            except Exception as e:
                print("Query error: {}\n".format(e))
                #self.server_list_sig2.emit("Query error: {}".format(e))
                alertArgs = {
                    "type" : "warning",
                    "title" : f"Query Error ",
                    "message" : "Unable to query " \
                        f"{self.ms_url} -" \
                        "Check details to see the exact error message.",
                    "detailedText" : str(e),
                }
                self.signalbus.alert.emit(alertArgs)
                self.signalbus.netgame_list_fetch_finish.emit({})
            self.query_ms = False                    
        if self.query_ms_rooms:
            print("QThread.masterserver = ", self.host.global_settings["current_ms"])
            try:
                rooms = query_ms_rooms(self.hostMsUrl)
            except Exception as e:
                rooms = {}
            print("Queried rooms: {}".format(rooms) )
            self.on_ms_rooms_sig.emit(rooms)


class ModDownloaderThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus
    
    def __init__(self, mods=[], dest=None):
        super(ModDownloaderThread, self).__init__()

        self.mods = mods
        self.dest = dest

    @QtCore.Slot()
    def run(self):
        print(f"ModDownloaderThread launched:\n\tdestination: {self.dest}\n\tmods: {self.mods}")
        if self.dest:
            for mod in self.mods:
                #mod.download(self.dest)    # GAH old! We'll download it ourselves!

                print(f"[ModDownloaderThread]: Processing mod URL {mod}")
                
                # Guarantee destination folder
                if not os.path.isdir(self.dest):
                    os.makedirs(self.dest)
                    
                # NOTE the stream=True parameter below
                with requests.get(mod, stream=True) as r:
                    r.raise_for_status()
                    # Safeguard in case there's no "Content-Disposition" header
                    print("[ModDownloaderThread]: ",r.headers)

                    filepath = f"{self.dest.rstrip('/')}/{mod.rstrip('/').split('/')[-1]}"
                    
                    if "Content-Disposition" in r.headers.keys():
                        #filepath = '{}/{}'.format(    base_path.rstrip('/'), parse('attachment; filename="{file}"',   r.headers["Content-Disposition"])["file"]    )
                        #filepath = base_path.rstrip('/')+download_url.split('/')[-3]
                        
                        filepath = f"{self.dest.rstrip('/')}/{parse('attachment; filename="{file}"',r.headers["Content-Disposition"])["file"]}"
                    
                    print("Proceeding to download file ", mod,  "into", filepath)

                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            #if chunk:
                            f.write(chunk)

                self.signalbus.mod_download_finish.emit(mod,self.dest)


"""There are two kinds of "searching" mods:
1. Text search/search(text, page): Query a ModSource's "search" endpoints for mods matching a string
2. Category browsing/browse(category, page): Each ModSource contains a string-indexed
   collection "self.categories". When a category matches, it's data is queried and returned.

Pagination support depends on the *ModSource implementation.
"""

class ModTextsearchThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus
    
    def __init__(self, modsource=None, searchtext=None, page=0, num=50):
        super(ModTextsearchThread, self).__init__()
        
        if type(searchtext) is not str:
            raise

        self.modsource = modsource
        self.searchtext = searchtext
        self.page = page
        self.num = num

    @QtCore.Slot()
    def run(self):
        res = self.modsource.search(self.searchtext, self.page, self.num)
        self.signalbus.mod_list_fetch_finish.emit(res)


class ModCategorybrowseThread(QtCore.QRunnable):
    
    signalbus = ll_signalbus
    
    def __init__(self, modsource, category, page=0):
        super(ModCategorybrowseThread, self).__init__()
        
        self.modsource = modsource
        self.category = category
        self.page = page

    def run(self):

        if "categories" in self.modsource.__dict__.keys() and self.category in self.modsource.categories.keys():
            
            url = self.modsource.categories[self.category]

            print("Querying forum {}".format(url.format(pagenum=self.page)))

            mods = self.modsource.browse(category=self.category,page=self.page,num=50)
            
            self.signalbus.mod_list_fetch_finish.emit(mods)
