import time
import requests

from PySide6 import QtCore
from PySide6.QtCore import Signal

from networking import mb_query
from networking.ms_query import get_server_list, query_ms_rooms

from ll_info import http_headers, version_check_url

class QueryLiquid(QtCore.QThread):
    # Emit latest version string for callback
    check_version_cb_sig = Signal(str)
    load_news_cb_sig = Signal(str, bool)
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
                    self.load_news_cb_sig.emit(feed_parsed, False)
                except Exception as e:
                    print("News fetch error: ",e)
                    self.load_news_cb_sig.emit(str(e), True)
                self.query_news = False
            if self.query_version:
                print("check_version")
                #link = "https://api.github.com/repos/liquidunderground/liquidlauncher/releases/latest"
                
                try:
                    f = requests.get(version_check_url, headers=http_headers, timeout=10).json()
                    feed.raise_for_status()

                    latest_version = f["tag_name"]
                    print("Latest: " + latest_version)
                    print("Current: " + self.versionString)
                    self.check_version_cb_sig.emit(latest_version)

                except Exception as e:
                    print("Version check error: ",e)
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
                    res = requests.post(self.snitch_dest.rstrip("/")+"/liquidms/snitch", headers=http_headers, files=snitch_csv_obj) # Pass CSV to Snitch API
                    res.raise_for_status()
                    self.update_snitchmsg_sig.emit('Successfully snitched {} to {}.  Thank you.'.format(self.snitch_src, self.snitch_dest))
                except Exception as e:
                    print('Snitch error: {}\n'.format(e))
                    self.update_snitchmsg_sig.emit('Snitch error: {}'.format(e))
                self.snitch = False                    
            time.sleep(1)

class QueryMessageBoard(QtCore.QThread):
    # Emits a string describing the mod
    mod_description_sig1 = Signal(object)
    # Emits a list of mods
    mod_list_sig1 = Signal(dict, str)
    mod_statmsg_sig1 = Signal(str)

    def __init__(self, host, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.mod = None
        self.get_mod_description = False
        self.get_mods = False
        self.mods_type = None
        self.host = host

    def on_request_mod_list(self, mods_type):
        print("on_request_mod_list({})".format(mods_type))
        self.get_mods = True
        self.mods_type = mods_type

    def on_request_mod_desc(self, mod):
        print("on_request_mod_desc")
        self.mod = mod

    def run(self):
        self.running = True
        while self.running:
            if self.get_mods:
                url = None
                mods = []
                modsources = []

                # Compose mod sources
                if self.host.global_settings["modsources"]["srb2mb"]:
                   modsources.append( mb_query.srb2mb )
                if self.host.global_settings["modsources"]["workshop_blue"]:
                   modsources.append( mb_query.workshop_blue )
                if self.host.global_settings["modsources"]["workshop_red"]:
                   modsources.append( mb_query.workshop_red )
                # Stubbed for future implementation
                #if self.host.global_settings["modsources"]["wadarchive"]:
                   #modsources.append( mb_query.wadarchive )
                if self.host.global_settings["modsources"]["skybase"]:
                   modsources.append( mb_query.skybase )
                if self.host.global_settings["modsources"]["gamebanana"]:
                   modsources.append( mb_query.gamebanana )

                for src in modsources:
                    if self.mods_type == "Maps":
                        url = src["maps"]
                    if self.mods_type == "Characters":
                        url = src["characters"]
                    if self.mods_type == "Lua":
                        url = src["lua"]
                    if self.mods_type == "Assets":
                        url = src["assets"]
                    if self.mods_type == "Misc":
                        url = src["misc"]
                    print("Querying forum {}".format(url))
                    self.mod_statmsg_sig1.emit("Querying {}".format(src["main"]))
                    try:
                        querybuf = mb_query.get_mods(url, src)
                        #mods = mods + mb_query.get_mods(url, src)
                        mods = mods + querybuf
                        for mod in querybuf:
                            self.mod_list_sig1.emit({mod.name: mod}, src["icon"])
                    except Exception as e:
                        print("Unable to get query modsource: {}".format(e))

                # Reset variables
                self.get_mods = False
                self.mods_type = None

            if self.mod:
                self.mod.get_description()
                self.mod_description_sig1.emit(self.mod)

                # Reset variables
                self.mod = None

            time.sleep(1)


class QueryMasterServer(QtCore.QThread):
    server_list_sig1 = Signal(list)
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
                server_list = get_server_list(
                    self.host.global_settings["current_ms"]["url"],
                    self.host.global_settings["current_ms"]["api"]
                    )
                self.server_list_sig1.emit(server_list)
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
                filepath = mb_query.download_mod(self.filepath, self.download_url)
                # Extract files, get wads/pk3/etc to add.

                self.mod_filepath_sig1.emit([filepath])
                self.download_url = None
                self.filepath = None
            time.sleep(1)
