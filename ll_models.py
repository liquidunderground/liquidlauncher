from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

import networking.ms_query as ms_query

class MasterServerAPIDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent=None):
        super(MasterServerAPIDelegate, self).__init__(parent=parent)

    def createEditor(self, parent, option, index):
        w_api = QtWidgets.QComboBox(parent)
        
        w_api.addItem("LiquidMS Snitch", "snitch")
        w_api.addItem("SRB2 MS", "v1")
        w_api.addItem("SRB2Kart/Ring Racers MS", "kartv2")
        
        #w_api.setCurrentIndex(twi_api.findData(api))

        return w_api

class MasterServerTableModel(QtCore.QAbstractTableModel):
    """ This class displays a table towards Qt,
        but represents an internal collection of
        MasterServer objects.

        Saving settings will trigger a config dump of
        this table's content and subsequent recreation
        of the MasterServer objects needed to query. 
    """

    def __init__(self, parent=None, master_servers=None, *args):

        super(MasterServerTableModel, self).__init__(parent=parent)

        self.master_servers = master_servers or []
        self.netgame_table_models = []

        self.column_fields = [
            "servername",
            "url",
            "api",
        ]

        pass
    
    def export(self):
        out = []


        for ms in self.master_servers:
            out.append( {k:v for k,v in ms.__dict__.items() if k not in ["netgames", "rooms"]})
        
        print(f"MSMODEL EXPORT: {out}")

        return out

    def insertMasterserver(self, row, mserver):

        if issubclass(type(mserver), ms_query.MasterServer):
            self.master_servers.insert(row, mserver)
        else:
            match mserver["api"].lower():
                case "v1":
                    self.master_servers.insert(row, ms_query.SRB2HTTPMasterServer(**mserver) )
                case "kartv2":
                    self.master_servers.insert(row, ms_query.SRB2KartMasterServer(**mserver) )
                case "snitch":
                    self.master_servers.insert(row, ms_query.SnitchV1MasterServer(**mserver) )
        
        self.netgame_table_models.insert(row, NetgameTableModel())
        self.layoutChanged.emit()

    def appendMasterserver(self, mserver):
        last_row = self.rowCount()
        self.insertMasterserver(last_row,mserver)

    def getMasterserverByIndex(self, index):
        return self.master_servers[index.row()]

    def getMasterserverByRow(self, row):
        if row in range(len(self.master_servers)):
            return self.master_servers[row]
        return None

    def get_NetgameTableModel(self, index):
        return self.netgame_table_models[index]

    def insertRows(self, position, rows=1, index=QtCore.QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)

        for row in range(position, position+rows):

            self.master_servers.insert(row, {"servername": "", "url": "", "api": "v1", "netgames": NetgameTableModel()})
            self.netgame_table_models.insert(row, NetgameTableModel())
            #self.master_servers.insert(position + row, {"mserver": ms_query.MasterServer(), "netgames": NetgameTableModel()})

        self.endInsertRows()
        return True

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.master_servers):
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            name = self.master_servers[index.row()].servername
            ms = self.master_servers[index.row()].url
            api = self.master_servers[index.row()].api

            if index.column() == 0:
                return name
            elif index.column() == 1:
                return ms
            elif index.column() == 2:
                return api

        return None
    
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        """ Adjust the data (set it to <value>) depending on the given
            index and role.
        """

        print(f"[MSTableModel]: setData({index}, {value})")

        if role != Qt.ItemDataRole.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.master_servers):
            ms = self.master_servers[index.row()]
            
            if index.column() == 0:
                ms.servername = value
            elif index.column() == 1:
                ms.address = value
            elif index.column() == 2:
                ms.api = value
                match ms.api.lower():
                    case "v1":
                        ms.__class__ = ms_query.SRB2HTTPMasterServer
                    case "kartv2":
                        ms.__class__ = ms_query.SRB2KartMasterServer
                    case "snitch":
                        ms.__class__ = ms_query.SnitchV1MasterServer
                    case _:
                        ms.__class__ = ms_query.MasterServer
            else:
                return False

            self.dataChanged.emit(index, index, 0)
            return True

        return False

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        self.master_servers[row:(row+count)] = []
        self.netgame_table_models[row:(row+count)] = []
        self.layoutChanged.emit()

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        self.removeRows(row,1,parent)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ["Title", "URL", "API"][section]
        return super().headerData(section, orientation, role)

    def columnCount(self, index):
        return 3

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.master_servers)



class NetgameTableModel(QtCore.QAbstractTableModel):

    i_status_good =    QtGui.QIcon(":/assets/img/icons/network-good.png")
    i_status_idle =    QtGui.QIcon(":/assets/img/icons/network-idle.png")
    i_status_error =   QtGui.QIcon(":/assets/img/icons/network-error.png")

    def __init__(self, parent=None, netgames=None, *args):
        super(NetgameTableModel, self).__init__(parent=parent)
        
        self.netgames = netgames or []

        self.headers = ["Status", "Name", "Gametype", "Version", "Room", "Origin"]

        pass


    def insertNetgame(self, row, netgame):

        if issubclass(type(netgame), ms_query.Netgame):
            self.netgames.insert(row, netgame)
        else:
            self.netgames.insert(row, ms_query.Netgame(**netgame) )
        self.layoutChanged.emit()

    def appendNetgame(self, netgame):
        last_row = self.rowCount()
        self.insertNetgame(last_row,netgame)

    def getNetgameByIndex(self, index):
        return self.netgames[index.row()]

    def getNetgameByRow(self, row):
        if row in range(len(self.netgames)):
            return self.netgames[row]
        return None



    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.netgames):
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            
            ng = self.netgames[index.row()]

            if index.column() == 0:   # Status icon
                return self.i_status_idle
            elif index.column() in self.headers:
                #return netgame.__dict__[["status", "name", "gametype", "version", "room", "origin"][index.column()]]
                return ["status", "name", "gametype", "version", "room", "origin"][index.column()]

        return None
    
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        """ Adjust the data (set it to <value>) depending on the given
            index and role.
        """
        if role != Qt.ItemDataRole.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.netgames):
            ms = self.netgames[index.row()]
            if index.column() == 0:
                ms["name"] = value
            elif index.column() == 1:
                ms["address"] = value
            elif index.column() == 2:
                ms["api"] = value
            else:
                return False

            self.dataChanged.emit(index, index, 0)
            return True

        return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ["Status", "Name", "Gametype", "Version", "Room", "Origin"][section]
        return super().headerData(section, orientation, role)

    def columnCount(self, index):
        return len(self.headers)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.netgames)



class GamefileListModel(QtCore.QAbstractListModel):

    def __init__(self, parent, files=None, *args):

        self.files = files or []

        pass

    def data(self, index, role):
        
        if role == Qt.DisplayRole:
            status, text = self.files[index.row()]
            return 

        return self.files

    def rowCount(self, index):
        return len(self.files)