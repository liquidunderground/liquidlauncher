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
    "download": "https://mb.srb2.org/addons/{thread}/download",
    "vendor": "stjr"
}

## Workshop for testing
workshop_blue = {
    "main": "https://srb2workshop.org",
    "maps": "https://srb2workshop.org/forums/maps.18/",
    "characters": "https://srb2workshop.org/forums/characters.19/",
    "lua": "https://srb2workshop.org/forums/lua.20/",
    "misc": "https://srb2workshop.org/forums/miscellaneous.21/",
    "assets": "https://srb2workshop.org/forums/assets.29/",
    "thread_link": "/threads/{thread}",
    "thread": "https://srb2workshop.org/threads/{thread}/",
    "download": "https://srb2workshop.org/resources/{thread}/download",
    "vendor": "workshop"
}

workshop_red = {
    "main": "https://srb2workshop.org",
    "maps": "https://srb2workshop.org/forums/maps.31/",
    "characters": "https://srb2workshop.org/forums/characters.33/",
    "lua": "https://srb2workshop.org/forums/lua.32/",
    "misc": "https://srb2workshop.org/forums/miscellaneous.52/",
    "assets": "https://srb2workshop.org/forums/assets.48/",
    "thread_link": "/threads/{thread}",
    "thread": "https://srb2workshop.org/threads/{thread}/",
    "download": "https://srb2workshop.org/resources/{thread}/download",
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
    "vendor": "skybase"
}

wadarchive = {
    "main": "about:wadarchive",
    "maps": "about:wadarchive",
    "characters": "about:wadarchive",
    "lua": "about:wadarchive",
    "misc": "about:wadarchive",
    "assets": "about:wadarchive",
    "thread_link": "about:wadarchive",
    "thread": "about:wadarchive",
    "download": "about:wadarchive",
    "vendor": "wadarchive"
}

gamebanana = {
    "main": "about:gamebanana",
    "maps": "about:gamebanana",
    "characters": "about:gamebanana",
    "lua": "about:gamebanana",
    "misc": "about:gamebanana",
    "assets": "about:gamebanana",
    "thread_link": "about:gamebanana",
    "thread": "about:gamebanana",
    "download": "about:gamebanana",
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
        self.url = self.base_url + self.thread_name
        self.set_download_url()
        self.html = None

    def set_download_url(self):

        #self.url = self.mb["main_url"] + self.mb["download"] + self.thread_name
        #self.url = self.mb["main_url"] + self.mb["thread"] + self.thread_name
        self.url = self.mb["thread"].format(thread=self.thread_name, mod=self.modid)
        if not self.thread_name:
            return None

        #self.download_url = self.url + self.mb["download_suffix"]
        #self.download_url = self.mb["main_url"] + self.mb["download"] + self.thread_name + self.mb["download_suffix"] 
        self.download_url = self.mb["download"].format(thread=self.thread_name, mod=self.modid)

        #print("Download URL:"+self.download_url)

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

def get_mods(addons_subforum_url, modsource):
    """
    Gets a list of all mods from addons subforum URL
    :param download_url: The URL of the SRB2 MB sub-forum to search
    :return: Returns a list containing Mod class instances
    """
    print("mb_query.get_mods({})".format(addons_subforum_url))
    last_page = False
    mod_list = []
    mod_links = []
    mod_names = []
    page_counter = 1
    previous_data = None
    # Iterate through pages grabbing thread names and their links:
    while not last_page:
        print("Querying page ", page_counter )
        tree = get_addons_page_html(addons_subforum_url, page_counter)
        current_mod_links = get_list_of_thread_links(tree)
        current_mod_names = get_list_of_thread_names(tree)
        if current_mod_names == previous_data:
            # This works because if you go past the real number of pages,
            #   the MB will send you back to the last valid page,
            #   making you get the same data twice
            last_page = True
            print("Last page reached!")
        else:
            # Filter out mod names using templates
            current_mod_links  = [
            parse(modsource["thread_link"],link)["thread"] for link in current_mod_links ]

            mod_names.extend(current_mod_names)
            mod_links.extend(current_mod_links)
        previous_data = current_mod_names
        page_counter += 1

    print("Mod links: ", mod_links )

    # Make our list of mods
    for index in range(len(mod_names)):
        #mod = Mod(mod_names[index], mod_links[index])
        mod = Mod(mod_names[index], modsource, mod_links[index])
        mod_list.append(mod)

    return mod_list

def get_addons_page_html(url, page_num):
    """
    SRB2 MB is broken up into subforums that sometimes have multiple pages.
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
    filepath = base_path + download_url.split('/')[-1]
    print("Proceeding to download file ", download_url,  "into", filepath)
    # NOTE the stream=True parameter below
    with requests.get(download_url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return filepath

def extract_mod(filepath):
    extracted_files = []  # full filepaths
    return extracted_files
