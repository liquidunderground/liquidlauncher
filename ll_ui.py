# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'll.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)
import ll_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 605)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
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
        icon1.addFile(u":/assets/img/icons/gamepad.png", QSize(), QIcon.Normal, QIcon.Off)
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


        self.gridLayout_2.addWidget(self.DockTabFrame, 0, 0, 1, 1)

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
        self.NewsScrollAreaContent.setGeometry(QRect(0, 0, 844, 535))
        self.NewsScrollAreaContent.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.NewsScrollAreaContent)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.RSSFeedLabel = QLabel(self.NewsScrollAreaContent)
        self.RSSFeedLabel.setObjectName(u"RSSFeedLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RSSFeedLabel.sizePolicy().hasHeightForWidth())
        self.RSSFeedLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.RSSFeedLabel, 2, 0, 1, 1)

        self.RSSFeedCombobox = QComboBox(self.NewsScrollAreaContent)
        self.RSSFeedCombobox.addItem("")
        self.RSSFeedCombobox.setObjectName(u"RSSFeedCombobox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.RSSFeedCombobox.sizePolicy().hasHeightForWidth())
        self.RSSFeedCombobox.setSizePolicy(sizePolicy3)
        self.RSSFeedCombobox.setEditable(True)

        self.gridLayout_7.addWidget(self.RSSFeedCombobox, 2, 1, 1, 1)

        self.RSSStatusLabel = QLabel(self.NewsScrollAreaContent)
        self.RSSStatusLabel.setObjectName(u"RSSStatusLabel")

        self.gridLayout_7.addWidget(self.RSSStatusLabel, 5, 0, 1, 3)

        self.RSSRefreshButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSRefreshButton.setObjectName(u"RSSRefreshButton")
        icon4 = QIcon()
        icon4.addFile(u":/assets/img/icons/view-refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSRefreshButton.setIcon(icon4)

        self.gridLayout_7.addWidget(self.RSSRefreshButton, 2, 3, 1, 1)

        self.RSSViewonlineButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSViewonlineButton.setObjectName(u"RSSViewonlineButton")
        self.RSSViewonlineButton.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/assets/img/icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSViewonlineButton.setIcon(icon5)

        self.gridLayout_7.addWidget(self.RSSViewonlineButton, 5, 3, 1, 1)

        self.splitter_4 = QSplitter(self.NewsScrollAreaContent)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.RSSArticleList = QListWidget(self.splitter_4)
        __qlistwidgetitem = QListWidgetItem(self.RSSArticleList)
        __qlistwidgetitem.setFlags(Qt.NoItemFlags);
        self.RSSArticleList.setObjectName(u"RSSArticleList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.RSSArticleList.sizePolicy().hasHeightForWidth())
        self.RSSArticleList.setSizePolicy(sizePolicy4)
        self.splitter_4.addWidget(self.RSSArticleList)
        self.RSSArticleView = QTextBrowser(self.splitter_4)
        self.RSSArticleView.setObjectName(u"RSSArticleView")
        self.RSSArticleView.setOpenExternalLinks(True)
        self.splitter_4.addWidget(self.RSSArticleView)

        self.gridLayout_7.addWidget(self.splitter_4, 4, 0, 1, 4)

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
        self.GamePageTabList = QListWidget(self.GamePageFrame)
        QListWidgetItem(self.GamePageTabList)
        QListWidgetItem(self.GamePageTabList)
        QListWidgetItem(self.GamePageTabList)
        QListWidgetItem(self.GamePageTabList)
        QListWidgetItem(self.GamePageTabList)
        self.GamePageTabList.setObjectName(u"GamePageTabList")
        sizePolicy4.setHeightForWidth(self.GamePageTabList.sizePolicy().hasHeightForWidth())
        self.GamePageTabList.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.GamePageTabList)

        self.splitter = QSplitter(self.GamePageFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
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
        self.gridLayout_5 = QGridLayout(self.ProfilePage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ProfileNameInput = QLineEdit(self.ProfilePage)
        self.ProfileNameInput.setObjectName(u"ProfileNameInput")

        self.gridLayout_5.addWidget(self.ProfileNameInput, 1, 0, 1, 1)

        self.ProfileNameLabel = QLabel(self.ProfilePage)
        self.ProfileNameLabel.setObjectName(u"ProfileNameLabel")

        self.gridLayout_5.addWidget(self.ProfileNameLabel, 0, 0, 1, 1)

        self.ProfileGameLabel = QLabel(self.ProfilePage)
        self.ProfileGameLabel.setObjectName(u"ProfileGameLabel")

        self.gridLayout_5.addWidget(self.ProfileGameLabel, 4, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_19.addItem(self.verticalSpacer_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_19, 8, 0, 1, 1)

        self.ProfileFilenameInput = QLineEdit(self.ProfilePage)
        self.ProfileFilenameInput.setObjectName(u"ProfileFilenameInput")

        self.gridLayout_5.addWidget(self.ProfileFilenameInput, 1, 1, 1, 1)

        self.ProfileGameSetting = QComboBox(self.ProfilePage)
        self.ProfileGameSetting.addItem("")
        self.ProfileGameSetting.addItem("")
        self.ProfileGameSetting.setObjectName(u"ProfileGameSetting")

        self.gridLayout_5.addWidget(self.ProfileGameSetting, 5, 0, 1, 1)

        self.label = QLabel(self.ProfilePage)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.ProfileVersionSetting = QComboBox(self.ProfilePage)
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.addItem("")
        self.ProfileVersionSetting.setObjectName(u"ProfileVersionSetting")

        self.gridLayout_5.addWidget(self.ProfileVersionSetting, 5, 1, 1, 1)

        self.ProfileVersionLabel = QLabel(self.ProfilePage)
        self.ProfileVersionLabel.setObjectName(u"ProfileVersionLabel")

        self.gridLayout_5.addWidget(self.ProfileVersionLabel, 4, 1, 1, 1)

        self.GameContentStackedWidget.addWidget(self.ProfilePage)
        self.GameSettingsPage = QWidget()
        self.GameSettingsPage.setObjectName(u"GameSettingsPage")
        self.verticalLayout_27 = QVBoxLayout(self.GameSettingsPage)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.GameSettingsTabWidget = QTabWidget(self.GameSettingsPage)
        self.GameSettingsTabWidget.setObjectName(u"GameSettingsTabWidget")
        self.PlayerSettingsTab = QWidget()
        self.PlayerSettingsTab.setObjectName(u"PlayerSettingsTab")
        self.verticalLayout_33 = QVBoxLayout(self.PlayerSettingsTab)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.PlayerNameTitleLabel = QLabel(self.PlayerSettingsTab)
        self.PlayerNameTitleLabel.setObjectName(u"PlayerNameTitleLabel")

        self.verticalLayout_33.addWidget(self.PlayerNameTitleLabel)

        self.PlayerNameInput = QLineEdit(self.PlayerSettingsTab)
        self.PlayerNameInput.setObjectName(u"PlayerNameInput")

        self.verticalLayout_33.addWidget(self.PlayerNameInput)

        self.PlayerSkinTitleLabel = QLabel(self.PlayerSettingsTab)
        self.PlayerSkinTitleLabel.setObjectName(u"PlayerSkinTitleLabel")

        self.verticalLayout_33.addWidget(self.PlayerSkinTitleLabel)

        self.PlayerSkinInput = QComboBox(self.PlayerSettingsTab)
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.setObjectName(u"PlayerSkinInput")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PlayerSkinInput.sizePolicy().hasHeightForWidth())
        self.PlayerSkinInput.setSizePolicy(sizePolicy5)
        self.PlayerSkinInput.setStyleSheet(u"")
        self.PlayerSkinInput.setEditable(True)

        self.verticalLayout_33.addWidget(self.PlayerSkinInput)

        self.PlayerSkinInfoWrapper = QFrame(self.PlayerSettingsTab)
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
        self.PlayerSkinImage.setMaximumSize(QSize(128, 128))
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


        self.verticalLayout_33.addWidget(self.PlayerSkinInfoWrapper)

        self.PlayerColorTitleLabel = QLabel(self.PlayerSettingsTab)
        self.PlayerColorTitleLabel.setObjectName(u"PlayerColorTitleLabel")

        self.verticalLayout_33.addWidget(self.PlayerColorTitleLabel)

        self.PlayerColorInput = QComboBox(self.PlayerSettingsTab)
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

        self.verticalLayout_33.addWidget(self.PlayerColorInput)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_5)

        self.GameSettingsTabWidget.addTab(self.PlayerSettingsTab, "")
        self.GameSettingsTab = QWidget()
        self.GameSettingsTab.setObjectName(u"GameSettingsTab")
        self.verticalLayout_32 = QVBoxLayout(self.GameSettingsTab)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.GameResolutionLabel = QLabel(self.GameSettingsTab)
        self.GameResolutionLabel.setObjectName(u"GameResolutionLabel")
        self.GameResolutionLabel.setMaximumSize(QSize(16777215, 26))
        self.GameResolutionLabel.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.GameResolutionLabel)

        self.GameResolutionSettingsWrapper = QFrame(self.GameSettingsTab)
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


        self.verticalLayout_32.addWidget(self.GameResolutionSettingsWrapper)

        self.GameRenderCfgLabel = QLabel(self.GameSettingsTab)
        self.GameRenderCfgLabel.setObjectName(u"GameRenderCfgLabel")

        self.verticalLayout_32.addWidget(self.GameRenderCfgLabel)

        self.GameRendererSetting = QComboBox(self.GameSettingsTab)
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.setObjectName(u"GameRendererSetting")

        self.verticalLayout_32.addWidget(self.GameRendererSetting)

        self.GameFullscreenSetting = QComboBox(self.GameSettingsTab)
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.setObjectName(u"GameFullscreenSetting")

        self.verticalLayout_32.addWidget(self.GameFullscreenSetting)

        self.GameSoundOptionsLabel = QLabel(self.GameSettingsTab)
        self.GameSoundOptionsLabel.setObjectName(u"GameSoundOptionsLabel")

        self.verticalLayout_32.addWidget(self.GameSoundOptionsLabel)

        self.GameMusicSetting = QComboBox(self.GameSettingsTab)
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.setObjectName(u"GameMusicSetting")

        self.verticalLayout_32.addWidget(self.GameMusicSetting)

        self.GameSoundSetting = QComboBox(self.GameSettingsTab)
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.setObjectName(u"GameSoundSetting")

        self.verticalLayout_32.addWidget(self.GameSoundSetting)

        self.GameExecPathLabel = QLabel(self.GameSettingsTab)
        self.GameExecPathLabel.setObjectName(u"GameExecPathLabel")

        self.verticalLayout_32.addWidget(self.GameExecPathLabel)

        self.GameExecFilePath = QFrame(self.GameSettingsTab)
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
        icon6 = QIcon()
        icon6.addFile(u":/assets/img/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameExecFilePathBrowse.setIcon(icon6)

        self.gridLayout_4.addWidget(self.GameExecFilePathBrowse, 0, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.GameExecFilePath)

        self.WineToggle = QCheckBox(self.GameSettingsTab)
        self.WineToggle.setObjectName(u"WineToggle")
        self.WineToggle.setEnabled(False)
        self.WineToggle.setChecked(False)

        self.verticalLayout_32.addWidget(self.WineToggle)

        self.GameArgsLabel = QLabel(self.GameSettingsTab)
        self.GameArgsLabel.setObjectName(u"GameArgsLabel")

        self.verticalLayout_32.addWidget(self.GameArgsLabel)

        self.GameArgsInput = QLineEdit(self.GameSettingsTab)
        self.GameArgsInput.setObjectName(u"GameArgsInput")

        self.verticalLayout_32.addWidget(self.GameArgsInput)

        self.verticalSpacer_2 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_2)

        self.GameSettingsTabWidget.addTab(self.GameSettingsTab, "")
        self.AddonsTab = QWidget()
        self.AddonsTab.setObjectName(u"AddonsTab")
        self.gridLayout_9 = QGridLayout(self.AddonsTab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.GameFilesClearButton = QPushButton(self.AddonsTab)
        self.GameFilesClearButton.setObjectName(u"GameFilesClearButton")
        self.GameFilesClearButton.setMinimumSize(QSize(0, 28))
        icon7 = QIcon()
        icon7.addFile(u":/assets/img/icons/edit-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesClearButton.setIcon(icon7)

        self.gridLayout_9.addWidget(self.GameFilesClearButton, 10, 4, 2, 1)

        self.GameFilesExecuteScriptLabel = QLabel(self.AddonsTab)
        self.GameFilesExecuteScriptLabel.setObjectName(u"GameFilesExecuteScriptLabel")

        self.gridLayout_9.addWidget(self.GameFilesExecuteScriptLabel, 13, 1, 1, 1)

        self.GameFilesDeleteButton = QPushButton(self.AddonsTab)
        self.GameFilesDeleteButton.setObjectName(u"GameFilesDeleteButton")
        self.GameFilesDeleteButton.setMinimumSize(QSize(0, 28))
        icon8 = QIcon()
        icon8.addFile(u":/assets/img/icons/list-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDeleteButton.setIcon(icon8)

        self.gridLayout_9.addWidget(self.GameFilesDeleteButton, 11, 7, 1, 1)

        self.GameFilesUpButton = QPushButton(self.AddonsTab)
        self.GameFilesUpButton.setObjectName(u"GameFilesUpButton")
        sizePolicy5.setHeightForWidth(self.GameFilesUpButton.sizePolicy().hasHeightForWidth())
        self.GameFilesUpButton.setSizePolicy(sizePolicy5)
        icon9 = QIcon()
        icon9.addFile(u":/assets/img/icons/go-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesUpButton.setIcon(icon9)

        self.gridLayout_9.addWidget(self.GameFilesUpButton, 10, 1, 1, 1)

        self.GameFilesExecScrBrowseButton = QPushButton(self.AddonsTab)
        self.GameFilesExecScrBrowseButton.setObjectName(u"GameFilesExecScrBrowseButton")
        self.GameFilesExecScrBrowseButton.setMinimumSize(QSize(0, 28))
        self.GameFilesExecScrBrowseButton.setIcon(icon6)

        self.gridLayout_9.addWidget(self.GameFilesExecScrBrowseButton, 13, 7, 1, 1)

        self.GameFilesExecScriptInput = QLineEdit(self.AddonsTab)
        self.GameFilesExecScriptInput.setObjectName(u"GameFilesExecScriptInput")

        self.gridLayout_9.addWidget(self.GameFilesExecScriptInput, 13, 3, 1, 3)

        self.line = QFrame(self.AddonsTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line, 12, 1, 1, 7)

        self.GameFilesSaveButton = QPushButton(self.AddonsTab)
        self.GameFilesSaveButton.setObjectName(u"GameFilesSaveButton")
        self.GameFilesSaveButton.setMinimumSize(QSize(0, 28))
        self.GameFilesSaveButton.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/assets/img/icons/document-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesSaveButton.setIcon(icon10)

        self.gridLayout_9.addWidget(self.GameFilesSaveButton, 10, 3, 2, 1)

        self.GameFilesDownButton = QPushButton(self.AddonsTab)
        self.GameFilesDownButton.setObjectName(u"GameFilesDownButton")
        sizePolicy5.setHeightForWidth(self.GameFilesDownButton.sizePolicy().hasHeightForWidth())
        self.GameFilesDownButton.setSizePolicy(sizePolicy5)
        icon11 = QIcon()
        icon11.addFile(u":/assets/img/icons/go-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDownButton.setIcon(icon11)

        self.gridLayout_9.addWidget(self.GameFilesDownButton, 11, 1, 1, 1)

        self.GameFilesAddButton = QPushButton(self.AddonsTab)
        self.GameFilesAddButton.setObjectName(u"GameFilesAddButton")
        self.GameFilesAddButton.setMinimumSize(QSize(0, 28))
        icon12 = QIcon()
        icon12.addFile(u":/assets/img/icons/list-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesAddButton.setIcon(icon12)

        self.gridLayout_9.addWidget(self.GameFilesAddButton, 10, 7, 1, 1)

        self.GameFilesLoadButton = QPushButton(self.AddonsTab)
        self.GameFilesLoadButton.setObjectName(u"GameFilesLoadButton")
        self.GameFilesLoadButton.setMinimumSize(QSize(0, 28))
        self.GameFilesLoadButton.setStyleSheet(u"")
        self.GameFilesLoadButton.setIcon(icon6)

        self.gridLayout_9.addWidget(self.GameFilesLoadButton, 10, 5, 2, 1)

        self.GameFilesList = QListWidget(self.AddonsTab)
        icon13 = QIcon()
        icon13.addFile(u":/assets/img/filetypes/wad.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem1.setIcon(icon13);
        icon14 = QIcon()
        icon14.addFile(u":/assets/img/filetypes/pk3.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem2.setIcon(icon14);
        icon15 = QIcon()
        icon15.addFile(u":/assets/img/filetypes/lua.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem3.setIcon(icon15);
        self.GameFilesList.setObjectName(u"GameFilesList")
        self.GameFilesList.setStyleSheet(u"")
        self.GameFilesList.setDragEnabled(True)
        self.GameFilesList.setDragDropOverwriteMode(False)
        self.GameFilesList.setDragDropMode(QAbstractItemView.DropOnly)
        self.GameFilesList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.GameFilesList.setIconSize(QSize(32, 32))
        self.GameFilesList.setMovement(QListView.Static)

        self.gridLayout_9.addWidget(self.GameFilesList, 0, 1, 9, 7)

        self.line_3 = QFrame(self.AddonsTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_3, 10, 6, 2, 1)

        self.line_2 = QFrame(self.AddonsTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_2, 10, 2, 2, 1)

        self.GameSettingsTabWidget.addTab(self.AddonsTab, "")

        self.verticalLayout_27.addWidget(self.GameSettingsTabWidget)

        self.GameContentStackedWidget.addWidget(self.GameSettingsPage)
        self.ModsPage = QWidget()
        self.ModsPage.setObjectName(u"ModsPage")
        self.verticalLayout_5 = QVBoxLayout(self.ModsPage)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.widget_3 = QWidget(self.ModsPage)
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
        self.ModBrowserLabel = QLabel(self.groupBox)
        self.ModBrowserLabel.setObjectName(u"ModBrowserLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ModBrowserLabel.sizePolicy().hasHeightForWidth())
        self.ModBrowserLabel.setSizePolicy(sizePolicy6)

        self.verticalLayout_24.addWidget(self.ModBrowserLabel)

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
        self.ModViewerLabel = QLabel(self.groupBox_2)
        self.ModViewerLabel.setObjectName(u"ModViewerLabel")
        sizePolicy6.setHeightForWidth(self.ModViewerLabel.sizePolicy().hasHeightForWidth())
        self.ModViewerLabel.setSizePolicy(sizePolicy6)

        self.verticalLayout_21.addWidget(self.ModViewerLabel)

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
        self.ModBrowser.setProperty("url", QUrl(u"about:blank"))

        self.verticalLayout_21.addWidget(self.ModBrowser)

        self.splitter_2.addWidget(self.groupBox_2)

        self.verticalLayout_25.addWidget(self.splitter_2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.ModStatusLabel = QLabel(self.widget_3)
        self.ModStatusLabel.setObjectName(u"ModStatusLabel")

        self.horizontalLayout_20.addWidget(self.ModStatusLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.ModTypeCombo = QComboBox(self.widget_3)
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.setObjectName(u"ModTypeCombo")

        self.horizontalLayout_20.addWidget(self.ModTypeCombo)

        self.OpenPageButton = QPushButton(self.widget_3)
        self.OpenPageButton.setObjectName(u"OpenPageButton")
        self.OpenPageButton.setEnabled(False)
        self.OpenPageButton.setIcon(icon5)

        self.horizontalLayout_20.addWidget(self.OpenPageButton)

        self.RefreshModsButton = QPushButton(self.widget_3)
        self.RefreshModsButton.setObjectName(u"RefreshModsButton")
        self.RefreshModsButton.setIcon(icon4)

        self.horizontalLayout_20.addWidget(self.RefreshModsButton)

        self.DownloadModButton = QPushButton(self.widget_3)
        self.DownloadModButton.setObjectName(u"DownloadModButton")
        self.DownloadModButton.setEnabled(False)
        icon16 = QIcon()
        iconThemeName = u"download"
        if QIcon.hasThemeIcon(iconThemeName):
            icon16 = QIcon.fromTheme(iconThemeName)
        else:
            icon16.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.DownloadModButton.setIcon(icon16)

        self.horizontalLayout_20.addWidget(self.DownloadModButton)


        self.verticalLayout_25.addLayout(self.horizontalLayout_20)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.GameContentStackedWidget.addWidget(self.ModsPage)
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 671, 686))
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.RoomLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.RoomLabel.setObjectName(u"RoomLabel")

        self.gridLayout.addWidget(self.RoomLabel, 1, 1, 1, 1)

        self.RoomInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.setObjectName(u"RoomInput")
        self.RoomInput.setEditable(False)

        self.gridLayout.addWidget(self.RoomInput, 2, 1, 1, 1)

        self.HostMSComboBox = QComboBox(self.scrollAreaWidgetContents_4)
        self.HostMSComboBox.addItem("")
        self.HostMSComboBox.addItem("")
        self.HostMSComboBox.setObjectName(u"HostMSComboBox")
        self.HostMSComboBox.setEnabled(False)
        self.HostMSComboBox.setEditable(True)

        self.gridLayout.addWidget(self.HostMSComboBox, 2, 2, 1, 1)

        self.HostMSLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.HostMSLabel.setObjectName(u"HostMSLabel")

        self.gridLayout.addWidget(self.HostMSLabel, 1, 2, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout)

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
        self.GametypeInput.addItem("")
        self.GametypeInput.setObjectName(u"GametypeInput")
        self.GametypeInput.setEditable(True)

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
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 844, 450))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.GameTabView = QTabWidget(self.scrollAreaWidgetContents_3)
        self.GameTabView.setObjectName(u"GameTabView")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.GameTabView.sizePolicy().hasHeightForWidth())
        self.GameTabView.setSizePolicy(sizePolicy7)
        self.GameTabView.setTabShape(QTabWidget.Rounded)
        self.BrowseTab = QWidget()
        self.BrowseTab.setObjectName(u"BrowseTab")
        self.verticalLayout_23 = QVBoxLayout(self.BrowseTab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.BrowseMSLabel = QLabel(self.BrowseTab)
        self.BrowseMSLabel.setObjectName(u"BrowseMSLabel")

        self.verticalLayout_23.addWidget(self.BrowseMSLabel)

        self.BrowseNetgameTable = QTableWidget(self.BrowseTab)
        if (self.BrowseNetgameTable.columnCount() < 5):
            self.BrowseNetgameTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.BrowseNetgameTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.BrowseNetgameTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.BrowseNetgameTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.BrowseNetgameTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.BrowseNetgameTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.BrowseNetgameTable.rowCount() < 1):
            self.BrowseNetgameTable.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.BrowseNetgameTable.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.BrowseNetgameTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.BrowseNetgameTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.BrowseNetgameTable.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.BrowseNetgameTable.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.BrowseNetgameTable.setItem(0, 4, __qtablewidgetitem10)
        self.BrowseNetgameTable.setObjectName(u"BrowseNetgameTable")
        self.BrowseNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.BrowseNetgameTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.BrowseNetgameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.BrowseNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.BrowseNetgameTable.verticalHeader().setVisible(False)

        self.verticalLayout_23.addWidget(self.BrowseNetgameTable)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MSSelectionLabel = QLabel(self.BrowseTab)
        self.MSSelectionLabel.setObjectName(u"MSSelectionLabel")

        self.horizontalLayout_18.addWidget(self.MSSelectionLabel)

        self.BrowseMSComboBox = QComboBox(self.BrowseTab)
        self.BrowseMSComboBox.addItem("")
        self.BrowseMSComboBox.setObjectName(u"BrowseMSComboBox")
        sizePolicy5.setHeightForWidth(self.BrowseMSComboBox.sizePolicy().hasHeightForWidth())
        self.BrowseMSComboBox.setSizePolicy(sizePolicy5)
        self.BrowseMSComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_18.addWidget(self.BrowseMSComboBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.MSStatusLabel = QLabel(self.BrowseTab)
        self.MSStatusLabel.setObjectName(u"MSStatusLabel")

        self.horizontalLayout_18.addWidget(self.MSStatusLabel)

        self.RefreshButton = QPushButton(self.BrowseTab)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setIcon(icon4)

        self.horizontalLayout_18.addWidget(self.RefreshButton)

        self.SaveNetgameButton = QPushButton(self.BrowseTab)
        self.SaveNetgameButton.setObjectName(u"SaveNetgameButton")
        icon17 = QIcon()
        icon17.addFile(u":/assets/img/icons/bookmark-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveNetgameButton.setIcon(icon17)

        self.horizontalLayout_18.addWidget(self.SaveNetgameButton)

        self.BrowseNetgameJoinButton = QPushButton(self.BrowseTab)
        self.BrowseNetgameJoinButton.setObjectName(u"BrowseNetgameJoinButton")
        icon18 = QIcon()
        icon18.addFile(u":/assets/img/icons/media-playback-start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowseNetgameJoinButton.setIcon(icon18)

        self.horizontalLayout_18.addWidget(self.BrowseNetgameJoinButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.GameTabView.addTab(self.BrowseTab, "")
        self.SavedNetgamesTab = QWidget()
        self.SavedNetgamesTab.setObjectName(u"SavedNetgamesTab")
        self.verticalLayout_22 = QVBoxLayout(self.SavedNetgamesTab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.JoinServerLabel = QLabel(self.SavedNetgamesTab)
        self.JoinServerLabel.setObjectName(u"JoinServerLabel")

        self.verticalLayout_22.addWidget(self.JoinServerLabel)

        self.frame_14 = QFrame(self.SavedNetgamesTab)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.frame_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.JoinAddressInput = QLineEdit(self.SavedNetgamesTab)
        self.JoinAddressInput.setObjectName(u"JoinAddressInput")
        self.JoinAddressInput.setPlaceholderText(u"IP Address")

        self.horizontalLayout_17.addWidget(self.JoinAddressInput)

        self.JoinAddressButton = QPushButton(self.SavedNetgamesTab)
        self.JoinAddressButton.setObjectName(u"JoinAddressButton")
        self.JoinAddressButton.setIcon(icon18)

        self.horizontalLayout_17.addWidget(self.JoinAddressButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_17)

        self.ServerListLabel = QLabel(self.SavedNetgamesTab)
        self.ServerListLabel.setObjectName(u"ServerListLabel")

        self.verticalLayout_22.addWidget(self.ServerListLabel)

        self.SavedNetgameTable = QTableWidget(self.SavedNetgamesTab)
        if (self.SavedNetgameTable.columnCount() < 3):
            self.SavedNetgameTable.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.SavedNetgameTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.SavedNetgameTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.SavedNetgameTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.SavedNetgameTable.setObjectName(u"SavedNetgameTable")
        self.SavedNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.SavedNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.SavedNetgameTable.verticalHeader().setVisible(False)
        self.SavedNetgameTable.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_22.addWidget(self.SavedNetgameTable)

        self.frame_10 = QFrame(self.SavedNetgamesTab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.JoinBookmarkButton = QPushButton(self.frame_10)
        self.JoinBookmarkButton.setObjectName(u"JoinBookmarkButton")
        self.JoinBookmarkButton.setSizeIncrement(QSize(0, 0))
        self.JoinBookmarkButton.setIcon(icon18)

        self.horizontalLayout_9.addWidget(self.JoinBookmarkButton)

        self.AddServerButton = QPushButton(self.frame_10)
        self.AddServerButton.setObjectName(u"AddServerButton")
        self.AddServerButton.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.AddServerButton)

        self.DeleteServerButton = QPushButton(self.frame_10)
        self.DeleteServerButton.setObjectName(u"DeleteServerButton")
        self.DeleteServerButton.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.DeleteServerButton)


        self.verticalLayout_22.addWidget(self.frame_10)

        self.GameTabView.addTab(self.SavedNetgamesTab, "")
        self.masterservers = QWidget()
        self.masterservers.setObjectName(u"masterservers")
        self.masterservers.setMinimumSize(QSize(824, 0))
        self.verticalLayout_30 = QVBoxLayout(self.masterservers)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.splitter_3 = QSplitter(self.masterservers)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.gridLayoutWidget = QWidget(self.splitter_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 2, 1, 1, 1)

        self.MSAddButton = QPushButton(self.gridLayoutWidget)
        self.MSAddButton.setObjectName(u"MSAddButton")
        self.MSAddButton.setIcon(icon12)

        self.gridLayout_6.addWidget(self.MSAddButton, 2, 4, 1, 1)

        self.MSTableLabel = QLabel(self.gridLayoutWidget)
        self.MSTableLabel.setObjectName(u"MSTableLabel")

        self.gridLayout_6.addWidget(self.MSTableLabel, 0, 0, 1, 1)

        self.MSMessageLabel = QLabel(self.gridLayoutWidget)
        self.MSMessageLabel.setObjectName(u"MSMessageLabel")

        self.gridLayout_6.addWidget(self.MSMessageLabel, 2, 0, 1, 1)

        self.MasterServersTable = QTableWidget(self.gridLayoutWidget)
        if (self.MasterServersTable.columnCount() < 3):
            self.MasterServersTable.setColumnCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.MasterServersTable.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.MasterServersTable.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.MasterServersTable.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        if (self.MasterServersTable.rowCount() < 2):
            self.MasterServersTable.setRowCount(2)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.MasterServersTable.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.MasterServersTable.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.MasterServersTable.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.MasterServersTable.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.MasterServersTable.setItem(0, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.MasterServersTable.setItem(1, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.MasterServersTable.setItem(1, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.MasterServersTable.setItem(1, 2, __qtablewidgetitem24)
        self.MasterServersTable.setObjectName(u"MasterServersTable")
        self.MasterServersTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.MasterServersTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.MasterServersTable.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.MasterServersTable, 1, 0, 1, 6)

        self.MSListSaveButton = QPushButton(self.gridLayoutWidget)
        self.MSListSaveButton.setObjectName(u"MSListSaveButton")
        self.MSListSaveButton.setIcon(icon10)

        self.gridLayout_6.addWidget(self.MSListSaveButton, 2, 2, 1, 1)

        self.MSRemoveButton = QPushButton(self.gridLayoutWidget)
        self.MSRemoveButton.setObjectName(u"MSRemoveButton")
        self.MSRemoveButton.setIcon(icon8)

        self.gridLayout_6.addWidget(self.MSRemoveButton, 2, 5, 1, 1)

        self.splitter_3.addWidget(self.gridLayoutWidget)
        self.verticalLayoutWidget = QWidget(self.splitter_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_28 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.MSAPILabel = QLabel(self.verticalLayoutWidget)
        self.MSAPILabel.setObjectName(u"MSAPILabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.MSAPILabel.sizePolicy().hasHeightForWidth())
        self.MSAPILabel.setSizePolicy(sizePolicy8)

        self.verticalLayout_28.addWidget(self.MSAPILabel)

        self.textBrowser_2 = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy6.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy6)

        self.verticalLayout_28.addWidget(self.textBrowser_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_9)

        self.splitter_3.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_30.addWidget(self.splitter_3)

        self.GameTabView.addTab(self.masterservers, "")

        self.verticalLayout_13.addWidget(self.GameTabView)

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
        sizePolicy3.setHeightForWidth(self.GameProfileComboBox.sizePolicy().hasHeightForWidth())
        self.GameProfileComboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.GameProfileComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.GamePlayButton = QPushButton(self.GamePlayFrame)
        self.GamePlayButton.setObjectName(u"GamePlayButton")
        self.GamePlayButton.setMinimumSize(QSize(240, 38))
        self.GamePlayButton.setMaximumSize(QSize(240, 38))
        self.GamePlayButton.setIcon(icon18)

        self.horizontalLayout_3.addWidget(self.GamePlayButton)

        self.GameOptionsDropDownButton = QPushButton(self.GamePlayFrame)
        self.GameOptionsDropDownButton.setObjectName(u"GameOptionsDropDownButton")
        self.GameOptionsDropDownButton.setMinimumSize(QSize(0, 28))
        self.GameOptionsDropDownButton.setMaximumSize(QSize(16, 38))
        icon19 = QIcon()
        iconThemeName = u"go-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon19 = QIcon.fromTheme(iconThemeName)
        else:
            icon19.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.GameOptionsDropDownButton.setIcon(icon19)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 844, 535))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.AboutText = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.AboutText.setObjectName(u"AboutText")
        self.AboutText.setReadOnly(True)
        self.AboutText.setOpenExternalLinks(True)

        self.verticalLayout_19.addWidget(self.AboutText)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 844, 535))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget_2 = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout = QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ProfileDirLabel = QLabel(self.tab_5)
        self.ProfileDirLabel.setObjectName(u"ProfileDirLabel")

        self.verticalLayout.addWidget(self.ProfileDirLabel)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit = QLineEdit(self.tab_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_21.addWidget(self.lineEdit)

        self.ProfileDirBrowseButton = QPushButton(self.tab_5)
        self.ProfileDirBrowseButton.setObjectName(u"ProfileDirBrowseButton")
        self.ProfileDirBrowseButton.setIcon(icon6)

        self.horizontalLayout_21.addWidget(self.ProfileDirBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.LauncherThemeLabel = QLabel(self.tab_5)
        self.LauncherThemeLabel.setObjectName(u"LauncherThemeLabel")

        self.verticalLayout.addWidget(self.LauncherThemeLabel)

        self.LauncherThemeInput = QComboBox(self.tab_5)
        self.LauncherThemeInput.addItem("")
        self.LauncherThemeInput.addItem("")
        self.LauncherThemeInput.setObjectName(u"LauncherThemeInput")
        self.LauncherThemeInput.setEnabled(True)

        self.verticalLayout.addWidget(self.LauncherThemeInput)

        self.SaveFilesToConfigToggle = QCheckBox(self.tab_5)
        self.SaveFilesToConfigToggle.setObjectName(u"SaveFilesToConfigToggle")
        self.SaveFilesToConfigToggle.setChecked(False)

        self.verticalLayout.addWidget(self.SaveFilesToConfigToggle)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_6 = QVBoxLayout(self.tab_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ModsourceDisclaimerLabel = QLabel(self.tab_6)
        self.ModsourceDisclaimerLabel.setObjectName(u"ModsourceDisclaimerLabel")

        self.verticalLayout_6.addWidget(self.ModsourceDisclaimerLabel)

        self.textBrowser = QTextBrowser(self.tab_6)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy9)

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.ModsourceCheckLabel = QLabel(self.tab_6)
        self.ModsourceCheckLabel.setObjectName(u"ModsourceCheckLabel")

        self.verticalLayout_6.addWidget(self.ModsourceCheckLabel)

        self.ModsourceMBCheckbox = QCheckBox(self.tab_6)
        self.ModsourceMBCheckbox.setObjectName(u"ModsourceMBCheckbox")
        self.ModsourceMBCheckbox.setChecked(True)

        self.verticalLayout_6.addWidget(self.ModsourceMBCheckbox)

        self.ModsourceWSBlueCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSBlueCheckbox.setObjectName(u"ModsourceWSBlueCheckbox")

        self.verticalLayout_6.addWidget(self.ModsourceWSBlueCheckbox)

        self.ModsourceWSRedCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSRedCheckbox.setObjectName(u"ModsourceWSRedCheckbox")

        self.verticalLayout_6.addWidget(self.ModsourceWSRedCheckbox)

        self.checkBox = QCheckBox(self.tab_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)

        self.verticalLayout_6.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tab_6)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.verticalLayout_6.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.tab_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.verticalLayout_6.addWidget(self.checkBox_3)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_8 = QGridLayout(self.tab_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.RSSRemoveButton = QPushButton(self.tab_9)
        self.RSSRemoveButton.setObjectName(u"RSSRemoveButton")
        self.RSSRemoveButton.setEnabled(False)
        self.RSSRemoveButton.setIcon(icon8)

        self.gridLayout_8.addWidget(self.RSSRemoveButton, 4, 2, 1, 1)

        self.RSSMoveupButton = QPushButton(self.tab_9)
        self.RSSMoveupButton.setObjectName(u"RSSMoveupButton")
        self.RSSMoveupButton.setEnabled(False)
        self.RSSMoveupButton.setIcon(icon9)

        self.gridLayout_8.addWidget(self.RSSMoveupButton, 3, 0, 1, 1)

        self.NewssourceLabel = QLabel(self.tab_9)
        self.NewssourceLabel.setObjectName(u"NewssourceLabel")

        self.gridLayout_8.addWidget(self.NewssourceLabel, 0, 0, 1, 3)

        self.RSSAddButton = QPushButton(self.tab_9)
        self.RSSAddButton.setObjectName(u"RSSAddButton")
        self.RSSAddButton.setIcon(icon12)

        self.gridLayout_8.addWidget(self.RSSAddButton, 3, 2, 1, 1)

        self.RSSMovedownButton = QPushButton(self.tab_9)
        self.RSSMovedownButton.setObjectName(u"RSSMovedownButton")
        self.RSSMovedownButton.setEnabled(False)
        self.RSSMovedownButton.setIcon(icon11)

        self.gridLayout_8.addWidget(self.RSSMovedownButton, 4, 0, 1, 1)

        self.RSSStatusLabel_2 = QLabel(self.tab_9)
        self.RSSStatusLabel_2.setObjectName(u"RSSStatusLabel_2")
        self.RSSStatusLabel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.RSSStatusLabel_2, 3, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 4, 1, 1, 1)

        self.RSSFeedList = QListWidget(self.tab_9)
        QListWidgetItem(self.RSSFeedList)
        QListWidgetItem(self.RSSFeedList)
        QListWidgetItem(self.RSSFeedList)
        QListWidgetItem(self.RSSFeedList)
        self.RSSFeedList.setObjectName(u"RSSFeedList")

        self.gridLayout_8.addWidget(self.RSSFeedList, 1, 0, 1, 3)

        self.tabWidget_2.addTab(self.tab_9, "")

        self.verticalLayout_18.addWidget(self.tabWidget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.MainTabsStackedWidget.addWidget(self.SettingsPage)

        self.horizontalLayout_2.addWidget(self.MainTabsStackedWidget)


        self.gridLayout_2.addWidget(self.MainAreaFrame, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTabsStackedWidget.setCurrentIndex(0)
        self.GameContentStackedWidget.setCurrentIndex(1)
        self.GameSettingsTabWidget.setCurrentIndex(0)
        self.PlayerSkinInput.setCurrentIndex(0)
        self.PlayerColorInput.setCurrentIndex(0)
        self.AdvanceMapInput.setCurrentIndex(1)
        self.GameTabView.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


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
        self.HelpTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.HelpTabButton.setText("")
#if QT_CONFIG(tooltip)
        self.SettingsTabButton.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.SettingsTabButton.setText("")
        self.RSSFeedLabel.setText(QCoreApplication.translate("MainWindow", u"Newsfeed URL", None))
        self.RSSFeedCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"http://srb2.org/feed", None))

        self.RSSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Please select a feed and click \"Refresh\"", None))
        self.RSSRefreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.RSSViewonlineButton.setText(QCoreApplication.translate("MainWindow", u"View online", None))

        __sortingEnabled = self.RSSArticleList.isSortingEnabled()
        self.RSSArticleList.setSortingEnabled(False)
        ___qlistwidgetitem = self.RSSArticleList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"No articles. Pleas click \"Refresh\" to load some.", None));
        self.RSSArticleList.setSortingEnabled(__sortingEnabled)

        self.RSSArticleView.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Atkinson Hyperlegible'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/assets/img/icons/news.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No article selected. Please select one from the list.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        __sortingEnabled1 = self.GamePageTabList.isSortingEnabled()
        self.GamePageTabList.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.GamePageTabList.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Profile", None));
        ___qlistwidgetitem2 = self.GamePageTabList.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Game", None));
        ___qlistwidgetitem3 = self.GamePageTabList.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Modding", None));
        ___qlistwidgetitem4 = self.GamePageTabList.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Host Netgame", None));
        ___qlistwidgetitem5 = self.GamePageTabList.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Join Netgame", None));
        self.GamePageTabList.setSortingEnabled(__sortingEnabled1)

        self.ProfileNameInput.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.ProfileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Profile Name", None))
        self.ProfileGameLabel.setText(QCoreApplication.translate("MainWindow", u"Game", None))
        self.ProfileGameSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"SRB2", None))
        self.ProfileGameSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"SRB2Kart", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.ProfileVersionSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"2.2", None))
        self.ProfileVersionSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"2.1", None))
        self.ProfileVersionSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"2.0", None))
        self.ProfileVersionSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"1.09.X", None))
        self.ProfileVersionSetting.setItemText(4, QCoreApplication.translate("MainWindow", u"1.08", None))
        self.ProfileVersionSetting.setItemText(5, QCoreApplication.translate("MainWindow", u"1.07", None))

        self.ProfileVersionLabel.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.PlayerNameTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.PlayerNameInput.setText("")
        self.PlayerNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Skin", None))
        self.PlayerSkinInput.setItemText(0, "")
        self.PlayerSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.PlayerSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.PlayerSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.PlayerSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.PlayerSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PlayerSkinImage.setText("")
        self.PlayerSkinInfoText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dddd00;\">Sonic</span> is the fastest of the three, but also the hardest to control. Begginers beware, but experts will find Sonic very powerful.</p><p><span style=\" color:#dddd00;\">Ability:</span> Speed Thok<br/>Double jump to zoom forward with a huge burst of speed</p><p><span style=\" color:#dddd00;\">Tip:</span> Simply letting go of forward does not slow down in SRB2. To slow down, hold the opposite direction.</p></body></html>", None))
        self.PlayerColorTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
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

        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.PlayerSettingsTab), QCoreApplication.translate("MainWindow", u"Player settings", None))
        self.GameResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"Resolutions", None))
        self.GameHorizontalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
        self.GameResMultLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.GameVerticalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
        self.GameRenderCfgLabel.setText(QCoreApplication.translate("MainWindow", u"Render Options", None))
        self.GameRendererSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.GameRendererSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"OpenGL", None))

        self.GameFullscreenSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.GameFullscreenSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Borderless fullscreen", None))
        self.GameFullscreenSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Windowed", None))

        self.GameSoundOptionsLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Options", None))
        self.GameMusicSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Digital music", None))
        self.GameMusicSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Midi music", None))
        self.GameMusicSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Load music from a CD", None))
        self.GameMusicSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"Disable music", None))

        self.GameSoundSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Enable sound", None))
        self.GameSoundSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Disable sound", None))

        self.GameExecPathLabel.setText(QCoreApplication.translate("MainWindow", u"Executable Path (EXE/ELF)", None))
        self.GameExecFilePathInput.setText(QCoreApplication.translate("MainWindow", u"srb2win.exe", None))
        self.GameExecFilePathBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.WineToggle.setText(QCoreApplication.translate("MainWindow", u"RUN SRB2 IN WINE", None))
        self.GameArgsLabel.setText(QCoreApplication.translate("MainWindow", u"Custom Shell Parameters", None))
        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.GameSettingsTab), QCoreApplication.translate("MainWindow", u"Game settings", None))
        self.GameFilesClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
        self.GameFilesExecuteScriptLabel.setText(QCoreApplication.translate("MainWindow", u"Launch Script", None))
        self.GameFilesDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete selected files", None))
        self.GameFilesUpButton.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.GameFilesExecScrBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse scripts...", None))
        self.GameFilesSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save list", None))
        self.GameFilesDownButton.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.GameFilesAddButton.setText(QCoreApplication.translate("MainWindow", u"Add file...", None))
        self.GameFilesLoadButton.setText(QCoreApplication.translate("MainWindow", u"Load list...", None))

        __sortingEnabled2 = self.GameFilesList.isSortingEnabled()
        self.GameFilesList.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.GameFilesList.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"place.wad", None));
        ___qlistwidgetitem7 = self.GameFilesList.item(1)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"hold.pk3", None));
        ___qlistwidgetitem8 = self.GameFilesList.item(2)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"er.lua", None));
        self.GameFilesList.setSortingEnabled(__sortingEnabled2)

        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.AddonsTab), QCoreApplication.translate("MainWindow", u"Add-ons", None))
        self.ModBrowserLabel.setText(QCoreApplication.translate("MainWindow", u"Mod List:", None))
        self.ModViewerLabel.setText(QCoreApplication.translate("MainWindow", u"About Mod:", None))
        self.ModStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Refresh\" to see a list of available mods.", None))
        self.ModTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Maps", None))
        self.ModTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Characters", None))
        self.ModTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Lua", None))
        self.ModTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Assets", None))
        self.ModTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Misc", None))

        self.OpenPageButton.setText(QCoreApplication.translate("MainWindow", u"Visit Page", None))
        self.RefreshModsButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.DownloadModButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.ServerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.AdminPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Admin Password", None))
        self.RoomLabel.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.RoomInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Offline", None))
        self.RoomInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.RoomInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Casual", None))
        self.RoomInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Hugs", None))
        self.RoomInput.setItemText(4, QCoreApplication.translate("MainWindow", u"OLDC", None))

        self.HostMSComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"https://ms.srb2.org/MS/0", None))
        self.HostMSComboBox.setItemText(1, "")

        self.HostMSLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.GametypeLabel.setText(QCoreApplication.translate("MainWindow", u"Gametype", None))
        self.GametypeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Co-op", None))
        self.GametypeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Competition", None))
        self.GametypeInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Race", None))
        self.GametypeInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Match", None))
        self.GametypeInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Team Match", None))
        self.GametypeInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Tag", None))
        self.GametypeInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Hide and Seek", None))
        self.GametypeInput.setItemText(7, QCoreApplication.translate("MainWindow", u"Capture the Flag", None))
        self.GametypeInput.setItemText(8, "")

        self.AdvanceMapLabel.setText(QCoreApplication.translate("MainWindow", u"Map Advancement Policy", None))
        self.AdvanceMapInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.AdvanceMapInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Next", None))
        self.AdvanceMapInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Random", None))

        self.PointLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Point Limit", None))
        self.PointLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.TimeLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Time Limit", None))
        self.TimeLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Off by default", None))
        self.MaxPlayersLabel.setText(QCoreApplication.translate("MainWindow", u"Max. Players", None))
        self.MaxPlayersInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"8", None))
        self.ForceSkinLabel.setText(QCoreApplication.translate("MainWindow", u"Force Skin", None))
        self.ForceSkinInput.setItemText(0, "")
        self.ForceSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.ForceSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.ForceSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.ForceSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.ForceSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.ForceSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.PortInput.setInputMask("")
        self.PortInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5029", None))
        self.DisableWeaponsToggle.setText(QCoreApplication.translate("MainWindow", u"Disable weapon rings", None))
        self.SuddenDeathToggle.setText(QCoreApplication.translate("MainWindow", u"Sudden Death", None))
        self.DedicatedServerToggle.setText(QCoreApplication.translate("MainWindow", u"Dedicated Server", None))
        self.UploadToggle.setText(QCoreApplication.translate("MainWindow", u"Enable Add-On downloads", None))
        self.BrowseMSLabel.setText(QCoreApplication.translate("MainWindow", u"NETGAMES", None))
        ___qtablewidgetitem = self.BrowseNetgameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.BrowseNetgameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Gametype", None));
        ___qtablewidgetitem2 = self.BrowseNetgameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Version", None));
        ___qtablewidgetitem3 = self.BrowseNetgameTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Room", None));
        ___qtablewidgetitem4 = self.BrowseNetgameTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Origin", None));

        __sortingEnabled3 = self.BrowseNetgameTable.isSortingEnabled()
        self.BrowseNetgameTable.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.BrowseNetgameTable.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Earless Adventure", None));
        ___qtablewidgetitem6 = self.BrowseNetgameTable.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Battle CTF", None));
        ___qtablewidgetitem7 = self.BrowseNetgameTable.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2.2.10", None));
        ___qtablewidgetitem8 = self.BrowseNetgameTable.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Standard", None));
        ___qtablewidgetitem9 = self.BrowseNetgameTable.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"mb.srb2.org", None));
        self.BrowseNetgameTable.setSortingEnabled(__sortingEnabled3)

        self.MSSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.BrowseMSComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ms.srb2.org", None))

        self.MSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Update\" to download a list of servers.", None))
        self.RefreshButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.SaveNetgameButton.setText(QCoreApplication.translate("MainWindow", u"Bookmark", None))
        self.BrowseNetgameJoinButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.BrowseTab), QCoreApplication.translate("MainWindow", u"Browse", None))
        self.JoinServerLabel.setText(QCoreApplication.translate("MainWindow", u"Join directly", None))
        self.JoinAddressButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.ServerListLabel.setText(QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        ___qtablewidgetitem10 = self.SavedNetgameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.SavedNetgameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem12 = self.SavedNetgameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        self.JoinBookmarkButton.setText(QCoreApplication.translate("MainWindow", u"Join server", None))
        self.AddServerButton.setText(QCoreApplication.translate("MainWindow", u"Add Boookmark", None))
        self.DeleteServerButton.setText(QCoreApplication.translate("MainWindow", u"Remove Bookmark", None))
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.SavedNetgamesTab), QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.MSAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.MSTableLabel.setText(QCoreApplication.translate("MainWindow", u"Master Servers", None))
        self.MSMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Please respect your master servers' rules", None))
        ___qtablewidgetitem13 = self.MasterServersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem14 = self.MasterServersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem15 = self.MasterServersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"API", None));

        __sortingEnabled4 = self.MasterServersTable.isSortingEnabled()
        self.MasterServersTable.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.MasterServersTable.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"STJr", None));
        ___qtablewidgetitem17 = self.MasterServersTable.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"http://mb.srb2.org/MS/0", None));
        ___qtablewidgetitem18 = self.MasterServersTable.item(0, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"v1", None));
        ___qtablewidgetitem19 = self.MasterServersTable.item(1, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Kart Krew", None));
        ___qtablewidgetitem20 = self.MasterServersTable.item(1, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"https://ms.kartkrew.org/ms/api/games/SRB2Kart/", None));
        ___qtablewidgetitem21 = self.MasterServersTable.item(1, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"kartv2", None));
        self.MasterServersTable.setSortingEnabled(__sortingEnabled4)

        self.MSListSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save List", None))
        self.MSRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.MSAPILabel.setText(QCoreApplication.translate("MainWindow", u"Valid APIs", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Atkinson Hyperlegible'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">v1</span>: Official SRB2 API</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">kartv2</span>: SRB2Kart API</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">snitch</span>: LiquidMS Snitch API</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All other APIs will be ignored</p></body></html>", None))
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.masterservers), QCoreApplication.translate("MainWindow", u"Master Servers", None))
        self.GameProfileComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New profile...", None))

        self.GamePlayButton.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.GameOptionsDropDownButton.setText("")
        self.AboutText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Atkinson Hyperlegible'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/assets/img/liquidlauncher.svg\" /><span style=\" font-size:16pt; font-weight:600;\"><br />LiquidLauncher</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">built by Liquid<br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://discord.gg/HVTzVfAWG6/\"><span style=\" text-decoration: underline; color:#00d3b8"
                        ";\">Join our Discord</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Contributers</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PixL<br /><a href=\"discord.gg/HVTzVfAWG6\"><span style=\" font-size:12pt; text-decoration: underline; color:#00d3b8;\"><br /></span></a></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Based on LauncherBlast2 &quot;reBoot&quot; by HitCoder</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:e"
                        "mpty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">LauncherBlast2 &quot;reBoot&quot; by HitCoder</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Built in PyQt5</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://mb.srb2.org/threads/launcherblast2-reboot.27592/\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; text-decoration: underline; color:#7777ff;\">View the SRB2 Message Board thread</span></a></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Credits</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FinestElite - icons for News and Help</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sonic Team Jr - SRB2 icon</li></ul>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">reBoot-2.0 changelog</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">UI Overhaul - main tabs are now at the top and use icons instead of text</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Introduction of profiles, allowing support for multiple installations of different versions of SRB2 or mods of SRB2 such as SRB2Kart</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\">Fixed a bug with spaces in filenames when adding files to the game</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed a bug with spaces in player nicknames</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The console no longer opens with the launcher</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added new icon for the launcher</li></ul>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; fo"
                        "nt-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">FAQ</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; text-decoration: underline;\">How do I host a server?</sp"
                        "an></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">To host a server, select the host server tab. You will be given a multitude of options for your server. To start your server, you will find that on this tab, your &quot;Play&quot; button has changed to read &quot;Start Server&quot;. You can only start a server with this tab selected.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; text-decoration: underline;\">My antivirus detects Launcherblast2 as a trojan. Is this t"
                        "rue?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Due to the nature of this utility, it is a small scale program that doesn't have a very big audience. Modern antivirus software may well detect it as a false-positive, as a precaution to &quot;unknown programs&quot;. If this happens, your antivirus may have an option to submit the program for analysis, in which case please do so!</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align="
                        "\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">About Launcherblast2</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">LAUNCHERBLAST2 is a project I started in 2019, before SRB2 2.2 was released. I wanted this to be released not long after 2.2 was, to go with it, but due to personal life and some other things I never got to finish it. Fast forward to early 2020, I remember this exists. I decided to finish it, though it's not to a standard I'd idea"
                        "lly like it to be. I do feel like it fits the bill for a nice looking launcher at it's forefront though.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">There are a couple of graphical glitches here and there because I realised not long into starting to develop this, that a lot of info on Qt5 is sparse, and some of the Qt4 stuff isn't directly compatible. I'm really sorry for the combo-boxes that have a weird square on them when you hover. I hope it doesn't bother you too much.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">In case you didn't already notice, the design is very much inspired by the 2019 Minecraft Launcher. It was actually that which kick-started me into creating this. Anyway, hope you enjoy it, if you find any bugs let me know! I'll be working on this from time to time regardless, so updates may come soon. I'm not implementing an auto-updater though, as I don't have a server to place the metadata on for now.</span></p></body></html>", None))
        self.ProfileDirLabel.setText(QCoreApplication.translate("MainWindow", u"Profile Directory", None))
        self.ProfileDirBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.LauncherThemeLabel.setText(QCoreApplication.translate("MainWindow", u"Launcher Theme (Requires Restart)", None))
        self.LauncherThemeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Dark", None))
        self.LauncherThemeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Light", None))

        self.SaveFilesToConfigToggle.setText(QCoreApplication.translate("MainWindow", u"CLEAR FILES LIST ON STARTUP", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"General settings", None))
        self.ModsourceDisclaimerLabel.setText(QCoreApplication.translate("MainWindow", u"DISCLAIMER", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Atkinson Hyperlegible'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">WARNING:</span><span style=\" font-weight:600;\"> </span>The use of mods from unofficial sources on the official Master Server [<a href=\"https://mb.srb2.org/MS/0\"><span style=\" text-decoration: underline; color:#00d3b8;\">https://mb.srb2.org/MS/0</span></a>] is prohibited by the Sonic Robo Blast 2 community administration team (&quot;STJr&quot;) and may be penalized by a permanent ban from their Master Server or the official SRB2 Message Board.</p>\n"
"<p align=\"center\" style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">USE THESE ALTERNATIVE MOD SOURCES AT YOUR OWN RISK!!!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Additionally, Liquid has no influence over, nor takes responsibility nor accountability for the quality, compliance or legality of mods or other content found within the provided sources, according to the terms of your or any other jurisdiction.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">YOU HAVE BEEN WARNED!!</span></p>\n"
"<p align=\"cente"
                        "r\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>", None))
        self.ModsourceCheckLabel.setText(QCoreApplication.translate("MainWindow", u"Mod sources", None))
        self.ModsourceMBCheckbox.setText(QCoreApplication.translate("MainWindow", u"Official SRB2 Message Board", None))
        self.ModsourceWSBlueCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Blue Sphere\" (unofficial)", None))
        self.ModsourceWSRedCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Red Sphere\" (non-compliant; unofficial)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Wad Archive \"2.2 section\" (unsupported)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"SRB2 Gamebanana (unsupported)", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"SRB2 Skybase (unsupported)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Mod Sources", None))
        self.RSSRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.RSSMoveupButton.setText(QCoreApplication.translate("MainWindow", u"Move up", None))
        self.NewssourceLabel.setText(QCoreApplication.translate("MainWindow", u"News Sources (RSS/Atom Feeds)", None))
        self.RSSAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.RSSMovedownButton.setText(QCoreApplication.translate("MainWindow", u"Move down", None))
        self.RSSStatusLabel_2.setText(QCoreApplication.translate("MainWindow", u"Select or double click an entry to edit.", None))

        __sortingEnabled5 = self.RSSFeedList.isSortingEnabled()
        self.RSSFeedList.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.RSSFeedList.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"https://srb2.org/feed", None));
        ___qlistwidgetitem10 = self.RSSFeedList.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"https://mb.srb2.org.org/forums/-/index.rss", None));
        ___qlistwidgetitem11 = self.RSSFeedList.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"https://srb2workshop.org/forums/-/index.rss", None));
        ___qlistwidgetitem12 = self.RSSFeedList.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"https://www.sonicstadium.org/feed/", None));
        self.RSSFeedList.setSortingEnabled(__sortingEnabled5)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"News Sources", None))
    # retranslateUi

