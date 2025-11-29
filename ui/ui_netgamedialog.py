# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'd_netgame.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import ll_rc

class Ui_NetgameDialog(object):
    def setupUi(self, NetgameDialog):
        if not NetgameDialog.objectName():
            NetgameDialog.setObjectName(u"NetgameDialog")
        NetgameDialog.resize(331, 425)
        self.verticalLayout = QVBoxLayout(NetgameDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(NetgameDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.widget_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.widget_6 = QWidget(self.splitter)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ServerinfoLabel = QTextBrowser(self.widget_6)
        self.ServerinfoLabel.setObjectName(u"ServerinfoLabel")
        self.ServerinfoLabel.setOpenExternalLinks(True)
        self.ServerinfoLabel.setOpenLinks(False)

        self.verticalLayout_4.addWidget(self.ServerinfoLabel)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/assets/img/icons/bookmark-new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.RefreshButton = QPushButton(self.widget_3)
        self.RefreshButton.setObjectName(u"RefreshButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefreshButton.sizePolicy().hasHeightForWidth())
        self.RefreshButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/assets/img/icons/view-refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RefreshButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.RefreshButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.splitter.addWidget(self.widget_6)
        self.PlayersAndFiles = QTabWidget(self.splitter)
        self.PlayersAndFiles.setObjectName(u"PlayersAndFiles")
        self.PlayersAndFiles.setTabPosition(QTabWidget.TabPosition.East)
        self.Players = QWidget()
        self.Players.setObjectName(u"Players")
        self.horizontalLayout = QHBoxLayout(self.Players)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PlayersTable = QListWidget(self.Players)
        self.PlayersTable.setObjectName(u"PlayersTable")

        self.horizontalLayout.addWidget(self.PlayersTable)

        icon2 = QIcon()
        icon2.addFile(u":/assets/img/sonic.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlayersAndFiles.addTab(self.Players, icon2, "")
        self.Files = QWidget()
        self.Files.setObjectName(u"Files")
        self.verticalLayout_2 = QVBoxLayout(self.Files)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.FilesTable = QListWidget(self.Files)
        self.FilesTable.setObjectName(u"FilesTable")
        self.FilesTable.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)

        self.verticalLayout_2.addWidget(self.FilesTable)

        icon3 = QIcon()
        icon3.addFile(u":/assets/img/filetypes/pk3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlayersAndFiles.addTab(self.Files, icon3, "")
        self.splitter.addWidget(self.PlayersAndFiles)

        self.verticalLayout_3.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget = QWidget(NetgameDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.JoinButton = QPushButton(self.widget)
        self.JoinButton.setObjectName(u"JoinButton")
        sizePolicy.setHeightForWidth(self.JoinButton.sizePolicy().hasHeightForWidth())
        self.JoinButton.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/assets/img/icons/media-playback-start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.JoinButton.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.JoinButton)

        self.CancelButton = QPushButton(self.widget)
        self.CancelButton.setObjectName(u"CancelButton")
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.CancelButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.CancelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(NetgameDialog)
        self.CancelButton.clicked.connect(NetgameDialog.close)
        self.JoinButton.clicked.connect(NetgameDialog.join_netgame)
        self.RefreshButton.clicked.connect(NetgameDialog.query)
        self.pushButton.clicked.connect(NetgameDialog.bookmark)

        self.PlayersAndFiles.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NetgameDialog)
    # setupUi

    def retranslateUi(self, NetgameDialog):
        NetgameDialog.setWindowTitle(QCoreApplication.translate("NetgameDialog", u"Dialog", None))
        self.ServerinfoLabel.setHtml(QCoreApplication.translate("NetgameDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Atkinson Hyperlegible'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Serverinfo unavailable</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("NetgameDialog", u"Bookmark", None))
        self.RefreshButton.setText(QCoreApplication.translate("NetgameDialog", u"Refresh", None))
        self.PlayersAndFiles.setTabText(self.PlayersAndFiles.indexOf(self.Players), QCoreApplication.translate("NetgameDialog", u"Players", None))
        self.PlayersAndFiles.setTabText(self.PlayersAndFiles.indexOf(self.Files), QCoreApplication.translate("NetgameDialog", u"Files", None))
        self.JoinButton.setText(QCoreApplication.translate("NetgameDialog", u"Join", None))
        self.CancelButton.setText(QCoreApplication.translate("NetgameDialog", u"Cancel", None))
    # retranslateUi

