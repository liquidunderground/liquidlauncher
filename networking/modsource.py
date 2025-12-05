import os
from lxml import html
from parse import *
import requests
import hashlib

from ll_info import http_headers

## Original MB values
srb2mb = {
    "main_url": "https://mb.srb2.org",
    "search_link": "https://mb.srb2.org/search/search",
    "search_link_iterator": "https://mb.srb2.org/search/{id}?page={pagenum}",
    "search_response_pattern": "https://mb.srb2.org/search/{id}",
    "resource_path": "/addons",
    "categories": {
        "Maps": "https://mb.srb2.org/addons/categories/maps.4?page={pagenum}",
        "Characters": "https://mb.srb2.org/addons/categories/characters.5?page={pagenum}",
        "Lua": "https://mb.srb2.org/addons/categories/lua.7?page={pagenum}",
        "Misc": "https://mb.srb2.org/addons/categories/miscellaneous.8?page={pagenum}",
        "Assets": "https://mb.srb2.org/addons/categories/assets.6?page={pagenum}",
    },
    "thread_link": "/addons/{thread}",
    "thread": "https://mb.srb2.org/addons/{thread}",
    "download": "https://mb.srb2.org/addons/{thread}download",
    "icon": "srb2mb",
    "vendor": "stjr"
}

## Workshop for testing
workshop_blue = {
    "main_url": "https://srb2workshop.org",
    "search_link": "https://srb2workshop.org/search/search",
    "search_link_iterator": "https://srb2workshop.org/search/{id}?page={pagenum}",
    "search_response_pattern": "https://srb2workshop.org/search/{id}",
    "search_link": "https://srb2workshop.org/search/{id}",
    "resource_path": "/resources",
    "categories":{
        "Maps": "https://srb2workshop.org/resources/categories/maps.3?page={pagenum}",
        "Characters": "https://srb2workshop.org/resources/categories/characters.19?page={pagenum}",
        "Lua": "https://srb2workshop.org/resources/categories/lua.6?page={pagenum}",
        "Misc": "https://srb2workshop.org/resources/categories/miscellaneous.7?page={pagenum}",
        "Assets": "https://srb2workshop.org/resources/categories/assets.16?page={pagenum}",
    },
    "thread_link": "/resources/{thread}",
    "thread": "https://srb2workshop.org/resources/{thread}/",
    "download": "https://srb2workshop.org/resources/{thread}download",
    "icon": "wsblue",
    "vendor": "workshop"
}

workshop_red = {
    "main_url": "https://srb2workshop.org",
    "search_link": "https://srb2workshop.org/search/search",
    "search_link_iterator": "https://srb2workshop.org/search/{id}?page={pagenum}",
    "search_response_pattern": "https://srb2workshop.org/search/{id}",
    "search_link": "https://srb2workshop.org/search/{id}",
    "resource_path": "/resources",
    "categories":{
        "Maps": "https://srb2workshop.org/resources/categories/maps.11?page={pagenum}",
        "Characters": "https://srb2workshop.org/resources/categories/characters.13?page={pagenum}",
        "Lua": "https://srb2workshop.org/resources/categories/lua.12?page={pagenum}",
        "Misc": "https://srb2workshop.org/resources/categories/miscellaneous.30?page={pagenum}",
        "Assets": "https://srb2workshop.org/resources/categories/assets.26?page={pagenum}",
    },
    "thread_link": "/resources/{thread}",
    "thread": "https://srb2workshop.org/resources/{thread}",
    "download": "https://srb2workshop.org/resources/{thread}download",
    "icon": "wsred",
    "vendor": "workshop"
}

skybase = {
    "main_url": "https://srb2skybase.org/mb",
    "categories": {
        "Maps": "https://srb2skybase.org/mb/forumdisplay.php?f=149&page={pagenum}",
        "Characters": "https://srb2skybase.org/mb/forumdisplay.php?f=150&page={pagenum}",
        "Misc": "https://srb2skybase.org/mb/forumdisplay.php?f=151&page={pagenum}",
    },
    "thread": "https://srb2skybase.org/mb/{thread}",
    "download": "https://srb2skybase.org/mb/attachment.php?attachmentid={mod}",
    "icon": "skybase",
    "vendor": "skybase"
}

