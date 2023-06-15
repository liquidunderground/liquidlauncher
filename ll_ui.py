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
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
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

        self.NewsTabButton = QToolButton(self.DockTabFrame)
        self.NewsTabButton.setObjectName(u"NewsTabButton")
        icon = QIcon()
        icon.addFile(u":/assets/img/icons/news.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NewsTabButton.setIcon(icon)
        self.NewsTabButton.setIconSize(QSize(48, 48))
        self.NewsTabButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.NewsTabButton)

        self.GameTabButton = QToolButton(self.DockTabFrame)
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
        self.GameTabButton.setCheckable(True)
        self.GameTabButton.setChecked(True)

        self.horizontalLayout.addWidget(self.GameTabButton)

        self.HelpTabButton = QToolButton(self.DockTabFrame)
        self.HelpTabButton.setObjectName(u"HelpTabButton")
        self.HelpTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/assets/img/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpTabButton.setIcon(icon2)
        self.HelpTabButton.setIconSize(QSize(48, 48))
        self.HelpTabButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.HelpTabButton)

        self.SettingsTabButton = QToolButton(self.DockTabFrame)
        self.SettingsTabButton.setObjectName(u"SettingsTabButton")
        self.SettingsTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/assets/img/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsTabButton.setIcon(icon3)
        self.SettingsTabButton.setIconSize(QSize(48, 48))
        self.SettingsTabButton.setCheckable(True)

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
        self.NewsScrollAreaContent.setGeometry(QRect(0, 0, 848, 539))
        self.NewsScrollAreaContent.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.NewsScrollAreaContent)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.RSSFeedCombobox = QComboBox(self.NewsScrollAreaContent)
        self.RSSFeedCombobox.addItem("")
        self.RSSFeedCombobox.setObjectName(u"RSSFeedCombobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RSSFeedCombobox.sizePolicy().hasHeightForWidth())
        self.RSSFeedCombobox.setSizePolicy(sizePolicy2)
        self.RSSFeedCombobox.setEditable(True)

        self.gridLayout_7.addWidget(self.RSSFeedCombobox, 0, 1, 1, 1)

        self.RSSFeedLabel = QLabel(self.NewsScrollAreaContent)
        self.RSSFeedLabel.setObjectName(u"RSSFeedLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.RSSFeedLabel.sizePolicy().hasHeightForWidth())
        self.RSSFeedLabel.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.RSSFeedLabel, 0, 0, 1, 1)

        self.RSSStatusLabel = QLabel(self.NewsScrollAreaContent)
        self.RSSStatusLabel.setObjectName(u"RSSStatusLabel")

        self.gridLayout_7.addWidget(self.RSSStatusLabel, 3, 0, 1, 2)

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
        self.RSSArticleView = QWebEngineView(self.splitter_4)
        self.RSSArticleView.setObjectName(u"RSSArticleView")
        sizePolicy.setHeightForWidth(self.RSSArticleView.sizePolicy().hasHeightForWidth())
        self.RSSArticleView.setSizePolicy(sizePolicy)
        self.RSSArticleView.setProperty("url", QUrl(u"qrc:/assets/default.html"))
        self.splitter_4.addWidget(self.RSSArticleView)

        self.gridLayout_7.addWidget(self.splitter_4, 2, 0, 1, 3)

        self.RSSRefreshButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSRefreshButton.setObjectName(u"RSSRefreshButton")
        icon4 = QIcon()
        icon4.addFile(u":/assets/img/icons/view-refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSRefreshButton.setIcon(icon4)

        self.gridLayout_7.addWidget(self.RSSRefreshButton, 0, 2, 1, 1)

        self.RSSViewonlineButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSViewonlineButton.setObjectName(u"RSSViewonlineButton")
        self.RSSViewonlineButton.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/assets/img/icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSViewonlineButton.setIcon(icon5)

        self.gridLayout_7.addWidget(self.RSSViewonlineButton, 3, 2, 1, 1)

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
        self.gridLayout_16 = QGridLayout(self.GamePageFrame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.splitter = QSplitter(self.GamePageFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.GamePageTabList = QListWidget(self.splitter)
        icon6 = QIcon()
        icon6.addFile(u":/assets/img/icons/srb2mb.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setPointSize(14)
        __qlistwidgetitem1 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem1.setIcon(icon6);
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        __qlistwidgetitem2 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem2.setFont(font1);
        __qlistwidgetitem2.setIcon(icon1);
        icon7 = QIcon()
        icon7.addFile(u":/assets/img/icons/list-add.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem3.setFont(font);
        __qlistwidgetitem3.setIcon(icon7);
        __qlistwidgetitem4 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem4.setFont(font);
        __qlistwidgetitem4.setIcon(icon3);
        __qlistwidgetitem5 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem5.setFont(font);
        __qlistwidgetitem5.setIcon(icon5);
        self.GamePageTabList.setObjectName(u"GamePageTabList")
        sizePolicy4.setHeightForWidth(self.GamePageTabList.sizePolicy().hasHeightForWidth())
        self.GamePageTabList.setSizePolicy(sizePolicy4)
        self.splitter.addWidget(self.GamePageTabList)
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
        self.gridLayout_2 = QGridLayout(self.ProfilePage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_5 = QScrollArea(self.ProfilePage)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 592, 447))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 9, 0, 1, 2)

        self.PlayerSkinImage = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinImage.setObjectName(u"PlayerSkinImage")
        self.PlayerSkinImage.setMaximumSize(QSize(128, 128))
        self.PlayerSkinImage.setStyleSheet(u"")
        self.PlayerSkinImage.setPixmap(QPixmap(u":/assets/img/sonic.png"))
        self.PlayerSkinImage.setScaledContents(True)

        self.gridLayout_5.addWidget(self.PlayerSkinImage, 6, 0, 1, 1)

        self.PlayerColorTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerColorTitleLabel.setObjectName(u"PlayerColorTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerColorTitleLabel, 7, 0, 1, 1)

        self.PlayerNameTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerNameTitleLabel.setObjectName(u"PlayerNameTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerNameTitleLabel, 0, 0, 1, 1)

        self.PlayerSkinTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinTitleLabel.setObjectName(u"PlayerSkinTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerSkinTitleLabel, 2, 0, 1, 1)

        self.PlayerSkinInfoText = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinInfoText.setObjectName(u"PlayerSkinInfoText")
        self.PlayerSkinInfoText.setMaximumSize(QSize(16777215, 1000007))
        self.PlayerSkinInfoText.setStyleSheet(u"")
        self.PlayerSkinInfoText.setTextFormat(Qt.RichText)
        self.PlayerSkinInfoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.PlayerSkinInfoText.setWordWrap(True)

        self.gridLayout_5.addWidget(self.PlayerSkinInfoText, 6, 1, 1, 1)

        self.PlayerSkinInput = QComboBox(self.scrollAreaWidgetContents_5)
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

        self.gridLayout_5.addWidget(self.PlayerSkinInput, 3, 0, 1, 2)

        self.PlayerNameInput = QLineEdit(self.scrollAreaWidgetContents_5)
        self.PlayerNameInput.setObjectName(u"PlayerNameInput")

        self.gridLayout_5.addWidget(self.PlayerNameInput, 1, 0, 1, 2)

        self.PlayerColorInput = QComboBox(self.scrollAreaWidgetContents_5)
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
        self.PlayerColorInput.setEditable(True)

        self.gridLayout_5.addWidget(self.PlayerColorInput, 8, 0, 1, 2)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_2.addWidget(self.scrollArea_5, 0, 1, 1, 1)

        self.GameContentStackedWidget.addWidget(self.ProfilePage)
        self.GameSettingsPage = QWidget()
        self.GameSettingsPage.setObjectName(u"GameSettingsPage")
        self.gridLayout_14 = QGridLayout(self.GameSettingsPage)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.scrollArea_6 = QScrollArea(self.GameSettingsPage)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 592, 447))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.GameRendererSetting = QComboBox(self.groupBox_6)
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.addItem("")
        self.GameRendererSetting.setObjectName(u"GameRendererSetting")

        self.horizontalLayout_4.addWidget(self.GameRendererSetting)

        self.GameFullscreenSetting = QComboBox(self.groupBox_6)
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.addItem("")
        self.GameFullscreenSetting.setObjectName(u"GameFullscreenSetting")

        self.horizontalLayout_4.addWidget(self.GameFullscreenSetting)


        self.gridLayout_13.addWidget(self.groupBox_6, 2, 2, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_5, 10, 2, 1, 3)

        self.GameArgsLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.GameArgsLabel.setObjectName(u"GameArgsLabel")

        self.gridLayout_13.addWidget(self.GameArgsLabel, 8, 2, 1, 1)

        self.GameArgsInput = QLineEdit(self.scrollAreaWidgetContents_6)
        self.GameArgsInput.setObjectName(u"GameArgsInput")

        self.gridLayout_13.addWidget(self.GameArgsInput, 9, 2, 1, 3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_20 = QGridLayout(self.groupBox_4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.GameExecFilePathBrowse = QPushButton(self.groupBox_4)
        self.GameExecFilePathBrowse.setObjectName(u"GameExecFilePathBrowse")
        self.GameExecFilePathBrowse.setMinimumSize(QSize(0, 28))
        icon8 = QIcon()
        icon8.addFile(u":/assets/img/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameExecFilePathBrowse.setIcon(icon8)

        self.gridLayout_20.addWidget(self.GameExecFilePathBrowse, 0, 2, 1, 1)

        self.GameExecFilePathInput = QLineEdit(self.groupBox_4)
        self.GameExecFilePathInput.setObjectName(u"GameExecFilePathInput")

        self.gridLayout_20.addWidget(self.GameExecFilePathInput, 0, 0, 1, 2)

        self.FlatpakRadiobutton = QRadioButton(self.groupBox_4)
        self.FlatpakRadiobutton.setObjectName(u"FlatpakRadiobutton")
        self.FlatpakRadiobutton.setEnabled(False)

        self.gridLayout_20.addWidget(self.FlatpakRadiobutton, 3, 2, 1, 1)

        self.NativeRadiobutton = QRadioButton(self.groupBox_4)
        self.NativeRadiobutton.setObjectName(u"NativeRadiobutton")
        self.NativeRadiobutton.setChecked(True)

        self.gridLayout_20.addWidget(self.NativeRadiobutton, 3, 0, 1, 1)

        self.WineRadiobutton = QRadioButton(self.groupBox_4)
        self.WineRadiobutton.setObjectName(u"WineRadiobutton")
        self.WineRadiobutton.setEnabled(False)

        self.gridLayout_20.addWidget(self.WineRadiobutton, 3, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_4, 6, 2, 1, 3)

        self.ExportClientScriptButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.ExportClientScriptButton.setObjectName(u"ExportClientScriptButton")
        icon9 = QIcon()
        icon9.addFile(u":/assets/img/icons/document-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ExportClientScriptButton.setIcon(icon9)

        self.gridLayout_13.addWidget(self.ExportClientScriptButton, 11, 2, 1, 3)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GameMusicSetting = QComboBox(self.groupBox_7)
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.addItem("")
        self.GameMusicSetting.setObjectName(u"GameMusicSetting")

        self.horizontalLayout_3.addWidget(self.GameMusicSetting)

        self.GameSoundSetting = QComboBox(self.groupBox_7)
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.addItem("")
        self.GameSoundSetting.setObjectName(u"GameSoundSetting")

        self.horizontalLayout_3.addWidget(self.GameSoundSetting)


        self.gridLayout_13.addWidget(self.groupBox_7, 3, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.GameHorizontalResolutionInput = QLineEdit(self.groupBox_5)
        self.GameHorizontalResolutionInput.setObjectName(u"GameHorizontalResolutionInput")
        self.GameHorizontalResolutionInput.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.GameHorizontalResolutionInput)

        self.GameResMultLabel = QLabel(self.groupBox_5)
        self.GameResMultLabel.setObjectName(u"GameResMultLabel")
        self.GameResMultLabel.setStyleSheet(u"padding: 0;\n"
"font-size: 12pt;")

        self.horizontalLayout_5.addWidget(self.GameResMultLabel)

        self.GameVerticalResolutionInput = QLineEdit(self.groupBox_5)
        self.GameVerticalResolutionInput.setObjectName(u"GameVerticalResolutionInput")

        self.horizontalLayout_5.addWidget(self.GameVerticalResolutionInput)


        self.gridLayout_13.addWidget(self.groupBox_5, 1, 2, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_14.addWidget(self.scrollArea_6, 0, 0, 1, 1)

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
        self.gridLayout_15 = QGridLayout(self.widget_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.GameSettingsTabWidget = QTabWidget(self.widget_3)
        self.GameSettingsTabWidget.setObjectName(u"GameSettingsTabWidget")
        self.AddonsLoaderTab = QWidget()
        self.AddonsLoaderTab.setObjectName(u"AddonsLoaderTab")
        self.gridLayout_9 = QGridLayout(self.AddonsLoaderTab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.GameFilesAddButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesAddButton.setObjectName(u"GameFilesAddButton")
        self.GameFilesAddButton.setMinimumSize(QSize(0, 28))
        self.GameFilesAddButton.setIcon(icon7)

        self.gridLayout_9.addWidget(self.GameFilesAddButton, 10, 6, 1, 1)

        self.GameFilesExecScrBrowseButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesExecScrBrowseButton.setObjectName(u"GameFilesExecScrBrowseButton")
        self.GameFilesExecScrBrowseButton.setMinimumSize(QSize(0, 28))
        self.GameFilesExecScrBrowseButton.setIcon(icon8)

        self.gridLayout_9.addWidget(self.GameFilesExecScrBrowseButton, 10, 4, 1, 1)

        self.GameFilesDownButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesDownButton.setObjectName(u"GameFilesDownButton")
        sizePolicy5.setHeightForWidth(self.GameFilesDownButton.sizePolicy().hasHeightForWidth())
        self.GameFilesDownButton.setSizePolicy(sizePolicy5)
        icon10 = QIcon()
        icon10.addFile(u":/assets/img/icons/go-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDownButton.setIcon(icon10)

        self.gridLayout_9.addWidget(self.GameFilesDownButton, 8, 8, 1, 1)

        self.GameFilesClearButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesClearButton.setObjectName(u"GameFilesClearButton")
        self.GameFilesClearButton.setMinimumSize(QSize(0, 28))
        icon11 = QIcon()
        icon11.addFile(u":/assets/img/icons/edit-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesClearButton.setIcon(icon11)

        self.gridLayout_9.addWidget(self.GameFilesClearButton, 1, 8, 1, 1)

        self.GameFilesDeleteButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesDeleteButton.setObjectName(u"GameFilesDeleteButton")
        self.GameFilesDeleteButton.setMinimumSize(QSize(0, 28))
        icon12 = QIcon()
        icon12.addFile(u":/assets/img/icons/list-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDeleteButton.setIcon(icon12)

        self.gridLayout_9.addWidget(self.GameFilesDeleteButton, 10, 7, 1, 1)

        self.GameFilesSaveButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesSaveButton.setObjectName(u"GameFilesSaveButton")
        self.GameFilesSaveButton.setMinimumSize(QSize(0, 28))
        self.GameFilesSaveButton.setStyleSheet(u"")
        self.GameFilesSaveButton.setIcon(icon9)

        self.gridLayout_9.addWidget(self.GameFilesSaveButton, 0, 8, 1, 1)

        self.GameFilesExecScriptInput = QLineEdit(self.AddonsLoaderTab)
        self.GameFilesExecScriptInput.setObjectName(u"GameFilesExecScriptInput")

        self.gridLayout_9.addWidget(self.GameFilesExecScriptInput, 10, 3, 1, 1)

        self.GameFilesList = QListWidget(self.AddonsLoaderTab)
        icon13 = QIcon()
        icon13.addFile(u":/assets/img/filetypes/wad.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem6 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem6.setIcon(icon13);
        icon14 = QIcon()
        icon14.addFile(u":/assets/img/filetypes/pk3.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem7 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem7.setIcon(icon14);
        icon15 = QIcon()
        icon15.addFile(u":/assets/img/filetypes/lua.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem8 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem8.setIcon(icon15);
        self.GameFilesList.setObjectName(u"GameFilesList")
        self.GameFilesList.setStyleSheet(u"")
        self.GameFilesList.setDragEnabled(True)
        self.GameFilesList.setDragDropOverwriteMode(False)
        self.GameFilesList.setDragDropMode(QAbstractItemView.DropOnly)
        self.GameFilesList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.GameFilesList.setIconSize(QSize(32, 32))
        self.GameFilesList.setMovement(QListView.Static)

        self.gridLayout_9.addWidget(self.GameFilesList, 0, 1, 9, 7)

        self.GameFilesUpButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesUpButton.setObjectName(u"GameFilesUpButton")
        sizePolicy5.setHeightForWidth(self.GameFilesUpButton.sizePolicy().hasHeightForWidth())
        self.GameFilesUpButton.setSizePolicy(sizePolicy5)
        icon16 = QIcon()
        icon16.addFile(u":/assets/img/icons/go-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesUpButton.setIcon(icon16)

        self.gridLayout_9.addWidget(self.GameFilesUpButton, 7, 8, 1, 1)

        self.GameFilesExecuteScriptLabel = QLabel(self.AddonsLoaderTab)
        self.GameFilesExecuteScriptLabel.setObjectName(u"GameFilesExecuteScriptLabel")

        self.gridLayout_9.addWidget(self.GameFilesExecuteScriptLabel, 10, 2, 1, 1)

        self.GameFilesLoadButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesLoadButton.setObjectName(u"GameFilesLoadButton")
        self.GameFilesLoadButton.setMinimumSize(QSize(0, 28))
        self.GameFilesLoadButton.setStyleSheet(u"")
        self.GameFilesLoadButton.setIcon(icon8)

        self.gridLayout_9.addWidget(self.GameFilesLoadButton, 2, 8, 1, 1)

        self.GameSettingsTabWidget.addTab(self.AddonsLoaderTab, "")
        self.ModBrowserTab = QWidget()
        self.ModBrowserTab.setObjectName(u"ModBrowserTab")
        self.gridLayout_12 = QGridLayout(self.ModBrowserTab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.splitter_2 = QSplitter(self.ModBrowserTab)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QGridLayout(self.groupBox)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ModTypeCombo = QComboBox(self.groupBox)
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.addItem("")
        self.ModTypeCombo.setObjectName(u"ModTypeCombo")

        self.gridLayout_17.addWidget(self.ModTypeCombo, 0, 2, 1, 1)

        self.ModsList = QListWidget(self.groupBox)
        self.ModsList.setObjectName(u"ModsList")
        sizePolicy.setHeightForWidth(self.ModsList.sizePolicy().hasHeightForWidth())
        self.ModsList.setSizePolicy(sizePolicy)

        self.gridLayout_17.addWidget(self.ModsList, 1, 0, 1, 4)

        self.ModBrowserLabel = QLabel(self.groupBox)
        self.ModBrowserLabel.setObjectName(u"ModBrowserLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ModBrowserLabel.sizePolicy().hasHeightForWidth())
        self.ModBrowserLabel.setSizePolicy(sizePolicy6)

        self.gridLayout_17.addWidget(self.ModBrowserLabel, 0, 0, 1, 1)

        self.RefreshModsButton = QPushButton(self.groupBox)
        self.RefreshModsButton.setObjectName(u"RefreshModsButton")
        self.RefreshModsButton.setIcon(icon4)

        self.gridLayout_17.addWidget(self.RefreshModsButton, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(6, 0, 0, 0)
        self.DownloadModButton = QPushButton(self.groupBox_2)
        self.DownloadModButton.setObjectName(u"DownloadModButton")
        self.DownloadModButton.setEnabled(False)
        icon17 = QIcon()
        icon17.addFile(u":/assets/img/icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DownloadModButton.setIcon(icon17)

        self.gridLayout_4.addWidget(self.DownloadModButton, 2, 1, 1, 1)

        self.OpenPageButton = QPushButton(self.groupBox_2)
        self.OpenPageButton.setObjectName(u"OpenPageButton")
        self.OpenPageButton.setEnabled(False)
        self.OpenPageButton.setIcon(icon5)

        self.gridLayout_4.addWidget(self.OpenPageButton, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.ModBrowser, 1, 0, 1, 3)

        self.ModViewerLabel = QLabel(self.groupBox_2)
        self.ModViewerLabel.setObjectName(u"ModViewerLabel")
        sizePolicy6.setHeightForWidth(self.ModViewerLabel.sizePolicy().hasHeightForWidth())
        self.ModViewerLabel.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.ModViewerLabel, 0, 0, 1, 3)

        self.splitter_2.addWidget(self.groupBox_2)

        self.gridLayout_12.addWidget(self.splitter_2, 0, 0, 1, 5)

        self.ModStatusLabel = QLabel(self.ModBrowserTab)
        self.ModStatusLabel.setObjectName(u"ModStatusLabel")

        self.gridLayout_12.addWidget(self.ModStatusLabel, 2, 0, 1, 5)

        self.GameSettingsTabWidget.addTab(self.ModBrowserTab, "")

        self.gridLayout_15.addWidget(self.GameSettingsTabWidget, 0, 0, 1, 1)


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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 595, 647))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PointLimitLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.PointLimitLabel.setObjectName(u"PointLimitLabel")

        self.gridLayout.addWidget(self.PointLimitLabel, 13, 0, 1, 2)

        self.AdvanceMapLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.AdvanceMapLabel.setObjectName(u"AdvanceMapLabel")

        self.gridLayout.addWidget(self.AdvanceMapLabel, 11, 0, 1, 2)

        self.HostMSCombobox = QComboBox(self.scrollAreaWidgetContents_4)
        self.HostMSCombobox.addItem("")
        self.HostMSCombobox.setObjectName(u"HostMSCombobox")
        self.HostMSCombobox.setEnabled(True)
        self.HostMSCombobox.setEditable(True)

        self.gridLayout.addWidget(self.HostMSCombobox, 7, 1, 1, 1)

        self.AdminPasswordInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.AdminPasswordInput.setObjectName(u"AdminPasswordInput")
        self.AdminPasswordInput.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.AdminPasswordInput, 3, 0, 2, 2)

        self.TimeLimitLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.TimeLimitLabel.setObjectName(u"TimeLimitLabel")

        self.gridLayout.addWidget(self.TimeLimitLabel, 15, 0, 1, 2)

        self.TimeLimitInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.TimeLimitInput.setObjectName(u"TimeLimitInput")

        self.gridLayout.addWidget(self.TimeLimitInput, 16, 0, 1, 2)

        self.MaxPlayersInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.MaxPlayersInput.setObjectName(u"MaxPlayersInput")

        self.gridLayout.addWidget(self.MaxPlayersInput, 18, 0, 1, 2)

        self.DedicatedServerToggle = QCheckBox(self.scrollAreaWidgetContents_4)
        self.DedicatedServerToggle.setObjectName(u"DedicatedServerToggle")
        self.DedicatedServerToggle.setStyleSheet(u"")
        self.DedicatedServerToggle.setChecked(False)

        self.gridLayout.addWidget(self.DedicatedServerToggle, 24, 0, 1, 1)

        self.PointLimitInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.PointLimitInput.setObjectName(u"PointLimitInput")

        self.gridLayout.addWidget(self.PointLimitInput, 14, 0, 1, 2)

        self.PortLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.PortLabel.setObjectName(u"PortLabel")

        self.gridLayout.addWidget(self.PortLabel, 21, 0, 1, 1)

        self.ServerNameInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.ServerNameInput.setObjectName(u"ServerNameInput")

        self.gridLayout.addWidget(self.ServerNameInput, 1, 0, 1, 2)

        self.SuddenDeathToggle = QCheckBox(self.scrollAreaWidgetContents_4)
        self.SuddenDeathToggle.setObjectName(u"SuddenDeathToggle")
        self.SuddenDeathToggle.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.SuddenDeathToggle, 23, 1, 1, 1)

        self.AdvanceMapInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.setObjectName(u"AdvanceMapInput")

        self.gridLayout.addWidget(self.AdvanceMapInput, 12, 0, 1, 2)

        self.ExportServerScriptButton = QPushButton(self.scrollAreaWidgetContents_4)
        self.ExportServerScriptButton.setObjectName(u"ExportServerScriptButton")
        self.ExportServerScriptButton.setIcon(icon9)

        self.gridLayout.addWidget(self.ExportServerScriptButton, 26, 0, 1, 2)

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

        self.gridLayout.addWidget(self.GametypeInput, 10, 0, 1, 2)

        self.MaxPlayersLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.MaxPlayersLabel.setObjectName(u"MaxPlayersLabel")

        self.gridLayout.addWidget(self.MaxPlayersLabel, 17, 0, 1, 2)

        self.UploadToggle = QCheckBox(self.scrollAreaWidgetContents_4)
        self.UploadToggle.setObjectName(u"UploadToggle")
        self.UploadToggle.setChecked(True)

        self.gridLayout.addWidget(self.UploadToggle, 24, 1, 1, 1)

        self.DisableWeaponsToggle = QCheckBox(self.scrollAreaWidgetContents_4)
        self.DisableWeaponsToggle.setObjectName(u"DisableWeaponsToggle")
        self.DisableWeaponsToggle.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.DisableWeaponsToggle, 23, 0, 1, 1)

        self.ServerNameLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ServerNameLabel.setObjectName(u"ServerNameLabel")

        self.gridLayout.addWidget(self.ServerNameLabel, 0, 0, 1, 2)

        self.PortInput = QLineEdit(self.scrollAreaWidgetContents_4)
        self.PortInput.setObjectName(u"PortInput")

        self.gridLayout.addWidget(self.PortInput, 22, 0, 1, 2)

        self.RoomInput = QComboBox(self.scrollAreaWidgetContents_4)
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.addItem("")
        self.RoomInput.setObjectName(u"RoomInput")
        self.RoomInput.setEditable(False)

        self.gridLayout.addWidget(self.RoomInput, 7, 0, 1, 1)

        self.RoomLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.RoomLabel.setObjectName(u"RoomLabel")

        self.gridLayout.addWidget(self.RoomLabel, 6, 0, 1, 1)

        self.AdminPasswordLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.AdminPasswordLabel.setObjectName(u"AdminPasswordLabel")

        self.gridLayout.addWidget(self.AdminPasswordLabel, 2, 0, 1, 2)

        self.GametypeLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.GametypeLabel.setObjectName(u"GametypeLabel")

        self.gridLayout.addWidget(self.GametypeLabel, 8, 0, 1, 2)

        self.HostMSLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.HostMSLabel.setObjectName(u"HostMSLabel")

        self.gridLayout.addWidget(self.HostMSLabel, 6, 1, 1, 1)

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

        self.gridLayout.addWidget(self.ForceSkinInput, 20, 0, 1, 2)

        self.ForceSkinLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ForceSkinLabel.setObjectName(u"ForceSkinLabel")

        self.gridLayout.addWidget(self.ForceSkinLabel, 19, 0, 1, 2)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 25, 0, 1, 2)

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
        self.GameTabView.setTabShape(QTabWidget.Rounded)
        self.BrowseTab = QWidget()
        self.BrowseTab.setObjectName(u"BrowseTab")
        self.gridLayout_18 = QGridLayout(self.BrowseTab)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MSStatusLabel = QLabel(self.BrowseTab)
        self.MSStatusLabel.setObjectName(u"MSStatusLabel")

        self.horizontalLayout_18.addWidget(self.MSStatusLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.SaveNetgameButton = QPushButton(self.BrowseTab)
        self.SaveNetgameButton.setObjectName(u"SaveNetgameButton")
        icon18 = QIcon()
        icon18.addFile(u":/assets/img/icons/bookmark-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveNetgameButton.setIcon(icon18)

        self.horizontalLayout_18.addWidget(self.SaveNetgameButton)

        self.BrowseNetgameJoinButton = QPushButton(self.BrowseTab)
        self.BrowseNetgameJoinButton.setObjectName(u"BrowseNetgameJoinButton")
        icon19 = QIcon()
        icon19.addFile(u":/assets/img/icons/media-playback-start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowseNetgameJoinButton.setIcon(icon19)

        self.horizontalLayout_18.addWidget(self.BrowseNetgameJoinButton)


        self.gridLayout_18.addLayout(self.horizontalLayout_18, 5, 0, 1, 4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.RefreshButton = QPushButton(self.BrowseTab)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setIcon(icon4)

        self.gridLayout_18.addWidget(self.RefreshButton, 0, 3, 1, 1)

        self.MSSelectionLabel = QLabel(self.BrowseTab)
        self.MSSelectionLabel.setObjectName(u"MSSelectionLabel")

        self.gridLayout_18.addWidget(self.MSSelectionLabel, 0, 0, 1, 1)

        self.BrowseMSCombobox = QComboBox(self.BrowseTab)
        self.BrowseMSCombobox.addItem("")
        self.BrowseMSCombobox.setObjectName(u"BrowseMSCombobox")
        sizePolicy5.setHeightForWidth(self.BrowseMSCombobox.sizePolicy().hasHeightForWidth())
        self.BrowseMSCombobox.setSizePolicy(sizePolicy5)
        self.BrowseMSCombobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_18.addWidget(self.BrowseMSCombobox, 0, 2, 1, 1)

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
        sizePolicy4.setHeightForWidth(self.BrowseNetgameTable.sizePolicy().hasHeightForWidth())
        self.BrowseNetgameTable.setSizePolicy(sizePolicy4)
        self.BrowseNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.BrowseNetgameTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.BrowseNetgameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.BrowseNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.BrowseNetgameTable.verticalHeader().setVisible(False)

        self.gridLayout_18.addWidget(self.BrowseNetgameTable, 4, 0, 1, 4)

        self.GameTabView.addTab(self.BrowseTab, "")
        self.SavedNetgamesTab = QWidget()
        self.SavedNetgamesTab.setObjectName(u"SavedNetgamesTab")
        self.gridLayout_10 = QGridLayout(self.SavedNetgamesTab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.JoinBookmarkButton = QPushButton(self.SavedNetgamesTab)
        self.JoinBookmarkButton.setObjectName(u"JoinBookmarkButton")
        self.JoinBookmarkButton.setSizeIncrement(QSize(0, 0))
        self.JoinBookmarkButton.setIcon(icon19)

        self.gridLayout_10.addWidget(self.JoinBookmarkButton, 8, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_10, 8, 0, 1, 1)

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
        sizePolicy4.setHeightForWidth(self.SavedNetgameTable.sizePolicy().hasHeightForWidth())
        self.SavedNetgameTable.setSizePolicy(sizePolicy4)
        self.SavedNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.SavedNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.SavedNetgameTable.verticalHeader().setVisible(False)
        self.SavedNetgameTable.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_10.addWidget(self.SavedNetgameTable, 4, 0, 1, 4)

        self.ServerListLabel = QLabel(self.SavedNetgamesTab)
        self.ServerListLabel.setObjectName(u"ServerListLabel")

        self.gridLayout_10.addWidget(self.ServerListLabel, 3, 0, 1, 1)

        self.JoinServerLabel = QLabel(self.SavedNetgamesTab)
        self.JoinServerLabel.setObjectName(u"JoinServerLabel")

        self.gridLayout_10.addWidget(self.JoinServerLabel, 0, 0, 1, 1)

        self.JoinAddressInput = QLineEdit(self.SavedNetgamesTab)
        self.JoinAddressInput.setObjectName(u"JoinAddressInput")
        sizePolicy5.setHeightForWidth(self.JoinAddressInput.sizePolicy().hasHeightForWidth())
        self.JoinAddressInput.setSizePolicy(sizePolicy5)
        self.JoinAddressInput.setPlaceholderText(u"IP Address")

        self.gridLayout_10.addWidget(self.JoinAddressInput, 1, 0, 1, 2)

        self.JoinAddressButton = QPushButton(self.SavedNetgamesTab)
        self.JoinAddressButton.setObjectName(u"JoinAddressButton")
        self.JoinAddressButton.setIcon(icon19)

        self.gridLayout_10.addWidget(self.JoinAddressButton, 1, 2, 1, 2)

        self.DeleteServerButton = QPushButton(self.SavedNetgamesTab)
        self.DeleteServerButton.setObjectName(u"DeleteServerButton")
        self.DeleteServerButton.setIcon(icon12)

        self.gridLayout_10.addWidget(self.DeleteServerButton, 8, 3, 1, 1)

        self.AddServerButton = QPushButton(self.SavedNetgamesTab)
        self.AddServerButton.setObjectName(u"AddServerButton")
        self.AddServerButton.setIcon(icon7)

        self.gridLayout_10.addWidget(self.AddServerButton, 8, 2, 1, 1)

        self.frame_10 = QFrame(self.SavedNetgamesTab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_10.addWidget(self.frame_10, 2, 0, 1, 4)

        self.GameTabView.addTab(self.SavedNetgamesTab, "")
        self.masterservers = QWidget()
        self.masterservers.setObjectName(u"masterservers")
        self.masterservers.setMinimumSize(QSize(824, 0))
        self.verticalLayout_30 = QVBoxLayout(self.masterservers)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.scrollArea_7 = QScrollArea(self.masterservers)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 806, 384))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_3, 8, 5, 1, 1)

        self.MSRemoveButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.MSRemoveButton.setObjectName(u"MSRemoveButton")
        self.MSRemoveButton.setIcon(icon12)

        self.gridLayout_19.addWidget(self.MSRemoveButton, 13, 4, 1, 1)

        self.MSListSaveButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.MSListSaveButton.setObjectName(u"MSListSaveButton")
        self.MSListSaveButton.setIcon(icon9)

        self.gridLayout_19.addWidget(self.MSListSaveButton, 13, 2, 1, 1)

        self.MSAddButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.MSAddButton.setObjectName(u"MSAddButton")
        self.MSAddButton.setIcon(icon7)

        self.gridLayout_19.addWidget(self.MSAddButton, 13, 3, 1, 1)

        self.MSVisitrepoButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.MSVisitrepoButton.setObjectName(u"MSVisitrepoButton")
        self.MSVisitrepoButton.setIcon(icon5)

        self.gridLayout_19.addWidget(self.MSVisitrepoButton, 4, 5, 1, 1)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font2 = QFont()
        font2.setBold(False)
        self.groupBox_3.setFont(font2)
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.snitchdescLabel = QLabel(self.groupBox_3)
        self.snitchdescLabel.setObjectName(u"snitchdescLabel")
        self.snitchdescLabel.setFont(font2)

        self.gridLayout_6.addWidget(self.snitchdescLabel, 2, 1, 1, 1)

        self.v1descLabel = QLabel(self.groupBox_3)
        self.v1descLabel.setObjectName(u"v1descLabel")
        self.v1descLabel.setFont(font2)

        self.gridLayout_6.addWidget(self.v1descLabel, 0, 1, 1, 1)

        self.msapiwarningLabel = QLabel(self.groupBox_3)
        self.msapiwarningLabel.setObjectName(u"msapiwarningLabel")
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        self.msapiwarningLabel.setFont(font3)
        self.msapiwarningLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.msapiwarningLabel, 3, 0, 1, 3)

        self.kartv2titleLabel = QLabel(self.groupBox_3)
        self.kartv2titleLabel.setObjectName(u"kartv2titleLabel")
        font4 = QFont()
        font4.setBold(True)
        self.kartv2titleLabel.setFont(font4)

        self.gridLayout_6.addWidget(self.kartv2titleLabel, 1, 0, 1, 1)

        self.kartv2descLabel = QLabel(self.groupBox_3)
        self.kartv2descLabel.setObjectName(u"kartv2descLabel")
        self.kartv2descLabel.setFont(font2)

        self.gridLayout_6.addWidget(self.kartv2descLabel, 1, 1, 1, 1)

        self.snitchtitleLabel = QLabel(self.groupBox_3)
        self.snitchtitleLabel.setObjectName(u"snitchtitleLabel")
        self.snitchtitleLabel.setFont(font4)

        self.gridLayout_6.addWidget(self.snitchtitleLabel, 2, 0, 1, 1)

        self.v1titleLabel = QLabel(self.groupBox_3)
        self.v1titleLabel.setObjectName(u"v1titleLabel")
        self.v1titleLabel.setFont(font4)

        self.gridLayout_6.addWidget(self.v1titleLabel, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_3, 5, 5, 1, 1)

        self.ConfigrepoadLabel = QLabel(self.scrollAreaWidgetContents_7)
        self.ConfigrepoadLabel.setObjectName(u"ConfigrepoadLabel")

        self.gridLayout_19.addWidget(self.ConfigrepoadLabel, 3, 5, 1, 1)

        self.MasterServersTable = QTableWidget(self.scrollAreaWidgetContents_7)
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
        sizePolicy4.setHeightForWidth(self.MasterServersTable.sizePolicy().hasHeightForWidth())
        self.MasterServersTable.setSizePolicy(sizePolicy4)
        self.MasterServersTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.MasterServersTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.MasterServersTable.verticalHeader().setVisible(False)

        self.gridLayout_19.addWidget(self.MasterServersTable, 3, 0, 9, 5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_9, 13, 1, 1, 1)

        self.MSTableLabel = QLabel(self.scrollAreaWidgetContents_7)
        self.MSTableLabel.setObjectName(u"MSTableLabel")

        self.gridLayout_19.addWidget(self.MSTableLabel, 2, 0, 1, 2)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_30.addWidget(self.scrollArea_7)

        self.GameTabView.addTab(self.masterservers, "")

        self.verticalLayout_13.addWidget(self.GameTabView)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_3)

        self.GameContentStackedWidget.addWidget(self.JoinGamePage)

        self.verticalLayout_4.addWidget(self.GameContentStackedWidget)

        self.splitter.addWidget(self.GamePageContentFrame)

        self.gridLayout_16.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.GamePageFrame)

        self.GamePlayFrame = QFrame(self.GamePage)
        self.GamePlayFrame.setObjectName(u"GamePlayFrame")
        self.GamePlayFrame.setMinimumSize(QSize(0, 56))
        self.GamePlayFrame.setMaximumSize(QSize(16777215, 56))
        self.GamePlayFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePlayFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.GamePlayFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 9, 2, 1)

        self.GameProfileComboBox = QComboBox(self.GamePlayFrame)
        self.GameProfileComboBox.addItem("")
        self.GameProfileComboBox.setObjectName(u"GameProfileComboBox")
        sizePolicy6.setHeightForWidth(self.GameProfileComboBox.sizePolicy().hasHeightForWidth())
        self.GameProfileComboBox.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.GameProfileComboBox, 1, 0, 1, 7)

        self.ProfilesRefreshButton = QToolButton(self.GamePlayFrame)
        self.ProfilesRefreshButton.setObjectName(u"ProfilesRefreshButton")
        self.ProfilesRefreshButton.setIcon(icon4)

        self.gridLayout_3.addWidget(self.ProfilesRefreshButton, 2, 0, 1, 1)

        self.ProfilesDeleteButton = QToolButton(self.GamePlayFrame)
        self.ProfilesDeleteButton.setObjectName(u"ProfilesDeleteButton")
        self.ProfilesDeleteButton.setEnabled(False)
        self.ProfilesDeleteButton.setIcon(icon12)

        self.gridLayout_3.addWidget(self.ProfilesDeleteButton, 2, 6, 1, 1)

        self.ProfilesAddButton = QToolButton(self.GamePlayFrame)
        self.ProfilesAddButton.setObjectName(u"ProfilesAddButton")
        self.ProfilesAddButton.setIcon(icon7)

        self.gridLayout_3.addWidget(self.ProfilesAddButton, 2, 5, 1, 1)

        self.GamePlayButton = QPushButton(self.GamePlayFrame)
        self.GamePlayButton.setObjectName(u"GamePlayButton")
        sizePolicy.setHeightForWidth(self.GamePlayButton.sizePolicy().hasHeightForWidth())
        self.GamePlayButton.setSizePolicy(sizePolicy)
        self.GamePlayButton.setMaximumSize(QSize(240, 38))
        self.GamePlayButton.setIcon(icon19)

        self.gridLayout_3.addWidget(self.GamePlayButton, 1, 10, 2, 1)

        self.ProfilesSaveButton = QToolButton(self.GamePlayFrame)
        self.ProfilesSaveButton.setObjectName(u"ProfilesSaveButton")
        self.ProfilesSaveButton.setIcon(icon9)

        self.gridLayout_3.addWidget(self.ProfilesSaveButton, 2, 1, 1, 1)

        self.ProfilesStatusLabel = QLabel(self.GamePlayFrame)
        self.ProfilesStatusLabel.setObjectName(u"ProfilesStatusLabel")

        self.gridLayout_3.addWidget(self.ProfilesStatusLabel, 2, 2, 1, 3)


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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 848, 539))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 848, 539))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget_2 = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_11 = QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.SaveFilesToConfigToggle = QCheckBox(self.tab_5)
        self.SaveFilesToConfigToggle.setObjectName(u"SaveFilesToConfigToggle")
        self.SaveFilesToConfigToggle.setChecked(False)

        self.gridLayout_11.addWidget(self.SaveFilesToConfigToggle, 2, 0, 1, 1)

        self.ProfileDirInput = QLineEdit(self.tab_5)
        self.ProfileDirInput.setObjectName(u"ProfileDirInput")

        self.gridLayout_11.addWidget(self.ProfileDirInput, 1, 0, 1, 1)

        self.ProfileDirBrowseButton = QPushButton(self.tab_5)
        self.ProfileDirBrowseButton.setObjectName(u"ProfileDirBrowseButton")
        self.ProfileDirBrowseButton.setIcon(icon8)

        self.gridLayout_11.addWidget(self.ProfileDirBrowseButton, 1, 2, 1, 1)

        self.ProfileDirLabel = QLabel(self.tab_5)
        self.ProfileDirLabel.setObjectName(u"ProfileDirLabel")

        self.gridLayout_11.addWidget(self.ProfileDirLabel, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer, 3, 0, 1, 1)

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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy7)

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.ModsourceCheckLabel = QLabel(self.tab_6)
        self.ModsourceCheckLabel.setObjectName(u"ModsourceCheckLabel")

        self.verticalLayout_6.addWidget(self.ModsourceCheckLabel)

        self.ModsourceMBCheckbox = QCheckBox(self.tab_6)
        self.ModsourceMBCheckbox.setObjectName(u"ModsourceMBCheckbox")
        self.ModsourceMBCheckbox.setIcon(icon6)
        self.ModsourceMBCheckbox.setChecked(True)

        self.verticalLayout_6.addWidget(self.ModsourceMBCheckbox)

        self.ModsourceGamebananaCheckbox = QCheckBox(self.tab_6)
        self.ModsourceGamebananaCheckbox.setObjectName(u"ModsourceGamebananaCheckbox")
        self.ModsourceGamebananaCheckbox.setEnabled(True)
        icon20 = QIcon()
        icon20.addFile(u":/assets/img/icons/gamebanana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceGamebananaCheckbox.setIcon(icon20)

        self.verticalLayout_6.addWidget(self.ModsourceGamebananaCheckbox)

        self.ModsourceSkybaseCheckbox = QCheckBox(self.tab_6)
        self.ModsourceSkybaseCheckbox.setObjectName(u"ModsourceSkybaseCheckbox")
        self.ModsourceSkybaseCheckbox.setEnabled(True)
        icon21 = QIcon()
        icon21.addFile(u":/assets/img/icons/skybase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceSkybaseCheckbox.setIcon(icon21)

        self.verticalLayout_6.addWidget(self.ModsourceSkybaseCheckbox)

        self.ModsourceWadarchiveCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWadarchiveCheckbox.setObjectName(u"ModsourceWadarchiveCheckbox")
        self.ModsourceWadarchiveCheckbox.setEnabled(False)

        self.verticalLayout_6.addWidget(self.ModsourceWadarchiveCheckbox)

        self.ModsourceWSBlueCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSBlueCheckbox.setObjectName(u"ModsourceWSBlueCheckbox")
        icon22 = QIcon()
        icon22.addFile(u":/assets/img/icons/wsblue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceWSBlueCheckbox.setIcon(icon22)

        self.verticalLayout_6.addWidget(self.ModsourceWSBlueCheckbox)

        self.ModsourceWSRedCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSRedCheckbox.setObjectName(u"ModsourceWSRedCheckbox")
        icon23 = QIcon()
        icon23.addFile(u":/assets/img/icons/wsred.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceWSRedCheckbox.setIcon(icon23)

        self.verticalLayout_6.addWidget(self.ModsourceWSRedCheckbox)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_8 = QGridLayout(self.tab_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.RSSRemoveButton = QPushButton(self.tab_9)
        self.RSSRemoveButton.setObjectName(u"RSSRemoveButton")
        self.RSSRemoveButton.setEnabled(False)
        self.RSSRemoveButton.setIcon(icon12)

        self.gridLayout_8.addWidget(self.RSSRemoveButton, 4, 2, 1, 1)

        self.RSSMoveupButton = QPushButton(self.tab_9)
        self.RSSMoveupButton.setObjectName(u"RSSMoveupButton")
        self.RSSMoveupButton.setEnabled(False)
        self.RSSMoveupButton.setIcon(icon16)

        self.gridLayout_8.addWidget(self.RSSMoveupButton, 3, 0, 1, 1)

        self.NewssourceLabel = QLabel(self.tab_9)
        self.NewssourceLabel.setObjectName(u"NewssourceLabel")

        self.gridLayout_8.addWidget(self.NewssourceLabel, 0, 0, 1, 3)

        self.RSSAddButton = QPushButton(self.tab_9)
        self.RSSAddButton.setObjectName(u"RSSAddButton")
        self.RSSAddButton.setIcon(icon7)

        self.gridLayout_8.addWidget(self.RSSAddButton, 3, 2, 1, 1)

        self.RSSMovedownButton = QPushButton(self.tab_9)
        self.RSSMovedownButton.setObjectName(u"RSSMovedownButton")
        self.RSSMovedownButton.setEnabled(False)
        self.RSSMovedownButton.setIcon(icon10)

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


        self.verticalLayout.addWidget(self.MainAreaFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTabsStackedWidget.setCurrentIndex(1)
        self.GameContentStackedWidget.setCurrentIndex(1)
        self.PlayerSkinInput.setCurrentIndex(0)
        self.PlayerColorInput.setCurrentIndex(0)
        self.GameSettingsTabWidget.setCurrentIndex(0)
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
        self.RSSFeedCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"http://srb2.org/feed", None))

        self.RSSFeedLabel.setText(QCoreApplication.translate("MainWindow", u"Newsfeed URL", None))
        self.RSSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Please select a feed and click \"Refresh\"", None))

        __sortingEnabled = self.RSSArticleList.isSortingEnabled()
        self.RSSArticleList.setSortingEnabled(False)
        ___qlistwidgetitem = self.RSSArticleList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"No articles. Pleas click \"Refresh\" to load some.", None));
        self.RSSArticleList.setSortingEnabled(__sortingEnabled)

        self.RSSRefreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.RSSViewonlineButton.setText(QCoreApplication.translate("MainWindow", u"View online", None))

        __sortingEnabled1 = self.GamePageTabList.isSortingEnabled()
        self.GamePageTabList.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.GamePageTabList.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Player Settings", None));
        ___qlistwidgetitem2 = self.GamePageTabList.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Game Settings", None));
        ___qlistwidgetitem3 = self.GamePageTabList.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Mods", None));
        ___qlistwidgetitem4 = self.GamePageTabList.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Host Netgame", None));
        ___qlistwidgetitem5 = self.GamePageTabList.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Join Netgame", None));
        self.GamePageTabList.setSortingEnabled(__sortingEnabled1)

        self.PlayerSkinImage.setText("")
        self.PlayerColorTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Skin Color", None))
        self.PlayerNameTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.PlayerSkinTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Skin", None))
        self.PlayerSkinInfoText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dddd00;\">Sonic</span> is the fastest of the three, but also the hardest to control. Begginers beware, but experts will find Sonic very powerful.</p><p><span style=\" color:#dddd00;\">Ability:</span> Speed Thok<br/>Double jump to zoom forward with a huge burst of speed</p><p><span style=\" color:#dddd00;\">Tip:</span> Simply letting go of forward does not slow down in SRB2. To slow down, hold the opposite direction.</p></body></html>", None))
        self.PlayerSkinInput.setItemText(0, "")
        self.PlayerSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.PlayerSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.PlayerSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.PlayerSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.PlayerSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PlayerNameInput.setText("")
        self.PlayerNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerColorInput.setItemText(0, "")
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

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Render Options", None))
        self.GameRendererSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.GameRendererSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"OpenGL", None))

        self.GameFullscreenSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.GameFullscreenSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Borderless fullscreen", None))
        self.GameFullscreenSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Windowed", None))

        self.GameArgsLabel.setText(QCoreApplication.translate("MainWindow", u"Custom Shell Parameters", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Executable", None))
        self.GameExecFilePathBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.GameExecFilePathInput.setText(QCoreApplication.translate("MainWindow", u"srb2win.exe", None))
        self.FlatpakRadiobutton.setText(QCoreApplication.translate("MainWindow", u"Flatpak (Linux)", None))
        self.NativeRadiobutton.setText(QCoreApplication.translate("MainWindow", u"Native EXE/ELF", None))
        self.WineRadiobutton.setText(QCoreApplication.translate("MainWindow", u"WINE (Linux/macOS)", None))
        self.ExportClientScriptButton.setText(QCoreApplication.translate("MainWindow", u"Save Client Launch Script...", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Audio Options", None))
        self.GameMusicSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Digital music", None))
        self.GameMusicSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Midi music", None))
        self.GameMusicSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Load music from a CD", None))
        self.GameMusicSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"Disable music", None))

        self.GameSoundSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Enable sound", None))
        self.GameSoundSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Disable sound", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.GameHorizontalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
        self.GameResMultLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.GameVerticalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<auto>", None))
#if QT_CONFIG(tooltip)
        self.GameSettingsTabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"Add file...", None))
#endif // QT_CONFIG(tooltip)
        self.GameFilesAddButton.setText("")
        self.GameFilesExecScrBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse scripts...", None))
#if QT_CONFIG(tooltip)
        self.GameFilesDownButton.setToolTip(QCoreApplication.translate("MainWindow", u"Move down", None))
#endif // QT_CONFIG(tooltip)
        self.GameFilesDownButton.setText("")
        self.GameFilesClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
#if QT_CONFIG(tooltip)
        self.GameFilesDeleteButton.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected files", None))
#endif // QT_CONFIG(tooltip)
        self.GameFilesDeleteButton.setText("")
        self.GameFilesSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save list", None))

        __sortingEnabled2 = self.GameFilesList.isSortingEnabled()
        self.GameFilesList.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.GameFilesList.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"place.wad", None));
        ___qlistwidgetitem7 = self.GameFilesList.item(1)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"hold.pk3", None));
        ___qlistwidgetitem8 = self.GameFilesList.item(2)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"er.lua", None));
        self.GameFilesList.setSortingEnabled(__sortingEnabled2)

