# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowPzAiVx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1356, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(248, 252, 255);\n"
"font: 8pt \"Aldrich\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(222, 234, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.barraMenu = QFrame(self.centralwidget)
        self.barraMenu.setObjectName(u"barraMenu")
        self.barraMenu.setMinimumSize(QSize(68, 0))
        self.barraMenu.setMaximumSize(QSize(80, 16777215))
        self.barraMenu.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.barraMenu.setFrameShape(QFrame.StyledPanel)
        self.barraMenu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.barraMenu)

        self.centro = QVBoxLayout()
        self.centro.setObjectName(u"centro")
        self.verticalSpacer_4 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.centro.addItem(self.verticalSpacer_4)

        self.title_usuarios = QLabel(self.centralwidget)
        self.title_usuarios.setObjectName(u"title_usuarios")
        font = QFont()
        font.setFamily(u"Aldrich")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        self.title_usuarios.setFont(font)
        self.title_usuarios.setStyleSheet(u"color: rgb(6, 74, 128);")

        self.centro.addWidget(self.title_usuarios, 0, Qt.AlignHCenter)

        self.mainFrame_searchBox = QFrame(self.centralwidget)
        self.mainFrame_searchBox.setObjectName(u"mainFrame_searchBox")
        self.mainFrame_searchBox.setMinimumSize(QSize(200, 50))
        self.mainFrame_searchBox.setStyleSheet(u"")
        self.mainFrame_searchBox.setFrameShape(QFrame.StyledPanel)
        self.mainFrame_searchBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.mainFrame_searchBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 16, 0)
        self.horizontalSpacer_7 = QSpacerItem(1065, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.search_box = QFrame(self.mainFrame_searchBox)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setMinimumSize(QSize(200, 32))
        self.search_box.setMaximumSize(QSize(200, 32))
        self.search_box.setStyleSheet(u"QFrame#search_box {border: 1px solid #c4c4c4; border-radius: 16px; color: #D2E4FF}\n"
"QLineEdit{border-radius: 15px}")
        self.search_box.setFrameShape(QFrame.StyledPanel)
        self.search_box.setFrameShadow(QFrame.Raised)
        self.buscar = QLineEdit(self.search_box)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(1, 1, 165, 30))
        self.buscar.setMinimumSize(QSize(165, 30))
        self.buscar.setMaximumSize(QSize(16777215, 16777215))
        self.buscar.setStyleSheet(u"QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;border-right:1px solid #c4c4c4;\n"
"padding-left: 14px; color: #A0A0A0;}")
        self.search_icon = QToolButton(self.search_box)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(170, 5, 22, 22))
        self.search_icon.setStyleSheet(u"QToolButton{ border:hidden}")
        icon = QIcon()
        icon.addFile(u"icons/search_black_18dp.svg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_icon.setIcon(icon)
        self.search_icon.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.search_box)


        self.centro.addWidget(self.mainFrame_searchBox)

        self.verticalSpacer_2 = QSpacerItem(20, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.centro.addItem(self.verticalSpacer_2)

        self.layout_table = QHBoxLayout()
        self.layout_table.setObjectName(u"layout_table")
        self.horizontalSpacer_5 = QSpacerItem(199, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_table.addItem(self.horizontalSpacer_5)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)

        font = QFont()
        font.setPointSize(18)
        font.setUnderline(True)

        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        __qtablewidgetitem.setForeground(QColor('#064A80'))
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        __qtablewidgetitem1.setForeground(QColor('#064A80'))
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font)
        __qtablewidgetitem2.setForeground(QColor('#064A80'))
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(0, 0))
        self.table.setMaximumSize(QSize(16777215, 16777215))
        #self.table.setStyleSheet(u"color: rgb(17, 17, 17);")

        p = self.table.palette()
        p.setColor(QPalette.Base, '#F8FCFF')
        p.setColor(QPalette.AlternateBase, '#EFF4FB')
        p.setColor(QPalette.Highlight, '#D2E4FF')
        p.setColor(QPalette.HighlightedText, '#000000')
        self.table.setPalette(p)


        self.layout_table.addWidget(self.table)

        self.horizontalSpacer_6 = QSpacerItem(199, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_table.addItem(self.horizontalSpacer_6)


        self.centro.addLayout(self.layout_table)

        self.verticalSpacer_3 = QSpacerItem(10, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.centro.addItem(self.verticalSpacer_3)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setObjectName(u"layout_btn")
        self.horizontalSpacer_3 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_btn.addItem(self.horizontalSpacer_3)

        self.frame_btns = QFrame(self.centralwidget)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(600, 45))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btns)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_excluir = QPushButton(self.frame_btns)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(163, 40))
        self.btn_excluir.setMaximumSize(QSize(163, 40))
        self.btn_excluir.setStyleSheet(u"border-radius: 20px;\n"
"font: 16pt \"Aldrich\";\n"
"border: 2px solid;\n"
"color: rgb(6, 74, 128);\n"
"border-color: rgb(6, 74, 128);")

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_imprimir = QPushButton(self.frame_btns)
        self.btn_imprimir.setObjectName(u"btn_imprimir")
        self.btn_imprimir.setMinimumSize(QSize(163, 40))
        self.btn_imprimir.setMaximumSize(QSize(163, 40))
        self.btn_imprimir.setStyleSheet(u"border-radius: 20px;\n"
"font: 16pt \"Aldrich\";\n"
"color: rgb(238, 238, 238);\n"
"background-color: rgb(6, 74, 128);")

        self.horizontalLayout.addWidget(self.btn_imprimir)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_cadastrar = QPushButton(self.frame_btns)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(163, 40))
        self.btn_cadastrar.setMaximumSize(QSize(163, 40))
        self.btn_cadastrar.setStyleSheet(u"border-radius: 20px;\n"
"font: 16pt \"Aldrich\";\n"
"color: rgb(238, 238, 238);\n"
"background-color: rgb(6, 74, 128);")

        self.horizontalLayout.addWidget(self.btn_cadastrar)


        self.layout_btn.addWidget(self.frame_btns)

        self.horizontalSpacer_4 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_btn.addItem(self.horizontalSpacer_4)


        self.centro.addLayout(self.layout_btn)

        self.verticalSpacer = QSpacerItem(10, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.centro.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.centro)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_usuarios.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Usu\u00e1rios</span></p></body></html>", None))
        self.buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.search_icon.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel Acesso", None));
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
    # retranslateUi

