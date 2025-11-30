from PySide6 import QtWidgets, QtCore

from ll_threading import NetgameThread, ll_signalbus
from networking.ms_query import Netgame

from ui.ui_netgamedialog import Ui_NetgameDialog

class NetgameDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NetgameDialog, self).__init__(parent)

        self.thread_pool = QtCore.QThreadPool.globalInstance()

        self.ui = Ui_NetgameDialog()
        self.netgame = None
        self.ui.setupUi(self)
        self.setWindowTitle("Netgame")

        # UI setup
        #self.ui.FilesTable.addAction(self.parent().qicons["copy"], "Copy MD5 to clipboard", lambda: self.file_copy_md5(self.ui.FilesTable.currentRow()))
        if self.parent().global_settings["modsources"]["gameserver"]:
            self.ui.FilesTable.addAction(self.parent().qicons["download"], "Download", self.download_file)

        ll_signalbus.netgame_update_finish.connect(self.refresh)
        
    def setNetgame(self, netgame):
        self.netgame = netgame
        self.refresh([self.netgame])

    def bookmark(self):
        self.parent().bookmark(self.netgame)

    @QtCore.Slot(list)
    def refresh(self, netgames:list):
        
        # Sanity check in case the signals screw up
        if self.netgame not in netgames:
            pass

        import hashlib

        self.ui.PlayersAndFiles.hide()
        text = f'<h1 align="center">{self.netgame.get("name_plain")}</h1>' \
            f'<p align="center">{self.netgame.get("url")}</p>' \
            f'<p>' \
            f'Game: {self.netgame.get("game")} {self.netgame.get("version")}<br>' \
            f'Origin: {self.netgame.get("room")} @ {self.netgame.get("origin")}<br>' \
            f'MS API: {self.netgame.get("api")}' \
            f'</p>' \
            f'<p align="center">' \
            f'<em>Serverinfo unavailable</em>' \
            f'</p>'
        
        serverinfo = self.netgame.get("serverinfo")

        if serverinfo != None:

            realfiles = [f for f in serverinfo.filesneeded if int.from_bytes(f["md5sum"], "big")]

            text = f'<h1 align="center">{serverinfo.servername}</h1>' \
                f'<p align="center">{self.netgame.get("url")}</p>' \
                f'<p align="center">' \
                f'{"Modified" if self.netgame.get("modifiedgame") else "Vanilla"} | ' \
                f'{"Cheats" if self.netgame.get("modifiedgame") else "No cheats"} | ' \
                f'{self.netgame.get("gametypename") if self.netgame.get("gametypename") != None else self.netgame.get("gametype")}' \
                f'</p>' \
                f'<p align="center">' \
                f'</p>' \
                f'<h2>Map details</h2>' \
                f'<table>' \
                f'<tr><th>Current Map</td><td>{serverinfo.maptitle}{" Zone" if serverinfo.iszone else ""}{serverinfo.actnum if serverinfo.actnum != 0 else ""} ({self.netgame.get("mapname")})</td></tr>' \
                f'<tr><th>MD5 Hash</td><td>{serverinfo.mapmd5.hex()}</td></tr>' \
                f'</table>' \
                f'<h2>Game & API Info</h2>' \
                f'<table>' \
                f'<tr><th>Game</th><td>{self.netgame.get("application")} {self.netgame.get("version")} {self.netgame.get("subversion")}</td></tr>' \
                f'<tr><th>Origin</th><td>{self.netgame.get("room")} @ {self.netgame.get("origin")}</td></tr>' \
                f'<tr><th>MS API</th><td>{self.netgame.get("api")}</td></tr>' \

            if self.netgame.get("httpsource"):
                text += f'<tr><th>HTTP Modsource URL</th><td><a href="{self.netgame.get("httpsource")}">{self.netgame.get("httpsource")}</a></p>'

            text += '</table>'

            if self.parent().global_settings["devsettings"]["verbose_serverinfo"]:
                
                # Print debug info if so desired
                text += "<hr>"
                
                text += "<h2>ServerInfo data</h2><table>"
                for si_i,si_v in serverinfo.__dict__.items():
                    text += f"<tr><th>{si_i}</th><td>{si_v}</td></tr>"
                text += "</table>"

                text += "<h2>File metadata</h2><table>"
                for mf_i,mfile in enumerate(realfiles):
                    text += f"<tr><th>{mf_i}</th><td><ul>"
                    for i,v in mfile.items():
                        text += f"<li><em>{i}</em>: {v}</li>"
                    text += "</ul></td></tr>"
                text += "</table>"

            # Refill players table
            self.ui.PlayersTable.clear()
            for p in self.netgame.playerinfo.players:
                item = QtWidgets.QListWidgetItem()
                item.setText(p["name"])
                if p["team"]:
                    item_icon = self.parent().qicons["_teams"]["red"] if p["team"] == 1 else self.parent().qicons["_teams"]["blue"]
                    item.setIcon(item_icon)
                self.ui.PlayersTable.addItem(item)

            # Refill Files Table
            self.ui.FilesTable.clear()
            for f in realfiles:
                item = QtWidgets.QListWidgetItem()
                item.setText(f["filename"])
                
                file_type = f["filename"].split('.')

                match file_type[-1]:
                    case "wad" | "pk3" | "soc" | "lua" | "kart" :
                        item_icon = self.parent().qicons["_filetypes"][file_type[-1]]
                        item.setIcon(item_icon)
                        item.setToolTip(f"MD5 hash: {f["md5sum"].hex()}")
                    

                self.ui.FilesTable.addItem(item)

            self.ui.PlayersAndFiles.setTabText(0, f"Players ({serverinfo.__dict__["numberofplayer"]}/{serverinfo.__dict__["maxplayer"]})")
            self.ui.PlayersAndFiles.setTabText(1, f"Files ({len(realfiles)})")

            self.ui.PlayersAndFiles.show()

        self.ui.ServerinfoLabel.setText(text)
        self.setWindowTitle(self.netgame.get("name_plain"))

    def join_netgame(self):
        print(f"join_netgame({self})")

    def download_file(self, file):
        print(f"Pretending to download file {file} ...")

    def file_copy_md5(self, file):
        from PySide6.QtWidgets import QApplication
        
        if self.netgame.get("serverinfo") == None:
            pass

        f = [f for f in self.netgame.get("serverinfo").filesneeded if int.from_bytes(f["md5sum"], "big")]
        
        clipboard = QApplication.clipboard()
        clipboard.setText(f[file]["md5sum"].hex())

    def query(self):
        thread = NetgameThread([self.netgame])
        self.thread_pool.start(thread)