#if QT_CONFIG(tooltip)
        self.GameFilesUpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Move up", None))
#endif // QT_CONFIG(tooltip)
        self.GameFilesUpButton.setText("")
        self.GameFilesExecuteScriptLabel.setText(QCoreApplication.translate("MainWindow", u"Launch Script", None))
        self.GameFilesLoadButton.setText(QCoreApplication.translate("MainWindow", u"Load list...", None))
        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.AddonsLoaderTab), QCoreApplication.translate("MainWindow", u"Launch Mods", None))
        self.ModTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Maps", None))
        self.ModTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Characters", None))
        self.ModTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Lua", None))
        self.ModTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Assets", None))
        self.ModTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Misc", None))

        self.ModBrowserLabel.setText(QCoreApplication.translate("MainWindow", u"Mods", None))
#if QT_CONFIG(tooltip)
        self.RefreshModsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh Mods", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshModsButton.setText("")
        self.DownloadModButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.OpenPageButton.setText(QCoreApplication.translate("MainWindow", u"Visit Page", None))
        self.ModViewerLabel.setText(QCoreApplication.translate("MainWindow", u"Mod details", None))
        self.ModStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Refresh mods\" to see a list of available mods.", None))
        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.ModBrowserTab), QCoreApplication.translate("MainWindow", u"Browse online", None))
        self.PointLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Point Limit", None))
        self.AdvanceMapLabel.setText(QCoreApplication.translate("MainWindow", u"Map Advancement Policy", None))
        self.HostMSCombobox.setItemText(0, "")

        self.HostMSCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://mb.srb2.org/MS/0", None))
        self.TimeLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Time Limit", None))
        self.TimeLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Off by default", None))
        self.MaxPlayersInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"8", None))
        self.DedicatedServerToggle.setText(QCoreApplication.translate("MainWindow", u"Dedicated Server", None))
        self.PointLimitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.PortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.SuddenDeathToggle.setText(QCoreApplication.translate("MainWindow", u"Sudden Death", None))
        self.AdvanceMapInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.AdvanceMapInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Next", None))
        self.AdvanceMapInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Random", None))

        self.ExportServerScriptButton.setText(QCoreApplication.translate("MainWindow", u"Save server launch script...", None))
        self.GametypeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Co-op", None))
        self.GametypeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Competition", None))
        self.GametypeInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Race", None))
        self.GametypeInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Match", None))
        self.GametypeInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Team Match", None))
        self.GametypeInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Tag", None))
        self.GametypeInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Hide and Seek", None))
        self.GametypeInput.setItemText(7, QCoreApplication.translate("MainWindow", u"Capture the Flag", None))
        self.GametypeInput.setItemText(8, "")

        self.MaxPlayersLabel.setText(QCoreApplication.translate("MainWindow", u"Max. Players", None))
        self.UploadToggle.setText(QCoreApplication.translate("MainWindow", u"Enable Add-On downloads", None))
        self.DisableWeaponsToggle.setText(QCoreApplication.translate("MainWindow", u"Disable weapon rings", None))
        self.ServerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.PortInput.setInputMask("")
        self.PortInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5029", None))
        self.RoomInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Offline", None))
        self.RoomInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.RoomInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Casual", None))
        self.RoomInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Hugs", None))
        self.RoomInput.setItemText(4, QCoreApplication.translate("MainWindow", u"OLDC", None))

        self.RoomLabel.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.AdminPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Admin Password", None))
        self.GametypeLabel.setText(QCoreApplication.translate("MainWindow", u"Gametype", None))
        self.HostMSLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.ForceSkinInput.setItemText(0, "")
        self.ForceSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.ForceSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.ForceSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.ForceSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.ForceSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.ForceSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.ForceSkinLabel.setText(QCoreApplication.translate("MainWindow", u"Force Skin", None))
        self.MSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Update\" to download a list of servers.", None))
        self.SaveNetgameButton.setText(QCoreApplication.translate("MainWindow", u"Bookmark", None))
        self.BrowseNetgameJoinButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
