import requests
import urllib.parse

# TODO: Get MS data from UI/Config
ms_kart_url = "https://ms.kartkrew.org/ms/api/games/SRB2Kart/7/servers?v=2"
ms_url = "https://mb.srb2.org/MS/0/servers"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}

def parse_server_line(server_string, room):
    server_data = server_string.split(" ")
    ip = server_data[0]
    port = server_data[1]
    name = urllib.parse.unquote(server_data[2]).encode('ascii', errors='ignore').decode()
    version = server_data[3]
    origin = "mb.srb2.org"
    server = {"ip": ip,
            "port": port,
            "name": name,
            "version": version,
            "room": room,
            "origin": origin
            }
    return server

def parse_ms_data(ms_data):
    server_list = []
    
    if "\n33\n" in ms_data.text:
        ms_standard_data = ms_data.text.split("\n33\n")[1].split("\n\n")[0].split("\n")
        ms_standard_data = filter(None, ms_standard_data)
        for server_line in ms_standard_data:
            server = parse_server_line(server_line, "standard")
            server_list.append(server)

    if "\n28\n" in ms_data.text:
        ms_casual_data = ms_data.text.split("\n28\n")[1].split("\n\n")[0].split("\n")
        ms_casual_data = filter(None, ms_casual_data)
        for server_line in ms_casual_data:
            server = parse_server_line(server_line, "casual")
            server_list.append(server)

    if "\n31\n" in ms_data.text:
        ms_oldc_data = ms_data.text.split("\n31\n")[1].split("\n\n")[0].split("\n")
        ms_oldc_data = filter(None, ms_oldc_data)
        for server_line in ms_oldc_data:
            server = parse_server_line(server_line, "oldc")
            server_list.append(server)

    if "\n38\n" in ms_data.text:
        ms_custom_data = ms_data.text.split("\n38\n")[1].split("\n\n")[0].split("\n")
        ms_custom_data = filter(None, ms_custom_data)
        for server_line in ms_custom_data:
            server = parse_server_line(server_line, "custom")
            server_list.append(server)
            
    return server_list

def parse_kart_data(data):
    server_list = []
    # TODO
    return server_list

def get_server_list(url, api="v1"):
    print("get_server_list")
    # first get a list of all servers from the master server     
    try:
        ms_data = requests.get(url, headers=headers)
    except:
        print("Could not get master server data. Not updating server information.")
        return
    
    # TODO: Check for API
    if api == "v1":
        return parse_ms_data(ms_data)
    elif url == "kartv2":
        return parse_kart_data(ms_data)
    elif url == "snitch":
        return parse_snitch_data(ms_data)
    else:
        return []
