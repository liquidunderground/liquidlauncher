import os
from lxml import html
from parse import *
import requests

## Original MB values
srb2mb = {
    "main": "https://mb.srb2.org",
    "maps": "https://mb.srb2.org/addons/categories/maps.4",
    "characters": "https://mb.srb2.org/addons/categories/characters.5",
    "lua": "https://mb.srb2.org/addons/categories/lua.7",
    "misc": "https://mb.srb2.org/addons/categories/miscellaneous.8",
    "assets": "https://mb.srb2.org/addons/categories/assets.6",
    "thread_link": "/addons/{thread}",
    "thread": "https://mb.srb2.org/addons/{thread}",
    "download": "https://mb.srb2.org/addons/{thread}download",
    "icon": ":/assets/img/icons/srb2mb.png",
    "vendor": "stjr"
}

## Workshop for testing
workshop_blue = {
    "main": "https://srb2workshop.org",
    "maps": "https://srb2workshop.org/resources/categories/maps.3",
    "characters": "https://srb2workshop.org/resources/categories/characters.19",
    "lua": "https://srb2workshop.org/resources/categories/lua.6",
    "misc": "https://srb2workshop.org/resources/categories/miscellaneous.7",
    "assets": "https://srb2workshop.org/resources/categories/assets.16",
    "thread_link": "/resources/{thread}",
    "thread": "https://srb2workshop.org/resources/{thread}/",
    "download": "https://srb2workshop.org/resources/{thread}download",
    "icon": ":/assets/img/icons/wsblue.png",
    "vendor": "workshop"
}

workshop_red = {
    "main": "https://srb2workshop.org",
    "maps": "https://srb2workshop.org/resources/categories/maps.11",
    "characters": "https://srb2workshop.org/resources/categories/characters.13",
    "lua": "https://srb2workshop.org/resources/categories/lua.12",
    "misc": "https://srb2workshop.org/resources/categories/miscellaneous.30",
    "assets": "https://srb2workshop.org/resources/categories/assets.26",
    "thread_link": "/resources/{thread}",
    "thread": "https://srb2workshop.org/resources/{thread}",
    "download": "https://srb2workshop.org/resources/{thread}download",
    "icon": ":/assets/img/icons/wsred.png",
    "vendor": "workshop"
}

skybase = {
    "main": "https://srb2skybase.org/mb",
    "maps": "https://srb2skybase.org/mb/forumdisplay.php?f=149",
    "characters": "https://srb2skybase.org/mb/forumdisplay.php?f=150",
    "lua": "about:blank",
    "misc": "https://srb2skybase.org/mb/forumdisplay.php?f=151",
    "assets": "about:blank",
    "thread_link": "showthread.php?t={thread}",
    "thread": "https://srb2skybase.org/mb/showthread.php?t={thread}",
    "download": "https://srb2skybase.org/mb/attachment.php?attachmentid={mod}",
    "icon": ":/assets/img/icons/skybase.png",
    "vendor": "skybase"
}

gamebanana = {
    # Useful reference links
    "main": "https://gamebanana.com",
    # gameid 6786 == SRB2
    "maps": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_csvModelInclusions=Mod&_nPerpage=50",
    "characters": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_csvModelInclusions=Mod&_nPerpage=50",
    "lua": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_csvModelInclusions=Mod&_nPerpage=50",
    "misc": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_csvModelInclusions=Mod&_nPerpage=50",
    "assets": "https://gamebanana.com/apiv11/Game/6786/Subfeed?_csvModelInclusions=Mod&__nPerpage=50",
    "thread_link": "about:gamebanana",
    "thread": "https://gamebanana.com/mods/{thread}",
    "download": "https://gamebanana.com/mods/download/{thread}",
    "icon": ":/assets/img/icons/gamebanana.png",
    "vendor": "gamebanana"
}