#if QT_CONFIG(tooltip)
        self.RefreshButton.setToolTip(QCoreApplication.translate("MainWindow", u"Update", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshButton.setText("")
        self.MSSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.BrowseMSCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"ms.srb2.org", None))

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

        self.GameTabView.setTabText(self.GameTabView.indexOf(self.BrowseTab), QCoreApplication.translate("MainWindow", u"Browse", None))
        self.JoinBookmarkButton.setText(QCoreApplication.translate("MainWindow", u"Join Bookmark", None))
        ___qtablewidgetitem10 = self.SavedNetgameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.SavedNetgameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem12 = self.SavedNetgameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        self.ServerListLabel.setText(QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.JoinServerLabel.setText(QCoreApplication.translate("MainWindow", u"Join directly", None))
        self.JoinAddressButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
#if QT_CONFIG(tooltip)
        self.DeleteServerButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Bookmark", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.AddServerButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add Bookmark", None))
#endif // QT_CONFIG(tooltip)
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.SavedNetgamesTab), QCoreApplication.translate("MainWindow", u"Bookmarks", None))
#if QT_CONFIG(tooltip)
        self.MSRemoveButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove selected Master Server", None))
#endif // QT_CONFIG(tooltip)
        self.MSRemoveButton.setText("")
        self.MSListSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save List", None))
