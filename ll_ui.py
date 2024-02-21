# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'll.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QSpacerItem, QSpinBox, QSplitter, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)
import ll_rc
import ll_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1034, 621)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_32 = QGridLayout(self.centralwidget)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
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
        self.NewsScrollAreaContent.setGeometry(QRect(0, 0, 381, 143))
        self.NewsScrollAreaContent.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.NewsScrollAreaContent)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.RSSFeedCombobox = QComboBox(self.NewsScrollAreaContent)
        self.RSSFeedCombobox.addItem("")
        self.RSSFeedCombobox.setObjectName(u"RSSFeedCombobox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RSSFeedCombobox.sizePolicy().hasHeightForWidth())
        self.RSSFeedCombobox.setSizePolicy(sizePolicy)
        self.RSSFeedCombobox.setEditable(True)

        self.gridLayout_7.addWidget(self.RSSFeedCombobox, 0, 1, 1, 1)

        self.RSSFeedLabel = QLabel(self.NewsScrollAreaContent)
        self.RSSFeedLabel.setObjectName(u"RSSFeedLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.RSSFeedLabel.sizePolicy().hasHeightForWidth())
        self.RSSFeedLabel.setSizePolicy(sizePolicy1)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RSSArticleList.sizePolicy().hasHeightForWidth())
        self.RSSArticleList.setSizePolicy(sizePolicy2)
        self.splitter_4.addWidget(self.RSSArticleList)
        self.RSSArticleView = QWebEngineView(self.splitter_4)
        self.RSSArticleView.setObjectName(u"RSSArticleView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.RSSArticleView.sizePolicy().hasHeightForWidth())
        self.RSSArticleView.setSizePolicy(sizePolicy3)
        self.RSSArticleView.setProperty("url", QUrl(u"qrc:/assets/default.html"))
        self.splitter_4.addWidget(self.RSSArticleView)

        self.gridLayout_7.addWidget(self.splitter_4, 2, 0, 1, 3)

        self.RSSRefreshButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSRefreshButton.setObjectName(u"RSSRefreshButton")
        icon = QIcon()
        icon.addFile(u":/assets/img/icons/view-refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSRefreshButton.setIcon(icon)

        self.gridLayout_7.addWidget(self.RSSRefreshButton, 0, 2, 1, 1)

        self.RSSViewonlineButton = QPushButton(self.NewsScrollAreaContent)
        self.RSSViewonlineButton.setObjectName(u"RSSViewonlineButton")
        self.RSSViewonlineButton.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/assets/img/icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RSSViewonlineButton.setIcon(icon1)

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
        icon2 = QIcon()
        icon2.addFile(u":/assets/img/icons/srb2mb.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setPointSize(14)
        __qlistwidgetitem1 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem1.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/assets/img/icons/gamepad.png", QSize(), QIcon.Normal, QIcon.Off)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        __qlistwidgetitem2 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem2.setFont(font1);
        __qlistwidgetitem2.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/assets/img/icons/list-add.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem3.setFont(font);
        __qlistwidgetitem3.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/assets/img/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem4.setFont(font);
        __qlistwidgetitem4.setIcon(icon5);
        __qlistwidgetitem5 = QListWidgetItem(self.GamePageTabList)
        __qlistwidgetitem5.setFont(font);
        __qlistwidgetitem5.setIcon(icon1);
        self.GamePageTabList.setObjectName(u"GamePageTabList")
        sizePolicy2.setHeightForWidth(self.GamePageTabList.sizePolicy().hasHeightForWidth())
        self.GamePageTabList.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.GamePageTabList)
        self.GamePageContentFrame = QFrame(self.splitter)
        self.GamePageContentFrame.setObjectName(u"GamePageContentFrame")
        self.GamePageContentFrame.setFrameShape(QFrame.StyledPanel)
        self.GamePageContentFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.GamePageContentFrame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 810, 447))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.PlayerSkinInfoText = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinInfoText.setObjectName(u"PlayerSkinInfoText")
        self.PlayerSkinInfoText.setMaximumSize(QSize(16777215, 1000007))
        self.PlayerSkinInfoText.setStyleSheet(u"")
        self.PlayerSkinInfoText.setTextFormat(Qt.RichText)
        self.PlayerSkinInfoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.PlayerSkinInfoText.setWordWrap(True)

        self.gridLayout_5.addWidget(self.PlayerSkinInfoText, 6, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 12, 0, 1, 2)

        self.PlayerSkinImage = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinImage.setObjectName(u"PlayerSkinImage")
        self.PlayerSkinImage.setMaximumSize(QSize(128, 128))
        self.PlayerSkinImage.setStyleSheet(u"")
        self.PlayerSkinImage.setPixmap(QPixmap(u":/assets/img/sonic.png"))
        self.PlayerSkinImage.setScaledContents(True)

        self.gridLayout_5.addWidget(self.PlayerSkinImage, 6, 0, 1, 1)

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

        self.gridLayout_5.addWidget(self.PlayerColorInput, 10, 0, 1, 2)

        self.PlayerSkinTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerSkinTitleLabel.setObjectName(u"PlayerSkinTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerSkinTitleLabel, 2, 0, 1, 1)

        self.PlayerNameInput = QLineEdit(self.scrollAreaWidgetContents_5)
        self.PlayerNameInput.setObjectName(u"PlayerNameInput")

        self.gridLayout_5.addWidget(self.PlayerNameInput, 1, 0, 1, 2)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_29.setObjectName(u"label_29")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_29.setFont(font2)

        self.gridLayout_5.addWidget(self.label_29, 4, 0, 1, 2)

        self.PlayerColorTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerColorTitleLabel.setObjectName(u"PlayerColorTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerColorTitleLabel, 8, 0, 1, 1)

        self.PlayerNameTitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.PlayerNameTitleLabel.setObjectName(u"PlayerNameTitleLabel")

        self.gridLayout_5.addWidget(self.PlayerNameTitleLabel, 0, 0, 1, 1)

        self.PlayerSkinInput = QComboBox(self.scrollAreaWidgetContents_5)
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.addItem("")
        self.PlayerSkinInput.setObjectName(u"PlayerSkinInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PlayerSkinInput.sizePolicy().hasHeightForWidth())
        self.PlayerSkinInput.setSizePolicy(sizePolicy4)
        self.PlayerSkinInput.setStyleSheet(u"")
        self.PlayerSkinInput.setEditable(True)

        self.gridLayout_5.addWidget(self.PlayerSkinInput, 3, 0, 1, 2)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_5.addWidget(self.label_30, 11, 0, 1, 2)

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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 797, 520))
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

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_20 = QGridLayout(self.groupBox_4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.GameExecFilePathBrowse = QPushButton(self.groupBox_4)
        self.GameExecFilePathBrowse.setObjectName(u"GameExecFilePathBrowse")
        self.GameExecFilePathBrowse.setMinimumSize(QSize(0, 28))
        icon6 = QIcon()
        icon6.addFile(u":/assets/img/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameExecFilePathBrowse.setIcon(icon6)

        self.gridLayout_20.addWidget(self.GameExecFilePathBrowse, 0, 2, 1, 1)

        self.GameExecFilePathInput = QLineEdit(self.groupBox_4)
        self.GameExecFilePathInput.setObjectName(u"GameExecFilePathInput")

        self.gridLayout_20.addWidget(self.GameExecFilePathInput, 0, 0, 1, 2)

        self.WineRadiobutton = QRadioButton(self.groupBox_4)
        self.WineRadiobutton.setObjectName(u"WineRadiobutton")
        self.WineRadiobutton.setEnabled(False)

        self.gridLayout_20.addWidget(self.WineRadiobutton, 3, 1, 1, 1)

        self.FlatpakRadiobutton = QRadioButton(self.groupBox_4)
        self.FlatpakRadiobutton.setObjectName(u"FlatpakRadiobutton")
        self.FlatpakRadiobutton.setEnabled(False)

        self.gridLayout_20.addWidget(self.FlatpakRadiobutton, 3, 2, 1, 1)

        self.NativeRadiobutton = QRadioButton(self.groupBox_4)
        self.NativeRadiobutton.setObjectName(u"NativeRadiobutton")
        self.NativeRadiobutton.setChecked(True)

        self.gridLayout_20.addWidget(self.NativeRadiobutton, 3, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_4, 6, 2, 1, 2)

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

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_21 = QGridLayout(self.groupBox_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")

        self.gridLayout_21.addWidget(self.label, 2, 0, 1, 2)

        self.line_2 = QFrame(self.groupBox_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_21.addWidget(self.line_2, 5, 0, 1, 2)

        self.HomePathInput = QLineEdit(self.groupBox_8)
        self.HomePathInput.setObjectName(u"HomePathInput")

        self.gridLayout_21.addWidget(self.HomePathInput, 3, 0, 1, 1)

        self.GameArgsLabel = QLabel(self.groupBox_8)
        self.GameArgsLabel.setObjectName(u"GameArgsLabel")

        self.gridLayout_21.addWidget(self.GameArgsLabel, 6, 0, 1, 1)

        self.HomePathBrowse = QPushButton(self.groupBox_8)
        self.HomePathBrowse.setObjectName(u"HomePathBrowse")
        self.HomePathBrowse.setIcon(icon6)

        self.gridLayout_21.addWidget(self.HomePathBrowse, 3, 1, 1, 1)

        self.GameArgsInput = QLineEdit(self.groupBox_8)
        self.GameArgsInput.setObjectName(u"GameArgsInput")

        self.gridLayout_21.addWidget(self.GameArgsInput, 7, 0, 1, 2)

        self.label_31 = QLabel(self.groupBox_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.gridLayout_21.addWidget(self.label_31, 4, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_8, 7, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_10, 8, 2, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_14.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.ExportClientScriptButton = QPushButton(self.GameSettingsPage)
        self.ExportClientScriptButton.setObjectName(u"ExportClientScriptButton")
        icon7 = QIcon()
        icon7.addFile(u":/assets/img/icons/document-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ExportClientScriptButton.setIcon(icon7)

        self.gridLayout_14.addWidget(self.ExportClientScriptButton, 1, 0, 1, 1)

        self.GameContentStackedWidget.addWidget(self.GameSettingsPage)
        self.ModsPage = QWidget()
        self.ModsPage.setObjectName(u"ModsPage")
        self.verticalLayout_5 = QVBoxLayout(self.ModsPage)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.widget_3 = QWidget(self.ModsPage)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
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
        self.GameFilesAddButton.setIcon(icon4)

        self.gridLayout_9.addWidget(self.GameFilesAddButton, 10, 6, 1, 1)

        self.GameFilesExecScrBrowseButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesExecScrBrowseButton.setObjectName(u"GameFilesExecScrBrowseButton")
        self.GameFilesExecScrBrowseButton.setMinimumSize(QSize(0, 28))
        self.GameFilesExecScrBrowseButton.setIcon(icon6)

        self.gridLayout_9.addWidget(self.GameFilesExecScrBrowseButton, 10, 4, 1, 1)

        self.GameFilesDownButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesDownButton.setObjectName(u"GameFilesDownButton")
        sizePolicy4.setHeightForWidth(self.GameFilesDownButton.sizePolicy().hasHeightForWidth())
        self.GameFilesDownButton.setSizePolicy(sizePolicy4)
        icon8 = QIcon()
        icon8.addFile(u":/assets/img/icons/go-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDownButton.setIcon(icon8)

        self.gridLayout_9.addWidget(self.GameFilesDownButton, 8, 8, 1, 1)

        self.GameFilesClearButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesClearButton.setObjectName(u"GameFilesClearButton")
        self.GameFilesClearButton.setMinimumSize(QSize(0, 28))
        icon9 = QIcon()
        icon9.addFile(u":/assets/img/icons/edit-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesClearButton.setIcon(icon9)

        self.gridLayout_9.addWidget(self.GameFilesClearButton, 1, 8, 1, 1)

        self.GameFilesDeleteButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesDeleteButton.setObjectName(u"GameFilesDeleteButton")
        self.GameFilesDeleteButton.setMinimumSize(QSize(0, 28))
        icon10 = QIcon()
        icon10.addFile(u":/assets/img/icons/list-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesDeleteButton.setIcon(icon10)

        self.gridLayout_9.addWidget(self.GameFilesDeleteButton, 10, 7, 1, 1)

        self.GameFilesSaveButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesSaveButton.setObjectName(u"GameFilesSaveButton")
        self.GameFilesSaveButton.setMinimumSize(QSize(0, 28))
        self.GameFilesSaveButton.setStyleSheet(u"")
        self.GameFilesSaveButton.setIcon(icon7)

        self.gridLayout_9.addWidget(self.GameFilesSaveButton, 0, 8, 1, 1)

        self.GameFilesExecScriptInput = QLineEdit(self.AddonsLoaderTab)
        self.GameFilesExecScriptInput.setObjectName(u"GameFilesExecScriptInput")

        self.gridLayout_9.addWidget(self.GameFilesExecScriptInput, 10, 3, 1, 1)

        self.GameFilesList = QListWidget(self.AddonsLoaderTab)
        icon11 = QIcon()
        icon11.addFile(u":/assets/img/filetypes/wad.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem6 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem6.setIcon(icon11);
        icon12 = QIcon()
        icon12.addFile(u":/assets/img/filetypes/pk3.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem7 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem7.setIcon(icon12);
        icon13 = QIcon()
        icon13.addFile(u":/assets/img/filetypes/lua.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem8 = QListWidgetItem(self.GameFilesList)
        __qlistwidgetitem8.setIcon(icon13);
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
        sizePolicy4.setHeightForWidth(self.GameFilesUpButton.sizePolicy().hasHeightForWidth())
        self.GameFilesUpButton.setSizePolicy(sizePolicy4)
        icon14 = QIcon()
        icon14.addFile(u":/assets/img/icons/go-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GameFilesUpButton.setIcon(icon14)

        self.gridLayout_9.addWidget(self.GameFilesUpButton, 7, 8, 1, 1)

        self.GameFilesExecuteScriptLabel = QLabel(self.AddonsLoaderTab)
        self.GameFilesExecuteScriptLabel.setObjectName(u"GameFilesExecuteScriptLabel")

        self.gridLayout_9.addWidget(self.GameFilesExecuteScriptLabel, 10, 2, 1, 1)

        self.GameFilesLoadButton = QPushButton(self.AddonsLoaderTab)
        self.GameFilesLoadButton.setObjectName(u"GameFilesLoadButton")
        self.GameFilesLoadButton.setMinimumSize(QSize(0, 28))
        self.GameFilesLoadButton.setStyleSheet(u"")
        self.GameFilesLoadButton.setIcon(icon6)

        self.gridLayout_9.addWidget(self.GameFilesLoadButton, 2, 8, 1, 1)

        self.line_4 = QFrame(self.AddonsLoaderTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_4, 10, 5, 1, 1)

        self.GameSettingsTabWidget.addTab(self.AddonsLoaderTab, "")
        self.ModBrowserTab = QWidget()
        self.ModBrowserTab.setObjectName(u"ModBrowserTab")
        self.gridLayout_12 = QGridLayout(self.ModBrowserTab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.ModDirBrowseButton = QPushButton(self.ModBrowserTab)
        self.ModDirBrowseButton.setObjectName(u"ModDirBrowseButton")
        self.ModDirBrowseButton.setIcon(icon6)

        self.gridLayout_12.addWidget(self.ModDirBrowseButton, 2, 4, 1, 1)

        self.label_23 = QLabel(self.ModBrowserTab)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 2, 2, 1, 1)

        self.ModDirInput = QLineEdit(self.ModBrowserTab)
        self.ModDirInput.setObjectName(u"ModDirInput")

        self.gridLayout_12.addWidget(self.ModDirInput, 2, 3, 1, 1)

        self.splitter_2 = QSplitter(self.ModBrowserTab)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy3.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy3)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
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

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.ModsList = QListWidget(self.groupBox)
        __qlistwidgetitem9 = QListWidgetItem(self.ModsList)
        __qlistwidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.ModsList.setObjectName(u"ModsList")
        sizePolicy3.setHeightForWidth(self.ModsList.sizePolicy().hasHeightForWidth())
        self.ModsList.setSizePolicy(sizePolicy3)

        self.gridLayout_17.addWidget(self.ModsList, 2, 0, 1, 5)

        self.ModPageInput = QSpinBox(self.groupBox)
        self.ModPageInput.setObjectName(u"ModPageInput")
        self.ModPageInput.setMinimum(1)

        self.gridLayout_17.addWidget(self.ModPageInput, 0, 3, 1, 1)

        self.ModBrowserLabel = QLabel(self.groupBox)
        self.ModBrowserLabel.setObjectName(u"ModBrowserLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ModBrowserLabel.sizePolicy().hasHeightForWidth())
        self.ModBrowserLabel.setSizePolicy(sizePolicy5)

        self.gridLayout_17.addWidget(self.ModBrowserLabel, 0, 0, 1, 1)

        self.ModStatusLabel = QLabel(self.groupBox)
        self.ModStatusLabel.setObjectName(u"ModStatusLabel")
        self.ModStatusLabel.setFont(font2)
        self.ModStatusLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.ModStatusLabel, 3, 0, 1, 4)

        self.RefreshModsButton = QPushButton(self.groupBox)
        self.RefreshModsButton.setObjectName(u"RefreshModsButton")
        self.RefreshModsButton.setIcon(icon)

        self.gridLayout_17.addWidget(self.RefreshModsButton, 0, 4, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(6, 0, 0, 0)
        self.DownloadModButton = QPushButton(self.groupBox_2)
        self.DownloadModButton.setObjectName(u"DownloadModButton")
        self.DownloadModButton.setEnabled(False)
        icon15 = QIcon()
        icon15.addFile(u":/assets/img/icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DownloadModButton.setIcon(icon15)

        self.gridLayout_4.addWidget(self.DownloadModButton, 2, 2, 1, 1)

        self.ModViewerLabel = QLabel(self.groupBox_2)
        self.ModViewerLabel.setObjectName(u"ModViewerLabel")
        sizePolicy5.setHeightForWidth(self.ModViewerLabel.sizePolicy().hasHeightForWidth())
        self.ModViewerLabel.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.ModViewerLabel, 0, 0, 1, 4)

        self.OpenPageButton = QPushButton(self.groupBox_2)
        self.OpenPageButton.setObjectName(u"OpenPageButton")
        self.OpenPageButton.setEnabled(False)
        self.OpenPageButton.setIcon(icon1)

        self.gridLayout_4.addWidget(self.OpenPageButton, 2, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.ModBrowser = QWebEngineView(self.groupBox_2)
        self.ModBrowser.setObjectName(u"ModBrowser")
        sizePolicy3.setHeightForWidth(self.ModBrowser.sizePolicy().hasHeightForWidth())
        self.ModBrowser.setSizePolicy(sizePolicy3)
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

        self.gridLayout_4.addWidget(self.ModBrowser, 1, 0, 1, 4)

        self.AdddownloadtolaunchmodsCheckbox = QCheckBox(self.groupBox_2)
        self.AdddownloadtolaunchmodsCheckbox.setObjectName(u"AdddownloadtolaunchmodsCheckbox")
        self.AdddownloadtolaunchmodsCheckbox.setChecked(True)

        self.gridLayout_4.addWidget(self.AdddownloadtolaunchmodsCheckbox, 3, 2, 1, 2)

        self.splitter_2.addWidget(self.groupBox_2)

        self.gridLayout_12.addWidget(self.splitter_2, 0, 0, 1, 5)

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
        self.HostGameTabwidget = QTabWidget(self.HostGamePage)
        self.HostGameTabwidget.setObjectName(u"HostGameTabwidget")
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.verticalLayout = QVBoxLayout(self.General)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_4 = QScrollArea(self.General)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 793, 648))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_25 = QGridLayout(self.groupBox_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.RoomLabel = QLabel(self.groupBox_11)
        self.RoomLabel.setObjectName(u"RoomLabel")

        self.gridLayout_25.addWidget(self.RoomLabel, 7, 0, 1, 1)

        self.ServerNameLabel = QLabel(self.groupBox_11)
        self.ServerNameLabel.setObjectName(u"ServerNameLabel")

        self.gridLayout_25.addWidget(self.ServerNameLabel, 0, 0, 1, 2)

        self.RoomInput = QComboBox(self.groupBox_11)
        self.RoomInput.addItem("")
        self.RoomInput.setObjectName(u"RoomInput")
        self.RoomInput.setEditable(False)

        self.gridLayout_25.addWidget(self.RoomInput, 8, 0, 1, 1)

        self.MSRoomqueryrefreshButton = QPushButton(self.groupBox_11)
        self.MSRoomqueryrefreshButton.setObjectName(u"MSRoomqueryrefreshButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.MSRoomqueryrefreshButton.sizePolicy().hasHeightForWidth())
        self.MSRoomqueryrefreshButton.setSizePolicy(sizePolicy6)
        self.MSRoomqueryrefreshButton.setIcon(icon)

        self.gridLayout_25.addWidget(self.MSRoomqueryrefreshButton, 8, 1, 1, 1)

        self.AdminPasswordLabel = QLabel(self.groupBox_11)
        self.AdminPasswordLabel.setObjectName(u"AdminPasswordLabel")

        self.gridLayout_25.addWidget(self.AdminPasswordLabel, 2, 0, 1, 2)

        self.HostMSCombobox = QComboBox(self.groupBox_11)
        self.HostMSCombobox.addItem("")
        self.HostMSCombobox.setObjectName(u"HostMSCombobox")
        self.HostMSCombobox.setEnabled(True)
        self.HostMSCombobox.setEditable(True)

        self.gridLayout_25.addWidget(self.HostMSCombobox, 8, 2, 1, 1)

        self.label_55 = QLabel(self.groupBox_11)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_55, 10, 2, 1, 1)

        self.AdminPasswordInput = QLineEdit(self.groupBox_11)
        self.AdminPasswordInput.setObjectName(u"AdminPasswordInput")
        self.AdminPasswordInput.setEchoMode(QLineEdit.Password)

        self.gridLayout_25.addWidget(self.AdminPasswordInput, 3, 0, 1, 3)

        self.ServerNameInput = QLineEdit(self.groupBox_11)
        self.ServerNameInput.setObjectName(u"ServerNameInput")

        self.gridLayout_25.addWidget(self.ServerNameInput, 1, 0, 1, 3)

        self.HostMSLabel = QLabel(self.groupBox_11)
        self.HostMSLabel.setObjectName(u"HostMSLabel")

        self.gridLayout_25.addWidget(self.HostMSLabel, 7, 2, 1, 1)

        self.label_51 = QLabel(self.groupBox_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_51, 10, 0, 1, 2)

        self.DedicatedServerToggle = QCheckBox(self.groupBox_11)
        self.DedicatedServerToggle.setObjectName(u"DedicatedServerToggle")
        self.DedicatedServerToggle.setStyleSheet(u"")
        self.DedicatedServerToggle.setChecked(False)

        self.gridLayout_25.addWidget(self.DedicatedServerToggle, 11, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.groupBox_11)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_23 = QGridLayout(self.groupBox_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.BandwidthInput = QSpinBox(self.groupBox_10)
        self.BandwidthInput.setObjectName(u"BandwidthInput")
        self.BandwidthInput.setMinimum(1000)
        self.BandwidthInput.setMaximum(250000)
        self.BandwidthInput.setValue(30000)

        self.gridLayout_23.addWidget(self.BandwidthInput, 4, 0, 1, 1)

        self.PortLabel = QLabel(self.groupBox_10)
        self.PortLabel.setObjectName(u"PortLabel")

        self.gridLayout_23.addWidget(self.PortLabel, 0, 0, 2, 2)

        self.PortInput = QSpinBox(self.groupBox_10)
        self.PortInput.setObjectName(u"PortInput")
        self.PortInput.setMaximum(65535)
        self.PortInput.setValue(5029)

        self.gridLayout_23.addWidget(self.PortInput, 2, 0, 1, 1)

        self.ExtraticLabel = QLabel(self.groupBox_10)
        self.ExtraticLabel.setObjectName(u"ExtraticLabel")

        self.gridLayout_23.addWidget(self.ExtraticLabel, 3, 1, 1, 1)

        self.BandwidthLabel = QLabel(self.groupBox_10)
        self.BandwidthLabel.setObjectName(u"BandwidthLabel")

        self.gridLayout_23.addWidget(self.BandwidthLabel, 3, 0, 1, 1)

        self.ExtraticInput = QSpinBox(self.groupBox_10)
        self.ExtraticInput.setObjectName(u"ExtraticInput")
        self.ExtraticInput.setValue(1)

        self.gridLayout_23.addWidget(self.ExtraticInput, 4, 1, 1, 1)

        self.Ipv6Checkbox = QCheckBox(self.groupBox_10)
        self.Ipv6Checkbox.setObjectName(u"Ipv6Checkbox")

        self.gridLayout_23.addWidget(self.Ipv6Checkbox, 2, 1, 1, 1)

        self.groupBox_23 = QGroupBox(self.groupBox_10)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.UploadToggle = QCheckBox(self.groupBox_23)
        self.UploadToggle.setObjectName(u"UploadToggle")
        self.UploadToggle.setChecked(True)

        self.verticalLayout_32.addWidget(self.UploadToggle)

        self.label_14 = QLabel(self.groupBox_23)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_32.addWidget(self.label_14)

        self.DownloadspeedInput = QSpinBox(self.groupBox_23)
        self.DownloadspeedInput.setObjectName(u"DownloadspeedInput")
        self.DownloadspeedInput.setMaximum(32)
        self.DownloadspeedInput.setValue(16)

        self.verticalLayout_32.addWidget(self.DownloadspeedInput)

        self.label_16 = QLabel(self.groupBox_23)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_32.addWidget(self.label_16)

        self.MaxsendInput = QSpinBox(self.groupBox_23)
        self.MaxsendInput.setObjectName(u"MaxsendInput")
        self.MaxsendInput.setMaximum(204800)
        self.MaxsendInput.setValue(32)

        self.verticalLayout_32.addWidget(self.MaxsendInput)


        self.gridLayout_23.addWidget(self.groupBox_23, 6, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.groupBox_10)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_15 = QLabel(self.groupBox_24)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_31.addWidget(self.label_15)

        self.MaxpingInput = QSpinBox(self.groupBox_24)
        self.MaxpingInput.setObjectName(u"MaxpingInput")
        self.MaxpingInput.setMaximum(1000)
        self.MaxpingInput.setValue(0)

        self.verticalLayout_31.addWidget(self.MaxpingInput)

        self.label_34 = QLabel(self.groupBox_24)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_31.addWidget(self.label_34)

        self.NettimeoutInput = QSpinBox(self.groupBox_24)
        self.NettimeoutInput.setObjectName(u"NettimeoutInput")
        self.NettimeoutInput.setMinimum(5)
        self.NettimeoutInput.setMaximum(2100)
        self.NettimeoutInput.setValue(350)

        self.verticalLayout_31.addWidget(self.NettimeoutInput)

        self.label_35 = QLabel(self.groupBox_24)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_31.addWidget(self.label_35)

        self.ResynchattemptsInput = QSpinBox(self.groupBox_24)
        self.ResynchattemptsInput.setObjectName(u"ResynchattemptsInput")
        self.ResynchattemptsInput.setMaximum(20)
        self.ResynchattemptsInput.setValue(10)

        self.verticalLayout_31.addWidget(self.ResynchattemptsInput)


        self.gridLayout_23.addWidget(self.groupBox_24, 6, 1, 1, 1)

        self.UpnpCheckbox = QCheckBox(self.groupBox_10)
        self.UpnpCheckbox.setObjectName(u"UpnpCheckbox")

        self.gridLayout_23.addWidget(self.UpnpCheckbox, 5, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        self.HostGameTabwidget.addTab(self.General, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_17 = QVBoxLayout(self.tab_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_10 = QScrollArea(self.tab_8)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 443, 630))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ForceSkinLabel = QLabel(self.scrollAreaWidgetContents_10)
        self.ForceSkinLabel.setObjectName(u"ForceSkinLabel")

        self.gridLayout.addWidget(self.ForceSkinLabel, 11, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 1, 1, 1)

        self.MaxPlayersInput = QSpinBox(self.scrollAreaWidgetContents_10)
        self.MaxPlayersInput.setObjectName(u"MaxPlayersInput")
        self.MaxPlayersInput.setMinimum(2)
        self.MaxPlayersInput.setMaximum(32)
        self.MaxPlayersInput.setValue(8)

        self.gridLayout.addWidget(self.MaxPlayersInput, 10, 0, 1, 1)

        self.GametypeInput = QComboBox(self.scrollAreaWidgetContents_10)
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

        self.gridLayout.addWidget(self.GametypeInput, 2, 0, 1, 2)

        self.AdvanceMapLabel = QLabel(self.scrollAreaWidgetContents_10)
        self.AdvanceMapLabel.setObjectName(u"AdvanceMapLabel")

        self.gridLayout.addWidget(self.AdvanceMapLabel, 3, 0, 1, 1)

        self.RespawnitemCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.RespawnitemCheckbox.setObjectName(u"RespawnitemCheckbox")
        self.RespawnitemCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.RespawnitemCheckbox, 16, 1, 1, 1)

        self.JoinnextroundCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.JoinnextroundCheckbox.setObjectName(u"JoinnextroundCheckbox")

        self.gridLayout.addWidget(self.JoinnextroundCheckbox, 10, 1, 1, 1)

        self.RestrictskinchangesCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.RestrictskinchangesCheckbox.setObjectName(u"RestrictskinchangesCheckbox")
        self.RestrictskinchangesCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.RestrictskinchangesCheckbox, 12, 1, 1, 1)

        self.TailspickupCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.TailspickupCheckbox.setObjectName(u"TailspickupCheckbox")
        self.TailspickupCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.TailspickupCheckbox, 13, 1, 1, 1)

        self.ForceSkinLabel_2 = QLabel(self.scrollAreaWidgetContents_10)
        self.ForceSkinLabel_2.setObjectName(u"ForceSkinLabel_2")

        self.gridLayout.addWidget(self.ForceSkinLabel_2, 14, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 17, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_36 = QGridLayout(self.groupBox_15)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.SoniccdCheckbox = QCheckBox(self.groupBox_15)
        self.SoniccdCheckbox.setObjectName(u"SoniccdCheckbox")

        self.gridLayout_36.addWidget(self.SoniccdCheckbox, 0, 0, 1, 1)

        self.KillingdeadCheckbox = QCheckBox(self.groupBox_15)
        self.KillingdeadCheckbox.setObjectName(u"KillingdeadCheckbox")

        self.gridLayout_36.addWidget(self.KillingdeadCheckbox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_15, 19, 0, 1, 2)

        self.InttimeInput = QSpinBox(self.scrollAreaWidgetContents_10)
        self.InttimeInput.setObjectName(u"InttimeInput")
        self.InttimeInput.setMaximum(3600)
        self.InttimeInput.setValue(20)

        self.gridLayout.addWidget(self.InttimeInput, 4, 1, 1, 1)

        self.AdvanceMapInput = QComboBox(self.scrollAreaWidgetContents_10)
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.addItem("")
        self.AdvanceMapInput.setObjectName(u"AdvanceMapInput")

        self.gridLayout.addWidget(self.AdvanceMapInput, 4, 0, 1, 1)

        self.GametypeLabel = QLabel(self.scrollAreaWidgetContents_10)
        self.GametypeLabel.setObjectName(u"GametypeLabel")

        self.gridLayout.addWidget(self.GametypeLabel, 1, 0, 1, 1)

        self.RespawnitemtimeInput = QSpinBox(self.scrollAreaWidgetContents_10)
        self.RespawnitemtimeInput.setObjectName(u"RespawnitemtimeInput")
        self.RespawnitemtimeInput.setMaximum(300)
        self.RespawnitemtimeInput.setValue(30)

        self.gridLayout.addWidget(self.RespawnitemtimeInput, 16, 0, 1, 1)

        self.ForceSkinInput = QComboBox(self.scrollAreaWidgetContents_10)
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

        self.gridLayout.addWidget(self.ForceSkinInput, 12, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_34 = QGridLayout(self.groupBox_14)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.ForceSkinLabel_15 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_15.setObjectName(u"ForceSkinLabel_15")
        self.ForceSkinLabel_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_15, 5, 2, 1, 1)

        self.ForceSkinLabel_3 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_3.setObjectName(u"ForceSkinLabel_3")
        self.ForceSkinLabel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_3, 0, 0, 1, 1)

        self.Tv_ringshieldInput = QSpinBox(self.groupBox_14)
        self.Tv_ringshieldInput.setObjectName(u"Tv_ringshieldInput")
        self.Tv_ringshieldInput.setMaximum(10)
        self.Tv_ringshieldInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_ringshieldInput, 4, 3, 1, 1)

        self.ForceSkinLabel_8 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_8.setObjectName(u"ForceSkinLabel_8")
        self.ForceSkinLabel_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_8, 2, 2, 1, 1)

        self.Tv_supersneakersInput = QSpinBox(self.groupBox_14)
        self.Tv_supersneakersInput.setObjectName(u"Tv_supersneakersInput")
        self.Tv_supersneakersInput.setMaximum(10)
        self.Tv_supersneakersInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_supersneakersInput, 2, 1, 1, 1)

        self.Tv_eggmanInput = QSpinBox(self.groupBox_14)
        self.Tv_eggmanInput.setObjectName(u"Tv_eggmanInput")
        self.Tv_eggmanInput.setMaximum(10)
        self.Tv_eggmanInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_eggmanInput, 0, 5, 1, 1)

        self.Tv_forceshieldInput = QSpinBox(self.groupBox_14)
        self.Tv_forceshieldInput.setObjectName(u"Tv_forceshieldInput")
        self.Tv_forceshieldInput.setMaximum(10)
        self.Tv_forceshieldInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_forceshieldInput, 1, 3, 1, 1)

        self.ForceSkinLabel_14 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_14.setObjectName(u"ForceSkinLabel_14")
        self.ForceSkinLabel_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_14, 4, 2, 1, 1)

        self.Tv_invincibilityInput = QSpinBox(self.groupBox_14)
        self.Tv_invincibilityInput.setObjectName(u"Tv_invincibilityInput")
        self.Tv_invincibilityInput.setMaximum(10)
        self.Tv_invincibilityInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_invincibilityInput, 1, 1, 1, 1)

        self.ForceSkinLabel_9 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_9.setObjectName(u"ForceSkinLabel_9")
        self.ForceSkinLabel_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_9, 4, 4, 1, 1)

        self.ForceSkinLabel_12 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_12.setObjectName(u"ForceSkinLabel_12")
        self.ForceSkinLabel_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_12, 2, 0, 1, 1)

        self.ForceSkinLabel_7 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_7.setObjectName(u"ForceSkinLabel_7")
        self.ForceSkinLabel_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_7, 1, 2, 1, 1)

        self.Tv_1upInput = QSpinBox(self.groupBox_14)
        self.Tv_1upInput.setObjectName(u"Tv_1upInput")
        self.Tv_1upInput.setMaximum(10)
        self.Tv_1upInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_1upInput, 0, 1, 1, 1)

        self.Tv_bombshieldInput = QSpinBox(self.groupBox_14)
        self.Tv_bombshieldInput.setObjectName(u"Tv_bombshieldInput")
        self.Tv_bombshieldInput.setMaximum(10)
        self.Tv_bombshieldInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_bombshieldInput, 0, 3, 1, 1)

        self.ForceSkinLabel_11 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_11.setObjectName(u"ForceSkinLabel_11")
        self.ForceSkinLabel_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_11, 0, 4, 1, 1)

        self.ForceSkinLabel_4 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_4.setObjectName(u"ForceSkinLabel_4")
        self.ForceSkinLabel_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_4, 0, 2, 1, 1)

        self.Tv_jumpshieldInput = QSpinBox(self.groupBox_14)
        self.Tv_jumpshieldInput.setObjectName(u"Tv_jumpshieldInput")
        self.Tv_jumpshieldInput.setMaximum(10)
        self.Tv_jumpshieldInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_jumpshieldInput, 2, 3, 1, 1)

        self.Tv_watershieldInput = QSpinBox(self.groupBox_14)
        self.Tv_watershieldInput.setObjectName(u"Tv_watershieldInput")
        self.Tv_watershieldInput.setMaximum(10)
        self.Tv_watershieldInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_watershieldInput, 5, 3, 1, 1)

        self.ForceSkinLabel_10 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_10.setObjectName(u"ForceSkinLabel_10")
        self.ForceSkinLabel_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_10, 1, 0, 1, 1)

        self.Tv_recyclerInput = QSpinBox(self.groupBox_14)
        self.Tv_recyclerInput.setObjectName(u"Tv_recyclerInput")
        self.Tv_recyclerInput.setMaximum(10)
        self.Tv_recyclerInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_recyclerInput, 4, 5, 1, 1)

        self.ForceSkinLabel_28 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_28.setObjectName(u"ForceSkinLabel_28")
        self.ForceSkinLabel_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_28, 2, 4, 1, 1)

        self.Tv_teleporterInput = QSpinBox(self.groupBox_14)
        self.Tv_teleporterInput.setObjectName(u"Tv_teleporterInput")
        self.Tv_teleporterInput.setMaximum(10)
        self.Tv_teleporterInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_teleporterInput, 2, 5, 1, 1)

        self.Tv_superringInput = QSpinBox(self.groupBox_14)
        self.Tv_superringInput.setObjectName(u"Tv_superringInput")
        self.Tv_superringInput.setMaximum(10)
        self.Tv_superringInput.setValue(5)

        self.gridLayout_34.addWidget(self.Tv_superringInput, 1, 5, 1, 1)

        self.ForceSkinLabel_27 = QLabel(self.groupBox_14)
        self.ForceSkinLabel_27.setObjectName(u"ForceSkinLabel_27")
        self.ForceSkinLabel_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.ForceSkinLabel_27, 1, 4, 1, 1)


        self.gridLayout.addWidget(self.groupBox_14, 18, 0, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(20, 204, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 20, 1, 1, 1)

        self.MaxPlayersLabel = QLabel(self.scrollAreaWidgetContents_10)
        self.MaxPlayersLabel.setObjectName(u"MaxPlayersLabel")

        self.gridLayout.addWidget(self.MaxPlayersLabel, 8, 0, 1, 1)

        self.AllowexitlevelCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.AllowexitlevelCheckbox.setObjectName(u"AllowexitlevelCheckbox")

        self.gridLayout.addWidget(self.AllowexitlevelCheckbox, 5, 0, 1, 1)

        self.ExitmoveCheckbox = QCheckBox(self.scrollAreaWidgetContents_10)
        self.ExitmoveCheckbox.setObjectName(u"ExitmoveCheckbox")

        self.gridLayout.addWidget(self.ExitmoveCheckbox, 5, 1, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_17.addWidget(self.scrollArea_10)

        self.HostGameTabwidget.addTab(self.tab_8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_9 = QScrollArea(self.tab)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 287, 257))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CoopSettingsCheckbox = QCheckBox(self.scrollAreaWidgetContents_9)
        self.CoopSettingsCheckbox.setObjectName(u"CoopSettingsCheckbox")

        self.verticalLayout_4.addWidget(self.CoopSettingsCheckbox)

        self.line_5 = QFrame(self.scrollAreaWidgetContents_9)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.CoopSettingsGroupbox = QGroupBox(self.scrollAreaWidgetContents_9)
        self.CoopSettingsGroupbox.setObjectName(u"CoopSettingsGroupbox")
        self.CoopSettingsGroupbox.setEnabled(False)
        self.gridLayout_31 = QGridLayout(self.CoopSettingsGroupbox)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_9 = QLabel(self.CoopSettingsGroupbox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_31.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_12 = QLabel(self.CoopSettingsGroupbox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_31.addWidget(self.label_12, 4, 0, 1, 1)

        self.PlayersforexitCombobox = QComboBox(self.CoopSettingsGroupbox)
        self.PlayersforexitCombobox.addItem("")
        self.PlayersforexitCombobox.addItem("")
        self.PlayersforexitCombobox.addItem("")
        self.PlayersforexitCombobox.addItem("")
        self.PlayersforexitCombobox.addItem("")
        self.PlayersforexitCombobox.setObjectName(u"PlayersforexitCombobox")

        self.gridLayout_31.addWidget(self.PlayersforexitCombobox, 3, 0, 1, 1)

        self.StartinglivesInput = QSpinBox(self.CoopSettingsGroupbox)
        self.StartinglivesInput.setObjectName(u"StartinglivesInput")
        self.StartinglivesInput.setMinimum(1)
        self.StartinglivesInput.setMaximum(99)
        self.StartinglivesInput.setValue(3)

        self.gridLayout_31.addWidget(self.StartinglivesInput, 1, 0, 1, 1)

        self.label_8 = QLabel(self.CoopSettingsGroupbox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_31.addWidget(self.label_8, 2, 0, 1, 1)

        self.CompetitionboxesCombobox = QComboBox(self.CoopSettingsGroupbox)
        self.CompetitionboxesCombobox.addItem("")
        self.CompetitionboxesCombobox.addItem("")
        self.CompetitionboxesCombobox.addItem("")
        self.CompetitionboxesCombobox.addItem("")
        self.CompetitionboxesCombobox.setObjectName(u"CompetitionboxesCombobox")

        self.gridLayout_31.addWidget(self.CompetitionboxesCombobox, 5, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.CoopSettingsGroupbox)

        self.verticalSpacer_8 = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_11.addWidget(self.scrollArea_9)

        self.HostGameTabwidget.addTab(self.tab, "")
        self.Ringslinger = QWidget()
        self.Ringslinger.setObjectName(u"Ringslinger")
        self.gridLayout_10 = QGridLayout(self.Ringslinger)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollArea_3 = QScrollArea(self.Ringslinger)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 619, 654))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.RingslingerSettingsGroupbox = QGroupBox(self.scrollAreaWidgetContents_3)
        self.RingslingerSettingsGroupbox.setObjectName(u"RingslingerSettingsGroupbox")
        self.RingslingerSettingsGroupbox.setEnabled(False)
        self.gridLayout_24 = QGridLayout(self.RingslingerSettingsGroupbox)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_7 = QLabel(self.RingslingerSettingsGroupbox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_24.addWidget(self.label_7, 0, 1, 1, 1)

        self.PowerstonesCheckbox = QCheckBox(self.RingslingerSettingsGroupbox)
        self.PowerstonesCheckbox.setObjectName(u"PowerstonesCheckbox")
        self.PowerstonesCheckbox.setChecked(True)

        self.gridLayout_24.addWidget(self.PowerstonesCheckbox, 11, 0, 1, 1)

        self.PointLimitInput = QSpinBox(self.RingslingerSettingsGroupbox)
        self.PointLimitInput.setObjectName(u"PointLimitInput")
        self.PointLimitInput.setMaximum(999999990)
        self.PointLimitInput.setValue(1000)

        self.gridLayout_24.addWidget(self.PointLimitInput, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.RingslingerSettingsGroupbox)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_33 = QGridLayout(self.groupBox_13)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.ScrambleteamsCombobox = QComboBox(self.groupBox_13)
        self.ScrambleteamsCombobox.addItem("")
        self.ScrambleteamsCombobox.addItem("")
        self.ScrambleteamsCombobox.addItem("")
        self.ScrambleteamsCombobox.setObjectName(u"ScrambleteamsCombobox")

        self.gridLayout_33.addWidget(self.ScrambleteamsCombobox, 1, 0, 1, 1)

        self.ScrambleTeamsLabel = QLabel(self.groupBox_13)
        self.ScrambleTeamsLabel.setObjectName(u"ScrambleTeamsLabel")

        self.gridLayout_33.addWidget(self.ScrambleTeamsLabel, 0, 0, 1, 1)

        self.AutobalanceCheckbox = QComboBox(self.groupBox_13)
        self.AutobalanceCheckbox.addItem("")
        self.AutobalanceCheckbox.addItem("")
        self.AutobalanceCheckbox.addItem("")
        self.AutobalanceCheckbox.addItem("")
        self.AutobalanceCheckbox.addItem("")
        self.AutobalanceCheckbox.setObjectName(u"AutobalanceCheckbox")

        self.gridLayout_33.addWidget(self.AutobalanceCheckbox, 1, 1, 1, 1)

        self.FriendlyfireCheckbox = QCheckBox(self.groupBox_13)
        self.FriendlyfireCheckbox.setObjectName(u"FriendlyfireCheckbox")

        self.gridLayout_33.addWidget(self.FriendlyfireCheckbox, 4, 0, 1, 1)

        self.FlagtimeInput = QSpinBox(self.groupBox_13)
        self.FlagtimeInput.setObjectName(u"FlagtimeInput")
        self.FlagtimeInput.setMaximum(300)
        self.FlagtimeInput.setValue(30)

        self.gridLayout_33.addWidget(self.FlagtimeInput, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_13)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_33.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_13)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_33.addWidget(self.label_10, 2, 0, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_13, 17, 0, 1, 2)

        self.TimeLimitLabel = QLabel(self.RingslingerSettingsGroupbox)
        self.TimeLimitLabel.setObjectName(u"TimeLimitLabel")

        self.gridLayout_24.addWidget(self.TimeLimitLabel, 3, 0, 1, 1)

        self.PointLimitLabel = QLabel(self.RingslingerSettingsGroupbox)
        self.PointLimitLabel.setObjectName(u"PointLimitLabel")

        self.gridLayout_24.addWidget(self.PointLimitLabel, 0, 0, 1, 1)

        self.MatchscoringCombobox = QComboBox(self.RingslingerSettingsGroupbox)
        self.MatchscoringCombobox.addItem("")
        self.MatchscoringCombobox.addItem("")
        self.MatchscoringCombobox.setObjectName(u"MatchscoringCombobox")

        self.gridLayout_24.addWidget(self.MatchscoringCombobox, 1, 1, 1, 1)

        self.label_11 = QLabel(self.RingslingerSettingsGroupbox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_24.addWidget(self.label_11, 7, 1, 1, 1)

        self.DisableWeaponsToggle = QCheckBox(self.RingslingerSettingsGroupbox)
        self.DisableWeaponsToggle.setObjectName(u"DisableWeaponsToggle")
        self.DisableWeaponsToggle.setMinimumSize(QSize(0, 0))

        self.gridLayout_24.addWidget(self.DisableWeaponsToggle, 7, 0, 1, 1)

        self.label_3 = QLabel(self.RingslingerSettingsGroupbox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_24.addWidget(self.label_3, 5, 0, 1, 1)

        self.OvertimeCheckbox = QCheckBox(self.RingslingerSettingsGroupbox)
        self.OvertimeCheckbox.setObjectName(u"OvertimeCheckbox")
        self.OvertimeCheckbox.setChecked(True)

        self.gridLayout_24.addWidget(self.OvertimeCheckbox, 4, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.RingslingerSettingsGroupbox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_30 = QGridLayout(self.groupBox_9)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.TouchtagCheckbox = QCheckBox(self.groupBox_9)
        self.TouchtagCheckbox.setObjectName(u"TouchtagCheckbox")

        self.gridLayout_30.addWidget(self.TouchtagCheckbox, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_9, 19, 0, 1, 1)

        self.RespawndelayInput = QSpinBox(self.RingslingerSettingsGroupbox)
        self.RespawndelayInput.setObjectName(u"RespawndelayInput")
        self.RespawndelayInput.setMaximum(999999990)
        self.RespawndelayInput.setValue(0)

        self.gridLayout_24.addWidget(self.RespawndelayInput, 6, 0, 1, 1)

        self.TimeLimitInput = QSpinBox(self.RingslingerSettingsGroupbox)
        self.TimeLimitInput.setObjectName(u"TimeLimitInput")
        self.TimeLimitInput.setMaximum(30)

        self.gridLayout_24.addWidget(self.TimeLimitInput, 4, 0, 1, 1)

        self.MatchboxesCombobox = QComboBox(self.RingslingerSettingsGroupbox)
        self.MatchboxesCombobox.addItem("")
        self.MatchboxesCombobox.addItem("")
        self.MatchboxesCombobox.addItem("")
        self.MatchboxesCombobox.addItem("")
        self.MatchboxesCombobox.setObjectName(u"MatchboxesCombobox")

        self.gridLayout_24.addWidget(self.MatchboxesCombobox, 11, 1, 1, 1)

        self.SuddenDeathToggle = QCheckBox(self.RingslingerSettingsGroupbox)
        self.SuddenDeathToggle.setObjectName(u"SuddenDeathToggle")
        self.SuddenDeathToggle.setMinimumSize(QSize(0, 0))

        self.gridLayout_24.addWidget(self.SuddenDeathToggle, 6, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.RingslingerSettingsGroupbox)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.groupBox_12)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_20.addWidget(self.label_4)

        self.HidetimeInput = QSpinBox(self.groupBox_12)
        self.HidetimeInput.setObjectName(u"HidetimeInput")
        self.HidetimeInput.setMaximum(999999990)
        self.HidetimeInput.setValue(0)

        self.verticalLayout_20.addWidget(self.HidetimeInput)


        self.gridLayout_24.addWidget(self.groupBox_12, 19, 1, 1, 1)


        self.gridLayout_18.addWidget(self.RingslingerSettingsGroupbox, 2, 0, 1, 2)

        self.RingslingerSettingsCheckbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.RingslingerSettingsCheckbox.setObjectName(u"RingslingerSettingsCheckbox")

        self.gridLayout_18.addWidget(self.RingslingerSettingsCheckbox, 1, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_18.addWidget(self.textEdit_2, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_10.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.HostGameTabwidget.addTab(self.Ringslinger, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_13 = QVBoxLayout(self.tab_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_8 = QScrollArea(self.tab_7)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 275, 194))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.CircuitraceSettingsCheckbox = QCheckBox(self.scrollAreaWidgetContents_8)
        self.CircuitraceSettingsCheckbox.setObjectName(u"CircuitraceSettingsCheckbox")

        self.verticalLayout_16.addWidget(self.CircuitraceSettingsCheckbox)

        self.CircuitraceSettingsGroupbox = QGroupBox(self.scrollAreaWidgetContents_8)
        self.CircuitraceSettingsGroupbox.setObjectName(u"CircuitraceSettingsGroupbox")
        self.CircuitraceSettingsGroupbox.setEnabled(False)
        self.gridLayout_29 = QGridLayout(self.CircuitraceSettingsGroupbox)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.NumlapsInput = QSpinBox(self.CircuitraceSettingsGroupbox)
        self.NumlapsInput.setObjectName(u"NumlapsInput")
        self.NumlapsInput.setMinimum(1)
        self.NumlapsInput.setMaximum(50)
        self.NumlapsInput.setValue(4)

        self.gridLayout_29.addWidget(self.NumlapsInput, 1, 0, 1, 1)

        self.CountdowntimeInput = QSpinBox(self.CircuitraceSettingsGroupbox)
        self.CountdowntimeInput.setObjectName(u"CountdowntimeInput")
        self.CountdowntimeInput.setMinimum(15)
        self.CountdowntimeInput.setMaximum(9999)
        self.CountdowntimeInput.setValue(60)

        self.gridLayout_29.addWidget(self.CountdowntimeInput, 3, 0, 1, 1)

        self.label_2 = QLabel(self.CircuitraceSettingsGroupbox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_29.addWidget(self.label_2, 0, 0, 1, 1)

        self.UsemaplapsCheckbox = QCheckBox(self.CircuitraceSettingsGroupbox)
        self.UsemaplapsCheckbox.setObjectName(u"UsemaplapsCheckbox")

        self.gridLayout_29.addWidget(self.UsemaplapsCheckbox, 1, 1, 1, 1)

        self.label_6 = QLabel(self.CircuitraceSettingsGroupbox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_29.addWidget(self.label_6, 2, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.CircuitraceSettingsGroupbox)

        self.verticalSpacer_7 = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_13.addWidget(self.scrollArea_8)

        self.HostGameTabwidget.addTab(self.tab_7, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_7 = QScrollArea(self.tab_2)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 748, 1041))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents_7)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.BattlemodSettingsCheckbox = QCheckBox(self.scrollAreaWidgetContents_7)
        self.BattlemodSettingsCheckbox.setObjectName(u"BattlemodSettingsCheckbox")

        self.verticalLayout_10.addWidget(self.BattlemodSettingsCheckbox)

        self.line = QFrame(self.scrollAreaWidgetContents_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line)

        self.BattlemodSettingsGroupbox = QGroupBox(self.scrollAreaWidgetContents_7)
        self.BattlemodSettingsGroupbox.setObjectName(u"BattlemodSettingsGroupbox")
        self.BattlemodSettingsGroupbox.setEnabled(False)
        self.gridLayout_22 = QGridLayout(self.BattlemodSettingsGroupbox)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_42 = QLabel(self.BattlemodSettingsGroupbox)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_22.addWidget(self.label_42, 19, 0, 1, 1)

        self.Battle_recoveryjumpCheckbox = QCheckBox(self.BattlemodSettingsGroupbox)
        self.Battle_recoveryjumpCheckbox.setObjectName(u"Battle_recoveryjumpCheckbox")

        self.gridLayout_22.addWidget(self.Battle_recoveryjumpCheckbox, 5, 1, 1, 1)

        self.groupBox_26 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_54 = QGridLayout(self.groupBox_26)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.label_53 = QLabel(self.groupBox_26)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_54.addWidget(self.label_53, 4, 0, 1, 1)

        self.label_50 = QLabel(self.groupBox_26)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_54.addWidget(self.label_50, 4, 1, 1, 1)

        self.Battle_preroundCheckbox = QCheckBox(self.groupBox_26)
        self.Battle_preroundCheckbox.setObjectName(u"Battle_preroundCheckbox")

        self.gridLayout_54.addWidget(self.Battle_preroundCheckbox, 10, 0, 1, 1)

        self.Battle_collisionsCheckbox = QCheckBox(self.groupBox_26)
        self.Battle_collisionsCheckbox.setObjectName(u"Battle_collisionsCheckbox")

        self.gridLayout_54.addWidget(self.Battle_collisionsCheckbox, 8, 0, 1, 1)

        self.Battle_shieldstocksCheckbox = QCheckBox(self.groupBox_26)
        self.Battle_shieldstocksCheckbox.setObjectName(u"Battle_shieldstocksCheckbox")

        self.gridLayout_54.addWidget(self.Battle_shieldstocksCheckbox, 9, 1, 1, 1)

        self.Battle_collisiontimerInput = QSpinBox(self.groupBox_26)
        self.Battle_collisiontimerInput.setObjectName(u"Battle_collisiontimerInput")
        self.Battle_collisiontimerInput.setMinimum(1)
        self.Battle_collisiontimerInput.setMaximum(105)
        self.Battle_collisiontimerInput.setValue(7)

        self.gridLayout_54.addWidget(self.Battle_collisiontimerInput, 1, 0, 1, 1)

        self.Battle_specialCheckbox = QCheckBox(self.groupBox_26)
        self.Battle_specialCheckbox.setObjectName(u"Battle_specialCheckbox")

        self.gridLayout_54.addWidget(self.Battle_specialCheckbox, 9, 0, 1, 1)

        self.Battle_launchfactorInput = QSpinBox(self.groupBox_26)
        self.Battle_launchfactorInput.setObjectName(u"Battle_launchfactorInput")
        self.Battle_launchfactorInput.setMinimum(1)
        self.Battle_launchfactorInput.setMaximum(20)
        self.Battle_launchfactorInput.setValue(7)

        self.gridLayout_54.addWidget(self.Battle_launchfactorInput, 5, 0, 1, 1)

        self.Battle_trainingCombobox = QComboBox(self.groupBox_26)
        self.Battle_trainingCombobox.addItem("")
        self.Battle_trainingCombobox.addItem("")
        self.Battle_trainingCombobox.addItem("")
        self.Battle_trainingCombobox.setObjectName(u"Battle_trainingCombobox")

        self.gridLayout_54.addWidget(self.Battle_trainingCombobox, 5, 1, 1, 1)

        self.Battle_slipstreamsheckbox = QCheckBox(self.groupBox_26)
        self.Battle_slipstreamsheckbox.setObjectName(u"Battle_slipstreamsheckbox")

        self.gridLayout_54.addWidget(self.Battle_slipstreamsheckbox, 8, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_26)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_54.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_54 = QLabel(self.groupBox_26)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_54.addWidget(self.label_54, 0, 1, 1, 1)

        self.Battle_maxrespawntimeInput = QSpinBox(self.groupBox_26)
        self.Battle_maxrespawntimeInput.setObjectName(u"Battle_maxrespawntimeInput")
        self.Battle_maxrespawntimeInput.setMinimum(3)
        self.Battle_maxrespawntimeInput.setMaximum(30)
        self.Battle_maxrespawntimeInput.setValue(5)

        self.gridLayout_54.addWidget(self.Battle_maxrespawntimeInput, 1, 1, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_26, 9, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.gridLayout_52 = QGridLayout(self.groupBox_25)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_45 = QLabel(self.groupBox_25)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_52.addWidget(self.label_45, 2, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_25)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_52.addWidget(self.label_44, 0, 0, 1, 1)

        self.Survival_livesInput = QSpinBox(self.groupBox_25)
        self.Survival_livesInput.setObjectName(u"Survival_livesInput")
        self.Survival_livesInput.setMinimum(1)
        self.Survival_livesInput.setValue(3)

        self.gridLayout_52.addWidget(self.Survival_livesInput, 1, 0, 1, 1)

        self.Survival_revengeCombobox = QComboBox(self.groupBox_25)
        self.Survival_revengeCombobox.addItem("")
        self.Survival_revengeCombobox.addItem("")
        self.Survival_revengeCombobox.addItem("")
        self.Survival_revengeCombobox.setObjectName(u"Survival_revengeCombobox")

        self.gridLayout_52.addWidget(self.Survival_revengeCombobox, 3, 0, 1, 1)

        self.Battle_startringsInput = QSpinBox(self.groupBox_25)
        self.Battle_startringsInput.setObjectName(u"Battle_startringsInput")
        self.Battle_startringsInput.setMinimum(1)
        self.Battle_startringsInput.setMaximum(999)
        self.Battle_startringsInput.setValue(50)

        self.gridLayout_52.addWidget(self.Battle_startringsInput, 1, 1, 1, 1)

        self.label_56 = QLabel(self.groupBox_25)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_52.addWidget(self.label_56, 0, 1, 1, 1)

        self.Survival_suddendeathCheckbox = QCheckBox(self.groupBox_25)
        self.Survival_suddendeathCheckbox.setObjectName(u"Survival_suddendeathCheckbox")
        self.Survival_suddendeathCheckbox.setChecked(True)

        self.gridLayout_52.addWidget(self.Survival_suddendeathCheckbox, 3, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_52.addItem(self.verticalSpacer_11, 4, 0, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_25, 9, 1, 1, 1)

        self.Battle_coyotefactorInput = QSpinBox(self.BattlemodSettingsGroupbox)
        self.Battle_coyotefactorInput.setObjectName(u"Battle_coyotefactorInput")
        self.Battle_coyotefactorInput.setMaximum(15)
        self.Battle_coyotefactorInput.setValue(15)

        self.gridLayout_22.addWidget(self.Battle_coyotefactorInput, 4, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_35 = QGridLayout(self.groupBox_16)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.Item_rateCombobox = QComboBox(self.groupBox_16)
        self.Item_rateCombobox.addItem("")
        self.Item_rateCombobox.addItem("")
        self.Item_rateCombobox.addItem("")
        self.Item_rateCombobox.setObjectName(u"Item_rateCombobox")

        self.gridLayout_35.addWidget(self.Item_rateCombobox, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_16)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_35.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_16)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_35.addWidget(self.label_22, 2, 1, 1, 1)

        self.Item_typeCombobox = QComboBox(self.groupBox_16)
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.addItem("")
        self.Item_typeCombobox.setObjectName(u"Item_typeCombobox")

        self.gridLayout_35.addWidget(self.Item_typeCombobox, 3, 1, 1, 1)

        self.Item_localCheckbox = QCheckBox(self.groupBox_16)
        self.Item_localCheckbox.setObjectName(u"Item_localCheckbox")

        self.gridLayout_35.addWidget(self.Item_localCheckbox, 4, 1, 1, 1)

        self.Item_globalCheckbox = QCheckBox(self.groupBox_16)
        self.Item_globalCheckbox.setObjectName(u"Item_globalCheckbox")

        self.gridLayout_35.addWidget(self.Item_globalCheckbox, 4, 0, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_16, 1, 0, 5, 1)

        self.groupBox_27 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.gridLayout_53 = QGridLayout(self.groupBox_27)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.Cp_radiusInput = QSpinBox(self.groupBox_27)
        self.Cp_radiusInput.setObjectName(u"Cp_radiusInput")
        self.Cp_radiusInput.setMaximum(359)

        self.gridLayout_53.addWidget(self.Cp_radiusInput, 7, 0, 1, 1)

        self.Cp_meterInput = QSpinBox(self.groupBox_27)
        self.Cp_meterInput.setObjectName(u"Cp_meterInput")

        self.gridLayout_53.addWidget(self.Cp_meterInput, 1, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox_27)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_53.addWidget(self.label_47, 0, 1, 1, 1)

        self.Cp_bonusInput = QSpinBox(self.groupBox_27)
        self.Cp_bonusInput.setObjectName(u"Cp_bonusInput")
        self.Cp_bonusInput.setMaximum(100000)
        self.Cp_bonusInput.setValue(99)

        self.gridLayout_53.addWidget(self.Cp_bonusInput, 5, 0, 1, 2)

        self.groupBox_28 = QGroupBox(self.groupBox_27)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.gridLayout_55 = QGridLayout(self.groupBox_28)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.Cp_spawnrailInput = QCheckBox(self.groupBox_28)
        self.Cp_spawnrailInput.setObjectName(u"Cp_spawnrailInput")

        self.gridLayout_55.addWidget(self.Cp_spawnrailInput, 1, 2, 1, 1)

        self.Cp_spawnscatterInput = QCheckBox(self.groupBox_28)
        self.Cp_spawnscatterInput.setObjectName(u"Cp_spawnscatterInput")

        self.gridLayout_55.addWidget(self.Cp_spawnscatterInput, 1, 3, 1, 1)

        self.Cp_spawnbounceInput = QCheckBox(self.groupBox_28)
        self.Cp_spawnbounceInput.setObjectName(u"Cp_spawnbounceInput")

        self.gridLayout_55.addWidget(self.Cp_spawnbounceInput, 0, 2, 1, 1)

        self.Cp_spawnbombInput = QCheckBox(self.groupBox_28)
        self.Cp_spawnbombInput.setObjectName(u"Cp_spawnbombInput")

        self.gridLayout_55.addWidget(self.Cp_spawnbombInput, 0, 3, 1, 1)

        self.Cp_spawngrenadeInput = QCheckBox(self.groupBox_28)
        self.Cp_spawngrenadeInput.setObjectName(u"Cp_spawngrenadeInput")

        self.gridLayout_55.addWidget(self.Cp_spawngrenadeInput, 1, 1, 1, 1)

        self.Cp_spawninfinityInput = QCheckBox(self.groupBox_28)
        self.Cp_spawninfinityInput.setObjectName(u"Cp_spawninfinityInput")

        self.gridLayout_55.addWidget(self.Cp_spawninfinityInput, 0, 0, 1, 1)

        self.Cp_spawnautoInput = QCheckBox(self.groupBox_28)
        self.Cp_spawnautoInput.setObjectName(u"Cp_spawnautoInput")

        self.gridLayout_55.addWidget(self.Cp_spawnautoInput, 0, 1, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_28, 11, 0, 1, 2)

        self.Cp_heightInput = QSpinBox(self.groupBox_27)
        self.Cp_heightInput.setObjectName(u"Cp_heightInput")
        self.Cp_heightInput.setMinimum(-1)
        self.Cp_heightInput.setMaximum(4)

        self.gridLayout_53.addWidget(self.Cp_heightInput, 7, 1, 1, 1)

        self.label_43 = QLabel(self.groupBox_27)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_53.addWidget(self.label_43, 6, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_27)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_53.addWidget(self.label_48, 4, 0, 1, 1)

        self.label_49 = QLabel(self.groupBox_27)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_53.addWidget(self.label_49, 6, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox_27)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_53.addWidget(self.label_46, 0, 0, 1, 1)

        self.Cp_waitInput = QSpinBox(self.groupBox_27)
        self.Cp_waitInput.setObjectName(u"Cp_waitInput")

        self.gridLayout_53.addWidget(self.Cp_waitInput, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_27)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_53.addWidget(self.label_18, 8, 0, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_27, 10, 0, 1, 2)

        self.Battle_coyotetimeInput = QSpinBox(self.BattlemodSettingsGroupbox)
        self.Battle_coyotetimeInput.setObjectName(u"Battle_coyotetimeInput")
        self.Battle_coyotetimeInput.setMinimum(1)

        self.gridLayout_22.addWidget(self.Battle_coyotetimeInput, 2, 1, 1, 1)

        self.groupBox_29 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.gridLayout_50 = QGridLayout(self.groupBox_29)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.Ctf_flagrespawn_graceperiodInput = QSpinBox(self.groupBox_29)
        self.Ctf_flagrespawn_graceperiodInput.setObjectName(u"Ctf_flagrespawn_graceperiodInput")
        self.Ctf_flagrespawn_graceperiodInput.setMaximum(15)
        self.Ctf_flagrespawn_graceperiodInput.setValue(6)

        self.gridLayout_50.addWidget(self.Ctf_flagrespawn_graceperiodInput, 2, 2, 1, 1)

        self.Ctf_flagdrop_graceperiodInput = QSpinBox(self.groupBox_29)
        self.Ctf_flagdrop_graceperiodInput.setObjectName(u"Ctf_flagdrop_graceperiodInput")
        self.Ctf_flagdrop_graceperiodInput.setMaximum(3)
        self.Ctf_flagdrop_graceperiodInput.setValue(2)

        self.gridLayout_50.addWidget(self.Ctf_flagdrop_graceperiodInput, 2, 1, 1, 1)

        self.label_38 = QLabel(self.groupBox_29)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_50.addWidget(self.label_38, 1, 1, 1, 1)

        self.label_39 = QLabel(self.groupBox_29)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_50.addWidget(self.label_39, 1, 2, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_29, 14, 0, 1, 1)

        self.label_20 = QLabel(self.BattlemodSettingsGroupbox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_20, 7, 0, 1, 2)

        self.label_36 = QLabel(self.BattlemodSettingsGroupbox)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_22.addWidget(self.label_36, 1, 1, 1, 1)

        self.groupBox_30 = QGroupBox(self.BattlemodSettingsGroupbox)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_51 = QGridLayout(self.groupBox_30)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_40 = QLabel(self.groupBox_30)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_51.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_30)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_51.addWidget(self.label_41, 0, 1, 1, 1)

        self.Diamond_capture_timeInput = QSpinBox(self.groupBox_30)
        self.Diamond_capture_timeInput.setObjectName(u"Diamond_capture_timeInput")
        self.Diamond_capture_timeInput.setMinimum(10)
        self.Diamond_capture_timeInput.setMaximum(60)
        self.Diamond_capture_timeInput.setValue(30)

        self.gridLayout_51.addWidget(self.Diamond_capture_timeInput, 1, 0, 1, 1)

        self.Diamond_capture_bonusInput = QSpinBox(self.groupBox_30)
        self.Diamond_capture_bonusInput.setObjectName(u"Diamond_capture_bonusInput")
        self.Diamond_capture_bonusInput.setMaximum(100000)
        self.Diamond_capture_bonusInput.setValue(1000)

        self.gridLayout_51.addWidget(self.Diamond_capture_bonusInput, 1, 1, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_30, 14, 1, 1, 1)

        self.Battle_addoptionsInput = QLineEdit(self.BattlemodSettingsGroupbox)
        self.Battle_addoptionsInput.setObjectName(u"Battle_addoptionsInput")

        self.gridLayout_22.addWidget(self.Battle_addoptionsInput, 20, 0, 1, 2)

        self.label_37 = QLabel(self.BattlemodSettingsGroupbox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_22.addWidget(self.label_37, 3, 1, 1, 1)

        self.line_3 = QFrame(self.BattlemodSettingsGroupbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_22.addWidget(self.line_3, 6, 0, 1, 2)


        self.verticalLayout_10.addWidget(self.BattlemodSettingsGroupbox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_7.addWidget(self.scrollArea_7)

        self.HostGameTabwidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.HostGameTabwidget)

        self.ExportServerScriptButton = QPushButton(self.HostGamePage)
        self.ExportServerScriptButton.setObjectName(u"ExportServerScriptButton")
        self.ExportServerScriptButton.setIcon(icon7)

        self.verticalLayout_8.addWidget(self.ExportServerScriptButton)

        self.GameContentStackedWidget.addWidget(self.HostGamePage)
        self.JoinGamePage = QWidget()
        self.JoinGamePage.setObjectName(u"JoinGamePage")
        self.verticalLayout_9 = QVBoxLayout(self.JoinGamePage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.GameTabView = QTabWidget(self.JoinGamePage)
        self.GameTabView.setObjectName(u"GameTabView")
        sizePolicy2.setHeightForWidth(self.GameTabView.sizePolicy().hasHeightForWidth())
        self.GameTabView.setSizePolicy(sizePolicy2)
        self.GameTabView.setTabShape(QTabWidget.Rounded)
        self.BrowseTab = QWidget()
        self.BrowseTab.setObjectName(u"BrowseTab")
        self.gridLayout_26 = QGridLayout(self.BrowseTab)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.RefreshButton = QPushButton(self.BrowseTab)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setIcon(icon)

        self.gridLayout_26.addWidget(self.RefreshButton, 0, 3, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MSStatusLabel = QLabel(self.BrowseTab)
        self.MSStatusLabel.setObjectName(u"MSStatusLabel")

        self.horizontalLayout_18.addWidget(self.MSStatusLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.SaveNetgameButton = QPushButton(self.BrowseTab)
        self.SaveNetgameButton.setObjectName(u"SaveNetgameButton")
        icon16 = QIcon()
        icon16.addFile(u":/assets/img/icons/bookmark-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveNetgameButton.setIcon(icon16)

        self.horizontalLayout_18.addWidget(self.SaveNetgameButton)

        self.BrowseNetgameJoinButton = QPushButton(self.BrowseTab)
        self.BrowseNetgameJoinButton.setObjectName(u"BrowseNetgameJoinButton")
        icon17 = QIcon()
        icon17.addFile(u":/assets/img/icons/media-playback-start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowseNetgameJoinButton.setIcon(icon17)

        self.horizontalLayout_18.addWidget(self.BrowseNetgameJoinButton)


        self.gridLayout_26.addLayout(self.horizontalLayout_18, 5, 0, 1, 4)

        self.MSSelectionLabel = QLabel(self.BrowseTab)
        self.MSSelectionLabel.setObjectName(u"MSSelectionLabel")

        self.gridLayout_26.addWidget(self.MSSelectionLabel, 0, 0, 1, 1)

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
        sizePolicy2.setHeightForWidth(self.BrowseNetgameTable.sizePolicy().hasHeightForWidth())
        self.BrowseNetgameTable.setSizePolicy(sizePolicy2)
        self.BrowseNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.BrowseNetgameTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.BrowseNetgameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.BrowseNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.BrowseNetgameTable.verticalHeader().setVisible(False)

        self.gridLayout_26.addWidget(self.BrowseNetgameTable, 1, 0, 1, 4)

        self.BrowseMSCombobox = QComboBox(self.BrowseTab)
        self.BrowseMSCombobox.addItem("")
        self.BrowseMSCombobox.setObjectName(u"BrowseMSCombobox")
        sizePolicy4.setHeightForWidth(self.BrowseMSCombobox.sizePolicy().hasHeightForWidth())
        self.BrowseMSCombobox.setSizePolicy(sizePolicy4)
        self.BrowseMSCombobox.setMinimumSize(QSize(80, 0))
        self.BrowseMSCombobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_26.addWidget(self.BrowseMSCombobox, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.GameTabView.addTab(self.BrowseTab, "")
        self.SavedNetgamesTab = QWidget()
        self.SavedNetgamesTab.setObjectName(u"SavedNetgamesTab")
        self.gridLayout_27 = QGridLayout(self.SavedNetgamesTab)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.DeleteServerButton = QPushButton(self.SavedNetgamesTab)
        self.DeleteServerButton.setObjectName(u"DeleteServerButton")
        self.DeleteServerButton.setIcon(icon10)

        self.gridLayout_27.addWidget(self.DeleteServerButton, 12, 3, 1, 1)

        self.ServerListLabel = QLabel(self.SavedNetgamesTab)
        self.ServerListLabel.setObjectName(u"ServerListLabel")

        self.gridLayout_27.addWidget(self.ServerListLabel, 3, 0, 1, 1)

        self.JoinServerLabel = QLabel(self.SavedNetgamesTab)
        self.JoinServerLabel.setObjectName(u"JoinServerLabel")

        self.gridLayout_27.addWidget(self.JoinServerLabel, 9, 0, 1, 1)

        self.AddServerButton = QPushButton(self.SavedNetgamesTab)
        self.AddServerButton.setObjectName(u"AddServerButton")
        self.AddServerButton.setIcon(icon4)

        self.gridLayout_27.addWidget(self.AddServerButton, 12, 2, 1, 1)

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
        sizePolicy2.setHeightForWidth(self.SavedNetgameTable.sizePolicy().hasHeightForWidth())
        self.SavedNetgameTable.setSizePolicy(sizePolicy2)
        self.SavedNetgameTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.SavedNetgameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SavedNetgameTable.horizontalHeader().setCascadingSectionResizes(True)
        self.SavedNetgameTable.verticalHeader().setVisible(False)
        self.SavedNetgameTable.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_27.addWidget(self.SavedNetgameTable, 11, 0, 1, 4)

        self.horizontalSpacer_10 = QSpacerItem(505, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_10, 12, 0, 1, 1)

        self.JoinBookmarkButton = QPushButton(self.SavedNetgamesTab)
        self.JoinBookmarkButton.setObjectName(u"JoinBookmarkButton")
        self.JoinBookmarkButton.setSizeIncrement(QSize(0, 0))
        self.JoinBookmarkButton.setIcon(icon17)

        self.gridLayout_27.addWidget(self.JoinBookmarkButton, 12, 1, 1, 1)

        self.JoinAddressInput = QLineEdit(self.SavedNetgamesTab)
        self.JoinAddressInput.setObjectName(u"JoinAddressInput")
        sizePolicy4.setHeightForWidth(self.JoinAddressInput.sizePolicy().hasHeightForWidth())
        self.JoinAddressInput.setSizePolicy(sizePolicy4)
        self.JoinAddressInput.setPlaceholderText(u"IP Address")

        self.gridLayout_27.addWidget(self.JoinAddressInput, 5, 0, 1, 1)

        self.JoinAddressButton = QPushButton(self.SavedNetgamesTab)
        self.JoinAddressButton.setObjectName(u"JoinAddressButton")
        self.JoinAddressButton.setIcon(icon17)

        self.gridLayout_27.addWidget(self.JoinAddressButton, 5, 1, 1, 3)

        self.frame_10 = QFrame(self.SavedNetgamesTab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_27.addWidget(self.frame_10, 6, 0, 1, 4)

        self.GameTabView.addTab(self.SavedNetgamesTab, "")
        self.masterservers = QWidget()
        self.masterservers.setObjectName(u"masterservers")
        self.masterservers.setMinimumSize(QSize(824, 0))
        self.gridLayout_28 = QGridLayout(self.masterservers)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.scrollArea_11 = QScrollArea(self.masterservers)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 793, 270))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_37 = QGridLayout(self.groupBox_17)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.ConfigrepoadLabel = QLabel(self.groupBox_17)
        self.ConfigrepoadLabel.setObjectName(u"ConfigrepoadLabel")

        self.gridLayout_37.addWidget(self.ConfigrepoadLabel, 1, 0, 1, 1)

        self.MSRemoveButton = QPushButton(self.groupBox_17)
        self.MSRemoveButton.setObjectName(u"MSRemoveButton")
        self.MSRemoveButton.setIcon(icon10)

        self.gridLayout_37.addWidget(self.MSRemoveButton, 1, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_9, 1, 2, 1, 1)

        self.MSAddButton = QPushButton(self.groupBox_17)
        self.MSAddButton.setObjectName(u"MSAddButton")
        self.MSAddButton.setIcon(icon4)

        self.gridLayout_37.addWidget(self.MSAddButton, 1, 4, 1, 1)

        self.MSListSaveButton = QPushButton(self.groupBox_17)
        self.MSListSaveButton.setObjectName(u"MSListSaveButton")
        self.MSListSaveButton.setIcon(icon7)

        self.gridLayout_37.addWidget(self.MSListSaveButton, 1, 3, 1, 1)

        self.MSVisitrepoButton = QPushButton(self.groupBox_17)
        self.MSVisitrepoButton.setObjectName(u"MSVisitrepoButton")
        self.MSVisitrepoButton.setIcon(icon1)

        self.gridLayout_37.addWidget(self.MSVisitrepoButton, 1, 1, 1, 1)

        self.MasterServersTable = QTableWidget(self.groupBox_17)
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
        self.MasterServersTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.MasterServersTable.verticalHeader().setVisible(False)

        self.gridLayout_37.addWidget(self.MasterServersTable, 0, 0, 1, 6)


        self.verticalLayout_21.addWidget(self.groupBox_17)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 1, 3, 1, 1)

        self.SnitchsrcCombobox = QComboBox(self.groupBox_3)
        self.SnitchsrcCombobox.setObjectName(u"SnitchsrcCombobox")

        self.gridLayout_6.addWidget(self.SnitchsrcCombobox, 2, 1, 1, 1)

        self.SnitchmsgLabel = QLabel(self.groupBox_3)
        self.SnitchmsgLabel.setObjectName(u"SnitchmsgLabel")
        self.SnitchmsgLabel.setFont(font2)
        self.SnitchmsgLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.SnitchmsgLabel, 3, 1, 1, 3)

        self.SnitchdestCombobox = QComboBox(self.groupBox_3)
        self.SnitchdestCombobox.setObjectName(u"SnitchdestCombobox")
        self.SnitchdestCombobox.setEditable(True)

        self.gridLayout_6.addWidget(self.SnitchdestCombobox, 2, 3, 1, 1)

        self.SnitchButton = QPushButton(self.groupBox_3)
        self.SnitchButton.setObjectName(u"SnitchButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.SnitchButton.sizePolicy().hasHeightForWidth())
        self.SnitchButton.setSizePolicy(sizePolicy7)
        self.SnitchButton.setIcon(icon17)

        self.gridLayout_6.addWidget(self.SnitchButton, 2, 2, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 1, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.groupBox_3)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.gridLayout_28.addWidget(self.scrollArea_11, 0, 0, 1, 1)

        self.GameTabView.addTab(self.masterservers, "")

        self.verticalLayout_9.addWidget(self.GameTabView)

        self.GameContentStackedWidget.addWidget(self.JoinGamePage)

        self.gridLayout_19.addWidget(self.GameContentStackedWidget, 2, 0, 1, 1)

        self.splitter.addWidget(self.GamePageContentFrame)

        self.gridLayout_16.addWidget(self.splitter, 0, 1, 1, 1)


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
        sizePolicy5.setHeightForWidth(self.GameProfileComboBox.sizePolicy().hasHeightForWidth())
        self.GameProfileComboBox.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.GameProfileComboBox, 1, 0, 1, 7)

        self.ProfilesRefreshButton = QToolButton(self.GamePlayFrame)
        self.ProfilesRefreshButton.setObjectName(u"ProfilesRefreshButton")
        self.ProfilesRefreshButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.ProfilesRefreshButton, 2, 0, 1, 1)

        self.ProfilesDeleteButton = QToolButton(self.GamePlayFrame)
        self.ProfilesDeleteButton.setObjectName(u"ProfilesDeleteButton")
        self.ProfilesDeleteButton.setEnabled(False)
        self.ProfilesDeleteButton.setIcon(icon10)

        self.gridLayout_3.addWidget(self.ProfilesDeleteButton, 2, 6, 1, 1)

        self.ProfilesAddButton = QToolButton(self.GamePlayFrame)
        self.ProfilesAddButton.setObjectName(u"ProfilesAddButton")
        self.ProfilesAddButton.setIcon(icon4)

        self.gridLayout_3.addWidget(self.ProfilesAddButton, 2, 5, 1, 1)

        self.GamePlayButton = QPushButton(self.GamePlayFrame)
        self.GamePlayButton.setObjectName(u"GamePlayButton")
        sizePolicy3.setHeightForWidth(self.GamePlayButton.sizePolicy().hasHeightForWidth())
        self.GamePlayButton.setSizePolicy(sizePolicy3)
        self.GamePlayButton.setMaximumSize(QSize(240, 38))
        self.GamePlayButton.setIcon(icon17)

        self.gridLayout_3.addWidget(self.GamePlayButton, 1, 10, 2, 1)

        self.ProfilesSaveButton = QToolButton(self.GamePlayFrame)
        self.ProfilesSaveButton.setObjectName(u"ProfilesSaveButton")
        self.ProfilesSaveButton.setIcon(icon7)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1030, 555))
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
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget_2 = QTabWidget(self.SettingsPage)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_11 = QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea = QScrollArea(self.tab_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 559, 293))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_39 = QGridLayout(self.groupBox_19)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.SaveFilesToConfigToggle = QCheckBox(self.groupBox_19)
        self.SaveFilesToConfigToggle.setObjectName(u"SaveFilesToConfigToggle")
        self.SaveFilesToConfigToggle.setChecked(False)

        self.gridLayout_39.addWidget(self.SaveFilesToConfigToggle, 3, 0, 1, 1)

        self.ProfileDirBrowseButton = QPushButton(self.groupBox_19)
        self.ProfileDirBrowseButton.setObjectName(u"ProfileDirBrowseButton")
        self.ProfileDirBrowseButton.setIcon(icon6)

        self.gridLayout_39.addWidget(self.ProfileDirBrowseButton, 1, 1, 1, 1)

        self.ProfileDirInput = QLineEdit(self.groupBox_19)
        self.ProfileDirInput.setObjectName(u"ProfileDirInput")

        self.gridLayout_39.addWidget(self.ProfileDirInput, 1, 0, 1, 1)

        self.ProfileDirLabel = QLabel(self.groupBox_19)
        self.ProfileDirLabel.setObjectName(u"ProfileDirLabel")

        self.gridLayout_39.addWidget(self.ProfileDirLabel, 0, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_39.addWidget(self.label_28, 2, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.groupBox_19)

        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_38 = QGridLayout(self.groupBox_18)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_19 = QLabel(self.groupBox_18)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_38.addWidget(self.label_19, 0, 0, 1, 1)

        self.UseragentInput = QLineEdit(self.groupBox_18)
        self.UseragentInput.setObjectName(u"UseragentInput")

        self.gridLayout_38.addWidget(self.UseragentInput, 1, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_38.addWidget(self.label_27, 2, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.groupBox_18)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_26)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 1, 0, 1, 1)

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
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy8)

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.ModsourceCheckLabel = QLabel(self.tab_6)
        self.ModsourceCheckLabel.setObjectName(u"ModsourceCheckLabel")

        self.verticalLayout_6.addWidget(self.ModsourceCheckLabel)

        self.ModsourceMBCheckbox = QCheckBox(self.tab_6)
        self.ModsourceMBCheckbox.setObjectName(u"ModsourceMBCheckbox")
        self.ModsourceMBCheckbox.setIcon(icon2)
        self.ModsourceMBCheckbox.setChecked(True)

        self.verticalLayout_6.addWidget(self.ModsourceMBCheckbox)

        self.ModsourceGamebananaCheckbox = QCheckBox(self.tab_6)
        self.ModsourceGamebananaCheckbox.setObjectName(u"ModsourceGamebananaCheckbox")
        self.ModsourceGamebananaCheckbox.setEnabled(True)
        icon18 = QIcon()
        icon18.addFile(u":/assets/img/icons/gamebanana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceGamebananaCheckbox.setIcon(icon18)

        self.verticalLayout_6.addWidget(self.ModsourceGamebananaCheckbox)

        self.ModsourceSkybaseCheckbox = QCheckBox(self.tab_6)
        self.ModsourceSkybaseCheckbox.setObjectName(u"ModsourceSkybaseCheckbox")
        self.ModsourceSkybaseCheckbox.setEnabled(True)
        icon19 = QIcon()
        icon19.addFile(u":/assets/img/icons/skybase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceSkybaseCheckbox.setIcon(icon19)

        self.verticalLayout_6.addWidget(self.ModsourceSkybaseCheckbox)

        self.ModsourceWSBlueCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSBlueCheckbox.setObjectName(u"ModsourceWSBlueCheckbox")
        icon20 = QIcon()
        icon20.addFile(u":/assets/img/icons/wsblue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceWSBlueCheckbox.setIcon(icon20)

        self.verticalLayout_6.addWidget(self.ModsourceWSBlueCheckbox)

        self.ModsourceWSRedCheckbox = QCheckBox(self.tab_6)
        self.ModsourceWSRedCheckbox.setObjectName(u"ModsourceWSRedCheckbox")
        icon21 = QIcon()
        icon21.addFile(u":/assets/img/icons/wsred.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModsourceWSRedCheckbox.setIcon(icon21)

        self.verticalLayout_6.addWidget(self.ModsourceWSRedCheckbox)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_8 = QGridLayout(self.tab_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.RSSRemoveButton = QPushButton(self.tab_9)
        self.RSSRemoveButton.setObjectName(u"RSSRemoveButton")
        self.RSSRemoveButton.setEnabled(False)
        self.RSSRemoveButton.setIcon(icon10)

        self.gridLayout_8.addWidget(self.RSSRemoveButton, 4, 2, 1, 1)

        self.RSSMoveupButton = QPushButton(self.tab_9)
        self.RSSMoveupButton.setObjectName(u"RSSMoveupButton")
        self.RSSMoveupButton.setEnabled(False)
        self.RSSMoveupButton.setIcon(icon14)

        self.gridLayout_8.addWidget(self.RSSMoveupButton, 3, 0, 1, 1)

        self.NewssourceLabel = QLabel(self.tab_9)
        self.NewssourceLabel.setObjectName(u"NewssourceLabel")

        self.gridLayout_8.addWidget(self.NewssourceLabel, 0, 0, 1, 3)

        self.RSSAddButton = QPushButton(self.tab_9)
        self.RSSAddButton.setObjectName(u"RSSAddButton")
        self.RSSAddButton.setIcon(icon4)

        self.gridLayout_8.addWidget(self.RSSAddButton, 3, 2, 1, 1)

        self.RSSMovedownButton = QPushButton(self.tab_9)
        self.RSSMovedownButton.setObjectName(u"RSSMovedownButton")
        self.RSSMovedownButton.setEnabled(False)
        self.RSSMovedownButton.setIcon(icon8)

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

        self.verticalLayout_12.addWidget(self.tabWidget_2)

        self.SaveSettingsButton = QPushButton(self.SettingsPage)
        self.SaveSettingsButton.setObjectName(u"SaveSettingsButton")
        self.SaveSettingsButton.setIcon(icon7)

        self.verticalLayout_12.addWidget(self.SaveSettingsButton)

        self.MainTabsStackedWidget.addWidget(self.SettingsPage)

        self.horizontalLayout_2.addWidget(self.MainTabsStackedWidget)


        self.gridLayout_32.addWidget(self.MainAreaFrame, 1, 0, 1, 1)

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
        icon22 = QIcon()
        icon22.addFile(u":/assets/img/icons/news.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NewsTabButton.setIcon(icon22)
        self.NewsTabButton.setIconSize(QSize(48, 48))
        self.NewsTabButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.NewsTabButton)

        self.GameTabButton = QToolButton(self.DockTabFrame)
        self.GameTabButton.setObjectName(u"GameTabButton")
        sizePolicy6.setHeightForWidth(self.GameTabButton.sizePolicy().hasHeightForWidth())
        self.GameTabButton.setSizePolicy(sizePolicy6)
        self.GameTabButton.setMaximumSize(QSize(16777215, 16777215))
        self.GameTabButton.setIcon(icon3)
        self.GameTabButton.setIconSize(QSize(48, 48))
        self.GameTabButton.setCheckable(True)
        self.GameTabButton.setChecked(True)

        self.horizontalLayout.addWidget(self.GameTabButton)

        self.HelpTabButton = QToolButton(self.DockTabFrame)
        self.HelpTabButton.setObjectName(u"HelpTabButton")
        self.HelpTabButton.setMaximumSize(QSize(16777215, 16777215))
        icon23 = QIcon()
        icon23.addFile(u":/assets/img/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpTabButton.setIcon(icon23)
        self.HelpTabButton.setIconSize(QSize(48, 48))
        self.HelpTabButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.HelpTabButton)

        self.SettingsTabButton = QToolButton(self.DockTabFrame)
        self.SettingsTabButton.setObjectName(u"SettingsTabButton")
        self.SettingsTabButton.setMaximumSize(QSize(16777215, 16777215))
        self.SettingsTabButton.setIcon(icon5)
        self.SettingsTabButton.setIconSize(QSize(48, 48))
        self.SettingsTabButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.SettingsTabButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_32.addWidget(self.DockTabFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTabsStackedWidget.setCurrentIndex(1)
        self.GameContentStackedWidget.setCurrentIndex(2)
        self.PlayerColorInput.setCurrentIndex(0)
        self.PlayerSkinInput.setCurrentIndex(0)
        self.GameSettingsTabWidget.setCurrentIndex(0)
        self.HostGameTabwidget.setCurrentIndex(0)
        self.AdvanceMapInput.setCurrentIndex(1)
        self.Battle_trainingCombobox.setCurrentIndex(0)
        self.Survival_revengeCombobox.setCurrentIndex(0)
        self.Item_rateCombobox.setCurrentIndex(1)
        self.GameTabView.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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

        self.PlayerSkinInfoText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dddd00;\">Sonic</span> is the fastest of the three, but also the hardest to control. Begginers beware, but experts will find Sonic very powerful.</p><p><span style=\" color:#dddd00;\">Ability:</span> Speed Thok<br/>Double jump to zoom forward with a huge burst of speed</p><p><span style=\" color:#dddd00;\">Tip:</span> Simply letting go of forward does not slow down in SRB2. To slow down, hold the opposite direction.</p></body></html>", None))
        self.PlayerSkinImage.setText("")
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

        self.PlayerColorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.PlayerSkinTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Skin", None))
        self.PlayerNameInput.setText("")
        self.PlayerNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"To pick non-standard characters, simply type their name in the field.", None))
        self.PlayerColorTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Skin Color", None))
        self.PlayerNameTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.PlayerSkinInput.setItemText(0, "")
        self.PlayerSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.PlayerSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.PlayerSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.PlayerSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.PlayerSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.PlayerSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.PlayerSkinInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"To pick non-standard skin colors, simply type their name in the field.", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Render Options", None))
        self.GameRendererSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.GameRendererSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"OpenGL", None))

        self.GameFullscreenSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.GameFullscreenSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Borderless fullscreen", None))
        self.GameFullscreenSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Windowed", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Executable", None))
        self.GameExecFilePathBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.GameExecFilePathInput.setText(QCoreApplication.translate("MainWindow", u"srb2win.exe", None))
        self.WineRadiobutton.setText(QCoreApplication.translate("MainWindow", u"WINE (Linux/macOS)", None))
        self.FlatpakRadiobutton.setText(QCoreApplication.translate("MainWindow", u"Flatpak (Linux)", None))
        self.NativeRadiobutton.setText(QCoreApplication.translate("MainWindow", u"Native EXE/ELF", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Audio Options", None))
        self.GameMusicSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Digital music", None))
        self.GameMusicSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Midi music", None))
        self.GameMusicSetting.setItemText(2, QCoreApplication.translate("MainWindow", u"Load music from a CD", None))
        self.GameMusicSetting.setItemText(3, QCoreApplication.translate("MainWindow", u"Disable music", None))

        self.GameSoundSetting.setItemText(0, QCoreApplication.translate("MainWindow", u"Enable sound", None))
        self.GameSoundSetting.setItemText(1, QCoreApplication.translate("MainWindow", u"Disable sound", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.GameHorizontalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<width>", None))
        self.GameResMultLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.GameVerticalResolutionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<height>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Launch settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SRB2 home directory (Windows)", None))
        self.HomePathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/path/to/liquidlauncher", None))
        self.GameArgsLabel.setText(QCoreApplication.translate("MainWindow", u"Custom Shell Parameters", None))
        self.HomePathBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Specify where SRB2 will look for it's assets (e.g. \"srb2.pk3\")", None))
        self.ExportClientScriptButton.setText(QCoreApplication.translate("MainWindow", u"Save Client Launch Script...", None))
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
        self.ModDirBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Download directory", None))
        self.ModDirInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Downloads/", None))
        self.ModTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Maps", None))
        self.ModTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Characters", None))
        self.ModTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Lua", None))
        self.ModTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Assets", None))
        self.ModTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Misc", None))


        __sortingEnabled3 = self.ModsList.isSortingEnabled()
        self.ModsList.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.ModsList.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"(Tip: You can also enable more sources in the settings)", None));
        self.ModsList.setSortingEnabled(__sortingEnabled3)

#if QT_CONFIG(tooltip)
        self.ModPageInput.setToolTip(QCoreApplication.translate("MainWindow", u"Page", None))
#endif // QT_CONFIG(tooltip)
        self.ModBrowserLabel.setText(QCoreApplication.translate("MainWindow", u"Mods", None))
        self.ModStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Select a category and click \"refresh\"", None))
#if QT_CONFIG(tooltip)
        self.RefreshModsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh Mods", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshModsButton.setText("")
#if QT_CONFIG(tooltip)
        self.DownloadModButton.setToolTip(QCoreApplication.translate("MainWindow", u"Coming soon. Hang in there, buddy!", None))
#endif // QT_CONFIG(tooltip)
        self.DownloadModButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.ModViewerLabel.setText(QCoreApplication.translate("MainWindow", u"Mod details", None))
        self.OpenPageButton.setText(QCoreApplication.translate("MainWindow", u"Visit Page", None))
        self.AdddownloadtolaunchmodsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Add finished download to launch mods", None))
        self.GameSettingsTabWidget.setTabText(self.GameSettingsTabWidget.indexOf(self.ModBrowserTab), QCoreApplication.translate("MainWindow", u"Browse online", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Server settings", None))
        self.RoomLabel.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.ServerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.RoomInput.setItemText(0, QCoreApplication.translate("MainWindow", u"No room/Offline", None))

#if QT_CONFIG(tooltip)
        self.MSRoomqueryrefreshButton.setToolTip(QCoreApplication.translate("MainWindow", u"Refres room query", None))
#endif // QT_CONFIG(tooltip)
        self.MSRoomqueryrefreshButton.setText("")
        self.AdminPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Admin Password", None))
        self.HostMSCombobox.setItemText(0, "")

        self.HostMSCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<default>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"(Press enter or click the button to query it's rooms)", None))
        self.HostMSLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"(Select a Master server to query it's rooms)", None))
        self.DedicatedServerToggle.setText(QCoreApplication.translate("MainWindow", u"Dedicated/headless Server", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Networking", None))
        self.BandwidthInput.setSuffix(QCoreApplication.translate("MainWindow", u" bytes/s", None))
        self.PortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.ExtraticLabel.setText(QCoreApplication.translate("MainWindow", u"Extra tics", None))
        self.BandwidthLabel.setText(QCoreApplication.translate("MainWindow", u"Bandwidth", None))
        self.ExtraticInput.setSuffix(QCoreApplication.translate("MainWindow", u" tics", None))
#if QT_CONFIG(tooltip)
        self.Ipv6Checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Listen for incoming IPv6 connections", None))
#endif // QT_CONFIG(tooltip)
        self.Ipv6Checkbox.setText(QCoreApplication.translate("MainWindow", u"IPv6 support", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Downloading", None))
        self.UploadToggle.setText(QCoreApplication.translate("MainWindow", u"Enable Add-On downloads", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Download speed", None))
        self.DownloadspeedInput.setSuffix(QCoreApplication.translate("MainWindow", u" packets/tic", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Max. file size", None))
        self.MaxsendInput.setSuffix(QCoreApplication.translate("MainWindow", u" KB", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Timeouts and synchronization", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Max. ping threshold", None))
        self.MaxpingInput.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Ping timeout threshold", None))
        self.NettimeoutInput.setSuffix(QCoreApplication.translate("MainWindow", u" tics", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Resynchronization attempts", None))
        self.UpnpCheckbox.setText(QCoreApplication.translate("MainWindow", u"Universal Plug and Play (uPnP) support", None))
        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.General), QCoreApplication.translate("MainWindow", u"General", None))
        self.ForceSkinLabel.setText(QCoreApplication.translate("MainWindow", u"Force Skin", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Map intermission time", None))
        self.MaxPlayersInput.setSuffix(QCoreApplication.translate("MainWindow", u" Players", None))
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
        self.RespawnitemCheckbox.setText(QCoreApplication.translate("MainWindow", u"Respawn items", None))
        self.JoinnextroundCheckbox.setText(QCoreApplication.translate("MainWindow", u"Only join at the beginning of a round", None))
        self.RestrictskinchangesCheckbox.setText(QCoreApplication.translate("MainWindow", u"Restrict skin changes", None))
        self.TailspickupCheckbox.setText(QCoreApplication.translate("MainWindow", u"Enable player pickup (tailspickup)", None))
        self.ForceSkinLabel_2.setText(QCoreApplication.translate("MainWindow", u"Item respawn time", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Gravity", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.SoniccdCheckbox.setText(QCoreApplication.translate("MainWindow", u"Replace flickies with flowers", None))
#if QT_CONFIG(tooltip)
        self.KillingdeadCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"75% chance to hit yourself upon enemy hit", None))
#endif // QT_CONFIG(tooltip)
        self.KillingdeadCheckbox.setText(QCoreApplication.translate("MainWindow", u"Killingdead mode", None))
        self.InttimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.AdvanceMapInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.AdvanceMapInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Next", None))
        self.AdvanceMapInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Random", None))

        self.GametypeLabel.setText(QCoreApplication.translate("MainWindow", u"Gametype", None))
        self.RespawnitemtimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.ForceSkinInput.setItemText(0, "")
        self.ForceSkinInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.ForceSkinInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Tails", None))
        self.ForceSkinInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Knuckles", None))
        self.ForceSkinInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Amy", None))
        self.ForceSkinInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Fang", None))
        self.ForceSkinInput.setItemText(6, QCoreApplication.translate("MainWindow", u"Metal Sonic", None))

        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Random monitor chances", None))
        self.ForceSkinLabel_15.setText(QCoreApplication.translate("MainWindow", u"Water shield", None))
        self.ForceSkinLabel_3.setText(QCoreApplication.translate("MainWindow", u"1-Up", None))
        self.ForceSkinLabel_8.setText(QCoreApplication.translate("MainWindow", u"Jump shield", None))
        self.ForceSkinLabel_14.setText(QCoreApplication.translate("MainWindow", u"Ring shield", None))
        self.ForceSkinLabel_9.setText(QCoreApplication.translate("MainWindow", u"Recycler", None))
        self.ForceSkinLabel_12.setText(QCoreApplication.translate("MainWindow", u"Super Sneakers", None))
        self.ForceSkinLabel_7.setText(QCoreApplication.translate("MainWindow", u"Force shield", None))
        self.ForceSkinLabel_11.setText(QCoreApplication.translate("MainWindow", u"Eggman", None))
        self.ForceSkinLabel_4.setText(QCoreApplication.translate("MainWindow", u"Bomb shield", None))
        self.ForceSkinLabel_10.setText(QCoreApplication.translate("MainWindow", u"Invincibility", None))
        self.ForceSkinLabel_28.setText(QCoreApplication.translate("MainWindow", u"Teleporter", None))
        self.ForceSkinLabel_27.setText(QCoreApplication.translate("MainWindow", u"Super ring", None))
        self.MaxPlayersLabel.setText(QCoreApplication.translate("MainWindow", u"Max. Players", None))
        self.AllowexitlevelCheckbox.setText(QCoreApplication.translate("MainWindow", u"Allow level exit", None))
        self.ExitmoveCheckbox.setText(QCoreApplication.translate("MainWindow", u"Allow movement after exit", None))
        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Game", None))
        self.CoopSettingsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Apply Co-op settings", None))
        self.CoopSettingsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Co-op settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Starting lives", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Available monitors (competitionboxes)", None))
        self.PlayersforexitCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"(0) One Player", None))
        self.PlayersforexitCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"(1) 1/4 of players", None))
        self.PlayersforexitCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"(2) Half of players", None))
        self.PlayersforexitCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"(3) 3/4 Players", None))
        self.PlayersforexitCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"(4) All Players", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Stage exit requirement (playersforexit)", None))
        self.CompetitionboxesCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"(0) Normal", None))
        self.CompetitionboxesCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"(1) Random", None))
        self.CompetitionboxesCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"(2) Teleporters", None))
        self.CompetitionboxesCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"(3) No monitors", None))

        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Co-op", None))
        self.RingslingerSettingsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Ringslinger Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Match scoring style", None))
        self.PowerstonesCheckbox.setText(QCoreApplication.translate("MainWindow", u"Enable Chaos Emeralds", None))
