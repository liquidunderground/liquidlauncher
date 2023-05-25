from lxml import html
import requests

## Original MB values
srb2mb = {
    "main_url": "https://mb.srb2.org",
    "maps_sublink": "/addons/categories/maps.4",
    "characters_sublink": "/addons/categories/characters.5",
    "lua_sublink": "/addons/categories/lua.7",
    "misc_sublink": "/addons/categories/miscellaneous.8",
    "assets_sublink": "/addons/categories/assets.6",
    "thread_base": "/addons",
    "download_base": "/addons",
    "download_suffix": "/download",
    "vendor": "stjr"
}

## Workshop for testing
workshop_blue = {
    "main_url": "https://srb2workshop.org",
    "maps_sublink": "/forums/maps.18/",
    "characters_sublink": "/forums/characters.19/",
    "lua_sublink": "/forums/lua.20/",
    "misc_sublink": "/forums/miscellaneous.21/",
    "assets_sublink": "/forums/assets.29/",
    "thread_base": "/threads",
    #"thread_base": "/resources",
    "download_base": "/resources",
    "download_suffix": "/download",
    "vendor": "workshop"
}

workshop_red = {
    "main_url": "https://srb2workshop.org",
    "maps_sublink": "/forums/maps.31/",
    "characters_sublink": "/forums/characters.33/",
    "lua_sublink": "/forums/lua.32/",
    "misc_sublink": "/forums/miscellaneous.52/",
    "assets_sublink": "/forums/assets.48/",
    "thread_base": "/threads",
    #"thread_base": "/resources",
    "download_base": "/resources",
    "download_suffix": "/download",
    "vendor": "workshop"
}

# Oh so sneaky:
headers =  {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'}

class Mod:
    def __init__(self, name, mb_info, thread_url):
        self.mb = mb_info
        self.base_url = mb_info["main_url"]
        self.name = name
        self.thread_name = thread_url
        self.description = None
        self.download_url = None
        self.url = self.base_url + self.thread_name
        self.set_download_url()
        self.html = None

    def set_download_url(self):

        #self.url = self.mb["main_url"] + self.mb["download_base"] + self.thread_name
        self.url = self.mb["main_url"] + self.mb["thread_base"] + self.thread_name
        if not self.thread_name:
            return None

        #self.download_url = self.url + self.mb["download_suffix"]
        self.download_url = self.mb["main_url"] + self.mb["download_base"] + self.thread_name + self.mb["download_suffix"] 
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
            # Filter out prefices
            current_mod_links  = [
            link.removeprefix(modsource["thread_base"]).rstrip('/') for link in current_mod_links ]

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