#if QT_CONFIG(tooltip)
        self.MSAddButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add Master Server", None))
#endif // QT_CONFIG(tooltip)
        self.MSAddButton.setText("")
        self.MSVisitrepoButton.setText(QCoreApplication.translate("MainWindow", u"Config repo >>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Valid APIs", None))
        self.snitchdescLabel.setText(QCoreApplication.translate("MainWindow", u"LiquidMS Snitch API", None))
        self.v1descLabel.setText(QCoreApplication.translate("MainWindow", u"Official SRB2 API", None))
        self.msapiwarningLabel.setText(QCoreApplication.translate("MainWindow", u"All other APIs will be ignored", None))
        self.kartv2titleLabel.setText(QCoreApplication.translate("MainWindow", u"kartv2", None))
        self.kartv2descLabel.setText(QCoreApplication.translate("MainWindow", u"SRB2Kart API", None))
        self.snitchtitleLabel.setText(QCoreApplication.translate("MainWindow", u"snitch", None))
        self.v1titleLabel.setText(QCoreApplication.translate("MainWindow", u"v1", None))
        self.ConfigrepoadLabel.setText(QCoreApplication.translate("MainWindow", u"Looking for master servers?", None))
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

        self.MSTableLabel.setText(QCoreApplication.translate("MainWindow", u"Master Servers", None))
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.masterservers), QCoreApplication.translate("MainWindow", u"Master Servers", None))
        self.GameProfileComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New profile...", None))