#if QT_CONFIG(tooltip)
        self.PointLimitInput.setToolTip(QCoreApplication.translate("MainWindow", u"Ringslinger score limit. 0 = no limit", None))
#endif // QT_CONFIG(tooltip)
        self.PointLimitInput.setSuffix(QCoreApplication.translate("MainWindow", u" points", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Team settings", None))
        self.ScrambleteamsCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Off (0)", None))
        self.ScrambleteamsCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Random (1)", None))
        self.ScrambleteamsCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Points (2)", None))

        self.ScrambleTeamsLabel.setText(QCoreApplication.translate("MainWindow", u"Scramble teams", None))
        self.AutobalanceCheckbox.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.AutobalanceCheckbox.setItemText(1, QCoreApplication.translate("MainWindow", u"1 Player", None))
        self.AutobalanceCheckbox.setItemText(2, QCoreApplication.translate("MainWindow", u"2 Players", None))
        self.AutobalanceCheckbox.setItemText(3, QCoreApplication.translate("MainWindow", u"3 Players", None))
        self.AutobalanceCheckbox.setItemText(4, QCoreApplication.translate("MainWindow", u"4 Players", None))

        self.FriendlyfireCheckbox.setText(QCoreApplication.translate("MainWindow", u"Friendly fire", None))
        self.FlagtimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Team balancing threshold", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CTF Flag decay", None))
        self.TimeLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Time Limit", None))
        self.PointLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Point Limit", None))
        self.MatchscoringCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"(0) Normal - 50 Point penalty for death", None))
        self.MatchscoringCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"(1) Classic - No death penalty; 25 points for shield break", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Available monitors (matchboxes)", None))
        self.DisableWeaponsToggle.setText(QCoreApplication.translate("MainWindow", u"Disable weapon rings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Respawn Delay", None))
        self.OvertimeCheckbox.setText(QCoreApplication.translate("MainWindow", u"Overtime", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.TouchtagCheckbox.setText(QCoreApplication.translate("MainWindow", u"Tag players by touch", None))
        self.RespawndelayInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
#if QT_CONFIG(tooltip)
        self.TimeLimitInput.setToolTip(QCoreApplication.translate("MainWindow", u"Time limit in minutes. 0 = no limit", None))
#endif // QT_CONFIG(tooltip)
        self.TimeLimitInput.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.MatchboxesCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"(0) Normal", None))
        self.MatchboxesCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"(1) Random monitors", None))
        self.MatchboxesCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"(2) Teleporter monitors", None))
        self.MatchboxesCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"(3) No monitors", None))

        self.SuddenDeathToggle.setText(QCoreApplication.translate("MainWindow", u"Sudden Death", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Hide and seek", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hiding time", None))
        self.HidetimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.RingslingerSettingsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Apply Ringslinger settings", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'CMU Serif Medium'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ringslinger</span> refers to all gamemodes that involve shooting rings in a first-person-shooter-like manner, namely:</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Match</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Team Match</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tag</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hide and Seek</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Capture The Flag</p></body></html>", None))
        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.Ringslinger), QCoreApplication.translate("MainWindow", u"Ringslinger", None))
        self.CircuitraceSettingsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Apply Circuit Race Settings", None))
        self.CircuitraceSettingsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Circuit Race Settings", None))
        self.NumlapsInput.setSuffix(QCoreApplication.translate("MainWindow", u" laps", None))
        self.CountdowntimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of Laps", None))
        self.UsemaplapsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Use map laps", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Countdown time", None))
        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Circuit Race", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'CMU Serif Medium'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Warning:</span> Battlemod is not an official game mode. Please make sure you've included the right PK3 in the launch mods section before adjusting settings here.</p></body></html>", None))
        self.BattlemodSettingsCheckbox.setText(QCoreApplication.translate("MainWindow", u" Apply Battlemod settings", None))
        self.BattlemodSettingsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Battlemod settings", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Additional options", None))
        self.Battle_recoveryjumpCheckbox.setText(QCoreApplication.translate("MainWindow", u"Enable recovery jumps", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Battle", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Launch factor", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Training mode", None))
        self.Battle_preroundCheckbox.setText(QCoreApplication.translate("MainWindow", u"Pre-rounds", None))
        self.Battle_collisionsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Collisions", None))
        self.Battle_shieldstocksCheckbox.setText(QCoreApplication.translate("MainWindow", u"Shield stocks", None))
        self.Battle_collisiontimerInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.Battle_specialCheckbox.setText(QCoreApplication.translate("MainWindow", u"Special", None))
        self.Battle_trainingCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Off (0)", None))
        self.Battle_trainingCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Spawn Tails doll (1)", None))
        self.Battle_trainingCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"??? (2)", None))

        self.Battle_slipstreamsheckbox.setText(QCoreApplication.translate("MainWindow", u"Slip streams", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Collision timer", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Max. respawn time", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Arena/Survival", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Revenge mode", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Lives", None))
        self.Survival_revengeCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"No revenge (0)", None))
        self.Survival_revengeCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Revenge without respawn (1)", None))
        self.Survival_revengeCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Revenge with respawn (2)", None))

