import csv
import requests
import urllib.parse
import urllib.request

# TODO: Remove old values
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}

def parse_server_line(url, server_string, room):
    server_data = server_string.split(" ")
    ip = server_data[0]
    port = server_data[1]
    name = urllib.parse.unquote(server_data[2]).encode('ascii', errors='ignore').decode()
    version = server_data[3]
    server = {"ip": ip,
            "port": port,
            "name": name,
            "gametype": "[DUMMY]",
            "version": version,
            "room": room,
            "origin": url,
            "api": "v1",
            }
    return server

def parse_ms_data(url):
    # TODO: Make room system MS agnostic
    # Two step system:
    #   1. Query /rooms to get info
    #   2. Query /servers and parse servers

    print("parse_v1_data ", url)
    ms_data = requests.get(url+"/servers", headers=headers)
    server_list = []

        #elif url == "kartv2":
        #elif url == "snitch":
            #ms_data = requests.get(url+"/snitch", headers=headers)
    
    if "\n33\n" in ms_data.text:
        ms_standard_data = ms_data.text.split("\n33\n")[1].split("\n\n")[0].split("\n")
        ms_standard_data = filter(None, ms_standard_data)
        for server_line in ms_standard_data:
            server = parse_server_line(url, server_line, "standard")
            server_list.append(server)

    if "\n28\n" in ms_data.text:
        ms_casual_data = ms_data.text.split("\n28\n")[1].split("\n\n")[0].split("\n")
        ms_casual_data = filter(None, ms_casual_data)
        for server_line in ms_casual_data:
            server = parse_server_line(url, server_line, "casual")
            server_list.append(server)

    if "\n31\n" in ms_data.text:
        ms_oldc_data = ms_data.text.split("\n31\n")[1].split("\n\n")[0].split("\n")
        ms_oldc_data = filter(None, ms_oldc_data)
        for server_line in ms_oldc_data:
            server = parse_server_line(url, server_line, "oldc")
            server_list.append(server)

    if "\n38\n" in ms_data.text:
        ms_custom_data = ms_data.text.split("\n38\n")[1].split("\n\n")[0].split("\n")
        ms_custom_data = filter(None, ms_custom_data)
        for server_line in ms_custom_data:
            server = parse_server_line(url, server_line, "custom")
            server_list.append(server)
            
    return server_list

def parse_kart_data(url):
    print("parse_kart_data ", url)
    ms_data = requests.get(url+"/servers?v=2", headers=headers)
    server_list = []
    rows = ms_data.text.split("\n")
    rows = filter(None, rows)
    # TODO: Parse kartv2
    for server_line in rows:
        sv_line_parsed = server_line.split(" ")
        netgame = {
            "ip": sv_line_parsed[0],
            "port": sv_line_parsed[1],
            #"name": sv_line_parsed[2],
            "name": urllib.parse.unquote(sv_line_parsed[2]).encode('ascii', errors='ignore').decode(),
            "gametype": "kart",
            "version": "kart",
            "room": "kart",
            "origin": url,
            "api": "kartv2",
        }
        server_list.append(netgame)

    return server_list

def parse_snitch_data(url):
    print("parse_snitch_data ", url)
    ms_data = requests.get(url+"/liquidms/snitch", headers=headers)
    lines = ms_data.text.splitlines()
    server_list = []
    reader = csv.reader(lines, delimiter=',', quotechar='"')
    for row in lines:
        row_parsed = row.split(',')
        netgame = {
            "ip": row_parsed[0],
            "port": row_parsed[1],
            "name": urllib.parse.unquote(row_parsed[2]).encode('ascii', errors='ignore').decode(),
            "gametype": "[DUMMY]",
            "version": row_parsed[3],
            "room": row_parsed[4],
            "origin": row_parsed[5],
            "api": "snitch",
        }
        server_list.append(netgame)

    return server_list

def get_server_list(url, api="v1"):
    # TODO: multi-server query. 
    # - Change API from URL+API to List of URL+API elements
    # - use foreach loop to accumulate results
    # (- Rewrite the calls to this function ofc)

    url_sanitized = url.rstrip("/ \t");
    print("get_server_list({}, {})".format(url_sanitized, api))
    # first get a list of all servers from the master server     
    try:
        if api == "v1":
            return parse_ms_data(url_sanitized)
        elif api == "kartv2":
            return parse_kart_data(url_sanitized)
        elif api == "snitch":
            return parse_snitch_data(url_sanitized)
        else:
            return []
    except Exception as e:
        print("Failed to update master server:", e)
        return
    
