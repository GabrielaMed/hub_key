# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowSddkMo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 767)
        MainWindow.setStyleSheet(u"background-color: rgb(248, 252, 255);\n"
"font: 8pt \"Aldrich\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(222, 234, 255);")
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        font = QFont()
        font.setFamily(u"Aldrich")
        font.setPointSize(26)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(260, 160, 701, 441))
        self.table.setStyleSheet(u"color: rgb(17, 17, 17);")
        self.barraMenu = QFrame(self.centralwidget)
        self.barraMenu.setObjectName(u"barraMenu")
        self.barraMenu.setGeometry(QRect(0, 0, 80, 768))
        self.barraMenu.setMinimumSize(QSize(68, 0))
        self.barraMenu.setMaximumSize(QSize(91, 16777215))
        self.barraMenu.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.barraMenu.setFrameShape(QFrame.StyledPanel)
        self.barraMenu.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel Acesso", None));
    # retranslateUi

