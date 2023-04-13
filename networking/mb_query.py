from lxml import html
import requests

## Original MB values
#mb_url = "https://mb.srb2.org"
#mb_link = mb_url
#maps_sublink = mb_link + "/addons/categories/maps.4/"
#characters_sublink = mb_link + "/addons/categories/characters.5/"
#lua_sublink = mb_link + "/addons/categories/lua.7/"
#misc_sublink = mb_link + "/addons/categories/miscellaneous.8/"
#assets_sublink = mb_link + "/addons/categories/assets.6/"

## Workshop for testing
mb_url = "https://srb2workshop.org"
mb_link = mb_url
maps_sublink = mb_link + "/forums/maps.31/"
characters_sublink = mb_link + "/forums/characters.33/"
lua_sublink = mb_link + "/forums/lua.32/"
misc_sublink = mb_link + "/forums/miscellaneous.52/"
assets_sublink = mb_link + "/forums/assets.48/"

# Oh so sneaky:
headers =  {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'}

class Mod:
    def __init__(self, name, thread_url):
        self.mb_base_url = mb_url
        self.name = name
        self.thread_base_url = thread_url
        self.description = None
        self.download_url = None
        self.url = self.mb_base_url + self.thread_base_url
        self.set_download_url()
        self.html = None

    def set_download_url(self):
        self.url = self.mb_base_url + self.thread_base_url
        if not self.thread_base_url:
            return None
        self.download_url = self.url + "download"
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

def get_mods(addons_subforum_url):
    """
    Gets a list of all mods from addons subforum URL
    :param download_url: The URL of the SRB2 MB sub-forum to search
    :return: Returns a list containing Mod class instances
    """
    last_page = False
    mod_list = []
    mod_links = []
    mod_names = []
    page_counter = 1
    previous_data = None
    # Iterate through pages grabbing thread names and their links:
    while not last_page:
        tree = get_addons_page_html(addons_subforum_url, page_counter)
        current_mod_links = get_list_of_thread_links(tree)
        current_mod_names = get_list_of_thread_names(tree)
        if current_mod_names == previous_data:
            # This works because if you go past the real number of pages,
            #   the MB will send you back to the last valid page,
            #   making you get the same data twice
            last_page = True
        else:
            mod_names.extend(current_mod_names)
            mod_links.extend(current_mod_links)
        previous_data = current_mod_names
        page_counter += 1

    # Make our list of mods
    for index in range(len(mod_names)):
        mod = Mod(mod_names[index], mod_links[index])
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
    response = requests.get(url + "?page={}".format(str(page_num)),
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
    return Mod("blank", "blank")  # Return a blank mod so functions that rely on this function don't crash

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
