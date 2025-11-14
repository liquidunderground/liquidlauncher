from PySide6.QtWidgets import QDialog

from ui.ui_netgamedialog import Ui_NetgameDialog

class NetgameDialog(QDialog):
    def __init__(self, parent=None):
        super(NetgameDialog, self).__init__(parent)
        self.ui = Ui_NetgameDialog()
        self.netgame = None
        self.ui.setupUi(self)
        self.setWindowTitle("Netgame")
    
    def setNetgame(self, netgame):
        self.netgame = netgame
        self._netgame_update()

    def bookmark(self):
        self.parent().bookmark(self.netgame)

    def _netgame_update(self):

        import hashlib

        self.ui.PlayersAndFiles.hide()
        text = f'<h1 align="center">{self.netgame.get("name_plain")}</h1>' \
            f'<p align="center">' \
            f'{self.netgame.get("ip")}:{self.netgame.get("port")}' \
            f'</p>' \
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
                f'<p align="center">' \
                f'{self.netgame.get("ip")}:{self.netgame.get("port")}' \
                f'</p>' \
                f'<p align="center">' \
                f'{"Modified" if serverinfo.modifiedgame else "Vanilla"} | ' \
                f'{"Cheats" if serverinfo.modifiedgame else "No cheats"} | ' \
                f'{serverinfo.gametypename}' \
                f'</p>' \
                f'<p align="center">' \
                f'</p>' \
                f'<h2>Map details</h2>' \
                f'<p>' \
                f'Current Map: {serverinfo.maptitle}{" Zone" if serverinfo.iszone else ""}{serverinfo.actnum if serverinfo.actnum != 0 else ""} ({serverinfo.mapname})<br>' \
                f'MD5 Hash: {serverinfo.mapmd5.hex()}<br>' \
                f'</p>' \
                f'<h2>Game & API Info</h2>' \
                f'<p>' \
                f'Game: {self.netgame.get("game")} {self.netgame.get("version")}<br>' \
                f'Origin: {self.netgame.get("room")} @ {self.netgame.get("origin")}<br>' \
                f'MS API: {self.netgame.get("api")}' \
                f'</p>'

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
                #if int.from_bytes(f["md5sum"], "big"):
                self.ui.FilesTable.addItem(f"{f["filename"]} (md5: {f["md5sum"].hex()})")

            self.ui.PlayersAndFiles.setTabText(0, f"Players ({serverinfo.numberofplayer}/{serverinfo.maxplayer})")
            self.ui.PlayersAndFiles.setTabText(1, f"Files ({len(realfiles)})")

            self.ui.PlayersAndFiles.show()

        self.ui.ServerinfoLabel.setText(text)
        self.setWindowTitle(self.netgame.get("name_plain"))

    def join_netgame(self):
        print(f"join_netgame({self})")

    def query(self):
        self.netgame.query()
        self._netgame_update()