#if QT_CONFIG(tooltip)
        self.GameProfileComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Current Profile", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ProfilesRefreshButton.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh profiles", None))
#endif // QT_CONFIG(tooltip)
        self.ProfilesRefreshButton.setText("")
#if QT_CONFIG(tooltip)
        self.ProfilesDeleteButton.setToolTip(QCoreApplication.translate("MainWindow", u"Delete profile", None))
#endif // QT_CONFIG(tooltip)
        self.ProfilesDeleteButton.setText("")
#if QT_CONFIG(tooltip)
        self.ProfilesAddButton.setToolTip(QCoreApplication.translate("MainWindow", u"Create Profile", None))
#endif // QT_CONFIG(tooltip)
        self.ProfilesAddButton.setText("")
        self.GamePlayButton.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
#if QT_CONFIG(tooltip)
        self.ProfilesSaveButton.setToolTip(QCoreApplication.translate("MainWindow", u"Save current profile", None))
#endif // QT_CONFIG(tooltip)
        self.ProfilesSaveButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ProfilesStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Game profiles", None))
        self.AboutText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'CMU Serif Medium'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/assets/img/liquidlauncher.svg\" /><span style=\" font-size:16pt; font-weight:600;\"><br />LiquidLauncher</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">the other launcher for Sonic Robo Blast 2</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; fo"
                        "nt-size:12pt; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">built by Liquid</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://liquidunderground.github.io\"><span style=\" font-size:10pt; text-decoration: underline; color:#00ffff;\">Visit our Website</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://discord.gg/HVTzVfAWG6/\"><span style=\" font-size:10pt; text-decoration: underline; color:#00ffff;\">Join our Discord</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><b"
                        "r /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Contributors</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PixL<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">This Project is based on the following technologies:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style"
                        "=\" font-size:12pt; font-weight:600;\">Feedparser</span><span style=\" font-size:12pt;\"> by Kurt McKee and Mark Pilgrim</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LauncherBlast2 &quot;reBoot&quot;</span><span style=\" font-size:12pt;\"> by HitCoder</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LXML</span><span style=\" font-size:12pt;\">(libxml binding for Python)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PyInstaller</span><span style=\" font-size:12pt;\"> (distribution)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PySide6</span><span style=\" font-size:12pt;\"> by the Qt Project</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Python 3</span><span style=\" font-family:'Atkinson Hyperlegible'; font-size:12pt;\"> by</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Packaging</span><span style=\" font-family:'Atkinson Hyperlegible'; font-size:12pt;\"> (PyPi)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Requests</span><span style=\" font"
                        "-family:'Atkinson Hyperlegible'; font-size:12pt;\"> (Python)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">TOML</span><span style=\" font-family:'Atkinson Hyperlegible'; font-size:12pt;\"> (Python)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Qt 6</span><span style=\" font-size:12pt;\"> by the Qt project</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Atkinson Hyperlegible'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt;\">LauncherBlast2 &quot;reBoot&quot; by HitCoder</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Built in PyQt5</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justi"
                        "fy\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://mb.srb2.org/threads/launcherblast2-reboot.27592/\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; text-decoration: underline; color:#00ffff;\">View the SRB2 Message Board thread</span></a></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600;\">Credits</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12"
                        "px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FinestElite - icons for News and Help</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sonic Team Jr - SRB2 icon</li></ul>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600;\">reBoot-2.0 changelog</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'MS Shell Dlg 2'; font-size:8p"
                        "t;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">UI Overhaul - main tabs are now at the top and use icons instead of text</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Introduction of profiles, allowing support for multiple installations of different versions of SRB2 or mods of SRB2 such as SRB2Kart</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed a bug with spaces in filenames when adding files to the game</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\">Fixed a bug with spaces in player nicknames</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The console no longer opens with the launcher</li>\n"