gamebanana = {
    # Useful reference links
    "main": "https://gamebanana.com",
    # gameid 6786 == SRB2
    "search_url": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_sName={query}&_nPage={pagenum}&_csvModelInclusions=Mod",
    "download": "https://gamebanana.com/apiv11/Mod/{id}?_csvProperties=_aFiles",
    "icon": "gamebanana",
    "vendor": "gamebanana"
}


# Oh so sneaky:
headers =  {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'}

# ===========================================
#
#   NEW ARCHITECTURE: Modsource classes
#
# ===========================================
#
# 1. ModSource is a quasi-virtual class from which other mod sources inherit.
# 2. Mod sources are forked off by API type and instances can be filled with appropriate API endpoints
# 3. Mod sources are mainly responsible for finding and displaying mods from their respective repositories
# 4. Depending on the API, some data may be missing from the results
#
#

class ModSource():
    def __new__(cls, *args, **kwargs):
        if cls is ModSource:
            # "Virtual" Class
            raise
        return object.__new__(cls)

    def browse(self, category, page=0, num=0):
        """Retrieves a list of mods from specific directories ("categories") within a ModSource
        """
        return []

    def search(self, text, page=0, num=0):
        """Retrieves a list of mods from the ModSource matching the search string 'text'
        """
        return []

    def show(self, text):
        """Passes/displays the mod's repository page
        """
        pass

class GamebananaModSource(ModSource):
    """
    ModSource for the Gamebanana API
    """

    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}
        pass

    def search(self, text, page=0, num=0):

        out = []

        response = requests.get(self.search_url.format(query=text, pagenum=page),
                                stream=True,
                                headers=http_headers)

        # Thankfully Gamebanana has an actual API
        api_data = response.json()["_aRecords"]
        
        for el in api_data:

            # Pull download link out of separate API call, ugh
            download_resolv = requests.get(self.download.format(id=el["_idRow"]),
                                            stream=True,
                                            headers=http_headers)

            # One mod may have multiple downloads (e.g. older versions)
            downloads = [ x["_sDownloadUrl"] for x in download_resolv.json()["_aFiles"] ]

            print(f"[GamebananaModSource] Download links for {el["_sName"]} ({el["_idRow"]}): {downloads}")

            out.append(Mod(
                    name=el["_sName"], 
                    ext_url=el["_sProfileUrl"],
                    download_urls=downloads,
                    icon=self.icon,
                ))

        return out
            
    def show(self, text):
        pass

class NetgameModSource(ModSource):
    """
    This mod source queries all netgames passed into it's constructor
    It locally searches the filenames given in the netgame's filesneeded entries.
    It cannot display mod pages. (It may try to pass the httpsource URL instead)
    It will download from the netgames' given httpsource
    """
    def __init__(self, netgames=[]):
        self.netgames = netgames
        pass

    def search(self, text, page=0, num=0):
        # "page" and "num" are ignored
        out = []

        for ng in self.netgames:
            ng_files = ng.get("filesneeded")
            httpsource = ng.get("httpsource")

            if ng_files != None and httpsource != None and httpsource != "":
                # Append mod list entries from netgames' neededfiles

                out += [Mod(
                    name=f"{f["filename"]} @ {httpsource.rstrip('/')}/",
                    ext_url=httpsource,
                    download_urls=[f"{httpsource.rstrip('/')}/{f["filename"]}"],
                    icon="server"
                ) for f in ng_files if int.from_bytes(f["md5sum"], "big") and text.lower() in f["filename"].lower()]

        return out
            
    def show(self, text):
        pass

class VbulletinModSource(ModSource):
    """
    ModSource for vBulletin-based forums (e.g. SRB2 Skybase)
    """
    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}
        pass

    def browse(self, category, page=0, num=0):

        out = []

        # Failsafe existence check
        if "categories" in self.__dict__.keys() and category in self.categories.keys():
            

            print(f"[VbulletinModSource] Browsing {self.categories[category].format(pagenum=page)}" )

            response = requests.get(self.categories[category].format(pagenum=page),
                                stream=True,
                                headers=http_headers)
            response.raw.decode_content = True
            tree = html.parse(response.raw)
                
            current_mod_elements = tree.xpath('.//*[@class="threadtitle"]/*[@class="title"]')
            for el in current_mod_elements:
                # Get current link
                el_href = el.xpath('./@href')[0]
                # Get current text
                el_text = el.xpath('./text()')[0]

                print(f'[VbulletinModSource] URL for "{el_text}: {self.thread.format(thread=el_href)}"')

                # TODO: Resolve mod download array
                out.append(Mod(
                        name=el_text, 
                        ext_url=self.thread.format(thread=el_href),
                        download_urls=[],
                        icon=self.icon,
                ))
            
            print("[VbulletinModSource] Fetched mods:", out )
        return out
       
