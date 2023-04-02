# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lb2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import lb2_rc
import lb2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 638)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DockTabFrame = QFrame(self.centralwidget)
        self.DockTabFrame.setObjectName(u"DockTabFrame")
        self.DockTabFrame.setMaximumSize(QSize(16777215, 128))
        self.DockTabFrame.setFrameShape(QFrame.StyledPanel)
        self.DockTabFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.DockTabFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.NewsTabButton = QRadioButton(self.DockTabFrame)
        self.NewsTabButton.setObjectName(u"NewsTabButton")
        icon = QIcon()
        icon.addFile(u":/assets/img/icons/news.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NewsTabButton.setIcon(icon)
        self.NewsTabButton.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.NewsTabButton)

        self.GameTabButton = QRadioButton(self.DockTabFrame)
        self.GameTabButton.setObjectName(u"GameTabButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.GameTabButton.sizePolicy().hasHeightForWidth())
        self.GameTabButton.setSizePolicy(sizePolicy1)
        self.GameTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/assets/img/icons/srb2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameTabButton.setIcon(icon1)
        self.GameTabButton.setIconSize(QSize(48, 48))
        self.GameTabButton.setChecked(True)

        self.horizontalLayout.addWidget(self.GameTabButton)

        self.HelpTabButton = QRadioButton(self.DockTabFrame)
        self.HelpTabButton.setObjectName(u"HelpTabButton")
        self.HelpTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/assets/img/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpTabButton.setIcon(icon2)
        self.HelpTabButton.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.HelpTabButton)

        self.SettingsTabButton = QRadioButton(self.DockTabFrame)
        self.SettingsTabButton.setObjectName(u"SettingsTabButton")
        self.SettingsTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/assets/img/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsTabButton.setIcon(icon3)
        self.SettingsTabButton.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.SettingsTabButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.DockTabFrame)

        self.MainAreaFrame = QFrame(self.centralwidget)
        self.MainAreaFrame.setObjectName(u"MainAreaFrame")
        self.MainAreaFrame.setFrameShape(QFrame.StyledPanel)
        self.MainAreaFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.MainAreaFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainTabsStackedWidget = QStackedWidget(self.MainAreaFrame)
        self.MainTabsStackedWidget.setObjectName(u"MainTabsStackedWidget")
        self.NewsPage = QWidget()
        self.NewsPage.setObjectName(u"NewsPage")
        self.verticalLayout_14 = QVBoxLayout(self.NewsPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.NewsScrollArea = QScrollArea(self.NewsPage)
        self.NewsScrollArea.setObjectName(u"NewsScrollArea")
        self.NewsScrollArea.setStyleSheet(u"")
        self.NewsScrollArea.setWidgetResizable(True)
        self.NewsScrollAreaContent = QWidget()
        self.NewsScrollAreaContent.setObjectName(u"NewsScrollAreaContent")
        self.NewsScrollAreaContent.setGeometry(QRect(0, 0, 190, 42))
        self.NewsScrollAreaContent.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.NewsScrollAreaContent)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.NewsTitleLabel = QLabel(self.NewsScrollAreaContent)
        self.NewsTitleLabel.setObjectName(u"NewsTitleLabel")
        self.NewsTitleLabel.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.NewsTitleLabel)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_7)

        self.NewsScrollArea.setWidget(self.NewsScrollAreaContent)

        self.verticalLayout_14.addWidget(self.NewsScrollArea)

        self.MainTabsStackedWidget.addWidget(self.NewsPage)
        self.GamePage = QWidget()
        self.GamePage.setObjectName(u"GamePage")
        self.verticalLayout_3 = QVBoxLayout(self.GamePage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.GamePageFrame = QFrame(self.GamePage)
        self.GamePageFrame.setObjectName(u"GamePageFrame")
        self.GamePageFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePageFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.GamePageFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.GamePageFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.GamePageTabsFrame = QFrame(self.splitter)
        self.GamePageTabsFrame.setObjectName(u"GamePageTabsFrame")
        self.GamePageTabsFrame.setMaximumSize(QSize(160, 16777215))
        self.GamePageTabsFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePageTabsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.GamePageTabsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ProfileTabButton = QRadioButton(self.GamePageTabsFrame)
        self.ProfileTabButton.setObjectName(u"ProfileTabButton")
        self.ProfileTabButton.setMinimumSize(QSize(0, 36))
        self.ProfileTabButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.ProfileTabButton)

        self.FilesTabButton = QRadioButton(self.GamePageTabsFrame)
        self.FilesTabButton.setObjectName(u"FilesTabButton")
        self.FilesTabButton.setMinimumSize(QSize(0, 36))

        self.verticalLayout_2.addWidget(self.FilesTabButton)

        self.GameSettingsTabButton = QRadioButton(self.GamePageTabsFrame)
        self.GameSettingsTabButton.setObjectName(u"GameSettingsTabButton")
        self.GameSettingsTabButton.setMinimumSize(QSize(0, 36))

        self.verticalLayout_2.addWidget(self.GameSettingsTabButton)

        self.line = QFrame(self.GamePageTabsFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.PlayerSetupTabButton = QRadioButton(self.GamePageTabsFrame)
        self.PlayerSetupTabButton.setObjectName(u"PlayerSetupTabButton")
        self.PlayerSetupTabButton.setMinimumSize(QSize(0, 36))

        self.verticalLayout_2.addWidget(self.PlayerSetupTabButton)

        self.HostGameTabButton = QRadioButton(self.GamePageTabsFrame)
        self.HostGameTabButton.setObjectName(u"HostGameTabButton")
        self.HostGameTabButton.setMinimumSize(QSize(0, 36))

        self.verticalLayout_2.addWidget(self.HostGameTabButton)

        self.JoinGameTabButton = QRadioButton(self.GamePageTabsFrame)
        self.JoinGameTabButton.setObjectName(u"JoinGameTabButton")
        self.JoinGameTabButton.setMinimumSize(QSize(0, 36))
        self.JoinGameTabButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.JoinGameTabButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.GamePageTabsFrame)
        self.GamePageContentFrame = QFrame(self.splitter)
        self.GamePageContentFrame.setObjectName(u"GamePageContentFrame")
        self.GamePageContentFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePageContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.GamePageContentFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GameContentStackedWidget = QStackedWidget(self.GamePageContentFrame)
        self.GameContentStackedWidget.setObjectName(u"GameContentStackedWidget")
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.verticalLayout_10 = QVBoxLayout(self.ProfilePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.ProfilePage)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label)

        self.ProfileNameInput = QLineEdit(self.ProfilePage)
        self.ProfileNameInput.setObjectName(u"ProfileNameInput")

        self.verticalLayout_10.addWidget(self.ProfileNameInput)

        self.label_8 = QLabel(self.ProfilePage)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.ProfileFilenameInput = QLineEdit(self.ProfilePage)
        self.ProfileFilenameInput.setObjectName(u"ProfileFilenameInput")

        self.verticalLayout_10.addWidget(self.ProfileFilenameInput)

        self.label_2 = QLabel(self.ProfilePage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.ProfileGameSetting = QComboBox(self.ProfilePage)
        self.ProfileGameSetting.addItem("")
        self.ProfileGameSetting.addItem("")
        self.ProfileGameSetting.setObjectName(u"ProfileGameSetting")

        self.verticalLayout_10.addWidget(self.ProfileGameSetting)

        self.label_3 = QLabel(self.ProfilePage)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.ProfileVersionSetting = QComboBox(self.ProfilePage)
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.setObjectName(u"ProfileVersionSetting")

        self.verticalLayout_10.addWidget(self.ProfileVersionSetting)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.GameContentStackedWidget.addWidget(self.ProfilePage)
        self.FilesPage = QWidget()
        self.FilesPage.setObjectName(u"FilesPage")
        self.verticalLayout_5 = QVBoxLayout(self.FilesPage)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.tabWidget = QTabWidget(self.FilesPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_17 = QVBoxLayout(self.tab_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.GameFilesList = QListWidget(self.tab_3)
        icon4 = QIcon()
        icon4.addFile(u":/assets/img/filetypes/wad.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/assets/img/filetypes/pk3.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem1.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/assets/img/filetypes/lua.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem2.setIcon(icon6);
        self.GameFilesList.setObjectName(u"GameFilesList")
        self.GameFilesList.setStyleSheet(u"")
        self.GameFilesList.setDragEnabled(True)
        self.GameFilesList.setDragDropOverwriteMode(False)
        self.GameFilesList.setDragDropMode(QAbstractItemView.DropOnly)
        self.GameFilesList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.GameFilesList.setIconSize(QSize(32, 32))
        self.GameFilesList.setMovement(QListView.Static)

        self.verticalLayout_17.addWidget(self.GameFilesList)

        self.GameFilesButtonFrame1 = QFrame(self.tab_3)
        self.GameFilesButtonFrame1.setObjectName(u"GameFilesButtonFrame1")
        self.GameFilesButtonFrame1.setFrameShape(QFrame.StyledPanel)
        self.GameFilesButtonFrame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.GameFilesButtonFrame1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.GameFilesUpButton = QPushButton(self.GameFilesButtonFrame1)
        self.GameFilesUpButton.setObjectName(u"GameFilesUpButton")
        self.GameFilesUpButton.setMinimumSize(QSize(0, 28))
        self.GameFilesUpButton.setMaximumSize(QSize(28, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/assets/img/uparrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesUpButton.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.GameFilesUpButton)

        self.GameFilesButtonFrame3 = QFrame(self.GameFilesButtonFrame1)
        self.GameFilesButtonFrame3.setObjectName(u"GameFilesButtonFrame3")
        self.GameFilesButtonFrame3.setFrameShape(QFrame.StyledPanel)
        self.GameFilesButtonFrame3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.GameFilesButtonFrame3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.GameFilesClearButton = QPushButton(self.GameFilesButtonFrame3)
        self.GameFilesClearButton.setObjectName(u"GameFilesClearButton")
        self.GameFilesClearButton.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_5.addWidget(self.GameFilesClearButton)

        self.GameFilesDeleteButton = QPushButton(self.GameFilesButtonFrame3)
        self.GameFilesDeleteButton.setObjectName(u"GameFilesDeleteButton")
        self.GameFilesDeleteButton.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_5.addWidget(self.GameFilesDeleteButton)


        self.horizontalLayout_13.addWidget(self.GameFilesButtonFrame3)


        self.verticalLayout_17.addWidget(self.GameFilesButtonFrame1)

        self.GameFilesButtonFrame2 = QFrame(self.tab_3)
        self.GameFilesButtonFrame2.setObjectName(u"GameFilesButtonFrame2")
        self.GameFilesButtonFrame2.setFrameShape(QFrame.StyledPanel)
        self.GameFilesButtonFrame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.GameFilesButtonFrame2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.GameFilesDownButton = QPushButton(self.GameFilesButtonFrame2)
        self.GameFilesDownButton.setObjectName(u"GameFilesDownButton")
        self.GameFilesDownButton.setMinimumSize(QSize(0, 28))
        self.GameFilesDownButton.setMaximumSize(QSize(28, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/assets/img/combobox-dropdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDownButton.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.GameFilesDownButton)

        self.GameFilesButtonFrame4 = QFrame(self.GameFilesButtonFrame2)
        self.GameFilesButtonFrame4.setObjectName(u"GameFilesButtonFrame4")
        self.GameFilesButtonFrame4.setFrameShape(QFrame.StyledPanel)
        self.GameFilesButtonFrame4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.GameFilesButtonFrame4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.GameFilesSaveButton = QPushButton(self.GameFilesButtonFrame4)
        self.GameFilesSaveButton.setObjectName(u"GameFilesSaveButton")
        self.GameFilesSaveButton.setMinimumSize(QSize(0, 28))
        self.GameFilesSaveButton.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.GameFilesSaveButton)

        self.GameFilesLoadButton = QPushButton(self.GameFilesButtonFrame4)
        self.GameFilesLoadButton.setObjectName(u"GameFilesLoadButton")
        self.GameFilesLoadButton.setMinimumSize(QSize(0, 28))
        self.GameFilesLoadButton.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.GameFilesLoadButton)

        self.GameFilesAddButton = QPushButton(self.GameFilesButtonFrame4)
        self.GameFilesAddButton.setObjectName(u"GameFilesAddButton")
        self.GameFilesAddButton.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_6.addWidget(self.GameFilesAddButton)


        self.horizontalLayout_12.addWidget(self.GameFilesButtonFrame4)


        self.verticalLayout_17.addWidget(self.GameFilesButtonFrame2)

        self.GameFilesExecuteScriptLabel = QLabel(self.tab_3)
        self.GameFilesExecuteScriptLabel.setObjectName(u"GameFilesExecuteScriptLabel")

        self.verticalLayout_17.addWidget(self.GameFilesExecuteScriptLabel)

        self.GameFilesExecuteScript = QFrame(self.tab_3)
        self.GameFilesExecuteScript.setObjectName(u"GameFilesExecuteScript")
        self.GameFilesExecuteScript.setFrameShape(QFrame.StyledPanel)
        self.GameFilesExecuteScript.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.GameFilesExecuteScript)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.GameFilesExecScriptInput = QLineEdit(self.GameFilesExecuteScript)
        self.GameFilesExecScriptInput.setObjectName(u"GameFilesExecScriptInput")

        self.horizontalLayout_7.addWidget(self.GameFilesExecScriptInput)

        self.GameFilesExecScrBrowseButton = QPushButton(self.GameFilesExecuteScript)
        self.GameFilesExecScrBrowseButton.setObjectName(u"GameFilesExecScrBrowseButton")
        self.GameFilesExecScrBrowseButton.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_7.addWidget(self.GameFilesExecScrBrowseButton)


        self.verticalLayout_17.addWidget(self.GameFilesExecuteScript)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_26 = QVBoxLayout(self.tab_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_3 = QWidget(self.tab_4)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_25 = QVBoxLayout(self.widget_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.splitter_2 = QSplitter(self.widget_3)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_24 = QVBoxLayout(self.groupBox)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.verticalLayout_24.addWidget(self.label_7)

        self.ModsList = QListWidget(self.groupBox)
        self.ModsList.setObjectName(u"ModsList")
        sizePolicy.setHeightForWidth(self.ModsList.sizePolicy().hasHeightForWidth())
        self.ModsList.setSizePolicy(sizePolicy)

        self.verticalLayout_24.addWidget(self.ModsList)

        self.splitter_2.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(6, 0, 0, 0)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.verticalLayout_21.addWidget(self.label_6)

        self.ModBrowser = QWebEngineView(self.groupBox_2)
        self.ModBrowser.setObjectName(u"ModBrowser")
        sizePolicy.setHeightForWidth(self.ModBrowser.sizePolicy().hasHeightForWidth())
        self.ModBrowser.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(110, 113, 115, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.ModBrowser.setPalette(palette)
        self.ModBrowser.setAutoFillBackground(True)
        self.ModBrowser.setStyleSheet(u"* {background-color: 1f1f1f;}")
        self.ModBrowser.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_21.addWidget(self.ModBrowser)

        self.splitter_2.addWidget(self.groupBox_2)

        self.verticalLayout_25.addWidget(self.splitter_2)


        self.verticalLayout_26.addWidget(self.widget_3)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.ModStatusLabel = QLabel(self.tab_4)
        self.ModStatusLabel.setObjectName(u"ModStatusLabel")

        self.horizontalLayout_20.addWidget(self.ModStatusLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.ModTypeCombo = QComboBox(self.tab_4)
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.setObjectName(u"ModTypeCombo")

        self.horizontalLayout_20.addWidget(self.ModTypeCombo)

        self.OpenPageButton = QPushButton(self.tab_4)
        self.OpenPageButton.setObjectName(u"OpenPageButton")

        self.horizontalLayout_20.addWidget(self.OpenPageButton)

        self.RefreshModsButton = QPushButton(self.tab_4)
        self.RefreshModsButton.setObjectName(u"RefreshModsButton")

        self.horizontalLayout_20.addWidget(self.RefreshModsButton)

        self.DownloadModButton = QPushButton(self.tab_4)
        self.DownloadModButton.setObjectName(u"DownloadModButton")

        self.horizontalLayout_20.addWidget(self.DownloadModButton)


        self.verticalLayout_26.addLayout(self.horizontalLayout_20)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.GameContentStackedWidget.addWidget(self.FilesPage)
        self.GameSettingsPage = QWidget()
        self.GameSettingsPage.setObjectName(u"GameSettingsPage")
        self.verticalLayout_27 = QVBoxLayout(self.GameSettingsPage)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.GameResolutionLabel = QLabel(self.GameSettingsPage)
        self.GameResolutionLabel.setObjectName(u"GameResolutionLabel")
        self.GameResolutionLabel.setMaximumSize(QSize(16777215, 26))
        self.GameResolutionLabel.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.GameResolutionLabel)

        self.GameResolutionSettingsWrapper = QFrame(self.GameSettingsPage)
        self.GameResolutionSettingsWrapper.setObjectName(u"GameResolutionSettingsWrapper")
        self.GameResolutionSettingsWrapper.setMaximumSize(QSize(16777215, 48))
        self.GameResolutionSettingsWrapper.setStyleSheet(u"")
        self.GameResolutionSettingsWrapper.setFrameShape(QFrame.StyledPanel)
        self.GameResolutionSettingsWrapper.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.GameResolutionSettingsWrapper)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.GameHorizontalResolutionInput = QLineEdit(self.GameResolutionSettingsWrapper)
        self.GameHorizontalResolutionInput.setObjectName(u"GameHorizontalResolutionInput")
        self.GameHorizontalResolutionInput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.GameHorizontalResolutionInput, 0, 0, 1, 1)

        self.GameResMultLabel = QLabel(self.GameResolutionSettingsWrapper)
        self.GameResMultLabel.setObjectName(u"GameResMultLabel")
        self.GameResMultLabel.setStyleSheet(u"padding: 0;\n"
"font-size: 12pt;")

        self.gridLayout_3.addWidget(self.GameResMultLabel, 0, 1, 1, 1)

        self.GameVerticalResolutionInput = QLineEdit(self.GameResolutionSettingsWrapper)
        self.GameVerticalResolutionInput.setObjectName(u"GameVerticalResolutionInput")

        self.gridLayout_3.addWidget(self.GameVerticalResolutionInput, 0, 2, 1, 1)


        self.verticalLayout_27.addWidget(self.GameResolutionSettingsWrapper)

        self.GameRenderCfgLabel = QLabel(self.GameSettingsPage)
        self.GameRenderCfgLabel.setObjectName(u"GameRenderCfgLabel")

        self.verticalLayout_27.addWidget(self.GameRenderCfgLabel)

        self.GameRendererSetting = QComboBox(self.GameSettingsPage)
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.setObjectName(u"GameRendererSetting")

        self.verticalLayout_27.addWidget(self.GameRendererSetting)

        self.GameFullscreenSetting = QComboBox(self.GameSettingsPage)
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.setObjectName(u"GameFullscreenSetting")

        self.verticalLayout_27.addWidget(self.GameFullscreenSetting)

        self.GameSoundOptionsLabel = QLabel(self.GameSettingsPage)
        self.GameSoundOptionsLabel.setObjectName(u"GameSoundOptionsLabel")

        self.verticalLayout_27.addWidget(self.GameSoundOptionsLabel)

        self.GameMusicSetting = QComboBox(self.GameSettingsPage)
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.setObjectName(u"GameMusicSetting")

        self.verticalLayout_27.addWidget(self.GameMusicSetting)

        self.GameSoundSetting = QComboBox(self.GameSettingsPage)
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.setObjectName(u"GameSoundSetting")

        self.verticalLayout_27.addWidget(self.GameSoundSetting)

        self.GameExecPathLabel = QLabel(self.GameSettingsPage)
        self.GameExecPathLabel.setObjectName(u"GameExecPathLabel")

        self.verticalLayout_27.addWidget(self.GameExecPathLabel)

        self.GameExecFilePath = QFrame(self.GameSettingsPage)
        self.GameExecFilePath.setObjectName(u"GameExecFilePath")
        self.GameExecFilePath.setFrameShape(QFrame.StyledPanel)
        self.GameExecFilePath.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.GameExecFilePath)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GameExecFilePathInput = QLineEdit(self.GameExecFilePath)
        self.GameExecFilePathInput.setObjectName(u"GameExecFilePathInput")

        self.gridLayout_4.addWidget(self.GameExecFilePathInput, 0, 0, 1, 1)

        self.GameExecFilePathBrowse = QPushButton(self.GameExecFilePath)
        self.GameExecFilePathBrowse.setObjectName(u"GameExecFilePathBrowse")
        self.GameExecFilePathBrowse.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.GameExecFilePathBrowse, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.GameExecFilePath)

        self.WineToggle = QCheckBox(self.GameSettingsPage)
        self.WineToggle.setObjectName(u"WineToggle")
        self.WineToggle.setEnabled(False)
        self.WineToggle.setChecked(False)

        self.verticalLayout_27.addWidget(self.WineToggle)

        self.GameArgsLabel = QLabel(self.GameSettingsPage)
        self.GameArgsLabel.setObjectName(u"GameArgsLabel")

        self.verticalLayout_27.addWidget(self.GameArgsLabel)

        self.GameArgsInput = QLineEdit(self.GameSettingsPage)
        self.GameArgsInput.setObjectName(u"GameArgsInput")

        self.verticalLayout_27.addWidget(self.GameArgsInput)

        self.verticalSpacer_2 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)

        self.GameContentStackedWidget.addWidget(self.GameSettingsPage)
        self.PlayerSetupPage = QWidget()
        self.PlayerSetupPage.setObjectName(u"PlayerSetupPage")
        self.verticalLayout_7 = QVBoxLayout(self.PlayerSetupPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.PlayerNameTitleLabel = QLabel(self.PlayerSetupPage)
        self.PlayerNameTitleLabel.setObjectName(u"PlayerNameTitleLabel")

        self.verticalLayout_7.addWidget(self.PlayerNameTitleLabel)

        self.PlayerNameInput = QLineEdit(self.PlayerSetupPage)
        self.PlayerNameInput.setObjectName(u"PlayerNameInput")

        self.verticalLayout_7.addWidget(self.PlayerNameInput)

        self.PlayerSkinTitleLabel = QLabel(self.PlayerSetupPage)
        self.PlayerSkinTitleLabel.setObjectName(u"PlayerSkinTitleLabel")

        self.verticalLayout_7.addWidget(self.PlayerSkinTitleLabel)

        self.PlayerSkinInput = QComboBox(self.PlayerSetupPage)
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.setObjectName(u"PlayerSkinInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PlayerSkinInput.sizePolicy().hasHeightForWidth())
        self.PlayerSkinInput.setSizePolicy(sizePolicy3)
        self.PlayerSkinInput.setStyleSheet(u"")
        self.PlayerSkinInput.setEditable(True)

        self.verticalLayout_7.addWidget(self.PlayerSkinInput)

        self.PlayerSkinInfoWrapper = QFrame(self.PlayerSetupPage)
        self.PlayerSkinInfoWrapper.setObjectName(u"PlayerSkinInfoWrapper")
        self.PlayerSkinInfoWrapper.setMinimumSize(QSize(0, 64))
        self.PlayerSkinInfoWrapper.setMaximumSize(QSize(16777215, 234))
        self.PlayerSkinInfoWrapper.setStyleSheet(u"")
        self.PlayerSkinInfoWrapper.setFrameShape(QFrame.StyledPanel)
        self.PlayerSkinInfoWrapper.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.PlayerSkinInfoWrapper)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.PlayerSkinImageBox = QFrame(self.PlayerSkinInfoWrapper)
        self.PlayerSkinImageBox.setObjectName(u"PlayerSkinImageBox")
        self.PlayerSkinImageBox.setMinimumSize(QSize(0, 0))
        self.PlayerSkinImageBox.setMaximumSize(QSize(135, 16777215))
        self.PlayerSkinImageBox.setFrameShape(QFrame.StyledPanel)
        self.PlayerSkinImageBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.PlayerSkinImageBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.PlayerSkinImage = QLabel(self.PlayerSkinImageBox)
        self.PlayerSkinImage.setObjectName(u"PlayerSkinImage")
        self.PlayerSkinImage.setMinimumSize(QSize(135, 217))
        self.PlayerSkinImage.setMaximumSize(QSize(135, 1000007))
        self.PlayerSkinImage.setStyleSheet(u"")
        self.PlayerSkinImage.setPixmap(QPixmap(u":/assets/img/sonic.png"))
        self.PlayerSkinImage.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.PlayerSkinImage)


        self.horizontalLayout_8.addWidget(self.PlayerSkinImageBox)

        self.PlayerSkinInfoText = QLabel(self.PlayerSkinInfoWrapper)
        self.PlayerSkinInfoText.setObjectName(u"PlayerSkinInfoText")
        self.PlayerSkinInfoText.setMaximumSize(QSize(16777215, 1000007))
        self.PlayerSkinInfoText.setStyleSheet(u"")
        self.PlayerSkinInfoText.setTextFormat(Qt.RichText)
        self.PlayerSkinInfoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.PlayerSkinInfoText.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.PlayerSkinInfoText)


        self.verticalLayout_7.addWidget(self.PlayerSkinInfoWrapper)

        self.PlayerColorTitleLabel = QLabel(self.PlayerSetupPage)
        self.PlayerColorTitleLabel.setObjectName(u"PlayerColorTitleLabel")

        self.verticalLayout_7.addWidget(self.PlayerColorTitleLabel)

        self.PlayerColorInput = QComboBox(self.PlayerSetupPage)
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.addItem("")
        self.PlayerColorInput.setObjectName(u"PlayerColorInput")

        self.verticalLayout_7.addWidget(self.PlayerColorInput)

        self.verticalSpacer_3 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.GameContentStackedWidget.addWidget(self.PlayerSetupPage)
        self.HostGamePage = QWidget()
        self.HostGamePage.setObjectName(u"HostGamePage")
        self.verticalLayout_8 = QVBoxLayout(self.HostGamePage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.HostGamePage)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 324, 686))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.ServerNameLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ServerNameLabel.setObjectName(u"ServerNameLabel")

        self.verticalLayout_16.addWidget(self.ServerNameLabel)

        self.ServerNameInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.ServerNameInput.setObjectName(u"ServerNameInput")

        self.verticalLayout_16.addWidget(self.ServerNameInput)

        self.AdminPasswordLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.AdminPasswordLabel.setObjectName(u"AdminPasswordLabel")

        self.verticalLayout_16.addWidget(self.AdminPasswordLabel)

        self.AdminPasswordInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.AdminPasswordInput.setObjectName(u"AdminPasswordInput")
        self.AdminPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_16.addWidget(self.AdminPasswordInput)

        self.RoomLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.RoomLabel.setObjectName(u"RoomLabel")

        self.verticalLayout_16.addWidget(self.RoomLabel)

        self.RoomInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.setObjectName(u"RoomInput")

        self.verticalLayout_16.addWidget(self.RoomInput)

        self.GametypeLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.GametypeLabel.setObjectName(u"GametypeLabel")

        self.verticalLayout_16.addWidget(self.GametypeLabel)

        self.GametypeInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.addItem("")
        self.GametypeInput.setObjectName(u"GametypeInput")

        self.verticalLayout_16.addWidget(self.GametypeInput)

        self.AdvanceMapLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.AdvanceMapLabel.setObjectName(u"AdvanceMapLabel")

        self.verticalLayout_16.addWidget(self.AdvanceMapLabel)

        self.AdvanceMapInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.setObjectName(u"AdvanceMapInput")

        self.verticalLayout_16.addWidget(self.AdvanceMapInput)

        self.PointLimitLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.PointLimitLabel.setObjectName(u"PointLimitLabel")

        self.verticalLayout_16.addWidget(self.PointLimitLabel)

        self.PointLimitInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.PointLimitInput.setObjectName(u"PointLimitInput")

        self.verticalLayout_16.addWidget(self.PointLimitInput)

        self.TimeLimitLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.TimeLimitLabel.setObjectName(u"TimeLimitLabel")

        self.verticalLayout_16.addWidget(self.TimeLimitLabel)

        self.TimeLimitInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.TimeLimitInput.setObjectName(u"TimeLimitInput")

        self.verticalLayout_16.addWidget(self.TimeLimitInput)

        self.MaxPlayersLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.MaxPlayersLabel.setObjectName(u"MaxPlayersLabel")

        self.verticalLayout_16.addWidget(self.MaxPlayersLabel)

        self.MaxPlayersInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.MaxPlayersInput.setObjectName(u"MaxPlayersInput")

        self.verticalLayout_16.addWidget(self.MaxPlayersInput)

        self.ForceSkinLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ForceSkinLabel.setObjectName(u"ForceSkinLabel")

        self.verticalLayout_16.addWidget(self.ForceSkinLabel)

        self.ForceSkinInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.addItem("")
        self.ForceSkinInput.setObjectName(u"ForceSkinInput")
        self.ForceSkinInput.setStyleSheet(u"")
        self.ForceSkinInput.setEditable(True)

        self.verticalLayout_16.addWidget(self.ForceSkinInput)

        self.PortLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.PortLabel.setObjectName(u"PortLabel")

        self.verticalLayout_16.addWidget(self.PortLabel)

        self.PortInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.PortInput.setObjectName(u"PortInput")

        self.verticalLayout_16.addWidget(self.PortInput)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.DisableWeaponsToggle = QCheckBox(self.frame_15)
        self.DisableWeaponsToggle.setObjectName(u"DisableWeaponsToggle")
        self.DisableWeaponsToggle.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.DisableWeaponsToggle)

        self.SuddenDeathToggle = QCheckBox(self.frame_15)
        self.SuddenDeathToggle.setObjectName(u"SuddenDeathToggle")
        self.SuddenDeathToggle.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.SuddenDeathToggle)


        self.verticalLayout_16.addWidget(self.frame_15)

        self.frame = QFrame(self.scrollAreaWidgetContents_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.DedicatedServerToggle = QCheckBox(self.frame)
        self.DedicatedServerToggle.setObjectName(u"DedicatedServerToggle")
        self.DedicatedServerToggle.setStyleSheet(u"")
        self.DedicatedServerToggle.setChecked(False)

        self.horizontalLayout_14.addWidget(self.DedicatedServerToggle)

        self.UploadToggle = QCheckBox(self.frame)
        self.UploadToggle.setObjectName(u"UploadToggle")
        self.UploadToggle.setChecked(True)

        self.horizontalLayout_14.addWidget(self.UploadToggle)


        self.verticalLayout_16.addWidget(self.frame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_8.addWidget(self.scrollArea_4)

        self.GameContentStackedWidget.addWidget(self.HostGamePage)
        self.JoinGamePage = QWidget()
        self.JoinGamePage.setObjectName(u"JoinGamePage")
        self.verticalLayout_9 = QVBoxLayout(self.JoinGamePage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.JoinGamePage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 587, 330))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.SaveButton = QTabWidget(self.scrollAreaWidgetContents_3)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setTabShape(QTabWidget.Rounded)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_23 = QVBoxLayout(self.tab_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.MasterServerList = QListWidget(self.tab_2)
        self.MasterServerList.setObjectName(u"MasterServerList")

        self.verticalLayout_23.addWidget(self.MasterServerList)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MSStatusLabel = QLabel(self.tab_2)
        self.MSStatusLabel.setObjectName(u"MSStatusLabel")

        self.horizontalLayout_18.addWidget(self.MSStatusLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.RefreshButton = QPushButton(self.tab_2)
        self.RefreshButton.setObjectName(u"RefreshButton")

        self.horizontalLayout_18.addWidget(self.RefreshButton)

        self.SaveMSButton = QPushButton(self.tab_2)
        self.SaveMSButton.setObjectName(u"SaveMSButton")

        self.horizontalLayout_18.addWidget(self.SaveMSButton)

        self.JoinMasterServerButton = QPushButton(self.tab_2)
        self.JoinMasterServerButton.setObjectName(u"JoinMasterServerButton")

        self.horizontalLayout_18.addWidget(self.JoinMasterServerButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.SaveButton.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_22 = QVBoxLayout(self.tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.JoinServerLabel = QLabel(self.tab)
        self.JoinServerLabel.setObjectName(u"JoinServerLabel")

        self.verticalLayout_22.addWidget(self.JoinServerLabel)

        self.frame_14 = QFrame(self.tab)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.frame_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.JoinAddressInput = QLineEdit(self.tab)
        self.JoinAddressInput.setObjectName(u"JoinAddressInput")

        self.horizontalLayout_17.addWidget(self.JoinAddressInput)

        self.JoinAddressButton = QPushButton(self.tab)
        self.JoinAddressButton.setObjectName(u"JoinAddressButton")

        self.horizontalLayout_17.addWidget(self.JoinAddressButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_17)

        self.ServerListLabel = QLabel(self.tab)
        self.ServerListLabel.setObjectName(u"ServerListLabel")

        self.verticalLayout_22.addWidget(self.ServerListLabel)

        self.ServerList = QListWidget(self.tab)
        QListWidgetItem(self.ServerList)
        QListWidgetItem(self.ServerList)
        QListWidgetItem(self.ServerList)
        self.ServerList.setObjectName(u"ServerList")
        self.ServerList.setStyleSheet(u"")
        self.ServerList.setDragEnabled(True)
        self.ServerList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ServerList.setIconSize(QSize(32, 32))

        self.verticalLayout_22.addWidget(self.ServerList)

        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.JoinServerButton = QPushButton(self.frame_10)
        self.JoinServerButton.setObjectName(u"JoinServerButton")
        self.JoinServerButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.JoinServerButton)

        self.AddServerButton = QPushButton(self.frame_10)
        self.AddServerButton.setObjectName(u"AddServerButton")

        self.horizontalLayout_9.addWidget(self.AddServerButton)


        self.verticalLayout_22.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.EditServerButton = QPushButton(self.frame_13)
        self.EditServerButton.setObjectName(u"EditServerButton")

        self.horizontalLayout_15.addWidget(self.EditServerButton)

        self.DeleteServerButton = QPushButton(self.frame_13)
        self.DeleteServerButton.setObjectName(u"DeleteServerButton")

        self.horizontalLayout_15.addWidget(self.DeleteServerButton)


        self.verticalLayout_22.addWidget(self.frame_13)

        self.SaveButton.addTab(self.tab, "")

        self.verticalLayout_13.addWidget(self.SaveButton)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_3)

        self.GameContentStackedWidget.addWidget(self.JoinGamePage)

        self.verticalLayout_4.addWidget(self.GameContentStackedWidget)

        self.splitter.addWidget(self.GamePageContentFrame)

        self.horizontalLayout_4.addWidget(self.splitter)


        self.verticalLayout_3.addWidget(self.GamePageFrame)

        self.GamePlayFrame = QFrame(self.GamePage)
        self.GamePlayFrame.setObjectName(u"GamePlayFrame")
        self.GamePlayFrame.setMinimumSize(QSize(0, 56))
        self.GamePlayFrame.setMaximumSize(QSize(16777215, 56))
        self.GamePlayFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePlayFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.GamePlayFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 0, 8, 0)
        self.GameProfileComboBox = QComboBox(self.GamePlayFrame)
        self.GameProfileComboBox.addItem("")
        self.GameProfileComboBox.setObjectName(u"GameProfileComboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.GameProfileComboBox.sizePolicy().hasHeightForWidth())
        self.GameProfileComboBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.GameProfileComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.GamePlayButton = QPushButton(self.GamePlayFrame)
        self.GamePlayButton.setObjectName(u"GamePlayButton")
        self.GamePlayButton.setMinimumSize(QSize(240, 38))
        self.GamePlayButton.setMaximumSize(QSize(240, 38))

        self.horizontalLayout_3.addWidget(self.GamePlayButton)

        self.GameOptionsDropDownButton = QPushButton(self.GamePlayFrame)
        self.GameOptionsDropDownButton.setObjectName(u"GameOptionsDropDownButton")
        self.GameOptionsDropDownButton.setMinimumSize(QSize(0, 28))
        self.GameOptionsDropDownButton.setMaximumSize(QSize(16, 38))

        self.horizontalLayout_3.addWidget(self.GameOptionsDropDownButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.GamePlayFrame)

        self.MainTabsStackedWidget.addWidget(self.GamePage)
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.verticalLayout_15 = QVBoxLayout(self.AboutPage)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.AboutPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 78))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.textEdit)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.MainTabsStackedWidget.addWidget(self.AboutPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_12 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.SettingsPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 261, 172))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ProfileDirLabel = QLabel(self.scrollAreaWidgetContents)
        self.ProfileDirLabel.setObjectName(u"ProfileDirLabel")

        self.verticalLayout_18.addWidget(self.ProfileDirLabel)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_21.addWidget(self.lineEdit)

        self.ProfileDirBrowseButton = QPushButton(self.scrollAreaWidgetContents)
        self.ProfileDirBrowseButton.setObjectName(u"ProfileDirBrowseButton")

        self.horizontalLayout_21.addWidget(self.ProfileDirBrowseButton)


        self.verticalLayout_18.addLayout(self.horizontalLayout_21)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_18.addWidget(self.label_4)

        self.LauncherThemeInput = QComboBox(self.scrollAreaWidgetContents)
        self.LauncherThemeInput.addItem("")
        self.LauncherThemeInput.addItem("")
        self.LauncherThemeInput.setObjectName(u"LauncherThemeInput")
        self.LauncherThemeInput.setEnabled(True)

        self.verticalLayout_18.addWidget(self.LauncherThemeInput)

        self.SaveFilesToConfigToggle = QCheckBox(self.scrollAreaWidgetContents)
        self.SaveFilesToConfigToggle.setObjectName(u"SaveFilesToConfigToggle")
        self.SaveFilesToConfigToggle.setChecked(False)

        self.verticalLayout_18.addWidget(self.SaveFilesToConfigToggle)

        self.verticalSpacer_6 = QSpacerItem(20, 244, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.MainTabsStackedWidget.addWidget(self.SettingsPage)

        self.horizontalLayout_2.addWidget(self.MainTabsStackedWidget)


        self.verticalLayout.addWidget(self.MainAreaFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTabsStackedWidget.setCurrentIndex(1)
        self.GameContentStackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.PlayerSkinInput.setCurrentIndex(0)
        self.PlayerColorInput.setCurrentIndex(0)
        self.AdvanceMapInput.setCurrentIndex(1)
        self.SaveButton.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.NewsTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"News", None))
