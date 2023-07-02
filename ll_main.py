import json
import os
import platform
import sys
import shlex
import webbrowser
from packaging import version # for version checks
import toml
from datetime import date

import feedparser
import subprocess32 as subprocess # Keep things drop-in
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog, QMenu, QInputDialog, QDialogButtonBox, QMessageBox
from PySide6.QtCore import Signal

import char_text
from ll_threading import QueryLiquid, QueryMessageBoard, QueryMasterServer, ModDownloader
from ll_ui import *
from ll_info import product_version as versionString
from ll_info import http_headers

global_settings_file = "ll_settings.toml"


class MainWindow(QMainWindow):
    # Emits instance of Mod() class from self.mods_list
    mod_description_sig = Signal(object)
    # Emits self.mods_list
    mod_list_sig = Signal(str)
    # Emits bool, telling QThread to query the master server
    query_ms_sig = Signal(bool)
    query_ms_rooms_sig = Signal(str)
    # Emits mod download URL string
    download_mod_url_sig = Signal(str)
    # Emits mod download filepath
    download_mod_path_sig = Signal(str)
    # Emits version string
    check_version_sig = Signal(str)
    # Emits URL for RSS query
    load_rss_sig = Signal(str)
    

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
                                    "https://liquidunderground.github.io/feed.rss",
                                    "https://srb2.org/feed",
                                    "https://www.sonicstadium.org/feed",
                                    ],
                                "devsettings": {
                                    "http_user_agent": http_headers["User-Agent"]
                                    },
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
        self.mb_qthread.mod_statmsg_sig1.connect(self.on_mod_statmsg)
        self.mb_qthread.mod_description_sig1.connect(self.on_mod_description)

        # Download mod multithreading
        self.mod_download_qthread = ModDownloader()
        self.mod_download_qthread.start()
        self.download_mod_url_sig.connect(self.mod_download_qthread.on_download_button)
        self.download_mod_path_sig.connect(self.mod_download_qthread.on_filepath_emit)
        self.mod_download_qthread.mod_filepath_sig1.connect(self.add_mod_to_files)

        # Liquid stuff multithreading
        self.query_liquid_qthread = QueryLiquid()
        self.query_liquid_qthread.start()
        self.check_version_sig.connect(self.query_liquid_qthread.on_check_version)
        self.query_liquid_qthread.check_version_cb_sig.connect(self.on_check_version_cb)
        self.load_rss_sig.connect(self.query_liquid_qthread.on_load_rss)
        self.query_liquid_qthread.load_news_cb_sig.connect(self.on_load_news_cb)
        self.query_liquid_qthread.update_snitchmsg_sig.connect(self.ui.SnitchmsgLabel.setText)

        # Emits mod download filepath
        download_mod_path_sig = Signal(str)
        
        # Master Server Multithreading
        self.ms_qthread = QueryMasterServer(self)
        self.ms_qthread.start()
        self.query_ms_sig.connect(self.ms_qthread.on_refresh)
        self.query_ms_rooms_sig.connect(self.ms_qthread.on_query_ms_rooms)
        self.ms_qthread.server_list_sig1.connect(self.on_server_list)
        self.ms_qthread.on_ms_rooms_sig.connect(self.on_ms_rooms)
        
        # load servers from file ===================================================== #
        # self.loadServerList()
        self.has_loaded_servers = False

        # allow posix systems to use wine ============================================ #
        if os.name == "posix":
            self.ui.WineRadiobutton.setEnabled(True)
        if platform.system() == "Linux":
            self.ui.FlatpakRadiobutton.setEnabled(True)

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

        # (Dev) settings hooks ======================================================= #
        self.ui.SaveSettingsButton.clicked.connect(self.save_settings)

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
        self.ui.WineRadiobutton.toggled.connect(self.update_binmode_in_ui)
        self.ui.FlatpakRadiobutton.toggled.connect(self.update_binmode_in_ui)
        self.ui.NativeRadiobutton.toggled.connect(self.update_binmode_in_ui)

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
        self.ui.ModDirBrowseButton.clicked.connect(self.set_download_path)
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
        #self.ui.ModsourceMBCheckbox.clicked.connect(self.update_modsources)
        #self.ui.ModsourceWSBlueCheckbox.clicked.connect(self.update_modsources)
        #self.ui.ModsourceWSRedCheckbox.clicked.connect(self.update_modsources)
        #self.ui.ModsourceGamebananaCheckbox.clicked.connect(self.update_modsources)
        #self.ui.ModsourceSkybaseCheckbox.clicked.connect(self.update_modsources)
        #self.ui.ModsourceWadarchiveCheckbox.clicked.connect(self.update_modsources)

        # MS table buttons ======================================================== #
        self.ui.MSAddButton.clicked.connect(self.add_new_ms_to_list)
        self.ui.MSRemoveButton.clicked.connect(self.remove_ms_from_list)
        self.ui.MSListSaveButton.clicked.connect(self.save_ms_list)
        self.ui.MSVisitrepoButton.clicked.connect(lambda: self.open_url("https://github.com/liquidunderground/configs-public"))
        self.ui.SnitchButton.clicked.connect(lambda: self.query_liquid_qthread.on_snitch(
            self.ui.SnitchsrcCombobox.currentData(), self.ui.SnitchdestCombobox.currentText()))

        # RSS buttons ======================================================== #
        self.ui.RSSFeedList.itemSelectionChanged.connect(self.rss_enable_edit)
        #self.ui.RSSFeedList.itemChanged.connect(self.rss_commit)
        #self.ui.RSSFeedList.dataChanged.connect(self.rss_commit)
        self.ui.RSSMoveupButton.clicked.connect(self.rss_moveup)
        self.ui.RSSMovedownButton.clicked.connect(self.rss_movedown)
        self.ui.RSSAddButton.clicked.connect(lambda: self.add_rss_to_list() )
        self.ui.RSSRemoveButton.clicked.connect( self.remove_rss_from_list )

        # Host settings Checkboxes ======================================================== #
        ## MS Room querying
        self.ui.HostMSCombobox.lineEdit().returnPressed.connect(self.query_ms_rooms)
        self.ui.MSRoomqueryrefreshButton.clicked.connect(self.query_ms_rooms)
        ## Settings sections
        self.ui.CoopSettingsCheckbox.stateChanged.connect(self.on_apply_checkbox)
        self.ui.RingslingerSettingsCheckbox.stateChanged.connect(self.on_apply_checkbox)
        self.ui.CircuitraceSettingsCheckbox.stateChanged.connect(self.on_apply_checkbox)
        self.ui.BattlemodSettingsCheckbox.stateChanged.connect(self.on_apply_checkbox)

        # play button ================================================================ #
        self.ui.GamePlayButton.clicked.connect(self.launch_game_normally)

        # ====== Launch section =======
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

    def remove_rss_from_list(self):
        # QListWidget.takeItem bc Qt is weird
        self.ui.RSSFeedList.takeItem( self.ui.RSSFeedList.currentRow() )

    def rss_moveup(self):
        reservedItems = []
        row = self.ui.RSSFeedList.currentRow()
        item = self.ui.RSSFeedList.takeItem(row)
        row -= 1
        self.ui.RSSFeedList.insertItem(row, item)
        self.ui.RSSFeedList.setCurrentRow(row)
        return

    def rss_movedown(self):
        reservedItems = []
        row = self.ui.RSSFeedList.currentRow()
        item = self.ui.RSSFeedList.takeItem(row)
        row += 1
        self.ui.RSSFeedList.insertItem(row, item)
        self.ui.RSSFeedList.setCurrentRow(row)
        return

    # Default functions

    def open_url(self, url):
        webbrowser.open(url)

    def show_game_options_dropdown(self):
        menu = QMenu()
        menu.addAction("Save current parameters to script", self.export_script)
        menu.exec()

    def load_news(self, feed="https://liquidunderground.github.io/feed.rss"):
        # ok lets uh, get the news feed or something?
        print("load_news({})".format(feed))
        self.ui.RSSStatusLabel.setText("Querying RSS feed...")
        self.load_rss_sig.emit(feed)

    def on_load_news_cb(self, content, error=False):
        if(error): # Emergency error kludge
            self.ui.RSSStatusLabel.setText(content)
            print(content)
            return
        msg = "News feed successfully loaded."
        #print("RAW CONTENT: {}\n".format(content))
        feed = feedparser.parse(content)
        if len(feed["items"]) < 1:
            msg = "No news found. Did you check the URL?"
            self.ui.RSSStatusLabel.setText(msg)
            print(msg)
            return

        self.news = feed["items"]

        print("Parsing articles...")
        self.ui.RSSArticleList.clear()
        for item in self.news:
            self.ui.RSSArticleList.addItem("{} (by {})".format(item.title, item.author))
        self.ui.RSSStatusLabel.setText(msg)

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

    def get_client_launch_command_headless(self):
        """
        This converts all of the launcher inputs to a single-string command to 
        launch SRB2
        """
        #com = ""
        com = []
        if self.ui.FlatpakRadiobutton.isChecked() and self.ui.FlatpakRadiobutton.isEnabled(): 
            com += ["flatpak","run","org.srb2.SRB2"]
        else:
            if self.ui.WineRadiobutton.isChecked() and self.ui.WineRadiobutton.isEnabled(): 
                com +=[ "wine"]
            com += [self.ui.GameExecFilePathInput.text()]

        if self.ui.HomePathInput.text() != "": 
            com += ["-home", self.ui.HomePathInput.text() ]

        if self.ui.PlayerNameInput.text() != "": com += ["+name",self.ui.PlayerNameInput.text()]
        if self.ui.PlayerColorInput.currentText():
            com += ["+color" , str(self.ui.PlayerColorInput.currentText().lower())]
        if self.ui.PlayerSkinInput.currentText():
            com += ["+skin" , str(
            self.ui.PlayerSkinInput.currentText().lower().replace(" ", ""))]

        # get all files ====================================================== #
        if self.ui.GameFilesList.count() > 0:
            com +=[ "-file"]
            for i in range(self.ui.GameFilesList.count()):
                com += [self.ui.GameFilesList.item(i).text()]

        # add a script ======================================================= #
        if self.ui.GameFilesExecScriptInput.text() != "": 
            com += ["+exec", self.ui.GameFilesExecScriptInput.text()]

        # custom parameters ================================================== #
        if self.ui.GameArgsInput.text() != "": 
            com += shlex.split(self.ui.GameArgsInput.text())

        return com

    def get_client_launch_command(self):

        com = []
        com = self.get_client_launch_command_headless()

        # game settings (from game settings tab) ============================= #
        if self.ui.GameRendererSetting.currentIndex() == 0: com += ["+renderer","1"]
        if self.ui.GameRendererSetting.currentIndex() == 1: com += ["+renderer","2"]
        if self.ui.GameFullscreenSetting.currentIndex() == 0: com += ["+fullscreen","1"]
        if self.ui.GameFullscreenSetting.currentIndex() == 1: com += ["-borderless"]
        if self.ui.GameFullscreenSetting.currentIndex() == 2: com += ["-win"]
        if self.ui.GameMusicSetting.currentIndex() == 0: com += ["+digimusic","On"]
        if self.ui.GameMusicSetting.currentIndex() == 1: com += ["+digimusic","Off"]
        if self.ui.GameMusicSetting.currentIndex() == 2: com += ["-usecd"]
        if self.ui.GameMusicSetting.currentIndex() == 3: com += ["-nomusic"]
        if self.ui.GameSoundSetting.currentIndex() == 1: com += ["-nosound"]
        if self.ui.GameHorizontalResolutionInput.text() != "" and self.ui.GameVerticalResolutionInput.text() != "":
            com += [" -width " , self.ui.GameHorizontalResolutionInput.text() , " -height " \
                   , self.ui.GameVerticalResolutionInput.text() ]
        print("CLIENT COMMAND: {}".format(com))
        return com

    def get_server_launch_command(self):
        """Launch server
        """
        launch_command = []
        #launch_command = self.ui.GameExecFilePathInput.text() + " -server"
        if self.ui.DedicatedServerToggle.isChecked():
            launch_command += self.get_client_launch_command_headless()
        else:
            launch_command += self.get_client_launch_command()

        launch_command += ["-server"]

        ### General settings tab ###
        if self.ui.ServerNameInput.text() != "": launch_command += ["+servername ",self.ui.ServerNameInput.text()]
        if self.ui.AdminPasswordInput.text() != "": launch_command += ["+password",self.ui.AdminPasswordInput.text()]
        if self.ui.HostMSCombobox.currentText() != "": launch_command += ["+masterserver",self.ui.HostMSCombobox.currentText()]
        # TODO: Live Master Server room queries
        if self.ui.RoomInput.currentIndex() != 0:
            launch_command += ["-id", str(self.ui.RoomInput.itemData(self.ui.RoomInput.currentIndex()))]
        if self.ui.DedicatedServerToggle.isChecked(): launch_command += ["-dedicated"]
        if self.ui.PortInput.text() != "":
            launch_command += ["-port" , self.ui.PortInput.text()]
        else:
            launch_command += ["-port","5029"]
        if self.ui.Ipv6Checkbox.isChecked(): launch_command += ["-ipv6"]
        if self.ui.UpnpCheckbox.isChecked(): launch_command += ["-upnp"]
        if self.ui.BandwidthInput.value() != 1000:
            launch_command += ["-bandwidth",str(self.ui.BandwidthInput.value())]
        if self.ui.ExtraticInput.value() != 1:
            launch_command += ["-extratic ",str(self.ui.ExtraticInput.value())]
        #### Downloading section ####
        if self.ui.UploadToggle.isChecked():
            launch_command += ["+downloading","1"]
        else:
            launch_command += ["+downloading","0"]
        launch_command += ["+downloadspeed" , str(self.ui.DownloadspeedInput.value())]
        launch_command += ["+maxsend" , str(self.ui.MaxsendInput.value())]
        #### Timeouts & Resynch section ####
        launch_command += ["+maxping" , str(self.ui.MaxpingInput.value())]
        launch_command += ["+nettimeout" , str(self.ui.NettimeoutInput.value())]
        launch_command += ["+resynchattempts" , str(self.ui.ResynchattemptsInput.value())]

        ### Game settings tab ###
        launch_command += ["-gametype" , str(self.ui.GametypeInput.currentIndex())]
        launch_command += ["+advancemap" , str(self.ui.AdvanceMapInput.currentIndex())]
        if self.ui.MaxPlayersInput.value() != 8:
            launch_command += ["+maxplayers" , str(self.ui.MaxPlayersInput.value())]
        if (self.ui.ForceSkinInput.currentText() != ""):
            launch_command += ["+forceskin" , self.ui.ForceSkinInput.currentText().lower().replace( " ", "")]
        # TODO: Add the rest

        ### Coop Settings Tab ###
        if self.ui.CoopSettingsCheckbox.isChecked():
            launch_command += ["+startinglives" , str(self.ui.StartinglivesInput.value())]
            launch_command += ["+playersforexit" , str(self.ui.PlayersforexitCombobox.currentIndex())]
            launch_command += ["+competitionboxes" , str(self.ui.CompetitionboxesCombobox.currentIndex())]

        ### Ringslinger Settings Tab ###
        if self.ui.RingslingerSettingsCheckbox.isChecked():
            if self.ui.PointLimitInput.value() != 0:
                launch_command += ["+pointlimit" , str(self.ui.PointLimitInput.value())]
            launch_command += ["+matchscoring" , str(self.ui.MatchscoringCombobox.currentIndex())]
            if self.ui.TimeLimitInput.text() != "":
                launch_command += ["+timelimit" , str(self.ui.TimeLimitInput.value())]
            else:
                launch_command += ["+timelimit","0"]
            launch_command += ["+overtime", "1" if self.ui.OvertimeCheckbox.isChecked() else "0"]
            launch_command += ["+respawndelay" , str(self.ui.RespawndelayInput.value())]
            launch_command += ["+specialrings", "1" if self.ui.PowerstonesCheckbox.isChecked() else "0"]
            launch_command += ["+suddendeath", "1" if self.ui.PowerstonesCheckbox.isChecked() else "0"]
            launch_command += ["+powerstones", "1" if self.ui.PowerstonesCheckbox.isChecked() else "0"]
            launch_command += ["+matchboxes" , str(self.ui.MatchboxesCombobox.currentIndex())]
            launch_command += ["+autobalance", str(self.ui.AutobalanceCheckbox.currentIndex())]
            launch_command += ["+flagtime", str(self.ui.FlagtimeInput.value())]
            launch_command += ["+friendlyfire", "1" if self.ui.FriendlyfireCheckbox.isChecked() else "0"]
            launch_command += ["+touchtag", "1" if self.ui.TouchtagCheckbox.isChecked() else "0"]
            launch_command += ["+hidetime", str(self.ui.HidetimeInput.value())]
            # TODO: Debug
           

        ### Circuit Race Settings Tab ###
        if self.ui.CircuitraceSettingsCheckbox.isChecked():
            if self.ui.NumlapsInput.value() != 0:
                launch_command += ["+numlaps" , str(self.ui.NumlapsInput.value())]
            if self.ui.CountdowntimeInput.value() != 0:
                launch_command += ["+countdowntime" , str(self.ui.CountdowntimeInput.value())]
            if self.ui.UsemaplapsCheckbox.isChecked():
                launch_command += ["+usemaplaps","1"]
            else:
                launch_command += ["+usemaplaps","0"]

        ### Battlmod Settings Tab ###
        if self.ui.BattlemodSettingsCheckbox.isChecked():
            # TODO: Debug everything
            # Battlemod Tab
            launch_command += ["+battle_coyotetime", str(self.ui.Battle_coyotetimeInput.value())]
            launch_command += ["+battle_coyotefactor", str(self.ui.Battle_coyotefactorInput.value())]
            launch_command += ["+battle_recoveryjump", "1" if self.ui.Battle_recoveryjumpCheckbox.isChecked() else "0"]
            ## Item settings
            launch_command += ["+item_rate", str(self.ui.Item_rateCombobox.currentIndex())]
            launch_command += ["+item_type", str(self.ui.Item_typeCombobox.currentIndex()-1)]
            launch_command += ["+item_global", "1" if self.ui.Item_globalCheckbox.isChecked() else "0"]
            launch_command += ["+item_local", "1" if self.ui.Item_localCheckbox.isChecked() else "0"]
            ## Battle mode settings
            launch_command += ["+survival_lives", str(self.ui.Survival_livesInput.value())]
            launch_command += ["+battle_startrings", str(self.ui.Battle_startringsInput.value())]
            launch_command += ["+survival_revenge", str(self.ui.Survival_revengeCombobox.currentIndex())]
            launch_command += ["+survival_suddendeath", "1" if self.ui.Survival_suddendeathCheckbox.isChecked() else "0"]
            ## Battle/Survival settings
            launch_command += ["+battle_collision", "1" if self.ui.Battle_collisionsCheckbox.isChecked() else "0"]
            launch_command += ["+battle_slipstreams", "1" if self.ui.Battle_slipstreamsheckbox.isChecked() else "0"]
            launch_command += ["+battle_special", "1" if self.ui.Battle_specialCheckbox.isChecked() else "0"]
            launch_command += ["+battle_shieldstock", "1" if self.ui.Battle_shieldstocksCheckbox.isChecked() else "0"]
            launch_command += ["+battle_preround", "1" if self.ui.Battle_preroundCheckbox.isChecked() else "0"]
            ## CP Ring spawns
            launch_command += ["+cp_spawninfinity", "1" if self.ui.Cp_spawninfinityInput.isChecked() else "0"]
            launch_command += ["+cp_spawnauto", "1" if self.ui.Cp_spawnautoInput.isChecked() else "0"]
            launch_command += ["+cp_spawnbounde", "1" if self.ui.Cp_spawnbounceInput.isChecked() else "0"]
            launch_command += ["+cp_spawnbomb", "1" if self.ui.Cp_spawnbombInput.isChecked() else "0"]
            launch_command += ["+cp_spawngrenade", "1" if self.ui.Cp_spawngrenadeInput.isChecked() else "0"]
            launch_command += ["+cp_spawnrail", "1" if self.ui.Cp_spawnrailInput.isChecked() else "0"]
            launch_command += ["+cp_spawnscatter", "1" if self.ui.Cp_spawnscatterInput.isChecked() else "0"]
            ## Battle CTF
            launch_command += ["+ctf_flagdrop_graceperiod", str(self.ui.Ctf_flagdrop_graceperiodInput.value())]
            launch_command += ["+ctf_flagrespawn_graceperiod", str(self.ui.Ctf_flagrespawn_graceperiodInput.value())]
            ## Battle Diamond hunt
            launch_command += ["+diamond_capture_time", str(self.ui.Diamond_capture_timeInput.value())]
            launch_command += ["+diamond_capture_bonus", str(self.ui.Diamond_capture_bonusInput.value())]
            ## Cutsom Battlemod flags ##
            if self.ui.Battle_addoptionsInput.text() != "": 
                com += shlex.split(self.ui.Battle_addoptionsInput.text())


        print("SERVER COMMAND: {}".format(launch_command))
        return launch_command

    def set_game_path(self):
        f = QFileDialog.getExistingDirectory()
        if (f):
            #self.PathGameFilesExecScriptInput.setText(f)
            self.ui.ProfileDirInput.setText(f)
            pass

    #ä
    def query_ms_rooms(self):
        print("query_ms_rooms()")
        self.ui.MSRoomqueryrefreshButton.setEnabled(False) # MutEx lock. unlock in on_query_rooms
        self.ui.RoomInput.setEnabled(False)
        url = self.ui.HostMSCombobox.currentText()
        self.query_ms_rooms_sig.emit(url)
        #self.on_ms_rooms({
            #33: "Standard",
            #28: "Casual",
            #38: "Custom Gametypes",
            #31: "OLDC",
            #101: "@Sonic",
            #102: "@Tails",
            #103: "@Knuckles",
        #}) # Debug switch

    def on_ms_rooms(self, data={}):
        print("on_ms_rooms({})\n".format(data))
        self.ui.RoomInput.blockSignals(True) # MutEx lock
        self.ui.RoomInput.clear()
        self.ui.RoomInput.insertItem( 0, "No room/Offline")
        for roomid, roomname in data.items():
            self.ui.RoomInput.addItem("{} (ID: {})".format(roomname,roomid),roomid)
            #self.ui.RoomInput.insertItem( self.ui.RoomInput.count(), "{} ({})".format(roomname,roomid))
        self.ui.RoomInput.blockSignals(False) # MutEx unlock
        self.ui.RoomInput.setEnabled(True) # MutEx unlock. lock in query_ms_rooms
        self.ui.MSRoomqueryrefreshButton.setEnabled(True)
        return

    #### Files tab ####
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
            subprocess.Popen(launchCommand_server)
        else:
            subprocess.Popen(launchCommand_client)
        return

    def change_main_tab(self, index):
        # Reset all buttons
        self.ui.NewsTabButton.setChecked(False)
        self.ui.GameTabButton.setChecked(False)
        self.ui.HelpTabButton.setChecked(False)
        self.ui.SettingsTabButton.setChecked(False)

        # Re-check correct button
        if index == 0:
            self.ui.NewsTabButton.setChecked(True)
        if index == 1:
            self.ui.GameTabButton.setChecked(True)
        if index == 2:
            self.ui.HelpTabButton.setChecked(True)
        if index == 3:
            self.ui.SettingsTabButton.setChecked(True)

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
        mod = self.get_selected_mod().url
        self.open_url(mod)
    
    def get_selected_mod(self):
        #selection = self.ui.ModsList.currentItem().text()
        #mod = self.mods_list[selection]
        #return mod
        selection = self.ui.ModsList.currentItem().data(3)
        return selection

    def set_download_path(self):
        f, _ = QFileDialog.getExistingDirectory()
        if (f):
            self.ui.ModDirInput.setText(f)

    def download_mod(self):
        print("MOD LIST: {}".format(self.mods_list))
        if self.mods_list:
            mod = self.get_selected_mod()
            print("SELECTED MOD: {}".format(mod))
            #mod.set_download_url()
            #path = os.path.join( self.ui.HomePathInput.text(), "DOWNLOAD")
            path = self.ui.ModDirInput.text() if self.ui.ModDirInput.text() != "" else os.path.join(os.path.expanduser("~"), "Downloads")
            self.ui.ModStatusLabel.setText("Downloading mod...")
            self.download_mod_url_sig.emit(mod.download_url)
            self.download_mod_path_sig.emit(path)

    def append_mod_to_list(self, mod, icon=None):
        print("append_mod_to_list({},{})".format(mod,icon))
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(mod)
        new_item.setData(3,self.mods_list[mod])
        if icon:
            qicon = QtGui.QIcon()
            qicon.addPixmap(QtGui.QPixmap(icon),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
            new_item.setIcon(qicon)
        self.ui.ModsList.addItem(new_item)

    def load_mod_page(self):
        self.ui.ModStatusLabel.setText("Downloading mod description...")
        if self.mods_list:
            mod = self.get_selected_mod().url
            #print("Mod URL: {}".format(mod.url))
            #self.ui.ModBrowser.load(mod.url)
            print("Mod URL: {}".format(mod))
            self.ui.ModBrowser.load(mod)
            self.ui.ModStatusLabel.setText("Mod successfully loaded.")
            self.ui.OpenPageButton.setEnabled(True)
            self.ui.DownloadModButton.setEnabled(True)
        else:
            self.ui.ModStatusLabel.setText("No mods found. Did you check your sources?")
            self.ui.OpenPageButton.setEnabled(False)
            self.ui.DownloadModButton.setEnabled(True)

    def refresh_mods_list(self):
        # TODO: multithreading to get rid of lag
        self.ui.ModStatusLabel.setText("Downloading mods list...")
        self.ui.ModsList.clear()
        self.mods_list = {}
        self.mod_list_sig.emit(self.ui.ModTypeCombo.currentText())

    def on_mod_description(self, mod):
        self.ui.ModStatusLabel.setText("Click on a mod to see more information.")
        self.ui.ModBrowser.setHtml(mod.description, mod.url)
        self.ui.ModBrowser.load(mod.url)

    def on_mod_statmsg(self,msg):
        self.ui.ModStatusLabel.setText(msg)

    def on_mod_list(self, mod_list, icon=None):
        self.ui.ModStatusLabel.setText("Click on a mod to see more "
                                       "information.")
        self.mods_list.update(mod_list)
        for item in mod_list:
            self.append_mod_to_list(item, icon)

    def add_mod_to_files(self, filepaths_list):
        # Unable to download?
        if filepaths_list == [None]:
            self.ui.ModStatusLabel.setText("Unable to download mod (maybe check the website)")
            pass
        else:
            self.ui.ModStatusLabel.setText("Download successfully finished.")
        if self.ui.AdddownloadtolaunchmodsCheckbox.isChecked():
            for filepath in filepaths_list:
                self.add_file(filepath)

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
                server.get("name_plain"),
                server.get("room"),
                server.get("version"),
                server.get("origin") 
                )
            new_item = QtWidgets.QListWidgetItem()
            new_item.setText(entry_label)
            # Create new row & fill with data
            self.ui.BrowseNetgameTable.insertRow( self.ui.BrowseNetgameTable.rowCount() )
            twi_name = QtWidgets.QTableWidgetItem(server.get("name_plain"))
            twi_room = QtWidgets.QTableWidgetItem(server.get("room"))
            twi_version = QtWidgets.QTableWidgetItem(server.get("version"))
            twi_gametype = QtWidgets.QTableWidgetItem(server.get("game"))
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
        selection = '{} | Room: {} | Version: {} | Origin: {}'.format(
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 0).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 3).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 2).text(),
            self.ui.BrowseNetgameTable.item(self.ui.BrowseNetgameTable.currentRow(), 4).text()
            )
        ip_string = '{}:{}'.format(
            self.master_server_list[selection].get("ip"),
            self.master_server_list[selection].get("port") )
        subprocess.Popen(self.get_client_launch_command() + ["-connect" , ip_string])
        return

    def save_ms_selection(self):
        for row in self.ui.BrowseNetgameTable.selectionModel().selectedRows():
            # ID: ip:port
            selection = '{} | Room: {} | Version: {} | Origin: {}'.format(
                self.ui.BrowseNetgameTable.item(row.row(), 0).text(),
                self.ui.BrowseNetgameTable.item(row.row(), 3).text(),
                self.ui.BrowseNetgameTable.item(row.row(), 2).text(),
                self.ui.BrowseNetgameTable.item(row.row(), 4).text()
                )
            server = self.master_server_list[selection]
            ip = server.get("ip")
            name = self.ui.BrowseNetgameTable.item(row.row(), 0).text()
            port = server.get("port")
            self.add_server_to_list(name, ip, port)

    # Saved servers

    def save_server_list(self):
        serv_list = {}
        for i in range(len(self.saved_server_ips)):
            serv_list[self.ui.SavedNetgameTable.item(i, 0).text()] = {
                    "ip": self.ui.SavedNetgameTable.item(i, 1).text(),
                    "port": self.ui.SavedNetgameTable.item(i, 2).text()
                    }
        with open("bookmarks.toml", "w") as f:
            toml.dump(serv_list, f)
        return

    def load_server_list(self):
        serv_list = []
        fpath = os.path.join(os.getcwd(), "bookmarks.toml")
        if not os.path.isfile(fpath):
            return
        with open(fpath, "r") as f:
            serv_list = toml.load(f)

        for sname, server in serv_list.items():
            self.add_server_to_list(sname, server["ip"], server["port"])
        return

    def add_server_to_list(self, name, ip, port):
        self.saved_server_ips.append(ip)
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
        self.childWindow = edit_server_main.ChildWindow(self, name, ip, False)
        self.childWindow.show()
        return

    def edit_selected_server(self, name, ip):
        self.saved_server_ips[self.ui.SavedNetgameTable.currentRow()] = ip
        # Is this even necessary if the table is editable?
        self.ui.ServerList.setItem(self.ui.ServerList.currentRow(), 0).setText(name)
        self.save_server_list()
        return

    def delete_selected_server(self):
        downcounter = 0
        for row in self.ui.SavedNetgameTable.selectionModel().selectedRows():
            self.saved_server_ips.pop(row.row())
            self.ui.SavedNetgameTable.removeRow(row.row()+downcounter)
            downcounter = downcounter-1
        self.save_server_list()
        return

    def join_selected_netgame_bookmark(self):
        """Join current selected server in list
        """
        ipString = "{}:{}".format(
            self.ui.SavedNetgameTable.item( self.ui.SavedNetgameTable.currentRow(), 1 ).text(),
            self.ui.SavedNetgameTable.item( self.ui.SavedNetgameTable.currentRow(), 2 ).text(),
        )
        subprocess.Popen(self.get_client_launch_command() + ["-connect" + ipString])
        return

    def join_from_ip(self):
        """Join direct address
        """
        ipString = self.ui.JoinAddressInput.text()
        subprocess.Popen(self.get_client_launch_command() + ["-connect" , ipString])
        return

    # Saved Master Servers
    def update_ms_list_in_ui(self): 
        print("update_ms_list_in_ui")
        # Add combobox Mutex to avoid event loops
        self.ui.BrowseMSCombobox.blockSignals(True)
        self.ui.HostMSCombobox.blockSignals(True)

        self.ui.BrowseMSCombobox.clear()
        self.ui.HostMSCombobox.clear()
        self.ui.SnitchsrcCombobox.clear()
        self.ui.SnitchdestCombobox.clear()
        # We only need the first column (names)
        rows = self.ui.MasterServersTable.rowCount()
        #self.ui.BrowseMSCombobox.insertItem( 0, "All")
        for i in range(0, rows):
            ms_name = self.ui.MasterServersTable.item(i, 0).text()
            ms_url = self.ui.MasterServersTable.item(i, 1).text()
            ms_api = self.ui.MasterServersTable.cellWidget(i, 2).currentData()
            self.ui.BrowseMSCombobox.insertItem( self.ui.BrowseMSCombobox.count(), ms_name)
            if self.ui.MasterServersTable.cellWidget(i, 2).currentData() == "snitch": # Fetch-from-Snitch
               self.ui.SnitchsrcCombobox.insertItem( self.ui.SnitchsrcCombobox.count(), ms_name, {"url": ms_url, "api": ms_api})
               self.ui.HostMSCombobox.insertItem( self.ui.HostMSCombobox.count(), ms_url.rstrip('/')+'/v1')
               self.ui.SnitchdestCombobox.insertItem( self.ui.SnitchdestCombobox.count(), ms_url, ms_api)
            elif self.ui.MasterServersTable.cellWidget(i, 2).currentData() == "kartv2": # Kart API
               ## No Kart servers for snitching (yet)
               self.ui.HostMSCombobox.insertItem( self.ui.HostMSCombobox.count(), ms_url, ms_api)
            elif self.ui.MasterServersTable.cellWidget(i, 2).currentData() == "v1": # Mirror V1 servers
               self.ui.SnitchsrcCombobox.insertItem( self.ui.SnitchsrcCombobox.count(), ms_name, {"url": ms_url, "api": ms_api})
               self.ui.HostMSCombobox.insertItem( self.ui.HostMSCombobox.count(), ms_url, ms_api)

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
            shim_name = ""
            shim_url = ""
            shim_api = ""

            if self.ui.MasterServersTable.item(i, 0) != None:
                shim_name = self.ui.MasterServersTable.item(i, 0).text()
            if self.ui.MasterServersTable.item(i, 1) != None:
                shim_url = self.ui.MasterServersTable.item(i, 1).text()
            if self.ui.MasterServersTable.cellWidget(i, 2).currentData != None:
                shim_api = self.ui.MasterServersTable.cellWidget(i, 2).currentData()

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
        # Add combobox for API selection
        twi_api = QtWidgets.QComboBox()
        #twi_api.addItems(["v1", "kartv2", "snitch"])
        twi_api.addItem("SRB2 MS", "v1")
        twi_api.addItem("SRB2Kart MS", "kartv2")
        twi_api.addItem("LiquidMS Snitch", "snitch")
        twi_api.setCurrentIndex(twi_api.findData(api))
        twi_name.setTextAlignment( Qt.AlignHCenter|Qt.AlignVCenter )
        twi_url.setTextAlignment( Qt.AlignHCenter|Qt.AlignVCenter )

        self.ui.MasterServersTable.setItem( self.ui.MasterServersTable.rowCount()-1 , 0, twi_name )
        self.ui.MasterServersTable.setItem( self.ui.MasterServersTable.rowCount()-1 , 1, twi_url )
        # Add combobox
        self.ui.MasterServersTable.setCellWidget(self.ui.MasterServersTable.rowCount()-1 , 2, twi_api)
        return

    def remove_ms_from_list(self): 
        print("remove_ms_from_list")
        downcounter = 0
        for row in self.ui.MasterServersTable.selectionModel().selectedRows():
            self.ui.MasterServersTable.removeRow( row.row() + downcounter)
            downcounter = downcounter-1
        return

    # Settings and profiles

    def closeEvent(self, e):
        self.save_all()
        return
    
    def save_all(self):
        self.save_settings()
        #self.save_global_settings_file()
        self.save_profile_file(self.global_settings["current_profile"])

    def applicationStarted(self):
        """Wait for window to fully start
        """
        # fix resolution of the image on the play tab ================================ #
        self.load_global_settings()
        self.load_server_list()
        self.load_current_profile()
        self.check_version_sig.emit(versionString)
        self.ui.RSSRefreshButton.clicked.emit() # "Virtual click" to fetch news
        try:
            self.query_ms()  # populates master server list
        except:
            print("Querying master server failed.")

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
                #"wadarchive": self.ui.ModsourceWadarchiveCheckbox.isChecked(),
                "wadarchive": False, # Dummy until Wad Archive is supported (probably never; site is down)
                "gamebanana": self.ui.ModsourceGamebananaCheckbox.isChecked(),
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
            if not filename.endswith(".toml"):
                filename = filename+".toml"
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
        print("USER AGENT: {}\n".format(self.global_settings["devsettings"]["http_user_agent"]))
        self.ui.UseragentInput.setText(self.global_settings["devsettings"]["http_user_agent"])

        # Update RSS List in UI
        self.ui.RSSFeedList.clear()
        if self.global_settings["rss"] != None:
            for feed in self.global_settings["rss"]:
                self.add_rss_to_list(feed)

        self.rss_commit()

        # Profiles combobox
        self.refresh_profiles()
        current_profile_file = self.global_settings["current_profile"]
        self.current_profile_settings = self.read_config_file(
            current_profile_file)
    
    def default_profile_exists(self):
        if self.global_settings == None:
            return False
        else:
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

    def save_settings(self):
        self.global_settings["profiles_dir"] = self.ui.ProfileDirInput.text()
        self.global_settings["devsettings"] = {
            "http_user_agent": self.ui.UseragentInput.text()
        }
        self.update_modsources()
        self.rss_commit()
        self.save_global_settings_file()
    
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
        # Stub Obsolete the way set_current_profile calls the loader
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
        # Load modsources from global_settings
        self.ui.ModsourceMBCheckbox.setChecked( self.global_settings["modsources"]["srb2mb"])
        self.ui.ModsourceWSBlueCheckbox.setChecked( self.global_settings["modsources"]["workshop_blue"])
        self.ui.ModsourceWSRedCheckbox.setChecked( self.global_settings["modsources"]["workshop_red"])
        self.ui.ModsourceSkybaseCheckbox.setChecked( self.global_settings["modsources"]["skybase"])
        #self.ui.ModsourceWadarchiveCheckbox.setChecked( self.global_settings["modsources"]["wadarchive"])
        self.ui.ModsourceGamebananaCheckbox.setChecked( self.global_settings["modsources"]["gamebanana"])


        # ===== Apply profile settings ===== #
        # Headless & client settings
        self.ui.PlayerNameInput.setText( profile_settings_dict["player"]["name"] )
        self.ui.PlayerSkinInput.setCurrentText( profile_settings_dict["player"]["skin"] )
        self.ui.PlayerColorInput.setCurrentText( profile_settings_dict["player"]["color"] )
        self.ui.GameHorizontalResolutionInput.setText( profile_settings_dict["game"]["resolution"]["width"] )
        self.ui.GameVerticalResolutionInput.setText( profile_settings_dict["game"]["resolution"]["height"] )
        self.ui.GameRendererSetting.setCurrentIndex( profile_settings_dict["game"]["renderer"] )
        self.ui.GameFullscreenSetting.setCurrentIndex( profile_settings_dict["game"]["windowmode"] )
        self.ui.GameMusicSetting.setCurrentIndex( profile_settings_dict["game"]["music"] )
        self.ui.GameSoundSetting.setCurrentIndex( profile_settings_dict["game"]["sound"] )
        self.ui.GameExecFilePathInput.setText( profile_settings_dict["game"]["exepath"] )
        self.ui.GameArgsInput.setText( profile_settings_dict["game"]["cliargs"] )
        try:
            if profile_settings_dict["settings"]["binmode"] == "wine":
                self.ui.NativeRadiobutton.setChecked(False)
                self.ui.WineRadiobutton.setChecked(True)
                self.ui.FlatpakRadiobutton.setChecked(False)
            elif profile_settings_dict["settings"]["binmode"] == "flatpak":
                self.ui.NativeRadiobutton.setChecked(False)
                self.ui.WineRadiobutton.setChecked(False)
                self.ui.FlatpakRadiobutton.setChecked(True)
            else:
                self.ui.NativeRadiobutton.setChecked(True)
                self.ui.WineRadiobutton.setChecked(False)
                self.ui.FlatpakRadiobutton.setChecked(False)
        except Exception as e:
            print("No binmode setting found. Defaulting to \"native\".")
            self.ui.NativeRadiobutton.setChecked(True)
            self.ui.WineRadiobutton.setChecked(False)
            self.ui.FlatpakRadiobutton.setChecked(False)

        # Modding section & Files
        self.ui.SaveFilesToConfigToggle.setChecked(profile_settings_dict["settings"]["includefiles"])
        self.ui.ModDirInput.setText(profile_settings_dict["settings"]["moddir"])

        self.ui.GameFilesList.clear()
        if self.ui.SaveFilesToConfigToggle.isChecked:
            for f in profile_settings_dict["files"]:
                self.add_file(f)

        # General Tab
        self.ui.ServerNameInput.setText( profile_settings_dict["host"]["hostname"] )
        self.ui.AdminPasswordInput.setText( profile_settings_dict["host"]["password"] )
        self.ui.RoomInput.setCurrentIndex( profile_settings_dict["host"]["room"] )
        self.ui.HostMSCombobox.setCurrentText( profile_settings_dict["host"]["masterserver"] )
        self.ui.DedicatedServerToggle.setChecked( profile_settings_dict["host"]["dedicated"] )
        ## Networking section
        self.ui.PortInput.setValue( profile_settings_dict["host"]["port"] )
        self.ui.Ipv6Checkbox.setChecked( profile_settings_dict["host"]["ipv6"] )
        self.ui.BandwidthInput.setValue( profile_settings_dict["host"]["bandwidth"] )
        self.ui.ExtraticInput.setValue( profile_settings_dict["host"]["extratic"] )
        self.ui.UpnpCheckbox.setChecked( profile_settings_dict["host"]["upnp"] )
        self.ui.UploadToggle.setChecked( profile_settings_dict["host"]["downloading"] )
        self.ui.DownloadspeedInput.setValue( profile_settings_dict["host"]["downloadspeed"] )
        self.ui.MaxsendInput.setValue( profile_settings_dict["host"]["maxsend"] )
        self.ui.MaxpingInput.setValue( profile_settings_dict["host"]["maxping"] )
        self.ui.ResynchattemptsInput.setValue( profile_settings_dict["host"]["resynchattempts"] )
        # Game Tab
        self.ui.GametypeInput.setCurrentIndex( profile_settings_dict["host"]["gametype"] )
        self.ui.AdvanceMapInput.setCurrentIndex( profile_settings_dict["host"]["advancemap"] )
        self.ui.PointLimitInput.setValue( profile_settings_dict["host"]["pointlimit"] )
        self.ui.AllowexitlevelCheckbox.setChecked( profile_settings_dict["host"]["allowexitlevel"] )
        self.ui.ExitmoveCheckbox.setChecked( profile_settings_dict["host"]["exitmove"] )
        self.ui.MaxPlayersInput.setValue( profile_settings_dict["host"]["maxplayers"] )
        self.ui.JoinnextroundCheckbox.setChecked( profile_settings_dict["host"]["joinnextround"] )
        self.ui.ForceSkinInput.setCurrentText( profile_settings_dict["host"]["forceskin"] )
        self.ui.RestrictskinchangesCheckbox.setChecked( profile_settings_dict["host"]["restrictskinchanges"] )
        self.ui.TailspickupCheckbox.setChecked( profile_settings_dict["host"]["tailspickup"] )
        self.ui.RespawnitemtimeInput.setValue( profile_settings_dict["host"]["respawnitemtime"] )
        self.ui.RespawnitemCheckbox.setChecked( profile_settings_dict["host"]["respawnitem"] )
        self.ui.Tv_1upInput.setValue( profile_settings_dict["host"]["tv_1up"] )
        self.ui.Tv_invincibilityInput.setValue( profile_settings_dict["host"]["tv_invincibility"] )
        self.ui.Tv_supersneakersInput.setValue( profile_settings_dict["host"]["tv_supersneakers"] )
        self.ui.Tv_bombshieldInput.setValue( profile_settings_dict["host"]["tv_bombshield"] )
        self.ui.Tv_forceshieldInput.setValue( profile_settings_dict["host"]["tv_forceshield"] )
        self.ui.Tv_jumpshieldInput.setValue( profile_settings_dict["host"]["tv_jumpshield"] )
        self.ui.Tv_ringshieldInput.setValue( profile_settings_dict["host"]["tv_ringshield"] )
        self.ui.Tv_watershieldInput.setValue( profile_settings_dict["host"]["tv_watershield"] )
        self.ui.Tv_eggmanInput.setValue( profile_settings_dict["host"]["tv_eggman"] )
        self.ui.Tv_superringInput.setValue( profile_settings_dict["host"]["tv_superring"] )
        self.ui.Tv_teleporterInput.setValue( profile_settings_dict["host"]["tv_teleporter"] )
        self.ui.Tv_recyclerInput.setValue( profile_settings_dict["host"]["tv_recycler"] )
        self.ui.SoniccdCheckbox.setChecked( profile_settings_dict["host"]["soniccd"] )
        self.ui.KillingdeadCheckbox.setChecked( profile_settings_dict["host"]["killingdead"] )
        # Co-op Tab
        self.ui.CoopSettingsCheckbox.setChecked( profile_settings_dict["host"]["applycoop"] )
        self.ui.StartinglivesInput.setValue( profile_settings_dict["host"]["startinglives"] )
        self.ui.PlayersforexitCombobox.setCurrentIndex( profile_settings_dict["host"]["playersforexit"] )
        self.ui.CompetitionboxesCombobox.setCurrentIndex( profile_settings_dict["host"]["competitionboxes"] )
        # Ringslinger Tab
        self.ui.RingslingerSettingsCheckbox.setChecked( profile_settings_dict["host"]["applyringslinger"] )
        self.ui.PointLimitInput.setValue( profile_settings_dict["host"]["pointlimit"] )
        self.ui.MatchscoringCombobox.setCurrentIndex( profile_settings_dict["host"]["matchscoring"] )
        self.ui.TimeLimitInput.setValue( profile_settings_dict["host"]["timelimit"] )
        self.ui.OvertimeCheckbox.setChecked( profile_settings_dict["host"]["overtime"] )
        self.ui.RespawndelayInput.setValue( profile_settings_dict["host"]["respawndelay"] )
        self.ui.SuddenDeathToggle.setChecked( profile_settings_dict["host"]["suddendeath"] )
        self.ui.DisableWeaponsToggle.setChecked( profile_settings_dict["host"]["disableweaponrings"] )
        self.ui.PowerstonesCheckbox.setChecked( profile_settings_dict["host"]["powerstones"] )
        self.ui.MatchboxesCombobox.setCurrentIndex( profile_settings_dict["host"]["matchboxes"] )
        self.ui.MatchboxesCombobox.setCurrentIndex( profile_settings_dict["host"]["scrambleteams"] )
        self.ui.AutobalanceCheckbox.setCurrentIndex( profile_settings_dict["host"]["autobalance"] )
        self.ui.FlagtimeInput.setValue( profile_settings_dict["host"]["flagtime"] )
        self.ui.FriendlyfireCheckbox.setChecked( profile_settings_dict["host"]["friendlyfire"] )
        self.ui.TouchtagCheckbox.setChecked( profile_settings_dict["host"]["touchtag"] )
        self.ui.HidetimeInput.setValue( profile_settings_dict["host"]["hidetime"] )
        # Circuit Race Tab
        self.ui.CircuitraceSettingsCheckbox.setChecked( profile_settings_dict["host"]["applycircuitrace"] )
        self.ui.NumlapsInput.setValue( profile_settings_dict["host"]["numlaps"] )
        self.ui.UsemaplapsCheckbox.setChecked( profile_settings_dict["host"]["usemaplaps"] )
        self.ui.CountdowntimeInput.setValue( profile_settings_dict["host"]["countdowntime"] )
        # Battlemod Tab
        self.ui.BattlemodSettingsCheckbox.setChecked( profile_settings_dict["host"]["applybattlemod"] )
        self.ui.Battle_coyotetimeInput.setValue( profile_settings_dict["host"]["battle_coyotetime"] )
        self.ui.Battle_coyotefactorInput.setValue( profile_settings_dict["host"]["battle_coyotefactor"] )
        self.ui.Battle_recoveryjumpCheckbox.setChecked( profile_settings_dict["host"]["battle_recoveryjump"] )
        ## Item settings
        self.ui.Item_rateCombobox.setCurrentIndex( profile_settings_dict["host"]["item_rate"])
        self.ui.Item_typeCombobox.setCurrentIndex( profile_settings_dict["host"]["item_type"])
        self.ui.Item_globalCheckbox.setChecked( profile_settings_dict["host"]["item_global"])
        self.ui.Item_localCheckbox.setChecked( profile_settings_dict["host"]["item_local"])
        ## Battle mode settings
        self.ui.Survival_livesInput.setValue( profile_settings_dict["host"]["survival_lives"] )
        self.ui.Battle_startringsInput.setValue( profile_settings_dict["host"]["battle_startrings"] )
        self.ui.Survival_revengeCombobox.setCurrentIndex( profile_settings_dict["host"]["survival_revenge"] )
        self.ui.Survival_suddendeathCheckbox.setChecked( profile_settings_dict["host"]["survival_suddendeath"] )
        ## Battle/Survival settings
        self.ui.Battle_collisionsCheckbox.setChecked( profile_settings_dict["host"]["battle_collisions"] )
        self.ui.Battle_slipstreamsheckbox.setChecked( profile_settings_dict["host"]["battle_slipstream"] )
        self.ui.Battle_specialCheckbox.setChecked( profile_settings_dict["host"]["battle_special"] )
        self.ui.Battle_shieldstocksCheckbox.setChecked( profile_settings_dict["host"]["battle_shieldstocks"] )
        self.ui.Battle_preroundCheckbox.setChecked( profile_settings_dict["host"]["battle_preround"] )
        ## CP Ring spawns
        self.ui.Cp_spawninfinityInput.setChecked( profile_settings_dict["host"]["cp_spawninfinity"] )
        self.ui.Cp_spawnautoInput.setChecked( profile_settings_dict["host"]["cp_spawnauto"] )
        self.ui.Cp_spawnbounceInput.setChecked( profile_settings_dict["host"]["cp_spawnbounce"] )
        self.ui.Cp_spawnbombInput.setChecked( profile_settings_dict["host"]["cp_spawnbomb"] )
        self.ui.Cp_spawngrenadeInput.setChecked( profile_settings_dict["host"]["cp_spawngrenade"] )
        self.ui.Cp_spawnrailInput.setChecked( profile_settings_dict["host"]["cp_spawnrail"] )
        self.ui.Cp_spawnscatterInput.setChecked( profile_settings_dict["host"]["cp_spawnscatter"] )
        ## Battle CTF
        self.ui.Ctf_flagdrop_graceperiodInput.setValue( profile_settings_dict["host"]["ctf_flagdrop_graceperiod"] )
        self.ui.Ctf_flagrespawn_graceperiodInput.setValue( profile_settings_dict["host"]["ctf_flagrespawn_graceperiod"] )
        ## Battle Diamond hunt
        self.ui.Diamond_capture_timeInput.setValue( profile_settings_dict["host"]["diamond_capture_time"] )
        self.ui.Diamond_capture_bonusInput.setValue( profile_settings_dict["host"]["diamond_capture_bonus"] )
        ## Battle Misc
        self.ui.Battle_addoptionsInput.setText( profile_settings_dict["host"]["battle_addoptions"] )

        self.change_skin_image()
        self.ui.ProfilesStatusLabel.setText("Profile successfully loaded.")

    
    def update_binmode_in_ui(self):
        if self.ui.WineRadiobutton.isChecked():
            self.ui.GameExecFilePathInput.setEnabled(True)
            self.ui.GameExecFilePathBrowse.setEnabled(True)
        elif self.ui.FlatpakRadiobutton.isChecked():
            self.ui.GameExecFilePathInput.setEnabled(False)
            self.ui.GameExecFilePathBrowse.setEnabled(False)
        else:
            self.ui.GameExecFilePathInput.setEnabled(True)
            self.ui.GameExecFilePathBrowse.setEnabled(True)

    def on_apply_checkbox(self):
        self.ui.CoopSettingsGroupbox.setEnabled(self.ui.CoopSettingsCheckbox.isChecked())
        self.ui.RingslingerSettingsGroupbox.setEnabled(self.ui.RingslingerSettingsCheckbox.isChecked())
        self.ui.CircuitraceSettingsGroupbox.setEnabled(self.ui.CircuitraceSettingsCheckbox.isChecked())
        self.ui.BattlemodSettingsGroupbox.setEnabled(self.ui.BattlemodSettingsCheckbox.isChecked())

    def generate_profile_dict(self):
        """Converts GUI state to a settings dictionary
        """
        toml_settings = {
            "files": [],
            "mod_download_dest": "",
            "player": {},
            "game": {"resolution": {}},
            "host": {},
            "settings": {
                "binmode": "native",
                "includefiles": True,
                "moddir": "./ll_downloads",
            }
            }

        if self.ui.WineRadiobutton.isChecked():
            toml_settings["settings"]["binmode"] = "wine"
        if self.ui.FlatpakRadiobutton.isChecked():
            toml_settings["settings"]["binmode"] = "flatpak"
        else:
            toml_settings["settings"]["binmode"] = "native"

        toml_settings["settings"]["includefiles"] = self.ui.SaveFilesToConfigToggle.isChecked()
        toml_settings["settings"]["moddir"] = self.ui.ModDirInput.text()

        for i in range(self.ui.GameFilesList.count()):
            toml_settings["files"].append(self.ui.GameFilesList.item(i).text())
        
        toml_settings["player"]["name"] = self.ui.PlayerNameInput.text()
        toml_settings["player"]["skin"] = str(self.ui.PlayerSkinInput.currentText())
        toml_settings["player"]["color"] = self.ui.PlayerColorInput.currentText()
        toml_settings["game"]["resolution"]["width"] = self.ui.GameHorizontalResolutionInput.text()
        toml_settings["game"]["resolution"]["height"] = self.ui.GameVerticalResolutionInput.text()
        toml_settings["game"]["renderer"] = self.ui.GameRendererSetting.currentIndex()
        toml_settings["game"]["windowmode"] = self.ui.GameFullscreenSetting.currentIndex()
        toml_settings["game"]["music"] = self.ui.GameMusicSetting.currentIndex()
        toml_settings["game"]["sound"] = self.ui.GameSoundSetting.currentIndex()
        toml_settings["game"]["exepath"] = self.ui.GameExecFilePathInput.text()
        toml_settings["game"]["cliargs"] = self.ui.GameArgsInput.text()

        # General Tab
        toml_settings["host"]["hostname"] = self.ui.ServerNameInput.text()
        toml_settings["host"]["password"] = self.ui.AdminPasswordInput.text()
        toml_settings["host"]["room"] = self.ui.RoomInput.currentIndex()
        toml_settings["host"]["masterserver"] = self.ui.HostMSCombobox.currentText()
        toml_settings["host"]["dedicated"] = self.ui.DedicatedServerToggle.isChecked()
        ## Networking section
        toml_settings["host"]["port"] = self.ui.PortInput.value()
        toml_settings["host"]["ipv6"] = self.ui.Ipv6Checkbox.isChecked()
        toml_settings["host"]["bandwidth"] = self.ui.BandwidthInput.value()
        toml_settings["host"]["extratic"] = self.ui.ExtraticInput.value()
        toml_settings["host"]["upnp"] = self.ui.UpnpCheckbox.isChecked()
        toml_settings["host"]["downloading"] = self.ui.UploadToggle.isChecked()
        toml_settings["host"]["downloadspeed"] = self.ui.DownloadspeedInput.value()
        toml_settings["host"]["maxsend"] = self.ui.MaxsendInput.value()
        toml_settings["host"]["maxping"] = self.ui.MaxpingInput.value()
        toml_settings["host"]["resynchattempts"] = self.ui.ResynchattemptsInput.value()
        # Game Tab
        toml_settings["host"]["gametype"] = self.ui.GametypeInput.currentIndex()
        toml_settings["host"]["advancemap"] = self.ui.AdvanceMapInput.currentIndex()
        toml_settings["host"]["pointlimit"] = self.ui.PointLimitInput.value()
        toml_settings["host"]["allowexitlevel"] = self.ui.AllowexitlevelCheckbox.isChecked()
        toml_settings["host"]["exitmove"] = self.ui.ExitmoveCheckbox.isChecked()
        toml_settings["host"]["maxplayers"] = self.ui.MaxPlayersInput.value()
        toml_settings["host"]["joinnextround"] = self.ui.JoinnextroundCheckbox.isChecked()
        toml_settings["host"]["forceskin"] = str(self.ui.ForceSkinInput.currentText())
        toml_settings["host"]["restrictskinchanges"] = self.ui.RestrictskinchangesCheckbox.isChecked()
        toml_settings["host"]["tailspickup"] = self.ui.TailspickupCheckbox.isChecked()
        toml_settings["host"]["respawnitemtime"] = self.ui.RespawnitemtimeInput.value()
        toml_settings["host"]["respawnitem"] = self.ui.RespawnitemCheckbox.isChecked()
        toml_settings["host"]["tv_1up"] = self.ui.Tv_1upInput.value()
        toml_settings["host"]["tv_invincibility"] = self.ui.Tv_invincibilityInput.value()
        toml_settings["host"]["tv_supersneakers"] = self.ui.Tv_supersneakersInput.value()
        toml_settings["host"]["tv_bombshield"] = self.ui.Tv_bombshieldInput.value()
        toml_settings["host"]["tv_forceshield"] = self.ui.Tv_forceshieldInput.value()
        toml_settings["host"]["tv_jumpshield"] = self.ui.Tv_jumpshieldInput.value()
        toml_settings["host"]["tv_ringshield"] = self.ui.Tv_ringshieldInput.value()
        toml_settings["host"]["tv_watershield"] = self.ui.Tv_watershieldInput.value()
        toml_settings["host"]["tv_eggman"] = self.ui.Tv_eggmanInput.value()
        toml_settings["host"]["tv_superring"] = self.ui.Tv_superringInput.value()
        toml_settings["host"]["tv_teleporter"] = self.ui.Tv_teleporterInput.value()
        toml_settings["host"]["tv_recycler"] = self.ui.Tv_recyclerInput.value()
        toml_settings["host"]["soniccd"] = self.ui.SoniccdCheckbox.isChecked()
        toml_settings["host"]["killingdead"] = self.ui.KillingdeadCheckbox.isChecked()
        # Co-op Tab
        toml_settings["host"]["applycoop"] = self.ui.CoopSettingsCheckbox.isChecked()
        toml_settings["host"]["startinglives"] = self.ui.StartinglivesInput.value()
        toml_settings["host"]["playersforexit"] = self.ui.PlayersforexitCombobox.currentIndex()
        toml_settings["host"]["competitionboxes"] = self.ui.CompetitionboxesCombobox.currentIndex()
        # Ringslinger Tab
        toml_settings["host"]["applyringslinger"] = self.ui.RingslingerSettingsCheckbox.isChecked()
        toml_settings["host"]["pointlimit"] = self.ui.PointLimitInput.value()
        toml_settings["host"]["matchscoring"] = self.ui.MatchscoringCombobox.currentIndex()
        toml_settings["host"]["timelimit"] = self.ui.TimeLimitInput.value()
        toml_settings["host"]["overtime"] = self.ui.OvertimeCheckbox.isChecked()
        toml_settings["host"]["respawndelay"] = self.ui.RespawndelayInput.value()
        toml_settings["host"]["suddendeath"] = self.ui.SuddenDeathToggle.isChecked()
        toml_settings["host"]["disableweaponrings"] = self.ui.DisableWeaponsToggle.isChecked()
        toml_settings["host"]["powerstones"] = self.ui.PowerstonesCheckbox.isChecked()
        toml_settings["host"]["matchboxes"] = self.ui.MatchboxesCombobox.currentIndex()
        toml_settings["host"]["scrambleteams"] = self.ui.MatchboxesCombobox.currentIndex()
        toml_settings["host"]["autobalance"] = self.ui.AutobalanceCheckbox.currentIndex()
        toml_settings["host"]["flagtime"] = self.ui.FlagtimeInput.value()
        toml_settings["host"]["friendlyfire"] = self.ui.FriendlyfireCheckbox.isChecked()
        toml_settings["host"]["touchtag"] = self.ui.TouchtagCheckbox.isChecked()
        toml_settings["host"]["hidetime"] = self.ui.HidetimeInput.value()
        # Circuit Race Tab
        toml_settings["host"]["applycircuitrace"] = self.ui.CircuitraceSettingsCheckbox.isChecked()
        toml_settings["host"]["numlaps"] = self.ui.NumlapsInput.value()
        toml_settings["host"]["usemaplaps"] = self.ui.UsemaplapsCheckbox.isChecked()
        toml_settings["host"]["countdowntime"] = self.ui.CountdowntimeInput.value()
        # Battlemod Tab
        toml_settings["host"]["applybattlemod"] = self.ui.BattlemodSettingsCheckbox.isChecked()
        toml_settings["host"]["battle_coyotetime"] = self.ui.Battle_coyotetimeInput.value()
        toml_settings["host"]["battle_coyotefactor"] = self.ui.Battle_coyotefactorInput.value()
        toml_settings["host"]["battle_recoveryjump"] = self.ui.Battle_recoveryjumpCheckbox.isChecked()
        ## Item settings
        toml_settings["host"]["item_rate"] = self.ui.Item_rateCombobox.currentIndex()
        toml_settings["host"]["item_type"] = self.ui.Item_typeCombobox.currentIndex()
        toml_settings["host"]["item_global"] = self.ui.Item_globalCheckbox.isChecked()
        toml_settings["host"]["item_local"] = self.ui.Item_localCheckbox.isChecked()
        ## Battle mode settings
        toml_settings["host"]["survival_lives"] = self.ui.Survival_livesInput.value()
        toml_settings["host"]["battle_startrings"] = self.ui.Battle_startringsInput.value()
        toml_settings["host"]["survival_revenge"] = self.ui.Survival_revengeCombobox.currentIndex()
        toml_settings["host"]["survival_suddendeath"] = self.ui.Survival_suddendeathCheckbox.isChecked()
        ## Battle/Survival settings
        toml_settings["host"]["battle_collisions"] = self.ui.Battle_collisionsCheckbox.isChecked()
        toml_settings["host"]["battle_slipstream"] = self.ui.Battle_slipstreamsheckbox.isChecked()
        toml_settings["host"]["battle_special"] = self.ui.Battle_specialCheckbox.isChecked()
        toml_settings["host"]["battle_shieldstocks"] = self.ui.Battle_shieldstocksCheckbox.isChecked()
        toml_settings["host"]["battle_preround"] = self.ui.Battle_preroundCheckbox.isChecked()
        ## CP Ring spawns
        toml_settings["host"]["cp_spawninfinity"] = self.ui.Cp_spawninfinityInput.isChecked()
        toml_settings["host"]["cp_spawnauto"] = self.ui.Cp_spawnautoInput.isChecked()
        toml_settings["host"]["cp_spawnbounce"] = self.ui.Cp_spawnbounceInput.isChecked()
        toml_settings["host"]["cp_spawnbomb"] = self.ui.Cp_spawnbombInput.isChecked()
        toml_settings["host"]["cp_spawngrenade"] = self.ui.Cp_spawngrenadeInput.isChecked()
        toml_settings["host"]["cp_spawnrail"] = self.ui.Cp_spawnrailInput.isChecked()
        toml_settings["host"]["cp_spawnscatter"] = self.ui.Cp_spawnscatterInput.isChecked()
        ## Battle CTF
        toml_settings["host"]["ctf_flagdrop_graceperiod"] = self.ui.Ctf_flagdrop_graceperiodInput.value()
        toml_settings["host"]["ctf_flagrespawn_graceperiod"] = self.ui.Ctf_flagrespawn_graceperiodInput.value()
        ## Battle Diamond hunt
        toml_settings["host"]["diamond_capture_time"] = self.ui.Diamond_capture_timeInput.value()
        toml_settings["host"]["diamond_capture_bonus"] = self.ui.Diamond_capture_bonusInput.value()
        ## Battle Misc
        toml_settings["host"]["battle_addoptions"] = self.ui.Battle_addoptionsInput.text()
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
                cmd = [ i if " " not in i else "\"{}\"".format(i) for i in self.get_server_launch_command()]
                out_text += ' '.join(cmd)
            else:
                cmd = [ i if " " not in i else "\"{}\"".format(i) for i in self.get_client_launch_command()]
                out_text += ' '.join(cmd)
            with open(fileName, "w") as f:
                f.write(out_text)
        return

    def on_check_version_cb(self, latest_version):
            # check launcher version ============================================= #
            if version.parse(latest_version) > version.parse(versionString):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Your version of LiquidLauncher seems to be outdated. Please download version {} from our <a href=\"https://github.com/liquidunderground/liquidlauncher/releases\">releases</a>.".format(latest_version) )
                msg.setWindowTitle("Version {} available".format(latest_version))
                msg.setDetailedText("Latest version of LiquidLauncher: " + latest_version+ "\nYou are currently running: " + versionString)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            elif version.parse(latest_version) < version.parse(versionString):
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