# Oh so sneaky:
headers =  {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'}

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

def get_mods_xenforo(addons_subforum_url, modsource, pagenum):
    """
    Gets a list of all mods from XenForo-based subforums
    :param download_url: The URL of the Xenforo sub-forum to search
    :param modsource: Internal modsource data (HTTP resources)
    :param pagenum: Page number
    :return: Returns a list containing Mod class instances
    """
    print("mb_query.get_mods_xenforo({})".format(addons_subforum_url))
    out = []
    tree = get_addons_page_html_xenforo(addons_subforum_url, pagenum)
    # Get Elements; sort our href an text later
    current_mod_elements = tree.xpath('.//div[@class="structItem-title"]/*[@data-tp-primary="on"]')
    # Filter out mod names using templates
    for el in current_mod_elements:
        # Get current link
        el_href = el.xpath('./@href')[0]
        # Get current text
        el_text = el.xpath('./text()')[0]
        out.append({
                "name": el_text, 
                "link": parse(modsource["thread_link"],el_href)["thread"]
                })

    print("Fetched mods: ", out )
    return out

def get_mods_vbulletin(addons_subforum_url, modsource, pagenum):
    """
    Gets a list of all mods from vBulletin-based subforums
    :param addons_subforum_url: The URL of the ivBulletin sub-forum to search
    :param modsource: Internal modsource data (HTTP resources)
    :param pagenum: Page number
    :return: Returns a list containing Mod class instances
    """
    print(f"mb_query.get_mods_vbulletin({addons_subforum_url}, {pagenum})")
    out = []
    # Iterate through pages grabbing thread names and their links:
    tree = get_addons_page_html_xenforo(addons_subforum_url, pagenum)
    current_mod_elements = tree.xpath('.//*[@class="threadtitle"]/*[@class="title"]')
    for el in current_mod_elements:
        # Get current link
        el_href = el.xpath('./@href')[0]
        # Get current text
        el_text = el.xpath('./text()')[0]
        out.append({
                "name": el_text, 
                "link": parse(modsource["thread_link"],el_href)["thread"]
                })
    print("Fetched mods:", out )
    return out

def get_mods_gamebanana(addons_subforum_url, modsource, pagenum):
    """
    Gets a list of all mods from Gamebanana
    :param download_url: The URL of the Gamebanana Category to search
    :param modsource: Internal modsource data (HTTP resources)
    :param pagenum: Page number
    :return: Returns a list containing Mod class instances
    """
    print(f"mb_query.get_mods_gamebanana({addons_subforum_url}, {pagenum})")
    out = []
    # Iterate through pages grabbing thread names and their links:
    remote_data = get_addons_gamebanana(addons_subforum_url, pagenum)
    # Most of the XPath stuff is not necessary here; just give good
    # params parse some JSON. Thank uncle Sonic.
    for el in remote_data:
        # Get current link (just the ID for now; generate link later)
        el_href = el["_idRow"]
        el_name = el["_sName"]
        out.append({
                "name": el_name, 
                "link": el_href
                })

    print("Fetched mods:", out )
    return out

def get_mods(addons_subforum_url, modsource, pagenum):
    """
    Gets a list of all mods from XenForo-based subforums
    :param download_url: The URL of the SRB2 MB sub-forum to search
    :param modsource: Internal modsource data (HTTP resources)
    :return: Returns a list containing Mod class instances
    """
    print("mb_query.get_mods({addons_subforum_url}, {pagenum})")

    # Cut it short for unsupported forums
    if addons_subforum_url == "about:blank":
        return []

    out = []
    mod_data = []
    if modsource["vendor"] == "stjr" or modsource["vendor"] == "workshop" :
        mod_data = get_mods_xenforo(addons_subforum_url, modsource, pagenum)
    elif modsource["vendor"] == "skybase" :
        mod_data = get_mods_vbulletin(addons_subforum_url, modsource, pagenum)
    elif modsource["vendor"] == "gamebanana" :
        mod_data = get_mods_gamebanana(addons_subforum_url, modsource, pagenum)
    # Make our list of mods
    #for index in range(len(mod_names)):
    for i in mod_data:
        #mod = Mod(mod_names[index], mod_links[index])
        #mod = Mod(mod_names[index], modsource, mod_links[index])
        mod = Mod(i["name"], modsource, i["link"])
        out.append(mod)

    return out

def get_addons_page_html_xenforo(url, page_num):
    """
    SRB2 MB and WS are broken up into subforums that sometimes have multiple pages.
    This function returns the html tree for a specified page.
    :param url: The base download_url for the subforum, not including the specific page.
    :param page_num: The page number as an integer
    :return: HTML tree: the results of html.parse(requests.get(download_url))
    """
    response = requests.get("{}?page={}".format(url, str(page_num)),
                            stream=True,
                            headers=headers)
    response.raw.decode_content = True
    return html.parse(response.raw)

def get_addons_page_html_vbulletin(url, page_num):
    """
    SRB2 MB is broken up into subforums that sometimes have multiple pages.
    This function returns the html tree for a specified page.
    :param url: The base download_url for the subforum, not including the specific page.
    :param page_num: The page number as an integer
    :return: HTML tree: the results of html.parse(requests.get(download_url))
    """
    response = requests.get("{}&page={}".format(url, str(page_num)),
                            stream=True,
                            headers=headers)
    response.raw.decode_content = True
    return html.parse(response.raw)

def get_addons_gamebanana(url, page_num):
    """
    Gamebanana's API paginates the results, but otherwise provides JSON
    which makes things a bit easier. Nonetheless, this de-paginizer is needed.
    :param url: The base download_url for the subforum, not including the specific page.
    :param page_num: The page number as an integer
    :return: HTML tree: the results of html.parse(requests.get(download_url))
    """
    try:
        response = requests.get("{}&_nPage={}".format(url, str(page_num)),
                                stream=True,
                                headers=headers)
        return response.json()["_aRecords"]
    except requests.exceptions.JSONDecodeError as e:
        print("Unable to fetch Gamebanana mod list: {}".format(e))
        return None

def get_mod_download_url(mod):
    if not mod.download_url:
        mod.set_download_url()
    return mod.download_url

def get_mod_by_name(name, mod_list):
    for mod in mod_list:
        if mod.name == name:
            return mod
    return Mod("blank", None, "blank")  # Return a blank mod so functions that rely on this function don't crash

def get_list_of_thread_names(parsed_html):
    """
    Get list of all thread names from a page on the MB
    :param request_response: The results of html.parse(response.raw)
    :return: List containing all thread names on the page
    """
    return parsed_html.xpath('.//div[@class="structItem-title"]/*[@data-tp-primary="on"]/text()')

def get_list_of_thread_links(parsed_html):
    #parsed_url = parsed_html.xpath('.//div[@class="structItem-title"]/*[@data-tp-primary="on"]/@href')
    return parsed_html.xpath('.//div[@class="structItem-title"]/*[@data-tp-primary="on"]/@href')

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
            filepath = "{}/{}".format(base_path.rstrip('/'), parse('attachment; filename="{file}"', r.headers["Content-Disposition"])["file"])
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

def extract_mod(filepath):
    extracted_files = []  # full filepaths
    return extracted_files