#endif // QT_CONFIG(tooltip)
        self.NewsTabButton.setText("")
#if QT_CONFIG(tooltip)
        self.GameTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"Game", None))
#endif // QT_CONFIG(tooltip)
        self.GameTabButton.setText("")
#if QT_CONFIG(tooltip)
        self.HelpTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.HelpTabButton.setText("")
#if QT_CONFIG(tooltip)
        self.SettingsTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"Launcher Settings", None))
#endif // QT_CONFIG(tooltip)
        self.SettingsTabButton.setText("")
        self.NewsTitleLabel.setText(QCoreApplication.translate("MainWindow", u"SONIC ROBO BLAST 2 NEWS", None))
        self.ProfileTabButton.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.FilesTabButton.setText(QCoreApplication.translate("MainWindow", u"Mods", None))
        self.GameSettingsTabButton.setText(QCoreApplication.translate("MainWindow", u"Game settings", None))
        self.PlayerSetupTabButton.setText(QCoreApplication.translate("MainWindow", u"Player setup", None))
        self.HostGameTabButton.setText(QCoreApplication.translate("MainWindow", u"Host game", None))
        self.JoinGameTabButton.setText(QCoreApplication.translate("MainWindow", u"Join game", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PROFILE NAME", None))
        self.ProfileNameInput.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FILENAME", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GAME", None))
        self.ProfileGameSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"SRB2", None))
        self.ProfileGameSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"SRB2Kart", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VERSION", None))
        self.ProfileVersionSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"2.2", None))
        self.ProfileVersionSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"2.1", None))
        self.ProfileVersionSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"2.0", None))
        self.ProfileVersionSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"1.09.X", None))
        self.ProfileVersionSetting.setItemText(4, QCoreApplication.translate("MainWindow", u"1.08", None))
        self.ProfileVersionSetting.setItemText(5, QCoreApplication.translate("MainWindow", u"1.07", None))


        __sortingEnabled = self.GameFilesList.isSortingEnabled()
        self.GameFilesList.setSortingEnabled(False)
        ___qlistwidgetitem = self.GameFilesList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"place.wad", None));
        ___qlistwidgetitem1 = self.GameFilesList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"hold.pk3", None));
        ___qlistwidgetitem2 = self.GameFilesList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"er.lua", None));
        self.GameFilesList.setSortingEnabled(__sortingEnabled)

        self.GameFilesUpButton.setText("")
        self.GameFilesClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
        self.GameFilesDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete selected files", None))
        self.GameFilesDownButton.setText("")
        self.GameFilesSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save list", None))
        self.GameFilesLoadButton.setText(QCoreApplication.translate("MainWindow", u"Load list", None))
        self.GameFilesAddButton.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.GameFilesExecuteScriptLabel.setText(QCoreApplication.translate("MainWindow", u"EXECUTE SCRIPT", None))
        self.GameFilesExecScrBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mod List:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"About Mod:", None))
        self.ModStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Refresh\" to see a list of available mods.", None))
        self.ModTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Maps", None))
        self.ModTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Characters", None))
        self.ModTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Lua", None))
        self.ModTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Assets", None))
        self.ModTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Misc", None))

        self.OpenPageButton.setText(QCoreApplication.translate("MainWindow", u"Open Page", None))
        self.RefreshModsButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.DownloadModButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Download Mods", None))
        self.GameResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"RESOLUTION", None))
        self.GameHorizontalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
        self.GameResMultLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.GameVerticalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
        self.GameRenderCfgLabel.setText(QCoreApplication.translate("MainWindow", u"RENDER OPTIONS", None))
        self.GameRendererSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.GameRendererSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"OpenGL", None))

        self.GameFullscreenSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.GameFullscreenSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Borderless fullscreen", None))
        self.GameFullscreenSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Windowed", None))

        self.GameSoundOptionsLabel.setText(QCoreApplication.translate("MainWindow", u"SOUND OPTIONS", None))
        self.GameMusicSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Digital music", None))
        self.GameMusicSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Midi music", None))
        self.GameMusicSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Load music from a CD", None))
        self.GameMusicSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"Disable music", None))

        self.GameSoundSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Enable sound", None))
        self.GameSoundSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Disable sound", None))

        self.GameExecPathLabel.setText(QCoreApplication.translate("MainWindow", u"EXE PATH", None))
        self.GameExecFilePathInput.setText(QCoreApplication.translate("MainWindow", u"srb2win.exe", None))
        self.GameExecFilePathBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.WineToggle.setText(QCoreApplication.translate("MainWindow", u"RUN SRB2 IN WINE", None))
        self.GameArgsLabel.setText(QCoreApplication.translate("MainWindow", u"CUSTOM CLI PARAMETERS", None))
        self.PlayerNameTitleLabel.setText(QCoreApplication.translate("MainWindow", u"NICKNAME", None))
        self.PlayerNameInput.setText("")
        self.PlayerNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinTitleLabel.setText(QCoreApplication.translate("MainWindow", u"SKIN", None))
        self.PlayerSkinInput.setItemText(0, "")
        self.PlayerSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.PlayerSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.PlayerSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.PlayerSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.PlayerSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PlayerSkinImage.setText("")
        self.PlayerSkinInfoText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dddd00;\">Sonic</span> is the fastest of the three, but also the hardest to control. Begginers beware, but experts will find Sonic very powerful.</p><p><span style=\" color:#dddd00;\">Ability:</span> Speed Thok<br/>Double jump to zoom forward with a huge burst of speed</p><p><span style=\" color:#dddd00;\">Tip:</span> Simply letting go of forward does not slow down in SRB2. To slow down, hold the opposite direction.</p></body></html>", None))
        self.PlayerColorTitleLabel.setText(QCoreApplication.translate("MainWindow", u"COLOR", None))
        self.PlayerColorInput.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PlayerColorInput.setItemText(1, QCoreApplication.translate("MainWindow", u"White", None))
        self.PlayerColorInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Bone", None))
        self.PlayerColorInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Cloudy", None))
        self.PlayerColorInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Grey", None))
        self.PlayerColorInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.PlayerColorInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Carbon", None))
        self.PlayerColorInput.setItemText(7, QCoreApplication.translate("MainWindow", u"Jet", None))
        self.PlayerColorInput.setItemText(8, QCoreApplication.translate("MainWindow", u"Black", None))
        self.PlayerColorInput.setItemText(9, QCoreApplication.translate("MainWindow", u"Aether", None))
        self.PlayerColorInput.setItemText(10, QCoreApplication.translate("MainWindow", u"Slate", None))
        self.PlayerColorInput.setItemText(11, QCoreApplication.translate("MainWindow", u"Pink", None))
        self.PlayerColorInput.setItemText(12, QCoreApplication.translate("MainWindow", u"Yoghurt", None))
        self.PlayerColorInput.setItemText(13, QCoreApplication.translate("MainWindow", u"Brown", None))
        self.PlayerColorInput.setItemText(14, QCoreApplication.translate("MainWindow", u"Tan", None))
        self.PlayerColorInput.setItemText(15, QCoreApplication.translate("MainWindow", u"Beige", None))
        self.PlayerColorInput.setItemText(16, QCoreApplication.translate("MainWindow", u"Moss", None))
        self.PlayerColorInput.setItemText(17, QCoreApplication.translate("MainWindow", u"Azure", None))
        self.PlayerColorInput.setItemText(18, QCoreApplication.translate("MainWindow", u"Lavender", None))
        self.PlayerColorInput.setItemText(19, QCoreApplication.translate("MainWindow", u"Ruby", None))
        self.PlayerColorInput.setItemText(20, QCoreApplication.translate("MainWindow", u"Salmon", None))
        self.PlayerColorInput.setItemText(21, QCoreApplication.translate("MainWindow", u"Red", None))
        self.PlayerColorInput.setItemText(22, QCoreApplication.translate("MainWindow", u"Crimson", None))
        self.PlayerColorInput.setItemText(23, QCoreApplication.translate("MainWindow", u"Flame", None))
        self.PlayerColorInput.setItemText(24, QCoreApplication.translate("MainWindow", u"Peachy", None))
        self.PlayerColorInput.setItemText(25, QCoreApplication.translate("MainWindow", u"Quail", None))
        self.PlayerColorInput.setItemText(26, QCoreApplication.translate("MainWindow", u"Sunset", None))
        self.PlayerColorInput.setItemText(27, QCoreApplication.translate("MainWindow", u"Apricot", None))
        self.PlayerColorInput.setItemText(28, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.PlayerColorInput.setItemText(29, QCoreApplication.translate("MainWindow", u"Rust", None))
        self.PlayerColorInput.setItemText(30, QCoreApplication.translate("MainWindow", u"Gold", None))
        self.PlayerColorInput.setItemText(31, QCoreApplication.translate("MainWindow", u"Sandy", None))
        self.PlayerColorInput.setItemText(32, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.PlayerColorInput.setItemText(33, QCoreApplication.translate("MainWindow", u"Olive", None))
        self.PlayerColorInput.setItemText(34, QCoreApplication.translate("MainWindow", u"Lime", None))
        self.PlayerColorInput.setItemText(35, QCoreApplication.translate("MainWindow", u"Peridot", None))
        self.PlayerColorInput.setItemText(36, QCoreApplication.translate("MainWindow", u"Green", None))
        self.PlayerColorInput.setItemText(37, QCoreApplication.translate("MainWindow", u"Forest", None))
        self.PlayerColorInput.setItemText(38, QCoreApplication.translate("MainWindow", u"Emerald", None))
        self.PlayerColorInput.setItemText(39, QCoreApplication.translate("MainWindow", u"Mint", None))
        self.PlayerColorInput.setItemText(40, QCoreApplication.translate("MainWindow", u"Seafoam", None))
        self.PlayerColorInput.setItemText(41, QCoreApplication.translate("MainWindow", u"Aqua", None))
        self.PlayerColorInput.setItemText(42, QCoreApplication.translate("MainWindow", u"Teal", None))
        self.PlayerColorInput.setItemText(43, QCoreApplication.translate("MainWindow", u"Wave", None))
        self.PlayerColorInput.setItemText(44, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.PlayerColorInput.setItemText(45, QCoreApplication.translate("MainWindow", u"Sky", None))
        self.PlayerColorInput.setItemText(46, QCoreApplication.translate("MainWindow", u"Cerulean", None))
        self.PlayerColorInput.setItemText(47, QCoreApplication.translate("MainWindow", u"Icy", None))
        self.PlayerColorInput.setItemText(48, QCoreApplication.translate("MainWindow", u"Sapphire", None))
        self.PlayerColorInput.setItemText(49, QCoreApplication.translate("MainWindow", u"Cornflower", None))
        self.PlayerColorInput.setItemText(50, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.PlayerColorInput.setItemText(51, QCoreApplication.translate("MainWindow", u"Cobalt", None))
        self.PlayerColorInput.setItemText(52, QCoreApplication.translate("MainWindow", u"Vapor", None))
        self.PlayerColorInput.setItemText(53, QCoreApplication.translate("MainWindow", u"Dusk", None))
        self.PlayerColorInput.setItemText(54, QCoreApplication.translate("MainWindow", u"Pastel", None))
        self.PlayerColorInput.setItemText(55, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.PlayerColorInput.setItemText(56, QCoreApplication.translate("MainWindow", u"Bubblegum", None))
        self.PlayerColorInput.setItemText(57, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.PlayerColorInput.setItemText(58, QCoreApplication.translate("MainWindow", u"Neon", None))
        self.PlayerColorInput.setItemText(59, QCoreApplication.translate("MainWindow", u"Violet", None))
        self.PlayerColorInput.setItemText(60, QCoreApplication.translate("MainWindow", u"Lilac", None))
        self.PlayerColorInput.setItemText(61, QCoreApplication.translate("MainWindow", u"Plum", None))
        self.PlayerColorInput.setItemText(62, QCoreApplication.translate("MainWindow", u"Rosy", None))

        self.ServerNameLabel.setText(QCoreApplication.translate("MainWindow", u"SERVER NAME", None))
        self.AdminPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"ADMIN PASSWORD", None))
        self.RoomLabel.setText(QCoreApplication.translate("MainWindow", u"ROOM", None))
        self.RoomInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Offline", None))
        self.RoomInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.RoomInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Casual", None))
        self.RoomInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Hugs", None))
        self.RoomInput.setItemText(4, QCoreApplication.translate("MainWindow", u"OLDC", None))

        self.GametypeLabel.setText(QCoreApplication.translate("MainWindow", u"GAMETYPE", None))
        self.GametypeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Co-op", None))
        self.GametypeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Competition", None))
        self.GametypeInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Race", None))
        self.GametypeInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Match", None))
        self.GametypeInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Team Match", None))
        self.GametypeInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Tag", None))
        self.GametypeInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Hide and Seek", None))
        self.GametypeInput.setItemText(7, QCoreApplication.translate("MainWindow", u"Capture the Flag", None))

        self.AdvanceMapLabel.setText(QCoreApplication.translate("MainWindow", u"ADVANCE MAP", None))
        self.AdvanceMapInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.AdvanceMapInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Next", None))
        self.AdvanceMapInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Random", None))

        self.PointLimitLabel.setText(QCoreApplication.translate("MainWindow", u"POINT LIMIT", None))
        self.PointLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.TimeLimitLabel.setText(QCoreApplication.translate("MainWindow", u"TIME LIMIT", None))
        self.TimeLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Off by default", None))
        self.MaxPlayersLabel.setText(QCoreApplication.translate("MainWindow", u"MAX PLAYERS", None))
        self.MaxPlayersInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"8", None))
        self.ForceSkinLabel.setText(QCoreApplication.translate("MainWindow", u"FORCE SKIN", None))
        self.ForceSkinInput.setItemText(0, "")
        self.ForceSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.ForceSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.ForceSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.ForceSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.ForceSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.ForceSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PortLabel.setText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.PortInput.setInputMask("")
        self.PortInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5029", None))
        self.DisableWeaponsToggle.setText(QCoreApplication.translate("MainWindow", u"DISABLE WEAPON RINGS", None))
        self.SuddenDeathToggle.setText(QCoreApplication.translate("MainWindow", u"SUDDEN DEATH", None))
        self.DedicatedServerToggle.setText(QCoreApplication.translate("MainWindow", u"DEDICATED", None))
        self.UploadToggle.setText(QCoreApplication.translate("MainWindow", u"ENABLE DOWNLOADING", None))
        self.MSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Refresh\" to download a list of servers.", None))
        self.RefreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.SaveMSButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.JoinMasterServerButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.SaveButton.setTabText(self.SaveButton.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.JoinServerLabel.setText(QCoreApplication.translate("MainWindow", u"JOIN SERVER", None))
        self.JoinAddressInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.JoinAddressButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.ServerListLabel.setText(QCoreApplication.translate("MainWindow", u"SERVER LIST", None))

        __sortingEnabled1 = self.ServerList.isSortingEnabled()
        self.ServerList.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.ServerList.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"not hitcoder", None));
        ___qlistwidgetitem4 = self.ServerList.item(1)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"maybe manic", None));
        ___qlistwidgetitem5 = self.ServerList.item(2)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"who needs utau when you have srb2", None));
        self.ServerList.setSortingEnabled(__sortingEnabled1)

        self.JoinServerButton.setText(QCoreApplication.translate("MainWindow", u"Join server", None))
        self.AddServerButton.setText(QCoreApplication.translate("MainWindow", u"Add server", None))
        self.EditServerButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.DeleteServerButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.SaveButton.setTabText(self.SaveButton.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Saved Servers", None))
        self.GameProfileComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New profile...", None))

        self.GamePlayButton.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.GameOptionsDropDownButton.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">LauncherBlast2 &quot;reBoot&quot; by HitCoder</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Built in PyQt5</span></p>\n"
"<p style=\"-qt-paragraph-"
                        "type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://mb.srb2.org/threads/launcherblast2-reboot.27592/\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; text-decoration: underline; color:#7777ff;\">View the SRB2 Message Board thread</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Credits</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: "
                        "0px; -qt-list-indent: 1;\"><li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FinestElite - icons for News and Help</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sonic Team Jr - SRB2 icon</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">reBoot-2.0 changelog</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" fon"
                        "t-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">UI Overhaul - main tabs are now at the top and use icons instead of text</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Introduction of profiles, allowing support for multiple installations of different versions of SRB2 or mods of SRB2 such as SRB2Kart</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed a bug with spaces in filenames when adding files to the game</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed a bug with spac"
                        "es in player nicknames</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The console no longer opens with the launcher</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added new icon for the launcher</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">FAQ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; text-decoration: underline;\">How do I host a server?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">To host a server, select the host server tab. You will be given a multitude of options for your server. To start your server, you will find that on this tab, your &quot;Play&quot; button has changed to read &quot;Start Server&quot;. You can only start a server wi"
                        "th this tab selected.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; text-decoration: underline;\">My antivirus detects Launcherblast2 as a trojan. Is this true?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Due to the nature of this utility, it is a small scale program that doesn't have a very big audience. Modern antivirus software may well detect it as a false-positive, as a precaution to &quot;unknown programs&quot;. If this happens, your antivirus may have an option to submit the program for analysis, in wh"
                        "ich case please do so!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">About Launcherblast2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">LAUNCHERBLAST2 is a project I started in 2019, before SRB2 2.2 was released. I wanted this to be released not long after 2.2 was, to go with it, but due to personal life and some other things I never got to finish it. Fast forward to early 2020, I remember this exists. I decided to finish it, though it's not to a standard I'd ideally like it to be. I do feel like it fits the bill for a nice looking launcher at it's forefront though.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">There are a couple of graphical glitches here and there because I realised not long into starting to develop th"
                        "is, that a lot of info on Qt5 is sparse, and some of the Qt4 stuff isn't directly compatible. I'm really sorry for the combo-boxes that have a weird square on them when you hover. I hope it doesn't bother you too much.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">In case you didn't already notice, the design is very much inspired by the 2019 Minecraft Launcher. It was actually that which kick-started me into creating this. Anyway, hope you enjoy it, if you find any bugs let me know! I'll be working on this from time to time regardless, so updates may come soon. I'm not implementing an auto-updater though, as I don't have a server to place the metadata on for"
                        " now.</span></p></body></html>", None))
        self.ProfileDirLabel.setText(QCoreApplication.translate("MainWindow", u"PROFILE DIRECTORY", None))
        self.ProfileDirBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LAUNCHER THEME (REQUIRES RESTART)", None))
        self.LauncherThemeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Dark", None))
        self.LauncherThemeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Light", None))

        self.SaveFilesToConfigToggle.setText(QCoreApplication.translate("MainWindow", u"CLEAR FILES LIST ON STARTUP", None))
    # retranslateUi