"<li style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added new icon for the launcher</li></ul>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"just"
                        "ify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">FAQ</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; text-decoration: underline;\">How do I host a server?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">To host a server, select the host server tab. You will be given a multitude of options for your server"
                        ". To start your server, you will find that on this tab, your &quot;Play&quot; button has changed to read &quot;Start Server&quot;. You can only start a server with this tab selected.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; text-decoration: underline;\">My antivirus detects Launcherblast2 as a trojan. Is this true?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Due to the nature of this utility, it is a small scale program that doesn't have a very big audience. Modern a"
                        "ntivirus software may well detect it as a false-positive, as a precaution to &quot;unknown programs&quot;. If this happens, your antivirus may have an option to submit the program for analysis, in which case please do so!</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; text-decoration: underline;\">About Launcherblast2</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:6pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">LAUNCHERBLAST2 is a project I started in 2019, before SRB2 2.2 was released. I wanted this to be released not long after 2.2 was, to go with it, but due to personal life and some other things I never got to finish it. Fast forward to early 2020, I remember this exists. I decided to finish it, though it's not to a standard I'd ideally like it to be. I do feel like it fits the bill for a nice looking launcher at it's forefront though.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><b"
                        "r /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">There are a couple of graphical glitches here and there because I realised not long into starting to develop this, that a lot of info on Qt5 is sparse, and some of the Qt4 stuff isn't directly compatible. I'm really sorry for the combo-boxes that have a weird square on them when you hover. I hope it doesn't bother you too much.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">In case you didn't already notice, the de"
                        "sign is very much inspired by the 2019 Minecraft Launcher. It was actually that which kick-started me into creating this. Anyway, hope you enjoy it, if you find any bugs let me know! I'll be working on this from time to time regardless, so updates may come soon. I'm not implementing an auto-updater though, as I don't have a server to place the metadata on for now.</span></p></body></html>", None))
        self.SaveFilesToConfigToggle.setText(QCoreApplication.translate("MainWindow", u"Save Launch Mods to Profile", None))
        self.ProfileDirBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.ProfileDirLabel.setText(QCoreApplication.translate("MainWindow", u"Profile Directory (requires restart)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.ModsourceDisclaimerLabel.setText(QCoreApplication.translate("MainWindow", u"DISCLAIMER", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'CMU Serif Medium'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">WARNING:</span><span style=\" font-size:10pt; font-weight:600;\"> </span><span style=\" font-size:10pt;\">The hosting of some unofficial mods on the official Master Server [</span><a href=\"https://mb.srb2.org/MS/0\"><span style=\" font-size:10pt; text-decoration: underline; color:#00d3b8;\">https://mb.srb2.org/MS/0</span></a><span style=\" font-size:10pt;\">] is prohibited by the Sonic Robo Blast 2 community administration team (&quot;STJr&quot;) and may be penalized by a "
                        "permanent ban from their Master Server or the official SRB2 Message Board.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">USE THESE ALTERNATIVE MOD SOURCES AT YOUR OWN RISK!!!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Additionally, Liquid has no influence over, nor takes responsibility nor accountability for the quality, compliance or legality of mods or other content found within the provided sources, according to the terms of your or any other jurisdiction.</span></p>\n"
"<p align=\"center\" style=\" margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">YOU HAVE BEEN WARNED!!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p></body></html>", None))
        self.ModsourceCheckLabel.setText(QCoreApplication.translate("MainWindow", u"Mod sources", None))
        self.ModsourceMBCheckbox.setText(QCoreApplication.translate("MainWindow", u"Official SRB2 Message Board", None))
        self.ModsourceGamebananaCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Gamebanana (unofficial)", None))
        self.ModsourceSkybaseCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Skybase (unofficial)", None))
        self.ModsourceWadarchiveCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Wad Archive \"2.2 section\" (unsupported)", None))
        self.ModsourceWSBlueCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Blue Sphere\" (unofficial)", None))
        self.ModsourceWSRedCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Red Sphere\" (non-compliant; unofficial)", None))
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

