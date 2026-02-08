import re
import csv
import requests
import urllib.parse
import urllib.request

import ipaddress

from . import srb2query
from ll_info import http_headers as headers

class Netgame():

    def __init__(self, ip, port=5029, **kwargs):
        self.__dict__ = kwargs
        # Insert IP/Port combo just to be sure
        self.ip = ipaddress.ip_address(ip)
        self.port = int(port)

        self.url = f"{self.ip}:{self.port}"
        if type(self.ip) == ipaddress.IPv6Address:
            self.url = f"[{self.ip}]:{self.port}"
        

        self.serverinfo = None
        self.playerinfo = None
        self.http_source = None
        
        #self.query()

    def __str__(self):
        return self.url

    def get(self, key):
        try:
            if self.playerinfo != None and key in self.playerinfo.__dict__.keys():
                return self.playerinfo.__dict__[key]
            if self.serverinfo != None and key in self.serverinfo.__dict__.keys():
                return self.serverinfo.__dict__[key]

            if key in self.__dict__.keys():
                return self.__dict__[key]
            
            return None
            
        except Exception as e:
            print(f"Could not get attribute \"{key}\" from {self.url} - {e}")
            return None
        

    def query(self):
        """Fetch netgame data using SRB2Query
        """
        try:
            print(f"Querying {self.url}")
            serverinfo,playerinfo = srb2query.SRB2Query(str(self.ip), int(self.port)).askinfo()
            self.serverinfo = serverinfo
            self.playerinfo = playerinfo
            print(f"{self.ip}:{self.port} DATA {self.__dict__}")

            metafiles = [f for f in serverinfo.filesneeded if not int.from_bytes(f["md5sum"], "big")]
            for mf in metafiles:
                if mf["filename"]:
                    self.http_source = mf["filename"]

        except Exception as e:
            print(f"Unable to query {self.url} - {e}")
            # Failsafe dummy values
            self.serverinfo = None
            self.playerinfo = None



class MasterServer():
    
    def __new__(cls, *args, **kwargs):
        if cls is MasterServer:
            # "Virtual" Class
            raise
        return object.__new__(cls)

    def __repr__(self):
        dict_kw = ', '.join([f"{key}={value.__repr__()}" for key,value in self.__dict__.items()])
        return f"{self.__class__.__name__}({dict_kw})"
    
    def export(self):
        out = { k:v for k,v in self.__dict__.items() if k not in ["netgames"]}
        return out

    def query_netgames(self):
        """Retrieves a netgame list from wherever appropriate
        
        Returns a list of Netgame objects
        """

    def query_rooms(self):
        """Retrieves a dict of rooms {id:name,...} hosted at the master server.
        - Returns a list of tuples (room_id, room_name)
        - If the API is not room-based, return None
        """
        return None


class SnitchV1MasterServer(MasterServer):

    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}

        self.netgames = []
        self.rooms = []

        pass
    
    def query_netgames(self):
        """Retrieves a netgame list from '/servers'
        """
        
        server_list = []
        
        ms_data = requests.get(self.url, headers=headers)
        lines = ms_data.text.strip().splitlines()

        if ms_data.status_code != requests.codes.ok:
            raise Exception('Faulty HTTP response ({})'.format(ms_data.status_code))

        reader = csv.reader(lines, delimiter=',', quotechar='"')
        for row in lines:
            row_parsed = row.split(',')
            netgame = Netgame(
                ip=row_parsed[0],
                port=row_parsed[1],
                name_plain=urllib.parse.unquote(row_parsed[2]).encode('ascii', errors='ignore').decode(),
                name=row_parsed[2],
                gametype="[DUMMY]",
                game="SRB2",
                version=row_parsed[3],
                room=row_parsed[4],
                origin=row_parsed[5],
                api="snitch",
            )
            server_list.append(netgame)

        self.netgames = server_list

        return self.netgames

    def query_rooms(self):
        """Generates a list of world rooms from self.netgames
        """
        # Get a set of world rooms
        out = {x.get("room"):x.get("room") for x in self.netgames if x.get("origin") == None}

        self.rooms = out

        return self.rooms