#if QT_CONFIG(tooltip)
        self.Battle_startringsInput.setToolTip(QCoreApplication.translate("MainWindow", u"battle_startrings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip(QCoreApplication.translate("MainWindow", u"battle_startrings", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Starting rings", None))
        self.Survival_suddendeathCheckbox.setText(QCoreApplication.translate("MainWindow", u"Sudden death", None))
#if QT_CONFIG(tooltip)
        self.Battle_coyotefactorInput.setToolTip(QCoreApplication.translate("MainWindow", u"Jump factor for walking off ledges", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Item settings", None))
        self.Item_rateCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.Item_rateCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.Item_rateCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Item rate", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Item type", None))
        self.Item_typeCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"-1 No items", None))
        self.Item_typeCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.Item_typeCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.Item_typeCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"2", None))
        self.Item_typeCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"3", None))
        self.Item_typeCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"4", None))
        self.Item_typeCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"5", None))
        self.Item_typeCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"6", None))
        self.Item_typeCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"7", None))
        self.Item_typeCombobox.setItemText(9, QCoreApplication.translate("MainWindow", u"8", None))
        self.Item_typeCombobox.setItemText(10, QCoreApplication.translate("MainWindow", u"9", None))
        self.Item_typeCombobox.setItemText(11, QCoreApplication.translate("MainWindow", u"10", None))
        self.Item_typeCombobox.setItemText(12, QCoreApplication.translate("MainWindow", u"11", None))
        self.Item_typeCombobox.setItemText(13, QCoreApplication.translate("MainWindow", u"12", None))
        self.Item_typeCombobox.setItemText(14, QCoreApplication.translate("MainWindow", u"13", None))
        self.Item_typeCombobox.setItemText(15, QCoreApplication.translate("MainWindow", u"14", None))
        self.Item_typeCombobox.setItemText(16, QCoreApplication.translate("MainWindow", u"15", None))
        self.Item_typeCombobox.setItemText(17, QCoreApplication.translate("MainWindow", u"16", None))

        self.Item_localCheckbox.setText(QCoreApplication.translate("MainWindow", u"Local items", None))
        self.Item_globalCheckbox.setText(QCoreApplication.translate("MainWindow", u"Global items", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Capture Point", None))
#if QT_CONFIG(tooltip)
        self.Cp_radiusInput.setToolTip(QCoreApplication.translate("MainWindow", u"FRACUNITs are a custom unit within the doom engine. 1 FRACUNIT about 2.25cm", None))
#endif // QT_CONFIG(tooltip)
        self.Cp_radiusInput.setSuffix(QCoreApplication.translate("MainWindow", u" FRACUNITs", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Wait", None))
        self.Cp_bonusInput.setSuffix(QCoreApplication.translate("MainWindow", u" points", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Ring spawns", None))
        self.Cp_spawnrailInput.setText(QCoreApplication.translate("MainWindow", u"Rail rings", None))
        self.Cp_spawnscatterInput.setText(QCoreApplication.translate("MainWindow", u"Scatter rings", None))
        self.Cp_spawnbounceInput.setText(QCoreApplication.translate("MainWindow", u"Bounce rings", None))
        self.Cp_spawnbombInput.setText(QCoreApplication.translate("MainWindow", u"Bomb rings", None))
        self.Cp_spawngrenadeInput.setText(QCoreApplication.translate("MainWindow", u"Grenade rings", None))
        self.Cp_spawninfinityInput.setText(QCoreApplication.translate("MainWindow", u"Infinity rings", None))
        self.Cp_spawnautoInput.setText(QCoreApplication.translate("MainWindow", u"Auto rings", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Capture point height", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Capture bonus", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Capture radius", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Meter fill rate", None))
        self.Cp_waitInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"(FRACUNITs are custom to the doom engine. 1 FRACUNIT about 2.25cm)", None))
#if QT_CONFIG(tooltip)
        self.Battle_coyotetimeInput.setToolTip(QCoreApplication.translate("MainWindow", u"Time between walking off ledges and gravity kicking in", None))
#endif // QT_CONFIG(tooltip)
        self.Battle_coyotetimeInput.setSuffix(QCoreApplication.translate("MainWindow", u" frames", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Battle CTF", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Flag drop grace period", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Flag respawn grace period", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Gamemodes", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("MainWindow", u"Time between walking off ledges and gravity kicking in", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Coyote Time (Fight Club only)", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Diamond Hunt", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Capture time", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Capture bonus", None))
        self.Diamond_capture_timeInput.setSuffix(QCoreApplication.translate("MainWindow", u" seconds", None))
        self.Diamond_capture_bonusInput.setSuffix(QCoreApplication.translate("MainWindow", u" points", None))
        self.Battle_addoptionsInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+battledebug +devcam", None))
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("MainWindow", u"Jump factor for walking off ledges", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Coyote factor (Fight Club only)", None))
        self.HostGameTabwidget.setTabText(self.HostGameTabwidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Battlemod", None))
        self.ExportServerScriptButton.setText(QCoreApplication.translate("MainWindow", u"Save server launch script...", None))
#if QT_CONFIG(tooltip)
        self.RefreshButton.setToolTip(QCoreApplication.translate("MainWindow", u"Update", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshButton.setText("")
        self.MSStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Click \"Update\" to download a list of servers.", None))
        self.SaveNetgameButton.setText(QCoreApplication.translate("MainWindow", u"Bookmark", None))
        self.BrowseNetgameJoinButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.MSSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"Master Server", None))
        ___qtablewidgetitem = self.BrowseNetgameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.BrowseNetgameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Game", None));
        ___qtablewidgetitem2 = self.BrowseNetgameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Version", None));
        ___qtablewidgetitem3 = self.BrowseNetgameTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Room", None));
        ___qtablewidgetitem4 = self.BrowseNetgameTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Origin", None));

        __sortingEnabled4 = self.BrowseNetgameTable.isSortingEnabled()
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
        self.BrowseNetgameTable.setSortingEnabled(__sortingEnabled4)

        self.BrowseMSCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"ms.srb2.org", None))

        self.GameTabView.setTabText(self.GameTabView.indexOf(self.BrowseTab), QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.DeleteServerButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Bookmark", None))
#endif // QT_CONFIG(tooltip)
        self.ServerListLabel.setText(QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.JoinServerLabel.setText(QCoreApplication.translate("MainWindow", u"Join directly", None))
#if QT_CONFIG(tooltip)
        self.AddServerButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add Bookmark", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem10 = self.SavedNetgameTable.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.SavedNetgameTable.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem12 = self.SavedNetgameTable.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        self.JoinBookmarkButton.setText(QCoreApplication.translate("MainWindow", u"Join Bookmark", None))
        self.JoinAddressButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.GameTabView.setTabText(self.GameTabView.indexOf(self.SavedNetgamesTab), QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Master Servers", None))
        self.ConfigrepoadLabel.setText(QCoreApplication.translate("MainWindow", u"Looking for master servers?", None))
#if QT_CONFIG(tooltip)
        self.MSRemoveButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove selected Master Server", None))
#endif // QT_CONFIG(tooltip)
        self.MSRemoveButton.setText("")
#if QT_CONFIG(tooltip)
        self.MSAddButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add Master Server", None))
#endif // QT_CONFIG(tooltip)
        self.MSAddButton.setText("")
        self.MSListSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save List", None))
        self.MSVisitrepoButton.setText(QCoreApplication.translate("MainWindow", u"Config repo >>", None))
        ___qtablewidgetitem13 = self.MasterServersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem14 = self.MasterServersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem15 = self.MasterServersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"API", None));

        __sortingEnabled5 = self.MasterServersTable.isSortingEnabled()
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
        self.MasterServersTable.setSortingEnabled(__sortingEnabled5)

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"One-time snitch", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.SnitchsrcCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a source", None))
        self.SnitchmsgLabel.setText(QCoreApplication.translate("MainWindow", u"Select two servers and click the button to snitch.", None))
        self.SnitchdestCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destination URL", None))
#if QT_CONFIG(tooltip)
        self.SnitchButton.setToolTip(QCoreApplication.translate("MainWindow", u"Mirror your source MS to a LiquidMS node", None))
#endif // QT_CONFIG(tooltip)
        self.SnitchButton.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Source", None))
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
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.SaveFilesToConfigToggle.setText(QCoreApplication.translate("MainWindow", u"Save Launch Mods to Profile", None))
        self.ProfileDirBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.ProfileDirLabel.setText(QCoreApplication.translate("MainWindow", u"Profile Directory (requires restart)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Upon launch, LiquidLauncher will check this directory for available profiles.", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Developer settings", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"HTTP User Agent", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Changes how LiquidLauncher presents itself to HTTP servers (news feeds, mod sources, master servers).", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Only change these settings if you know what you're doing.", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"General", None))
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
        self.ModsourceWSBlueCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Blue Sphere\" (unofficial)", None))
        self.ModsourceWSRedCheckbox.setText(QCoreApplication.translate("MainWindow", u"SRB2 Workshop \"Red Sphere\" (non-compliant; unofficial)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Mod Sources", None))
        self.RSSRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.RSSMoveupButton.setText(QCoreApplication.translate("MainWindow", u"Move up", None))
        self.NewssourceLabel.setText(QCoreApplication.translate("MainWindow", u"News Sources (RSS/Atom Feeds)", None))
        self.RSSAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.RSSMovedownButton.setText(QCoreApplication.translate("MainWindow", u"Move down", None))
        self.RSSStatusLabel_2.setText(QCoreApplication.translate("MainWindow", u"Select or double click an entry to edit.", None))

        __sortingEnabled6 = self.RSSFeedList.isSortingEnabled()
        self.RSSFeedList.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.RSSFeedList.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"https://srb2.org/feed", None));
        ___qlistwidgetitem11 = self.RSSFeedList.item(1)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"https://mb.srb2.org.org/forums/-/index.rss", None));
        ___qlistwidgetitem12 = self.RSSFeedList.item(2)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"https://srb2workshop.org/forums/-/index.rss", None));
        ___qlistwidgetitem13 = self.RSSFeedList.item(3)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"https://www.sonicstadium.org/feed/", None));
        self.RSSFeedList.setSortingEnabled(__sortingEnabled6)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"News Sources", None))
        self.SaveSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
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
    # retranslateUi