class XenforoModSource(ModSource):
    """
    ModSource for Xenforo-based forums (e.g. SRB2 Message Board)
    """

    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}
        pass

    
    def browse(self, category, page=0, num=0):
        out = []

        # Failsafe existence check
        if "categories" in self.__dict__.keys() and category in self.categories.keys():
            
            response = requests.get(self.categories[category].format(pagenum=page),
                                    stream=True,
                                    headers=headers)
            response.raw.decode_content = True
            tree = html.parse(response.raw)

            # Get Elements; sort our href an text later
            mod_elements = tree.xpath('.//div[@class="structItem-title"]/*[@data-tp-primary="on"]')
            # Filter out mod names using templates
            for el in mod_elements:
                # Get current text
                el_text = el.xpath('./text()')[0]
                # Get current link
                el_href = el.xpath('./@href')[0]
                el_href_relative = '/'.join(el_href.split('/')[2:])

                print(f'Relative Path for "{el_text}: {el_href_relative}"')

                # TODO: Resolve mod download array
                out.append(Mod(
                        name=el_text, 
                        ext_url=self.thread.format(thread=el_href_relative),
                        download_urls=[self.download.format(thread=el_href_relative)],
                        icon=self.icon,
                    ))

        print("Fetched mods: ", out )

        return out



    def search(self, text, page=0, num=0):
        """
        Queries a XenForo search page, then filters out the needed info using XPath
        """

        headers =  {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'}
        
        out = []
                
        """
        XenForo indexes searches. If we ain't got an ID, we'll get one.
        """
        
        if "search_id" not in self.__dict__.keys():

            print(f"[XenforoModSource]: Request Headers = {http_headers}")
            
            # Get XSRF token to request a valid search
            mainpage_request = requests.get(self.main_url, stream=True, headers=headers)
            mainpage_tree = html.parse(mainpage_request.raw)
            xf_token = mainpage_tree.xpath('.//form[@action="/search/search"]//input[@name="_xfToken"]/@value')

            response = requests.post(self.search_link,
                                    data={"keywords": text, "c[users]": "", "_xfToken": xf_token},
                                    cookies=mainpage_request.cookies,
                                    stream=True,
                                    headers=http_headers)

            print(f"[XenforoModSource]: Response Headers from {self.search_link} = {response.headers}")
            #self.search_id = parse(self.search_response_pattern,response.url)["id"]
            self.search_id = parse(self.search_response_pattern,response.headers["location"])["id"]
            print(f"[XenforoModSource]: set search ID {self.search_id} for {self.main} ({response.url})")

        response = requests.get(self.search_link_iterator.format(id=self.search_id, pagenum=page),
                                stream=True,
                                #headers=http_headers)
                                headers=headers)
        
        response.raw.decode_content = True
        tree = html.parse(response.raw)
        
        # Filter out mod thread links now; pick apart for metadata later
        current_mod_elements = tree.xpath(f'.//*[@class="contentRow-title"]/a[contains(@href,"{self.resource_path}")]')
        for el in current_mod_elements:
            # Now is later
            # Get current link
            #el_href = el.xpath('./@href')[0]
            el_href = '/'.join(el.xpath('./@href')[0].split('/')[:2])
            el_href = '/'.join(el.xpath('./@href')[0].split('/')[:2])
            el_thread_num = re.match(r'\/addons\/.*\.([0-9]+)', el_href).group(1)
            # Get current text
            el_text = el.xpath('./text()')[0]
            """
            out.append({
                    "name": el_text, 
                    "link": parse(modsource["thread_link"],el_href)["thread"]
                    })
            """
            out.append(Mod(
                    name=el_text, 
                    #ext_url=parse(modsource["thread_link"],el_href)["thread"],
                    ext_url=el_href,
                    download_url=parse(self.download,el_href),
                    icon=self.icon,
                ))

        print("Fetched mods: ", out )
        return out
            
    def show(self, text):
        pass
         
"""
class Mod:
    def __init__(self, name, mb_info, thread_url):
        self.mb = mb_info
        self.base_url = mb_info["main"]
        self.name = name
        self.modid = None
        self.thread_name = thread_url
        self.description = None
        self.download_url = None
        self.url = "{}{}".format(self.base_url, self.thread_name)
        self.set_download_url()
        self.html = None

    def set_download_url(self):

        self.url = self.mb["thread"].format(thread=self.thread_name, mod=self.modid)
        if not self.thread_name:
            return None

        self.download_url = self.mb["download"].format(thread=self.thread_name, mod=self.modid)

        return self.download_url
    
    def get_html(self):
        url = self.url
        response = requests.get(url,
                                stream=True,
                                headers=headers)
        response.raw.decode_content = True
        self.html = html.parse(response.raw)
        return self.html

    def get_description(self):
        print("get_mod_description")
        if not self.html:
            self.get_html()
        self.description = '\n'.join(self.html.xpath(
            '//div[@class="bbWrapper"]/text()'))
        return self.description
"""

class Mod():
    def __init__(self, **kwargs):
        self.name           = kwargs.get("name", None)
        self.ext_url        = kwargs.get("ext_url", None)
        self.download_urls   = kwargs.get("download_urls", None)
        self.icon           = kwargs.get("icon", None)
        self.md5sum         = kwargs.get("md5sum", None)

    def __str__(self):
        if self.md5sum:
            return self.md5sum.hex()
        if self.download_url:
            return hashlib.md5(self.download_url.encode('utf-8')).hexdigest()
        return self.name

    def get_url(self):
        """
        Display Mod in browser
        """
        if "ext_url" in self.__dict__.keys():
            return self.ext_url
        return None

    def get_download_url_base(self):
        """
        Download Mod from download URL
        """
        if "download_url" in self.__dict__.keys():
            return self.download_url
        return None

    def get_download_url(self):
        """
        Download Mod from download URL
        """
        if "download_urls" in self.__dict__.keys():
            return self.download_urls
        return []


    def download(self, dest):
        """
        :dest   Filepath to destination folder
        """

        # Guarantee destination folder
        if not os.path.isdir(dest):
            os.makedirs(dest)
            
        # NOTE the stream=True parameter below
        with requests.get(self.get_download_url(), stream=True, headers=headers) as r:
            r.raise_for_status()
            # Safeguard in case there's no "Content-Disposition" header
            try:
                #filepath = '{}/{}'.format(    base_path.rstrip('/'), parse('attachment; filename="{file}"',   r.headers["Content-Disposition"])["file"]    )
                #filepath = base_path.rstrip('/')+download_url.split('/')[-3]
                
                filepath = f"{dest.rstrip('/')}/{parse('attachment; filename="{file}"',r.headers["Content-Disposition"])["file"]}"
                
                print("Proceeding to download file ", self.get_download_url(),  "into", filepath)
                
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        # If you have chunk encoded response uncomment if
                        # and set chunk_size parameter to None.
                        #if chunk:
                        f.write(chunk)

            except KeyError as ke:
                return None
        return filepath

def download_mod(base_path, download_url):
    # TODO: apparently https://.../download isn't the actual download URL! It crashes this function.
    # Guarantee downloads directory
    if not os.path.isdir(base_path):
        os.makedirs(base_path)
        
    # NOTE the stream=True parameter below
    with requests.get(download_url, stream=True, headers=headers) as r:
        r.raise_for_status()
        # Safeguard in case there's no "Content-Disposition" header
        try:
            filepath = '{}/{}'.format(    base_path.rstrip('/'), parse('attachment; filename="{file}"',   r.headers["Content-Disposition"])["file"]    )
            #filepath = base_path.rstrip('/')+download_url.split('/')[-3]
            print("Proceeding to download file ", download_url,  "into", filepath)
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk:
                    f.write(chunk)
        except KeyError as ke:
            return None
    return filepath