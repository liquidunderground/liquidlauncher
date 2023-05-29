import json
import os
import sys
import webbrowser
from packaging import version # for version checks
import urllib
import urllib.parse
import toml
from datetime import date
from urllib.request import urlretrieve

import feedparser
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog, QMenu, QInputDialog, QDialogButtonBox, QMessageBox
from PySide6.QtCore import Signal

import char_text
from ll_threading import QueryMessageBoard, QueryMasterServer, ModDownloader
from ll_ui import *
from qss import themes

fool = date.today() == date(date.today().year, 4, 1)

versionString = "1.0b1"
global_settings_file = "ll_settings.toml"


class MainWindow(QMainWindow):
    # Emits instance of Mod() class from self.mods_list
    mod_description_sig = Signal(object)
    # Emits self.mods_list
    mod_list_sig = Signal(str)
    # Emits bool, telling QThread to query the master server
    query_ms_sig = Signal(bool)
    # Emits mod download URL string
    download_mod_url_sig = Signal(str)
    # Emits mod download filepath
    download_mod_path_sig = Signal(str)
    

    def __init__(self, app):
        super().__init__()
        
        # Default Launcher settings. Profiles are filenames read from profiles_dir
        self.global_settings = {"current_profile": "default.toml",
                                "profiles_dir": os.path.join(os.getcwd(), "ll_profiles"),
                                "current_ms":{
                                    "url": "http://mb.srb2.org/MS/0",
                                    "api": "v1",
                                },
                                "modsources": {
                                    "srb2mb": True,
                                    "workshop_blue": False,
                                    "workshop_red": False,
                                    "wadarchive": False,
                                    "skybase": False,
                                    "gamebanana": False
                                    },
                                "rss": [
                                    "https://srb2.org/feed",
                                    "https://sonicstadium.org/feed",
                                    "https://nitter.net/SonicTeamJr/rss",
                                    "https://nitter.net/SRB2Workshop/rss",
                                    ]
                                }
        self.current_profile_settings = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app = app
        self.setWindowTitle("LiquidLauncher "+versionString)

        # server ips stored internally so u don't dox people's ips if you're streaming or smth
        self.saved_server_ips = []

        # Dict associate master server widget items with server data
        self.master_server_list = {}
        self.ms_list = {}

        # RSS Article cache
        self.news = {}

        # Dict associating mod list widget items with mods:
        self.mods_list = {}

        # MB Query Multithreading
        self.mb_qthread = QueryMessageBoard(self)
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
        self.ms_qthread = QueryMasterServer(self)
        self.ms_qthread.start()
        self.query_ms_sig.connect(self.ms_qthread.on_refresh)
        self.ms_qthread.server_list_sig1.connect(self.on_server_list)
        
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
        #self.ui.ServerList.clear()
        self.ui.SavedNetgameTable.setRowCount(0)

        # dock "tabs" ================================================================ #
        self.ui.NewsTabButton.clicked.connect(lambda: self.change_main_tab(0))
        self.ui.GameTabButton.clicked.connect(lambda: self.change_main_tab(1))
        self.ui.HelpTabButton.clicked.connect(lambda: self.change_main_tab(2))
        self.ui.SettingsTabButton.clicked.connect(lambda: self.change_main_tab(3))

        # game "tabs" ================================================================ #
        self.ui.GamePageTabList.currentRowChanged.connect(self.change_game_tab)

        # profile buttons ======================================================= #
        self.ui.ProfileDirBrowseButton.clicked.connect(self.set_game_path)
        self.ui.ProfilesAddButton.clicked.connect(self.add_profile)
        self.ui.ProfilesDeleteButton.clicked.connect(self.confirm_delete_profile)
        self.ui.ProfilesRefreshButton.clicked.connect(self.refresh_profiles)
        self.ui.ProfilesSaveButton.clicked.connect(lambda: self.save_profile_file(self.ui.GameProfileComboBox.currentText()))
        #self.ui.GameProfileComboBox.currentIndexChanged.connect(self.set_current_profile)
        self.ui.GameProfileComboBox.currentTextChanged.connect(self.set_current_profile)
        #self.ui.ProfileDirBrowseButton.clicked.connect(self.set_game_path)

        # Launch sript export buttons ================================================ #
        self.ui.ExportServerScriptButton.clicked.connect(self.export_script)
        self.ui.ExportClientScriptButton.clicked.connect(self.export_script)

        # game settings buttons ========================================================= #
        self.ui.GameExecFilePathBrowse.clicked.connect(self.set_game_exec_path)

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
        #self.ui.AddServerButton.clicked.connect(self.show_add_server_dialog)
        self.ui.AddServerButton.clicked.connect(self.add_new_server_to_list)
        self.ui.JoinBookmarkButton.clicked.connect(self.join_selected_netgame_bookmark)
        self.ui.BrowseNetgameJoinButton.clicked.connect(self.join_selected_netgame_browse)
        self.ui.DeleteServerButton.clicked.connect(self.delete_selected_server)
        self.ui.BrowseMSCombobox.currentTextChanged.connect(self.change_current_ms)
        self.ui.BrowseNetgameTable.itemDoubleClicked.connect(self.join_selected_netgame_browse)
        # Stubbed to make it editable
        #self.ui.SavedNetgameTable.itemDoubleClicked.connect(self.join_selected_netgame_bookmark)
        #
        #self.ui.BrowseMSCombobox.clicked.connect(self.change_current_ms)
        #self.ui.EditServerButton.clicked.connect(self.open_server_editor)
        self.ui.JoinAddressButton.clicked.connect(self.join_from_ip)
        self.ui.RefreshButton.clicked.connect(self.query_ms)
        #self.ui.JoinMasterServerButton.clicked.connect(self.join_ms_selection)
        self.ui.SaveNetgameButton.clicked.connect(self.save_ms_selection)

        # RSS feed controls ======================================================== #
        self.ui.RSSRefreshButton.clicked.connect(lambda: self.load_news(str(self.ui.RSSFeedCombobox.currentText())))
        self.ui.RSSFeedCombobox.lineEdit().returnPressed.connect(lambda: self.load_news(str(self.ui.RSSFeedCombobox.currentText())))
        self.ui.RSSViewonlineButton.clicked.connect(self.view_article_online)
        self.ui.RSSArticleList.doubleClicked.connect(self.view_article_online)
        self.ui.RSSArticleList.currentRowChanged.connect(self.load_article)

        # modsources checkboxes ================================================================ #
        self.ui.ModsourceMBCheckbox.clicked.connect(self.update_modsources)
        self.ui.ModsourceWSBlueCheckbox.clicked.connect(self.update_modsources)
        self.ui.ModsourceWSRedCheckbox.clicked.connect(self.update_modsources)

        # MS table buttons ======================================================== #
        self.ui.MSAddButton.clicked.connect(self.add_new_ms_to_list)
        self.ui.MSRemoveButton.clicked.connect(self.remove_ms_from_list)
        self.ui.MSListSaveButton.clicked.connect(self.save_ms_list)
        self.ui.MSVisitrepoButton.clicked.connect(lambda: self.open_url("https://github.com/liquidunderground/configs-public"))

        # RSS buttons ======================================================== #
        self.ui.RSSFeedList.itemSelectionChanged.connect(self.rss_enable_edit)
        self.ui.RSSFeedList.itemChanged.connect(self.rss_commit)
        #self.ui.RSSFeedList.dataChanged.connect(self.rss_commit)
        self.ui.RSSMoveupButton.clicked.connect(self.rss_moveup)
        self.ui.RSSMovedownButton.clicked.connect(self.rss_movedown)
        self.ui.RSSAddButton.clicked.connect(lambda: self.add_rss_to_list() )
        self.ui.RSSRemoveButton.clicked.connect( self.remove_rss_from_list )

        # play button ================================================================ #
        self.ui.GamePlayButton.clicked.connect(self.launch_game_normally)

        # ====== Launch section =======
        # load news feed from srb2.org =============================================== #
        self.load_news()

        # Load MSes to be used
        self.load_ms_list()
        

    # RSS Functions

    def rss_enable_edit(self):
        self.ui.RSSMoveupButton.setEnabled(True)
        self.ui.RSSMovedownButton.setEnabled(True)
        self.ui.RSSRemoveButton.setEnabled(True)

    def add_rss_to_list(self, url="https://example.com/feed" ):
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(url)
        new_item.setFlags(  QtCore.Qt.ItemIsSelectable | 
                            QtCore.Qt.ItemIsEditable |
                            QtCore.Qt.ItemIsDragEnabled |
                            QtCore.Qt.ItemIsDropEnabled |
                            QtCore.Qt.ItemIsEnabled
                            )
        self.ui.RSSFeedList.addItem(new_item)
        self.ui.RSSFeedList.setCurrentRow(self.ui.RSSFeedList.count()-1)
        self.rss_commit()

    def remove_rss_from_list(self):
        # QListWidget.takeItem bc Qt is weird
        self.ui.RSSFeedList.takeItem( self.ui.RSSFeedList.currentRow() )
        self.rss_commit()

    def rss_moveup(self):
        reservedItems = []
        row = self.ui.RSSFeedList.currentRow()
        item = self.ui.RSSFeedList.takeItem(row)
        row -= 1
        self.ui.RSSFeedList.insertItem(row, item)
        self.ui.RSSFeedList.setCurrentRow(row)
        self.rss_commit()
        return

    def rss_movedown(self):
        reservedItems = []
        row = self.ui.RSSFeedList.currentRow()
        item = self.ui.RSSFeedList.takeItem(row)
        row += 1
        self.ui.RSSFeedList.insertItem(row, item)
        self.ui.RSSFeedList.setCurrentRow(row)
        self.rss_commit()
        return

    # Default functions

    def open_url(self, url):
        webbrowser.open(url)

    def show_game_options_dropdown(self):
        menu = QMenu()
        menu.addAction("Save current parameters to script", self.export_script)
        menu.exec()

    def load_news(self, feed="https://www.srb2.org/feed/"):
        # ok lets uh, get the news feed or something?
        print("load_news({})".format(feed))

        try:
            msg = "Select an article to view."
            self.ui.RSSArticleList.clear()
            self.ui.RSSStatusLabel.setText("Querying RSS feed...")
            feed = feedparser.parse(feed)
            if len(feed["items"]) < 1:
                raise IndexError("No news found. Did you check the URL?")

            self.news = feed["items"]

            print("Parsing articles...")
            for item in self.news:
                self.ui.RSSArticleList.addItem("{} (by {})".format(item.title, item.author))
        except Exception as e:
            msg = str(e)
        self.ui.RSSStatusLabel.setText(msg)
        print(msg)

    def load_article(self, index):
        self.ui.RSSViewonlineButton.setEnabled(True);
        if hasattr(self.news[index], "content"):
            self.ui.RSSArticleView.setHtml(self.news[index].content[0].value)
        else:
            self.ui.RSSArticleView.setHtml("<h1>{}</h1>"
                                           "<p><img src=\":/assets/img/icons/about.png\" /></p>"
                                           "<p>No content available. This "
                                           "is most likely an issue with "
                                           "your RSS/Atom feed, not with "
                                           "your Liquid Launcher</p>"
                                           "<a href={}>View online</a>"
                                           .format(self.news[index].title, self.news[index].link))

    def view_article_online(self, index):
        idx = self.ui.RSSArticleList.currentRow()
        self.open_url(self.news[idx].link)

    def show_add_server_dialog(self):
        self.childWindow = edit_server_main.ChildWindow(self, "", "", True)
        self.childWindow.show()
        return

    def add_new_server_to_list(self): 
        print("add_new_server_to_list")
        self.add_server_to_list("Dummy Server", "127.0.0.1", "5029")
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

    def get_client_launch_command(self):
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

        print("CLIENT COMMAND: {}".format(com))
        return com

    def get_server_launch_command(self):
        """Launch server
        """
        launch_command = self.ui.GameExecFilePathInput.text() + " -server"
        if not self.ui.DedicatedServerToggle.isChecked:
            launch_command = self.get_client_launch_command()

        if self.ui.ServerNameInput.text() != "": launch_command += " +servername  \"{}\"".format(self.ui.ServerNameInput.text())
        if self.ui.AdminPasswordInput.text() != "": launch_command += " +password \"{}\"".format(self.ui.AdminPasswordInput.text())
        if self.ui.HostMSCombobox.currentText() != "": launch_command += " +masterserver \"{}\"".format(self.ui.HostMSCombobox.currentText())
        # TODO: Live Master Server room queries
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

        print("SERVER COMMAND: {}".format(launch_command))
        return launch_command

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

    def set_game_exec_path(self):
        f, _ = QFileDialog.getOpenFileName(self, "Open script to execute on launch", "",
                                           "All compatible files (*.exe *.elf);;All files (*)",
                                           options=self.FileDialogOptions)
        if (f):
            self.ui.GameExecFilePathInput.setText(f)

    def set_exec_file_path(self):
        f, _ = QFileDialog.getOpenFileName(self, "Open script to execute on launch", "",
                                           "All compatible files (*.txt *.cfg);;All files (*)",
                                           options=self.FileDialogOptions)
        if (f):
            self.ui.GameFilesExecScriptInput.setText(f)

    def launch_game_normally(self):
        launchCommand_client = self.get_client_launch_command()
        launchCommand_server = self.get_server_launch_command()

        # Check mode: Hosting?
        if self.ui.GamePageTabList.currentRow() == 3:
            os.system(launchCommand_server)
        else:
            os.system(launchCommand_client)
        return

    def change_main_tab(self, index):
        self.ui.MainTabsStackedWidget.setCurrentIndex(index)
        return

    def change_game_tab(self, index):
        self.ui.GameContentStackedWidget.setCurrentIndex(index)
        # Check mode: Hosting? -> Adjust GamePlayButton text
        if self.ui.GamePageTabList.currentRow() == 3:
            self.ui.GamePlayButton.setText("LAUNCH SERVER")
        else:
            self.ui.GamePlayButton.setText("PLAY")
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
        self.ui.OpenPageButton.setEnabled(True)
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

    def change_current_ms(self, newText):
        print("change_current_ms({})".format(newText))
        try:
            if newText == "":
                return
            print("> old current_ms: ", self.global_settings.get("current_ms", "<NONE>"))
            self.global_settings["current_ms"] = self.ms_list[newText];
            print("> new current_ms: ", self.global_settings.get("current_ms", "<NONE>"))
            self.query_ms()
        except Exception as e:
            print("Unable to change MS: ",e)


    def query_ms(self):
        print("query_ms")
        self.ui.MSStatusLabel.setText("Downloading netgame list...")
        #self.ui.MasterServerList.clear()
        self.ui.BrowseNetgameTable.setRowCount(0)
        self.query_ms_sig.emit(True)
    
    def on_server_list(self, server_list):
        self.ui.MSStatusLabel.setText('Click "Refresh" to download a list of '
                                      'servers.')
        print("on_server_list")
        del self.master_server_list
        self.master_server_list = {}
        for server in server_list:
            entry_label = '{} | Room: {} | Version: {} | Origin: {}'.format(
                server.get("name"),
                server.get("room"),
                server.get("version"),
                server.get("origin") 
                )
            #entry_label = '{}:{}'.format(
                #server.get("ip"),
                #server.get("port"),
                #server.get("version"))
            new_item = QtWidgets.QListWidgetItem()
            new_item.setText(entry_label)
            #self.ui.MasterServerList.addItem(new_item)
            # Create new row & fill with data
            #new_row = QtWidgets.QTableWidgetItem()
            #self.ui.BrowseNetgameTable.addItem(new_row)
            self.ui.BrowseNetgameTable.insertRow( self.ui.BrowseNetgameTable.rowCount() )
            twi_name = QtWidgets.QTableWidgetItem(server.get("name"))
            twi_room = QtWidgets.QTableWidgetItem(server.get("room"))
            twi_version = QtWidgets.QTableWidgetItem(server.get("version"))
            twi_gametype = QtWidgets.QTableWidgetItem(server.get("gametype"))
            twi_origin = QtWidgets.QTableWidgetItem(server.get("origin")) 

            twi_name.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
            twi_room.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
            twi_version.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
            twi_gametype.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
            twi_origin.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )

            self.ui.BrowseNetgameTable.setItem( self.ui.BrowseNetgameTable.rowCount()-1 , 0, twi_name )
            self.ui.BrowseNetgameTable.setItem( self.ui.BrowseNetgameTable.rowCount()-1 , 3, twi_room )
            self.ui.BrowseNetgameTable.setItem( self.ui.BrowseNetgameTable.rowCount()-1 , 2, twi_version )
            self.ui.BrowseNetgameTable.setItem( self.ui.BrowseNetgameTable.rowCount()-1 , 1, twi_gametype )
            self.ui.BrowseNetgameTable.setItem( self.ui.BrowseNetgameTable.rowCount()-1 , 4, twi_origin)

            self.master_server_list[entry_label] = server

        self.ui.BrowseNetgameTable.resizeColumnsToContents()

    def join_selected_netgame_browse(self):
        #selection = self.ui.BrowseNetgameTable.currentRow().text()
        #selection = '{}:{}'.format(
            #self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 3).text(),
            #self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 2).text() )
        selection = '{} | Room: {} | Version: {} | Origin: {}'.format(
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 0).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 3).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 2).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 4).text()
            )
        ip_string = '{}:{}'.format(
            self.master_server_list[selection].get("ip"),
            self.master_server_list[selection].get("port") )
        os.system(self.get_client_launch_command() + " -connect " + ip_string)
        return

    def save_ms_selection(self):
        #selection = '{} | Room: {} | Version: {}'.format(
            #self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 0).text(),
            #self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 3).text(),
            #self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 2).text() )
        # ID: ip:port
        selection = '{} | Room: {} | Version: {} | Origin: {}'.format(
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 0).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 3).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 2).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 4).text()
            )
        server = self.master_server_list[selection]
        ip = server.get("ip")
        name = self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 0).text()
        port = server.get("port")
        self.add_server_to_list(name, ip, port)

    # Saved servers

    def save_server_list(self):
        serv_list = []
        for i in range(len(self.saved_server_ips)):
            #data = {"name": self.ui.ServerList.item(i).text(), "ip": self.saved_server_ips[i]}
            data = {"name": self.ui.SavedNetgameTable.item(i, 0).text(),
                    "ip": self.ui.SavedNetgameTable.item(i, 1).text(),
                    "port": self.ui.SavedNetgameTable.item(i, 2).text()}
            serv_list.append(data)
        with open("netgames.json", "w") as f:
            json.dump(serv_list, f)
        return

    def load_server_list(self):
        serv_list = []
        fpath = os.path.join(os.getcwd(), "netgames.json")
        if not os.path.isfile(fpath):
            return
        with open(fpath, "r") as f:
            serv_list = json.load(f)

        for server in serv_list:
            self.add_server_to_list(server["name"], server["ip"], server["port"])
        return

    def add_server_to_list(self, name, ip, port):
        #new_item = QtWidgets.QListWidgetItem()
        #new_item.setText(name)
        self.saved_server_ips.append(ip)
        #self.ui.ServerList.addItem(new_item)
        # Stub until I can fill the data
        self.ui.SavedNetgameTable.insertRow(0)

        twi_title = QtWidgets.QTableWidgetItem(name)
        twi_ip = QtWidgets.QTableWidgetItem(ip)
        twi_port = QtWidgets.QTableWidgetItem(port)
        #twi_title.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        #twi_ip.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        self.ui.SavedNetgameTable.setItem( 0, 0, twi_title )
        self.ui.SavedNetgameTable.setItem( 0, 1, twi_ip )
        self.ui.SavedNetgameTable.setItem( 0, 2, twi_port )
        self.ui.BrowseNetgameTable.resizeColumnsToContents()

        self.save_server_list()
        self.ui.MSStatusLabel.setText('"{}" successfully bookmarked.'.format(name))
        return

    def open_server_editor(self):
        ip = self.saved_server_ips[self.ui.SavedNetgameTable.currentRow()]
        name = self.ui.ServerList.selectedItems()[0].text()
        #ip = self.saved_server_ips[self.ui.SavedNetgameTable.selectedIndexes()[0].row()]
        #name = self.ui.SavedNetgameTable.selectedItems()[0].text()
        self.childWindow = edit_server_main.ChildWindow(self, name, ip, False)
        self.childWindow.show()
        return

    def edit_selected_server(self, name, ip):
        self.saved_server_ips[self.ui.SavedNetgameTable.currentRow()] = ip
        # Is this even necessary if the table is editable?
        #self.ui.ServerList.currentRow().setText(name)
        self.ui.ServerList.setItem(self.ui.ServerList.currentRow(), 0).setText(name)
        #self.saved_server_ips[self.ui.SavedNetgameTable.selectedIndexes()[0].row()] = ip
        #self.ui.SavedNetgameTable.selectedItems()[0].setText(name)
        self.save_server_list()
        return

    def delete_server_from_list(self, index):
        self.saved_server_ips.pop(index)
        #self.ui.ServerList.takeItem(index)
        self.ui.SavedNetgameTable.removeRow(index)
        self.save_server_list()
        return

    def delete_selected_server(self):
        #self.delete_server_from_list(self.ui.ServerList.selectedIndexes()[0].row())
        self.delete_server_from_list( self.ui.SavedNetgameTable.currentRow() )
        return

    def join_selected_netgame_bookmark(self):
        """Join current selected server in list
        """
        #ipString = self.saved_server_ips[self.ui.ServerList.selectedIndexes()[0].row()]
        ipString = "{}:{}".format(
            self.ui.SavedNetgameTable.item( self.ui.SavedNetgameTable.currentRow(), 1 ).text(),
            self.ui.SavedNetgameTable.item( self.ui.SavedNetgameTable.currentRow(), 2 ).text(),
        )
        os.system(self.get_client_launch_command() + " -connect " + ipString)
        return

    def join_from_ip(self):
        """Join direct address
        """
        ipString = self.ui.JoinAddressInput.text()
        os.system(self.get_client_launch_command() + " -connect " + ipString)
        return

    # Saved Master Servers
    def update_ms_list_in_ui(self): 
        print("update_ms_list_in_ui")
        # Add combobox Mutex to avoid event loops
        self.ui.BrowseMSCombobox.blockSignals(True)
        self.ui.HostMSCombobox.blockSignals(True)

        self.ui.BrowseMSCombobox.clear()
        self.ui.HostMSCombobox.clear()
        # We only need the first column (names)
        rows = self.ui.MasterServersTable.rowCount()
        self.ui.BrowseMSCombobox.insertItem( 0, "All")
        for i in range(0, rows):
            ms_name = self.ui.MasterServersTable.item(i, 0).text()
            ms_url = self.ui.MasterServersTable.item(i, 1).text()
            self.ui.BrowseMSCombobox.insertItem( self.ui.BrowseMSCombobox.count(), ms_name)
            self.ui.HostMSCombobox.insertItem( self.ui.HostMSCombobox.count(), ms_url)

        self.ui.MasterServersTable.resizeColumnsToContents()

        # Remove combobox Mutex
        self.ui.HostMSCombobox.blockSignals(False)
        self.ui.BrowseMSCombobox.blockSignals(False)
        return

    def load_ms_list(self): 
        print("load_ms_list")
        self.ms_list = {}
        fpath = os.path.join(os.getcwd(), "masterservers.toml")
        if not os.path.isfile(fpath):
            return
        with open(fpath, "r") as f:
            self.ms_list = toml.load(f)["masterservers"]
            print("TOML Data: ", self.ms_list)

        self.ui.MasterServersTable.setRowCount(0)
        for ms in self.ms_list:
            print("MS list:", self.ms_list)
            self.add_ms_to_list(
                #self.ms_list[ms]["name"],
                ms,
                self.ms_list[ms]["url"],
                self.ms_list[ms]["api"],
                )

        self.update_ms_list_in_ui()
        return

    def save_ms_list(self): 
        print("save_ms_list")
        self.ms_list = {}
        for i in range(self.ui.MasterServersTable.rowCount()):
            #data = {"name": self.ui.ServerList.item(i).text(), "ip": self.saved_server_ips[i]}
            shim_name = ""
            shim_url = ""
            shim_api = ""

            if self.ui.MasterServersTable.item(i, 0) != None:
                shim_name = self.ui.MasterServersTable.item(i, 0).text()
            if self.ui.MasterServersTable.item(i, 1) != None:
                shim_url = self.ui.MasterServersTable.item(i, 1).text()
            if self.ui.MasterServersTable.item(i, 2) != None:
                shim_api = self.ui.MasterServersTable.item(i, 2).text()

            data = {"url": shim_url, "api": shim_api }
            self.ms_list[shim_name] = data
        with open("masterservers.toml", "w") as f:
            toml.dump({"masterservers": self.ms_list}, f)
        self.load_ms_list()
        return

    def add_new_ms_to_list(self): 
        print("add_new_ms_to_list")
        self.add_ms_to_list("Dummy MS", "http://localhost/v1", "v1")
        return

    def add_ms_to_list(self, name, url, api): 
        print("add_ms_to_list")
        self.ui.MasterServersTable.insertRow( self.ui.MasterServersTable.rowCount() )

        twi_name = QtWidgets.QTableWidgetItem(name)
        twi_url = QtWidgets.QTableWidgetItem(url)
        twi_api = QtWidgets.QTableWidgetItem(api)
        twi_name.setTextAlignment( Qt.AlignHCenter|Qt.AlignVCenter )
        twi_url.setTextAlignment( Qt.AlignHCenter|Qt.AlignVCenter )
        twi_api.setTextAlignment( Qt.AlignHCenter|Qt.AlignVCenter )

        self.ui.MasterServersTable.setItem( self.ui.MasterServersTable.rowCount()-1 , 0, twi_name )
        self.ui.MasterServersTable.setItem( self.ui.MasterServersTable.rowCount()-1 , 1, twi_url )
        self.ui.MasterServersTable.setItem( self.ui.MasterServersTable.rowCount()-1 , 2, twi_api )
        return

    def remove_ms_from_list(self): 
        print("remove_ms_from_list")
        self.ui.MasterServersTable.removeRow( self.ui.MasterServersTable.currentRow() )
        return

    #def change_ms_in_list(self, row, column): 
        #print("change_ms_in_ui: {} {}".format(row,column))
        ##return

    # Settings and profiles

    def closeEvent(self, e):
        self.save_all()
        return
    
    def save_all(self):
        self.save_global_settings_file()
        self.save_profile_file(self.global_settings["current_profile"])

    def applicationStarted(self):
        """Wait for window to fully start
        """
        # fix resolution of the image on the play tab ================================ #
        self.load_global_settings()
        self.load_server_list()
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

    def update_modsources(self):
        print("update_modsources()")
        # kludge. dunno where else to stuff it
        self.global_settings["modsources"].update({
                "srb2mb": self.ui.ModsourceMBCheckbox.isChecked(),
                "workshop_blue": self.ui.ModsourceWSBlueCheckbox.isChecked(),
                "workshop_red": self.ui.ModsourceWSRedCheckbox.isChecked(),
                "skybase": self.ui.ModsourceSkybaseCheckbox.isChecked(),
                "wadarchive": self.ui.ModsourceSkybaseCheckbox.isChecked(),
                "gamebanana": self.ui.ModsourceSkybaseCheckbox.isChecked(),
                })
        print(self.global_settings["modsources"])

    def set_current_profile(self, profile):
        # Stub check but might be handy
        iprofile = profile
        if isinstance(profile, int):
            iprofile = self.ui.GameProfileComboBox.itemText(profile)

        print("set_current_profile({})".format(iprofile))
        self.global_settings["current_profile"] = iprofile

        # Mutex lock for auto-updates
        self.ui.GameProfileComboBox.blockSignals(True)
        self.ui.GameProfileComboBox.setCurrentText(iprofile)
        self.ui.GameProfileComboBox.blockSignals(False)
        self.load_current_profile()
    
    def verify_global_settings_integrity(self):
        """Verifies that profile files specified in the global settings file
        all exist.
        """
        pass
        # TODO
    
    def add_profile(self):
        filename, res = QInputDialog.getText(self, 'Create new profile', 'Filename:')
        if res and filename:
            self.save_profile_file(filename)
            self.refresh_profiles(filename)
        self.ui.ProfilesStatusLabel.setText("{} succesfully added.".format(filename))

    def confirm_delete_profile(self):
        profilepath = os.path.join(
            self.global_settings["profiles_dir"],
            self.ui.GameProfileComboBox.currentText()
            )
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Do you really wanna delete {}? This cannot be undone.".format(profilepath) )
        msg.setWindowTitle("Delete profile?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        res = msg.exec()
        if res == QMessageBox.Yes:
            # Delete old profile file:
            os.remove(profilepath)
            self.refresh_profiles(-1) # Select the first one

    def refresh_profiles(self, newprof = None):
        profiles = self.find_profile_files_in_dir()
        self.ui.GameProfileComboBox.blockSignals(True)
        self.ui.GameProfileComboBox.clear()
        self.ui.GameProfileComboBox.addItems(profiles)
        if isinstance(newprof, str):
            self.set_current_profile(newprof)
        elif isinstance(newprof, int) and newprof < 0:
            self.ui.GameProfileComboBox.setCurrentIndex(0)
            self.set_current_profile(self.ui.GameProfileComboBox.currentText())
        elif isinstance(self.global_settings["current_profile"], str):
            self.set_current_profile(self.global_settings["current_profile"])
        self.ui.ProfilesDeleteButton.setEnabled(True)
        self.ui.GameProfileComboBox.blockSignals(False)
        self.ui.ProfilesStatusLabel.setText("Profile list updated.")

    def load_global_settings(self):
        print("load_global_settings()")

        if not self.global_settings_exist():
            self.create_settings_on_first_run()
            print("Creating settings on first run!")
        
        toml_settings = self.read_config_file(global_settings_file)
        self.global_settings.update(toml_settings)

        self.ui.ProfileDirInput.setText(self.global_settings["profiles_dir"])

        # Update RSS List in UI
        self.ui.RSSFeedList.clear()
        if self.global_settings["rss"] != None:
            for feed in self.global_settings["rss"]:
                self.add_rss_to_list(feed)

        # Profiles combobox
        self.refresh_profiles()
        current_profile_file = self.global_settings["current_profile"]
        self.current_profile_settings = self.read_config_file(
            current_profile_file)
    
    def default_profile_exists(self):
        if self.global_settings == None:
            return False
        else:
            #if not self.profile_exists(self.global_settings["current_profile"]):
            default_path = os.path.join(os.path.join(os.getcwd(), "ll_profiles"), "default.toml")
            return self.profile_exists(default_path)
    
    def global_settings_exist(self):
        return self.config_file_exists(global_settings_file)
    
    def profile_exists(self, name=None):
        if not os.path.isdir(self.global_settings["profiles_dir"]):
            return False

        fpath = os.path.join(self.global_settings["profiles_dir"], name)
        return os.path.isfile(fpath)

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
        profile_files = []
        # Bad profiles_dir? Not my job.
        if os.path.isdir(self.global_settings["profiles_dir"]):
            for file in os.listdir(self.global_settings["profiles_dir"]):
                if file.endswith(".toml"):
                    profile_files.append(file)
        return profile_files
    
    def save_global_settings_file(self):
        """This saves the global settings, which is different from profiles
        """
        with open(global_settings_file, "w") as f:
            new_toml_string = toml.dump(self.global_settings, f)
        print("saved config")
        return
    
    def rss_commit(self):
        feeds = []
        self.ui.RSSFeedCombobox.clear()
        for i in range(self.ui.RSSFeedList.count()):
            self.ui.RSSFeedCombobox.addItem(self.ui.RSSFeedList.item(i).text())
            feeds.append(self.ui.RSSFeedList.item(i).text())
        self.global_settings["rss"] = feeds

    def create_settings_on_first_run(self):
        self.save_global_settings_file()
        self.save_ms_list()
        self.save_server_list()
        self.save_profile_file(self.global_settings["current_profile"])
    
    def load_current_profile(self):
        if not self.default_profile_exists():
            self.create_settings_on_first_run()
            print("Creating settings on first run!")

        print("Current profile: {}".format(self.global_settings["current_profile"]))
        self.current_profile_settings = self.read_config_file(
            os.path.join(self.global_settings["profiles_dir"], self.global_settings["current_profile"])
            )
        print("Current profile settings: {}".format(self.current_profile_settings))
        self.apply_profile_settings_to_gui(self.current_profile_settings)
        
    def load_different_profile(self, profile):
        #profile_settings = self.read_config_file(profile.value())
        # Stub Obsolete the way set_current_profile calls the loader
        #profile_settings = self.read_config_file(
            #os.path.join(self.global_settings["profiles_dir"], self.global_settings["current_profile"])
            #)
        #self.apply_profile_settings_to_gui(profile_settings)
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
        self.ui.HostMSCombobox.setCurrentText(profile_settings_dict["host"]["masterserver"])
        self.ui.WineToggle.setChecked(profile_settings_dict["settings"]["wine"])
        self.ui.SaveFilesToConfigToggle.setChecked(profile_settings_dict["settings"]["includefiles"])

        if self.ui.SaveFilesToConfigToggle.isChecked:
            for f in profile_settings_dict["files"]:
                self.add_file(f)

        print("read_modsources")
        # Reset modsources
        #self.ui.ModsourceMBCheckbox.checked = False
        #self.ui.ModsourceWSBlueCheckbox.checked = False
        #self.ui.ModsourceWSRedCheckbox.checked = False
        # Load modsources from global_settings
        self.ui.ModsourceMBCheckbox.setChecked( self.global_settings["modsources"]["srb2mb"])
        self.ui.ModsourceWSBlueCheckbox.setChecked( self.global_settings["modsources"]["workshop_blue"])
        self.ui.ModsourceWSRedCheckbox.setChecked( self.global_settings["modsources"]["workshop_red"])
        self.ui.ModsourceSkybaseCheckbox.setChecked( self.global_settings["modsources"]["skybase"])
        self.ui.ModsourceWadarchiveCheckbox.setChecked( self.global_settings["modsources"]["wadarchive"])
        self.ui.ModsourceGamebananaCheckbox.setChecked( self.global_settings["modsources"]["gamebanana"])

        self.change_skin_image()
        self.ui.ProfilesStatusLabel.setText("Profile successfully loaded.")
    
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
        toml_settings["host"]["masterserver"] = self.ui.HostMSCombobox.currentText()
        toml_settings["settings"]["wine"] = self.ui.WineToggle.isChecked()
        toml_settings["settings"]["includefiles"] = self.ui.SaveFilesToConfigToggle.isChecked()

        for i in range(self.ui.GameFilesList.count()):
            toml_settings["files"].append(self.ui.GameFilesList.item(i).text())
        
        return toml_settings
    
    def save_profile_file(self, filename):
        """This takes GUI state, converts to a dictionary, and saves the 
        variables to a TOML file.
        """
        # generate the TOML data for the config
        print("save_profile_file({})".format(filename))

        # Guarantee profiles dir
        if not os.path.isdir(self.global_settings["profiles_dir"]):
            os.makedirs(self.global_settings["profiles_dir"])
        
        toml_settings = self.generate_profile_dict()
        profilepath = os.path.join(self.global_settings["profiles_dir"], filename)
        
        with open(profilepath, "w") as f:
            new_toml_string = toml.dump(toml_settings, f)

        print("saved profile file")
        self.ui.ProfilesStatusLabel.setText("{} succesfully saved.".format(filename))
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
            if self.ui.GamePageTabList.currentRow() == 3:
                out_text += self.get_server_launch_command()
            else:
                out_text += self.get_client_launch_command()
            with open(fileName, "w") as f:
                f.write(out_text)
        return

    def check_version(self):
        print("check_version")

        link = "https://api.github.com/repos/liquidunderground/liquidlauncher/releases/latest"
        
        try:
            f = json.load(urllib.request.urlopen(link, timeout=100))

            latest_version = f["tag_name"]
            print("Latest: " + latest_version)
            print("Current: " + versionString)

            # check launcher version ============================================= #
            #if float(ver_num) > float(versionString.replace("reBoot-", "")):
            if version.parse(latest_version) > version.parse(versionString):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Your version of LiquidLauncher seems to be outdated. Please download version {} from our <a href=\"https://github.com/liquidunderground/liquidlauncher/releases\">releases</a>.".format(latest_version) )
                msg.setWindowTitle("Version {} available".format(latest_version))
                msg.setDetailedText("Latest version of LiquidLauncher: " + latest_version+ "\nYou are currently running: " + versionString)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            #elif float(ver_num) < float(versionString.replace("reBoot-", "")):
            elif version.parse(latest_version) < version.parse(versionString):
                print("Greetings, time traveller.")
            else:
                print("up-to-date (" + versionString + ")")
        except Exception as e:
            print("Version check error: ",e)
            return


def main():
    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()
    t = QtCore.QTimer()
    t.singleShot(0, w.applicationStarted)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
