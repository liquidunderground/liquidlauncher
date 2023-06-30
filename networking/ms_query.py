import re
import csv
import requests
import urllib.parse
import urllib.request

from ll_info import http_headers as headers

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
            "game": "SRB2",
            "version": version,
            "room": room,
            "origin": url,
            "api": "v1",
            }
    return server

def v1_parse_rooms(txt):
    out = {}
    roomblocks = re.split("\n{3,}", txt)
    roomblocks = filter(lambda blk: len(blk)>1, roomblocks)

    for block in roomblocks:
        roomlines = re.split("\n", block)
        out[roomlines[0]] = roomlines[1]

    return out

def query_ms_rooms(url):
    print("query_ms_rooms ", url)
    ms_rooms = requests.get(url+"/rooms", headers=headers)

    # Query sanity check
    if ms_rooms.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response in /rooms request ({})'.format(ms_rooms.status_code))

    rooms = v1_parse_rooms(ms_rooms.text)
        
    return rooms

def parse_ms_data(url):
    # TODO: Make room system MS agnostic
    # Two step system:
    #   1. Query /rooms to get info
    #   2. Query /servers and parse servers

    print("parse_v1_data ", url)
    ms_rooms = requests.get(url+"/rooms", headers=headers)
    ms_netgames = requests.get(url+"/servers", headers=headers)
    server_list = []

    # Query sanity check
    if ms_rooms.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response in /rooms request ({})'.format(ms_rooms.status_code))
    if ms_netgames.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response in /servers request ({})'.format(ms_netgames.status_code))

    rooms = v1_parse_rooms(ms_rooms.text)
    netgameblocks = re.split("\n{2,}", ms_netgames.text)
    netgameblocks = filter(lambda blk: len(blk)>1, netgameblocks)

    for ngb in netgameblocks:
        netgamelines = re.split("\n", ngb)
        roomno = netgamelines[0]
        netgamelines.pop(0)
        netgamelines = filter(lambda ln: len(ln)>1, netgamelines)
        for ngl in netgamelines:
            netgame = parse_server_line(url, ngl, rooms[roomno])
            server_list.append(netgame)
        
    return server_list

def parse_kart_data(url):
    print("parse_kart_data ", url)
    ms_data = requests.get(url+"/servers?v=2", headers=headers)
    server_list = []
    if ms_data.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response ({})'.format(ms_data.status_code))
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
            "game": "SRB2Kart",
            "version": "kart",
            "room": "",
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
    if ms_data.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response ({})'.format(ms_data.status_code))
    reader = csv.reader(lines, delimiter=',', quotechar='"')
    for row in lines:
        row_parsed = row.split(',')
        netgame = {
            "ip": row_parsed[0],
            "port": row_parsed[1],
            "name": urllib.parse.unquote(row_parsed[2]).encode('ascii', errors='ignore').decode(),
            "gametype": "[DUMMY]",
            "game": "SRB2",
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
    if api == "v1":
        return parse_ms_data(url_sanitized)
    elif api == "kartv2":
        return parse_kart_data(url_sanitized)
    elif api == "snitch":
        return parse_snitch_data(url_sanitized)
    else:
        return []
    
