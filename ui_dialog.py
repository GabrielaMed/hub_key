# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogOHaDWg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        
        font = QFont()
        font.setFamilies([u"Aldrich"])
        font.setPointSize(20)

        Dialog.resize(470, 198)
        Dialog.setFont(font)
        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.borda = QFrame(Dialog)
        self.borda.setObjectName(u"borda")
        self.borda.setStyleSheet(u"*{background-color: #fff} #borda{border-radius:5px; border: 2px solid #064A80}")
        self.borda.setFrameShape(QFrame.StyledPanel)
        self.borda.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.borda)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.borda)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 30, 0, 30)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        font1 = QFont()
        font1.setFamilies([u"Aldrich"])
        font1.setPointSize(16)

        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")

        font2 = QFont()
        font2.setPointSize(20)
        font2.setFamilies([u"Aldrich"])

        self.buttonBox.setFont(font2)
        self.buttonBox.setStyleSheet(u"#buttonBox *[text=\"&No\"]{color: #064A80} QDialogButtonBox *[text=\"&Yes\"]{background-color: #064A80; color: #fff}"
        "QPushButton:hover{font-weight: 600; border-width: 2px} QPushButton:focus{font-weight: 600; border-width: 2px; outline: 0;}"
        "QPushButton{width: 155px; height:32px; border-radius:16px; border: 1px solid #064A80; margin-left: 16px; margin-right: 16px; font-size: 18px;font-weight: 450}")
        self.buttonBox.setLocale(QLocale(QLocale.Italian, QLocale.Italy))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.buttonBox.button(QDialogButtonBox.No).setFont(font2)
        self.buttonBox.button(QDialogButtonBox.No).setText('Não')
        self.buttonBox.button(QDialogButtonBox.No).setDefault(True)
        self.buttonBox.button(QDialogButtonBox.No).setCursor(Qt.PointingHandCursor)
        self.buttonBox.button(QDialogButtonBox.Yes).setFont(font2)
        self.buttonBox.button(QDialogButtonBox.Yes).setText('Sim')
        self.buttonBox.button(QDialogButtonBox.Yes).setDefault(False)
        self.buttonBox.button(QDialogButtonBox.Yes).setCursor(Qt.PointingHandCursor)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.horizontalSpacer_2 = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)
        self.horizontalLayout.addWidget(self.borda)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"", None))
    # retranslateUi

class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.resize(370, 184)
        Dialog.setWindowFlags(Qt.Dialog|Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.borda = QFrame(Dialog)
        self.borda.setObjectName(u"borda")
        self.borda.setMaximumSize(QSize(16777215, 184))
        self.borda.setStyleSheet(u"*{background-color: #fff} #borda {border-radius:5px; border: 2px solid #064A80}")
        self.borda.setFrameShape(QFrame.StyledPanel)
        self.borda.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.borda)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(65, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.borda)
        self.frame_2.setObjectName(u"frame_2")

        font = QFont()
        font.setFamilies([u"Aldrich"])
        font.setPointSize(20)

        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 30, 0, 30)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")

        font1 = QFont()
        font1.setFamilies([u"Aldrich"])
        font1.setPointSize(20)

        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        font2 = QFont()
        font2.setFamilies([u"Aldrich"])
        font2.setPointSize(16)

        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")

        font3 = QFont()
        font3.setPointSize(20)
        font3.setFamilies([u"Aldrich"])

        self.buttonBox.setFont(font3)
        self.buttonBox.setStyleSheet(u"QDialogButtonBox *[text=\"OK\"]{background-color: #064A80; color: #fff} QPushButton:hover{font-weight: 600; border-width: 2px}"
        "QPushButton:focus{outline: 0;}"
        "QPushButton{width: 155px; height:32px; border-radius:16px; border: 1px solid #064A80; margin-left: 16px; margin-right: 16px; font-size: 18px;font-weight: 450}")
        self.buttonBox.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).setFont(font3)
        self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        self.buttonBox.button(QDialogButtonBox.Ok).setCursor(Qt.PointingHandCursor)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalSpacer_2 = QSpacerItem(66, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addWidget(self.borda)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_2.setText("")
    # retranslateUi