class SRB2HTTPMasterServer(MasterServer):

    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}

        self.netgames = []
        self.rooms = []

        pass
    
    def query_netgames(self):
        """Retrieves a netgame list from '/servers'.
        """
        out = []
        netgame_list = []

        print(f"[SRB2HTTPMasterServer]: querying {self.url}")
        
        rooms = self.query_rooms()

        ms_rooms = requests.get(self.url+"/rooms", headers=headers)
        ms_netgames = requests.get(self.url+"/servers", headers=headers)
        
        if ms_netgames.status_code != requests.codes.ok:
            raise Exception('Faulty HTTP response in /servers request ({})'.format(ms_netgames.status_code))


        netgameblocks = re.split("\n{2,}", ms_netgames.text.strip())
        netgameblocks = filter(lambda blk: len(blk)>1, netgameblocks)

        for ngb in netgameblocks:
            
            # Split response text by rooms and pop first line (room ID)
            netgamelines = re.split("\n", ngb)
            room_id = netgamelines[0]
            netgamelines.pop(0)
            netgamelines = filter(lambda ln: len(ln)>1, netgamelines)

            for ngl in netgamelines:

                netgame_data = ngl.split(" ")
                ip = netgame_data[0]
                port = netgame_data[1]
                name = urllib.parse.unquote(netgame_data[2]).encode('ascii', errors='ignore').decode()
                version = netgame_data[3]
                netgame = Netgame(
                    ip=ip,
                    port=port,
                    name_plain=name,
                    name=netgame_data[2],
                    gametype="[DUMMY]",
                    game="SRB2",
                    version=version,
                    room=rooms[room_id],
                    origin=self.url,
                    api="v1",
                )

                netgame_list.append(netgame)
            
        self.netgames = netgame_list


        return self.netgames

    def query_rooms(self):
        """Retrieves a list of rooms hosted at the master server.
        - Returns a list of tuples (room_id, room_name)
        - If the API is not room-based, return None
        """
        out = {}

        ms_rooms = requests.get(self.url.rstrip('/')+"/rooms", headers=headers)

        # Query sanity check
        if ms_rooms.status_code != requests.codes.ok:
            raise Exception('Faulty HTTP response in /rooms request ({})'.format(ms_rooms.status_code))

        # Parse response text into room blocks
        roomblocks = re.split("\n{3,}", ms_rooms.text)
        roomblocks = filter(lambda blk: len(blk)>1, roomblocks)

        for block in roomblocks:
            # Parse room blocks into lines. Line 0 is the room ID, line 1 the room name
            roomlines = re.split("\n", block)
            out[roomlines[0]] = roomlines[1]

        self.rooms =  out

        return self.rooms



class SRB2KartMasterServer(MasterServer):

    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}

        self.netgames = []
        self.rooms = None # Not available bc API is not room-based (thankfully)

        pass
    
    def query_netgames(self):
        """Retrieves a netgame list from '/servers'
        """
        
        server_list = []

        ms_data = requests.get(self.url+"/servers?v=2", headers=headers)
        if ms_data.status_code != requests.codes.ok:
            raise Exception('Faulty HTTP response ({})'.format(ms_data.status_code))
        
        rows = ms_data.text.split("\n")
        rows = filter(None, rows)
        
        # TODO: Parse kartv2
        
        for server_line in rows:
            sv_line_parsed = server_line.split(" ")
            netgame = Netgame(
                ip=sv_line_parsed[0],
                port=sv_line_parsed[1],
                name_plain=urllib.parse.unquote(sv_line_parsed[2]).encode('ascii', errors='ignore').decode(),
                name=sv_line_parsed[2],
                gametype="kart",
                game="SRB2Kart",
                version="kart",
                room="",
                origin=self.url,
                api="kartv2",
            )
            server_list.append(netgame)

        self.netgames = server_list


        return self.netgames

    def query_rooms(self):
        """SRB2Kart's API doesn't support rooms -> return None
        """
        return None




def parse_server_line(url, server_string, room):
    server_data = server_string.split(" ")
    ip = server_data[0]
    port = server_data[1]
    name = urllib.parse.unquote(server_data[2]).encode('ascii', errors='ignore').decode()
    version = server_data[3]
    server = Netgame(
        ip=ip,
        port=port,
        name_plain=name,
        name=server_data[2],
        gametype="[DUMMY]",
        game="SRB2",
        version=version,
        room=room,
        origin=url,
        api="v1",
    )
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

    rooms = v1_parse_rooms(ms_rooms.text.strip())
    netgameblocks = re.split("\n{2,}", ms_netgames.text.strip())
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
        netgame = Netgame(
            ip=sv_line_parsed[0],
            port=sv_line_parsed[1],
            name_plain=urllib.parse.unquote(sv_line_parsed[2]).encode('ascii', errors='ignore').decode(),
            name=sv_line_parsed[2],
            gametype="kart",
            game="SRB2Kart",
            version="kart",
            room="",
            origin=url,
            api="kartv2",
        )
        server_list.append(netgame)

    return server_list

def parse_snitch_data(url):
    print("parse_snitch_data ", url)
    ms_data = requests.get(url, headers=headers)
    lines = ms_data.text.strip().splitlines()
    server_list = []
    if ms_data.status_code != requests.codes.ok:
        raise Exception('Faulty HTTP response ({})'.format(ms_data.status_code))
    reader = csv.reader(lines, delimiter=',', quotechar='"')
    for row in lines:
        row_parsed = row.split(',')
        netgame = Netgame(
            ip=row_parsed[0],
            port=row_parsed[1],
            name_plain=urllib.parse.unquote(row_parsed[2]).encode('ascii', errors='ignore').decode(),
            name=row_parsed[2],
            gametype="[DUMMY]",
            game="SRB2",
            version=row_parsed[3],
            room=row_parsed[4],
            origin=row_parsed[5],
            api="snitch",
        )
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
    
