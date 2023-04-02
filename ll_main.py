import json
import os
import sys
import webbrowser
import urllib
import urllib.parse
import toml
from datetime import date
from urllib.request import urlretrieve

import feedparser
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog, QMenu, QMessageBox
from PySide6.QtCore import Signal

import edit_server_main
import char_text
from lb2_threading import QueryMessageBoard, QueryMasterServer, ModDownloader
from lb2_ui import *
from qss import themes

fool = date.today() == date(date.today().year, 4, 1)

versionString = "reBoot-2.0"
global_settings_file = "LauncherBlast2_settings.toml"


class MainWindow(QMainWindow):
    # Emits instance of Mod() class from self.mods_list
    mod_description_sig = Signal(object)
    # Emits self.mods_list
    mod_list_sig = Signal(dict)
    # Emits bool, telling QThread to query the master server
    query_ms_sig = Signal(bool)
    # Emits mod download URL string
    download_mod_url_sig = Signal(str)
    # Emits mod download filepath
    download_mod_path_sig = Signal(str)
    

    def __init__(self, app):
        super().__init__()
        
        # Launcher settings and profile variables
        self.global_settings = None
        self.current_profile = None
        self.current_profile_file = None
        self.current_profile_settings = None
        
        self.apply_style()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app = app
        self.setWindowTitle("Launcherblast2 reBoot-2.0")

        # server ips stored internally so u don't dox people's ips if you're streaming or smth
        self.saved_server_ips = []

        # Dict associate master server widget items with server data
        self.master_server_list = {}

        # Dict associating mod list widget items with mods:
        self.mods_list = {}

        # MB Query Multithreading
        self.mb_qthread = QueryMessageBoard()
        self.mb_qthread.start()
        self.mod_list_sig.connect(self.mb_qthread.on_request_mod_list)
        self.mod_description_sig.connect(self.mb_qthread.on_request_mod_desc)
        self.mb_qthread.mod_list_sig1.connect(self.on_mod_list)
        self.mb_qthread.mod_description_sig1.connect(self.on_mod_description)

        # Download mod multithreading
        self.mod_download_qthread = ModDownloader()
        self.mod_download_qthread.start()
        self.download_mod_url_sig.connect(self.mod_download_qthread.on_download_button)
        self.download_mod_path_sig.connect(self.mod_download_qthread.on_filepath_emit)
        self.mod_download_qthread.mod_filepath_sig1.connect(self.add_mod_to_files)

        # Emits mod download filepath
        download_mod_path_sig = Signal(str)
        
        # Master Server Multithreading
        self.ms_qthread = QueryMasterServer()
        self.ms_qthread.start()
        self.query_ms_sig.connect(self.ms_qthread.on_refresh)
        self.ms_qthread.server_list_sig1.connect(self.on_server_list)
        
        # QTimer helps us know when user stops typing into profile name textbox
        self.typing_timer = QtCore.QTimer()
        self.typing_timer.setSingleShot(True)
        self.typing_timer.timeout.connect(self.alter_profile_info)
        self.ui.ProfileNameInput.textChanged.connect(self.start_typing_timer)
        
        # load servers from file ===================================================== #
        # self.loadServerList()
        self.has_loaded_servers = False

        # allow posix systems to use wine ============================================ #
        if os.name == "posix":
            self.ui.WineToggle.setEnabled(True)

        # file dialog options to keep shit consistent ================================ #
        self.FileDialogOptions = QFileDialog.Options()
        # self.FileDialogOptions |= QFileDialog.DontUseNativeDialog

        # set tab to game tab initially ============================================== #
        self.ui.MainTabsStackedWidget.setCurrentIndex(1)
        self.ui.GameContentStackedWidget.setCurrentIndex(0)

        # fix resolution of skin image =============================================== #
        self.ui.PlayerSkinImage.setPixmap(QtGui.QPixmap(":/assets/img/sonic.png")
                                          .scaled(135,
                                                  190,
                                                  QtCore.Qt.KeepAspectRatio,
                                                  QtCore.Qt.FastTransformation))

        # changed skin index ========================================================= #
        self.ui.PlayerSkinInput.currentIndexChanged.connect(self.change_skin_image)

        # clear files list =========================================================== #
        self.ui.GameFilesList.clear()

        # clear servers list ========================================================= #
        self.ui.ServerList.clear()

        # dock "tabs" ================================================================ #
        self.ui.NewsTabButton.clicked.connect(lambda: self.change_main_tab(0))
        self.ui.GameTabButton.clicked.connect(lambda: self.change_main_tab(1))
        self.ui.HelpTabButton.clicked.connect(lambda: self.change_main_tab(2))
        self.ui.SettingsTabButton.clicked.connect(lambda: self.change_main_tab(3))

        # game "tabs" ================================================================ #
        self.ui.ProfileTabButton.clicked.connect(lambda: self.change_game_tab(0))
        self.ui.FilesTabButton.clicked.connect(lambda: self.change_game_tab(1))
        self.ui.GameSettingsTabButton.clicked.connect(lambda: self.change_game_tab(2))
        self.ui.PlayerSetupTabButton.clicked.connect(lambda: self.change_game_tab(3))
        self.ui.HostGameTabButton.clicked.connect(lambda: self.change_game_tab(4))
        self.ui.JoinGameTabButton.clicked.connect(lambda: self.change_game_tab(5))

        # profile page buttons ======================================================= #
        self.ui.ProfileDirBrowseButton.clicked.connect(self.set_game_path)

        # files list buttons ========================================================= #
        self.ui.GameFilesClearButton.clicked.connect(self.clear_files_list)
        self.ui.GameFilesDeleteButton.clicked.connect(self.delete_selected_files)
        self.ui.GameFilesUpButton.clicked.connect(self.move_selected_files_up)
        self.ui.GameFilesDownButton.clicked.connect(self.move_selected_files_down)
        self.ui.GameFilesAddButton.clicked.connect(self.add_files)
        self.ui.GameFilesSaveButton.clicked.connect(self.save_file_list)
        self.ui.GameFilesLoadButton.clicked.connect(self.load_file_list)
        self.ui.GameFilesExecScrBrowseButton.clicked.connect(self.set_exec_file_path)

        # modding list buttons ======================================================= #
        self.ui.RefreshModsButton.clicked.connect(self.refresh_mods_list)
        self.ui.DownloadModButton.clicked.connect(self.download_mod)
        self.ui.ModsList.itemSelectionChanged.connect(self.load_mod_page)
        self.ui.OpenPageButton.clicked.connect(self.open_mod_page)

        # server list buttons ======================================================== #
        self.ui.AddServerButton.clicked.connect(self.show_add_server_dialog)
        self.ui.JoinServerButton.clicked.connect(self.join_selected_server)
        self.ui.DeleteServerButton.clicked.connect(self.delete_selected_server)
        self.ui.EditServerButton.clicked.connect(self.open_server_editor)
        self.ui.JoinAddressButton.clicked.connect(self.join_from_ip)
        self.ui.RefreshButton.clicked.connect(self.query_ms)
        self.ui.JoinMasterServerButton.clicked.connect(self.join_ms_selection)
        self.ui.SaveMSButton.clicked.connect(self.save_ms_selection)

        # play button ================================================================ #
        self.ui.GamePlayButton.clicked.connect(self.launch_game_normally)
        # self.ui.GameOptionsDropDownButton.clicked.connect()
        self.gameOptionsDropDownMenu = QMenu()
        self.gameOptionsDropDownMenu.addAction("Save current parameters to script", self.export_script)
        self.ui.GameOptionsDropDownButton.setMenu(self.gameOptionsDropDownMenu)
        self.ui.GameOptionsDropDownButton.clicked.connect(self.show_game_options_dropdown)

        # load news feed from srb2.org =============================================== #
        self.load_news()

        # and then add the spacer at the bottom
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_20.addItem(spacerItem)
        
    def open_url(self, url):
        webbrowser.open(url)

    def show_game_options_dropdown(self):
        menu = QMenu()
        menu.addAction("Save current parameters to script", self.export_script)
        menu.exec()

    def load_news(self):
        # ok lets uh, get the news feed or something?
        srb2_rss_url = "https://www.srb2.org/feed/"

        feed = feedparser.parse(srb2_rss_url)
        items = feed["items"]

        for item in items:
            # title
            article_title_label = QtWidgets.QLabel(self.ui.NewsScrollAreaContent)
            article_title_label.setStyleSheet("font-size: 14pt;")
            url_link = "<a href=\"" + item["link"] + "\" style=\"color: #ddd;\">" + item["title"] + "</a>"
            article_title_label.setText(QtCore.QCoreApplication.translate("MainWindow", url_link))
            article_title_label.setOpenExternalLinks(True)
            self.ui.verticalLayout_20.addWidget(article_title_label)

            # author name and date
            author_name_label = QtWidgets.QLabel(self.ui.NewsScrollAreaContent)
            author_name_label.setStyleSheet("font-weight: 400;")
            author_name_label.setText(item["author"] + " - " + item["published"].replace(" +0000", ""))
            self.ui.verticalLayout_20.addWidget(author_name_label)

            # snippet
            info_label = QtWidgets.QLabel(self.ui.NewsScrollAreaContent)
            info_label.setStyleSheet("font-weight: 400;")
            info_label.setText("<div style=\"text-wrap: wrap-word;\">" + item["summary"] + "</div>")
            info_label.setWordWrap(True)
            info_label.adjustSize()
            info_label.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.ui.verticalLayout_20.addWidget(info_label)

    def show_add_server_dialog(self):
        self.childWindow = edit_server_main.ChildWindow(self, "", "", True)
        self.childWindow.show()
        return

    def change_skin_image(self):
        asset_img = ":/assets/img/sonic.png"
        self.ui.PlayerSkinInfoText.setText(char_text.sonic)
        if self.ui.PlayerSkinInput.currentIndex() == 2:
            asset_img = ":/assets/img/tails.png"
            self.ui.PlayerSkinInfoText.setText(char_text.tails)
        if self.ui.PlayerSkinInput.currentIndex() == 3:
            asset_img = ":/assets/img/knuckles.png"
            self.ui.PlayerSkinInfoText.setText(char_text.knux)
        if self.ui.PlayerSkinInput.currentIndex() == 4:
            asset_img = ":/assets/img/rosy.png"
            self.ui.PlayerSkinInfoText.setText(char_text.amy)
        if self.ui.PlayerSkinInput.currentIndex() == 5:
            asset_img = ":/assets/img/fang.png"
            self.ui.PlayerSkinInfoText.setText(char_text.fang)
        if self.ui.PlayerSkinInput.currentIndex() == 6:
            asset_img = ":/assets/img/metal.png"
            self.ui.PlayerSkinInfoText.setText(char_text.metal)

        self.ui.PlayerSkinImage.setPixmap(
            QtGui.QPixmap(asset_img).scaled(135,
                                            190,
                                            QtCore.Qt.KeepAspectRatio,
                                            QtCore.Qt.FastTransformation))
        return

    def get_launch_command(self):
        """
        This converts all of the launcher inputs to a single-string command to 
        launch SRB2
        """
        ui = self.ui
        com = ""
        if self.ui.WineToggle.isChecked() and self.ui.WineToggle.isEnabled(): 
            com += "wine "
        com += "\"" + ui.GameExecFilePathInput.text() + "\""

        # game settings (from game settings tab) ============================= #
        if ui.GameRendererSetting.currentIndex() == 0: com += " +renderer 1"
        if ui.GameRendererSetting.currentIndex() == 1: com += " +renderer 2"
        if ui.GameFullscreenSetting.currentIndex() == 0: com += " +fullscreen 1"
        if ui.GameFullscreenSetting.currentIndex() == 1: com += " -borderless"
        if ui.GameFullscreenSetting.currentIndex() == 2: com += " -win"
        if ui.GameMusicSetting.currentIndex() == 0: com += " +digimusic On"
        if ui.GameMusicSetting.currentIndex() == 1: com += " +digimusic Off"
        if ui.GameMusicSetting.currentIndex() == 2: com += " -usecd"
        if ui.GameMusicSetting.currentIndex() == 3: com += " -nomusic"
        if ui.GameSoundSetting.currentIndex() == 1: com += " -nosound"
        if ui.GameHorizontalResolutionInput.text() != "" and ui.GameVerticalResolutionInput.text() != "":
            com += " -width " + ui.GameHorizontalResolutionInput.text() + " -height " \
                   + ui.GameVerticalResolutionInput.text()
        if ui.PlayerNameInput.text() != "": com += " +name \"" + ui.PlayerNameInput.text() + "\""
        if ui.PlayerColorInput.currentIndex() != 0:
            com += " +color " + str(ui.PlayerColorInput.currentText().lower())
        if ui.PlayerSkinInput.currentIndex() != 0:
            com += " +skin " + str(
            ui.PlayerSkinInput.currentText().lower().replace(" ", ""))

        # get all files ====================================================== #
        com += " -file"
        for i in range(ui.GameFilesList.count()):
            com += " \"" + ui.GameFilesList.item(i).text() + "\""

        # add a script ======================================================= #
        if ui.GameFilesExecScriptInput.text() != "": 
            com += " +exec " + ui.GameFilesExecScriptInput.text()

        # custom parameters ================================================== #
        if ui.GameArgsInput.text() != "": 
            com += " " + ui.GameArgsInput.text()

        return com

    def set_game_path(self):
        f, _ = QFileDialog.getExistingDirectory()
        if (f):
            #self.PathGameFilesExecScriptInput.setText(f)
            pass

    # Files tab

    def clear_files_list(self):
        self.ui.GameFilesList.clear()
        return

    def delete_selected_files(self):
        for item in self.ui.GameFilesList.selectedItems():
            self.ui.GameFilesList.takeItem(self.ui.GameFilesList.row(item))
        return

    def move_selected_files_up(self):
        for item in self.ui.GameFilesList.selectedItems():
            row = self.ui.GameFilesList.row(item)
            if row == 0: return
            c_item = self.ui.GameFilesList.takeItem(row)
            self.ui.GameFilesList.insertItem(row - 1, c_item)
            c_item.setSelected(True)
        return

    def move_selected_files_down(self):
        reservedItems = []
        row = 0
        for item in self.ui.GameFilesList.selectedItems():
            row = self.ui.GameFilesList.row(item)
            cItem = self.ui.GameFilesList.takeItem(row)
            reservedItems.append(cItem)
        for item in reservedItems:
            row += 1
            self.ui.GameFilesList.insertItem(row, item)
            item.setSelected(True)
        return

    def add_file(self, f):
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(os.path.basename(str(f)))
        new_item_icon = QtGui.QIcon()
        filetype = str(f).split(".")[-1]
        new_item_icon.addPixmap(QtGui.QPixmap(":/assets/img/filetypes/" + filetype + ".png"), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)
        new_item.setIcon(new_item_icon)
        self.ui.GameFilesList.addItem(new_item)
        return

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Open files to add to SRB2", "",
                                                "All compatible SRB2 files (*.pk3 *.wad *.lua *.soc)"
                                                ";;PK3 Files (*.pk3);;WAD Files (*.wad)"
                                                ";;Lua Files (*.lua);;SOC files (*.soc)",
                                                options=self.FileDialogOptions)
        if files:
            # add each file to the file list with icon =============================== #
            for f in files:
                self.add_file(f)
        return

    def save_file_list(self):
        # convert to json compatible list ============================================ #
        items = []
        for i in range(self.ui.GameFilesList.count()):
            items.append(self.ui.GameFilesList.item(i).text())

        # open a file dialog ========================================================= #
        f, _ = QFileDialog.getSaveFileName(self, "Save file list", "", "JSON files (*.json)",
                                           options=self.FileDialogOptions)
        if f:
            with open(f, 'w') as outfile:
                json.dump(items, outfile)
        return

    def load_file_list(self):
        # open file ================================================================== #
        f, _ = QFileDialog.getOpenFileName(self, "Open file list", "", "JSON files (*.json)",
                                           options=self.FileDialogOptions)
        if f:
            with open(f, 'r') as jsonFile:
                items = json.load(jsonFile)
                for item in items:
                    self.add_file(item)
        return

    #

    def set_exec_file_path(self):
        f, _ = QFileDialog.getOpenFileName(self, "Open script to execute on launch", "",
                                           "All compatible files (*.txt *.cfg);;All files (*)",
                                           options=self.FileDialogOptions)
        if (f):
            self.ui.GameFilesExecScriptInput.setText(f)

    def launch_game_normally(self):
        launchCommand = self.get_launch_command()
        os.system(launchCommand)
        return

    def change_main_tab(self, index):
        self.ui.MainTabsStackedWidget.setCurrentIndex(index)
        return

    def change_game_tab(self, index):
        self.ui.GameContentStackedWidget.setCurrentIndex(index)
        return

    # Mods browser
    
    def open_mod_page(self):
        mod = self.get_selected_mod()
        self.open_url(mod.url)
    
    def get_selected_mod(self):
        selection = self.ui.ModsList.currentItem().text()
        mod = self.mods_list[selection]
        return mod

    def download_mod(self):
        if self.mods_list:

            mod = self.get_selected_mod()
            mod.set_download_url()
            path = self.ui.GameExecFilePathInput.text()
            # TODO: delete next line
            path = "~/"
            self.ui.ModStatusLabel.setText("Downloading mod...")
            self.download_mod_url_sig.emit(mod.download_url)
            self.download_mod_path_sig.emit(path)

    def append_mod_to_list(self, mod_name):
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(mod_name)
        self.ui.ModsList.addItem(new_item)

    def load_mod_page(self):
        self.ui.ModStatusLabel.setText("Downloading mod description...")
        if self.mods_list:
            mod = self.get_selected_mod()
            self.ui.ModBrowser.load(mod.url)
        self.ui.ModStatusLabel.setText("Click on a mod to see more information.")
            # Alternatively, if we only want a mod description instead
            #   of the full web page:
            #self.mod_description_sig.emit(mod)

    def refresh_mods_list(self):
        # TODO: multithreading to get rid of lag
        self.ui.ModStatusLabel.setText("Downloading mods list...")
        self.ui.ModsList.clear()
        self.mod_list_sig.emit(self.ui.ModTypeCombo.currentText())

    def on_mod_description(self, mod):
        self.ui.ModStatusLabel.setText("Click on a mod to see more information.")
        self.ui.ModBrowser.setHtml(mod.description, mod.url)
        self.ui.ModBrowser.load(mod.url)

    def on_mod_list(self, mod_list):
        self.ui.ModStatusLabel.setText("Click on a mod to see more "
                                       "information.")
        self.ui.ModsList.clear()
        self.mods_list = mod_list
        for item in self.mods_list:
            self.append_mod_to_list(item)

    def add_mod_to_files(self, filepaths_list):
        self.ui.ModStatusLabel.setText("Click on a mod to see more information.")
        pass
        #for filepath in filepaths_list:
        #    self.add_file(filepath)

    # Master server browser

    def query_ms(self):
        self.ui.MSStatusLabel.setText("Downloading servers list...")
        self.ui.MasterServerList.clear()
        print("query_ms")
        self.query_ms_sig.emit(True)
    
    def on_server_list(self, server_list):
        self.ui.MSStatusLabel.setText('Click "Refresh" to download a list of '
                                      'servers.')
        print("on_server_list")
        del self.master_server_list
        self.master_server_list = {}
        for server in server_list:
            entry_label = '{} | Room: {} | Version: {}'.format(
                server.get("name"),
                server.get("room"),
                server.get("version"))
            new_item = QtWidgets.QListWidgetItem()
            new_item.setText(entry_label)
            self.ui.MasterServerList.addItem(new_item)
            self.master_server_list[entry_label] = server

    def join_ms_selection(self):
        selection = self.ui.MasterServerList.currentItem().text()
        ip_string = self.master_server_list[selection].get("ip")
        os.system(self.get_launch_command() + " -connect " + ip_string)
        return

    def save_ms_selection(self):
        selection = self.ui.MasterServerList.currentItem().text()
        server = self.master_server_list[selection]
        ip = server.get("ip")
        name = server.get("name")
        self.add_server_to_list(name, ip)

    # Saved servers

    def save_server_list(self):
        serv_list = []
        for i in range(len(self.saved_server_ips)):
            data = {"name": self.ui.ServerList.item(i).text(), "ip": self.saved_server_ips[i]}
            serv_list.append(data)
        with open("lb2ServerList.json", "w") as f:
            json.dump(serv_list, f)
        return

    def load_server_list(self):
        serv_list = []
        fpath = os.path.join(os.getcwd(), "lb2ServerList.json")
        if not os.path.isfile(fpath):
            return
        with open(fpath, "r") as f:
            serv_list = json.load(f)

        for server in serv_list:
            self.add_server_to_list(server["name"], server["ip"])
        return

    def add_server_to_list(self, name, ip):
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(name)
        self.saved_server_ips.append(ip)
        self.ui.ServerList.addItem(new_item)
        self.save_server_list()
        return

    def open_server_editor(self):
        ip = self.saved_server_ips[self.ui.ServerList.selectedIndexes()[0].row()]
        name = self.ui.ServerList.selectedItems()[0].text()
        self.childWindow = edit_server_main.ChildWindow(self, name, ip, False)
        self.childWindow.show()
        return

    def edit_selected_server(self, name, ip):
        self.saved_server_ips[self.ui.ServerList.selectedIndexes()[0].row()] = ip
        self.ui.ServerList.selectedItems()[0].setText(name)
        self.save_server_list()
        return

    def delete_server_from_list(self, index):
        self.saved_server_ips.pop(index)
        self.ui.ServerList.takeItem(index)
        self.save_server_list()
        return

    def delete_selected_server(self):
        self.delete_server_from_list(self.ui.ServerList.selectedIndexes()[0].row())
        return

    def join_selected_server(self):
        """Join current selected server in list
        """
        ipString = self.saved_server_ips[self.ui.ServerList.selectedIndexes()[0].row()]
        os.system(self.get_launch_command() + " -connect " + ipString)
        return

    def join_from_ip(self):
        """Join direct address
        """
        ipString = self.ui.JoinAddressInput.text
        os.system(self.get_launch_command() + " -connect " + ipString)
        return

    def start_server(self):
        """Join current selected server in list
        """
        launch_command = self.ui.GameExecFilePathInput.text() + " -server"
        if not self.ui.DedicatedServerToggle.isChecked:
            launch_command = self.get_launch_command()

        if self.ui.ServerNameInput.text() != "": launch_command += " +servername " + self.ui.ServerNameInput.text()
        if self.ui.AdminPasswordInput.text() != "": launch_command += " +password " + self.ui.AdminPasswordInput.text()
        if self.ui.RoomInput.currentIndex() != 0:
            launch_command += " -id "
            if self.ui.RoomInput.currentIndex() == 1: launch_command += "33"
            if self.ui.RoomInput.currentIndex() == 2: launch_command += "28"
            if self.ui.RoomInput.currentIndex() == 3: launch_command += "38"
            if self.ui.RoomInput.currentIndex() == 4: launch_command += "31"
        launch_command += " -gametype " + str(self.ui.GametypeInput.currentIndex())
        launch_command += " +advancemap " + str(self.ui.AdvanceMapInput.currentIndex())
        if "" != self.ui.PointLimitInput.text():
            launch_command += " +pointlimit " + self.ui.PointLimitInput.text()
        else:
            launch_command += " +pointlimit 1000"
        if self.ui.TimeLimitInput.text() != "":
            launch_command += " +timelimit " + self.ui.TimeLimitInput.text()
        else:
            launch_command += " +timelimit 0"
        if self.ui.MaxPlayersInput.text() != "":
            launch_command += " +maxplayers " + self.ui.MaxPlayersInput.text()
        else:
            launch_command += " +maxplayers 8"
        if (
                self.ui.ForceSkinInput.currentText() != ""):
            launch_command += " +forceskin " + self.ui.ForceSkinInput.currentText().lower().replace(
            " ", "")
        if self.ui.PortInput.text() != "":
            launch_command += " -port " + self.ui.PortInput.text()
        else:
            launch_command += " -port 5029"
        if self.ui.DisableWeaponsToggle.isChecked():
            launch_command += " +specialrings 1"
        else:
            launch_command += " +specialrings 0"
        if self.ui.SuddenDeathToggle.isChecked():
            launch_command += " +suddendeath 1"
        else:
            launch_command += " +suddendeath 0"
        if self.ui.DedicatedServerToggle.isChecked(): launch_command += " -dedicated"
        if self.ui.UploadToggle.isChecked():
            launch_command += " +downloading 1"
        else:
            launch_command += " +downloading 0"

        os.system(launch_command)
        return

    # Settings and profiles

    def closeEvent(self, e):
        self.save_all()
        return
    
    def save_all(self):
        self.save_global_settings_file()
        self.save_profile_file(self.get_current_profile_file())

    def applicationStarted(self):
        """Wait for window to fully start
        """
        # fix resolution of the image on the play tab ================================ #
        self.load_server_list()
        self.load_global_settings()
        self.load_current_profile()
        self.check_version()
        try:
            self.query_ms()  # populates master server list
        except:
            print("Querying master server failed.")

        # april fools day stuff
        if (fool):
            self.ui.PlayerSkinInput.setCurrentIndex(4)
            self.ui.PlayerColorInput.setCurrentIndex(57)
            self.ui.PlayerColorInput.setEnabled(False)
            self.ui.PlayerSkinInput.setEnabled(False)

        return

    def read_config_file(self, toml_file=global_settings_file):
        """This loads the global settings file, which is different from profiles
        """
        config_data = {}
        
        if not self.config_file_exists(toml_file):
            return None 
        
        config_data = toml.load(toml_file)

        return config_data

    def set_current_profile(self, profile):
        self.global_settings["current_profile"] = profile.key()
    
    def get_profile_name_list(self):
        return self.global_settings["profiles"].keys()
    
    def get_profile_file_list(self):
        return self.global_settings["profiles"].values()
    
    def verify_global_settings_integrity(self):
        """Verifies that profile files specified in the global settings file
        all exist.
        """
        pass
        # TODO
    
    def if_profile_name_already_exists(self, name):
        if name in self.get_profile_name_list():
            return True
        else:
            return False
    
    def if_profile_file_already_exists(self, file):
        if file in self.get_profile_file_list():
            return True
        else:
            return False
    
    def generate_new_profile_name(self):
        profile_name_list = self.get_profile_name_list()
        starter_name = "New Profile"
        count = 0
        while starter_name in profile_name_list:
            count += 1
        if count > 0:
            starter_name = "{} {}".format(starter_name, count)
        return starter_name
        
    def generate_new_profile_filename(self):
        profile_file_list = self.get_profile_file_list()
        starter_name = "new_profile"
        count = 0
        while starter_name in profile_file_list:
            count += 1
        if count > 0:
            starter_name = "{}_{}".format(starter_name, count)
        full_filename = starter_name + ".toml"
        return full_filename
    
    def add_new_profile(self):
        name = self.generate_new_profile_name()
        filename = self.generate_new_profile_filename()
        self.global_settings["profiles"][name] = filename
        self.add_profiles_to_combobox()
        self.save_profile_file(filename)
        self.load_different_profile(name)
        
    def start_typing_timer(self):
        """Wait until there are no changes for 1 second before making changes."""
        self.typing_timer.start(1000)

    def alter_profile_info(self):
        old_profile = self.global_settings["current_profile"]
        old_filename = self.global_settings["profiles"][old_profile]
        new_name = self.ui.ProfileNameInput.text()
        new_filename = new_name.lower().replace(" ", "_") + ".toml"
        self.ui.ProfileFilenameInput.setText(new_filename)
        self.global_settings["profiles"].pop(old_profile)
        self.global_settings["profiles"][new_name] = new_filename
        self.global_settings["current_profile"] = new_name
        self.save_global_settings_file()
        self.save_profile_file(new_filename)
        # Delete old profile file:
        os.remove(old_filename)

    def add_profiles_to_combobox(self):
        profiles = self.get_profile_name_list()
        self.ui.GameProfileComboBox.clear()
        self.ui.GameProfileComboBox.addItems(profiles)
        self.ui.GameProfileComboBox.setCurrentText(self.global_settings["current_profile"])

    def load_global_settings(self):
        if not self.global_settings_exist():
            self.create_settings_on_first_run()
            print("Creating settings on first run!")
        
        toml_settings = self.read_config_file(global_settings_file)
        self.global_settings = toml_settings
        self.add_profiles_to_combobox()
        current_profile_file = self.get_current_profile_file()
        self.current_profile_settings = self.read_config_file(
            current_profile_file)
        self.ui.ProfileFilenameInput.setText(current_profile_file)
        self.ui.ProfileNameInput.setText(self.global_settings["current_profile"])
    
    def get_current_profile_file(self):
        return self.global_settings["profiles"].get(
            self.global_settings["current_profile"])
    
    def default_profile_exists(self):
        if self.global_settings == None:
            return False
        else:
            if not self.config_file_exists(self.get_current_profile_file()):
                return False
            else:
                return True
    
    def global_settings_exist(self):
        if not self.config_file_exists(global_settings_file):
            return False
        else:
            return True
    
    def config_file_exists(self, config_file):
        fpath = os.path.join(os.getcwd(), config_file)
        #fpath = config_file
        if not os.path.isfile(fpath):
            return False
        else:
            return True
    
    def is_first_run(self):
        if not self.global_settings_exist():
            return True
        elif not self.default_profile_exists():
            return True
        else:
            return False
    
    def find_profile_files_in_dir(self):
        """Finds all profile .toml files in a directory
        """
        profile_dir = "./"
        profile_files = []
        for file in os.listdir(profile_dir):
            if file.endswith("profile.toml"):
                profile_files.append(file)
        return profile_files
    
    def save_global_settings_file(self):
        """This saves the global settings, which is different from profiles
        """
        with open(global_settings_file, "w") as f:
            new_toml_string = toml.dump(self.global_settings, f)
        print("saved config")
        return
    
    def create_settings_on_first_run(self):
        self.global_settings = {"current_profile": "Default",
                                "profiles": 
                                    {"Default": "default_profile.toml"}
                                }
        self.save_global_settings_file()
        self.save_profile_file(self.get_current_profile_file())
    
    def load_current_profile(self):
        if not self.default_profile_exists():
            self.create_settings_on_first_run()
            print("Creating settings on first run!")
        self.current_profile_settings = self.read_config_file(
            self.get_current_profile_file())
        self.apply_profile_settings_to_gui(self.current_profile_settings)
        
    def load_different_profile(self, profile):
        profile_settings = self.read_config_file(profile.value())
        self.apply_profile_settings_to_gui(profile_settings)
        self.set_current_profile(profile)
        
    def get_profile_dict_from_file(self, profile_filename):
        """Gets profile settings as a dictionary from a profile TOML file

        Args:
            profile_filename (str): the profile;s TOML filename

        Returns:
            dict: profile settings as a dictionary
        """
        return self.read_config_file(profile_filename)

    def apply_profile_settings_to_gui(self, profile_settings_dict):
        """Takes profile settings dictionary and applies to the GUI state

        Args:
            profile_settings_dict (dict): A dictionary created from a
            profile TOML file
        """
        # now set all elements to their saved values
        self.ui.PlayerNameInput.setText(profile_settings_dict["player"]["name"])
        self.ui.PlayerSkinInput.setCurrentText(profile_settings_dict["player"]["skin"])
        self.ui.PlayerColorInput.setCurrentIndex(profile_settings_dict["player"]["color"])
        self.ui.GameHorizontalResolutionInput.setText(profile_settings_dict["game"]["resolution"]["width"])
        self.ui.GameVerticalResolutionInput.setText(profile_settings_dict["game"]["resolution"]["height"])
        self.ui.GameRendererSetting.setCurrentIndex(profile_settings_dict["game"]["renderer"])
        self.ui.GameFullscreenSetting.setCurrentIndex(profile_settings_dict["game"]["windowmode"])
        self.ui.GameMusicSetting.setCurrentIndex(profile_settings_dict["game"]["music"])
        self.ui.GameSoundSetting.setCurrentIndex(profile_settings_dict["game"]["sound"])
        self.ui.GameExecFilePathInput.setText(profile_settings_dict["game"]["exepath"])
        self.ui.GameArgsInput.setText(profile_settings_dict["game"]["cliargs"])
        self.ui.ServerNameInput.setText(profile_settings_dict["host"]["hostname"])
        self.ui.AdminPasswordInput.setText(profile_settings_dict["host"]["password"])
        self.ui.RoomInput.setCurrentIndex(profile_settings_dict["host"]["room"])
        self.ui.GametypeInput.setCurrentIndex(profile_settings_dict["host"]["gametype"])
        self.ui.AdvanceMapInput.setCurrentIndex(profile_settings_dict["host"]["advancemap"])
        self.ui.PointLimitInput.setText(profile_settings_dict["host"]["pointlimit"])
        self.ui.TimeLimitInput.setText(profile_settings_dict["host"]["timelimit"])
        self.ui.MaxPlayersInput.setText(profile_settings_dict["host"]["maxplayers"])
        self.ui.ForceSkinInput.setCurrentText(profile_settings_dict["host"]["forceskin"])
        self.ui.DisableWeaponsToggle.setChecked(profile_settings_dict["host"]["disableweaponrings"])
        self.ui.SuddenDeathToggle.setChecked(profile_settings_dict["host"]["suddendeath"])
        self.ui.DedicatedServerToggle.setChecked(profile_settings_dict["host"]["dedicated"])
        self.ui.WineToggle.setChecked(profile_settings_dict["settings"]["wine"])
        self.ui.LauncherThemeInput.setCurrentIndex(profile_settings_dict["settings"]["theme"])
        self.ui.SaveFilesToConfigToggle.setChecked(profile_settings_dict["settings"]["includefiles"])

        if self.ui.SaveFilesToConfigToggle.isChecked:
            for f in profile_settings_dict["files"]:
                self.add_file(f)

        self.change_skin_image()
    
    def generate_profile_dict(self):
        """Converts GUI state to a settings dictionary
        """
        toml_settings = {"files": [], "player": {}, "game": {"resolution": {}}, "host": {}, "settings": {}}
        toml_settings["player"]["name"] = self.ui.PlayerNameInput.text()
        toml_settings["player"]["skin"] = str(self.ui.PlayerSkinInput.currentText())
        toml_settings["player"]["color"] = self.ui.PlayerColorInput.currentIndex()
        toml_settings["game"]["resolution"]["width"] = self.ui.GameHorizontalResolutionInput.text()
        toml_settings["game"]["resolution"]["height"] = self.ui.GameVerticalResolutionInput.text()
        toml_settings["game"]["renderer"] = self.ui.GameRendererSetting.currentIndex()
        toml_settings["game"]["windowmode"] = self.ui.GameFullscreenSetting.currentIndex()
        toml_settings["game"]["music"] = self.ui.GameMusicSetting.currentIndex()
        toml_settings["game"]["sound"] = self.ui.GameSoundSetting.currentIndex()
        toml_settings["game"]["exepath"] = self.ui.GameExecFilePathInput.text()
        toml_settings["game"]["cliargs"] = self.ui.GameArgsInput.text()
        toml_settings["host"]["hostname"] = self.ui.ServerNameInput.text()
        toml_settings["host"]["password"] = self.ui.AdminPasswordInput.text()
        toml_settings["host"]["room"] = self.ui.RoomInput.currentIndex()
        toml_settings["host"]["gametype"] = self.ui.GametypeInput.currentIndex()
        toml_settings["host"]["advancemap"] = self.ui.AdvanceMapInput.currentIndex()
        toml_settings["host"]["pointlimit"] = self.ui.PointLimitInput.text()
        toml_settings["host"]["timelimit"] = self.ui.TimeLimitInput.text()
        toml_settings["host"]["maxplayers"] = self.ui.MaxPlayersInput.text()
        toml_settings["host"]["forceskin"] = str(self.ui.ForceSkinInput.currentText())
        toml_settings["host"]["disableweaponrings"] = self.ui.DisableWeaponsToggle.isChecked()
        toml_settings["host"]["suddendeath"] = self.ui.SuddenDeathToggle.isChecked()
        toml_settings["host"]["dedicated"] = self.ui.DedicatedServerToggle.isChecked()
        toml_settings["settings"]["wine"] = self.ui.WineToggle.isChecked()
        toml_settings["settings"]["theme"] = self.ui.LauncherThemeInput.currentIndex()
        toml_settings["settings"]["includefiles"] = self.ui.SaveFilesToConfigToggle.isChecked()

        for i in range(self.ui.GameFilesList.count()):
            toml_settings["files"].append(self.ui.GameFilesList.item(i).text())
        
        return toml_settings
    
    def save_profile_file(self, filename):
        """This takes GUI state, converts to a dictionary, and saves the 
        variables to a TOML file.
        """
        # generate the json data for the config
        
        toml_settings = self.generate_profile_dict()
        
        with open(filename, "w") as f:
            new_toml_string = toml.dump(toml_settings, f)

        print("saved profile file")
        return

    def apply_style(self):
        # set up the launcher theme
        if not self.current_profile_settings:
            self.setStyleSheet(themes.main + themes.dark)
            return

        if self.current_profile_settings["settings"]["theme"] == 0: 
            chosentheme = themes.dark
        if self.current_profile_settings["settings"]["theme"] == 1: 
            chosentheme = themes.light
        if self.current_profile_settings["settings"]["theme"] == 2: 
            chosentheme = themes.blue
        if self.current_profile_settings["settings"]["theme"] == 3: 
            chosentheme = themes.orange
        if self.current_profile_settings["settings"]["theme"] == 4: 
            chosentheme = themes.red
        if self.current_profile_settings["settings"]["theme"] == 5: 
            chosentheme = themes.pink
        if self.current_profile_settings["settings"]["theme"] == 6: 
            chosentheme = themes.lightsout

        # april fools day stuff. pls dont spoil for others!11!1
        if (fool):
            chosentheme = themes.pink

        self.setStyleSheet(themes.main + chosentheme)
        return

    # Misc

    def export_script(self):
        file_filter = "Batch files (*.bat);;Shell scripts (*.sh)"
        if (os.name == "posix"):
            file_filter = "Shell scripts (*.sh);;Batch files (*.bat)"
        file_filter += ";;All files (*)"
        fileName, _ = QFileDialog.getSaveFileName(self, "Save script", os.getcwd(), file_filter)
        if fileName:
            out_text = ""
            if fileName.endswith(".sh"): out_text += "#!bin/bash\n"
            out_text += self.get_launch_command()
            with open(fileName, "w") as f:
                f.write(out_text)
        return

    def check_version(self):
        print("checking version")

        link = "https://hitcoder-test.neocities.org/launcherblast-version.html"
        try:
            f = urllib.request.urlopen(link, timeout=100)
        except:
            print("Version check error")
            return

        my_file = f.read()
        version_got = (str(my_file).replace("b'", "").replace("\\n'", ""))
        print("Latest: " + version_got)
        print("Current: " + versionString)
        ver_num = version_got.replace("reBoot-", "")

        # check launcher version ============================================= #
        if float(ver_num) > float(versionString.replace("reBoot-", "")):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("There is a new version available. Please check the SRB2 Message Board.")
            msg.setWindowTitle("Launcher update")
            msg.setDetailedText("Running: " + versionString + "\nLatest: " + version_got)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif float(ver_num) < float(versionString.replace("reBoot-", "")):
            print("Greetings, time traveller.")
        else:
            print("up-to-date (" + versionString + ")")


def main():
    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()
    t = QtCore.QTimer()
    t.singleShot(0, w.applicationStarted)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
