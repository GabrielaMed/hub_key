# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledKFWiOI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class LineEdit(QLineEdit):
	def __init__(self, parent):
		super().__init__(parent)
		self._parent = parent

	def focusInEvent(self, event) -> None:
		self.setStyleSheet("border-top-right-radius:0px; border-bottom-right-radius:0px; border-right:1px solid #5EA2FA; padding-left: 14px")
		self._parent.setStyleSheet("QFrame{border: 1px solid #5EA2FA; background-color: #FFF; border-radius: 16px} QLineEdit{border-radius: 15px; background-color: #fff}")
		return super().focusInEvent(event)

	def focusOutEvent(self, event) -> None:
		self.setStyleSheet("border-top-right-radius:0px; border-bottom-right-radius:0px; border-right:1px solid #E2E2E2; padding-left: 14px")
		self._parent.setStyleSheet("QFrame{border: 1px solid #E2E2E2; background-color: #FFF; border-radius: 16px} QLineEdit{border-radius: 15px; background-color: #fff}")
		return super().focusOutEvent(event)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)

        font = QFont()
        font.setPointSize(16)
        font.setFamilies([u"Aldrich"])

        font1 = QFont()
        font1.setFamilies([u"Aldrich"])
        font1.setPointSize(26)

        font2 = QFont()
        font2.setFamilies([u"Aldrich"])
        font2.setPointSize(30)

        font3 = QFont()
        font3.setFamilies([u"Aldrich"])
        font3.setPointSize(12)

        font4 = QFont()
        font4.setFamilies([u"Aldrich"])
        font4.setPointSize(18)
                
        font5 = QFont()
        font5.setFamilies([u"Aldrich"])
        font5.setPointSize(7)

        font6 = QFont()
        font6.setFamilies([u"Aldrich"])
        font6.setPointSize(36)

        font7 = QFont()
        font7.setFamilies([u"Aldrich"])
        font7.setPointSize(10)

        font8 = QFont()
        font8.setFamilies([u"Aldrich"])
        font8.setPointSize(8)

        font9 = QFont()
        font9.setFamilies([u"Aldrich"])
        font9.setPointSize(42)

        #EXPS REGULARES
        ##########################################################
        #VALIDADOR INTEIRO
        self.validaInteiro = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        #VALIDADOR NOME
        self.validaNome = QRegularExpressionValidator(QRegularExpression("[a-zA-z çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ-]+"))
        #VALIDADOR TEXTO
        self.validaTexto = QRegularExpressionValidator(QRegularExpression("[a-zA-z0-9 çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ\\.-]+"))
        #VALIDADOR EMAIL
        self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
        ##########################################################        

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.bem_vindo = QWidget()
        self.bem_vindo.setObjectName(u"bem_vindo")

        self.horizontalLayout_23 = QHBoxLayout(self.bem_vindo)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)

        self.lado_esq = QFrame(self.bem_vindo)
        self.lado_esq.setObjectName(u"lado_esq")
        self.lado_esq.setMinimumSize(QSize(645, 0))
        self.lado_esq.setMaximumSize(QSize(16777215, 16777215))
        self.lado_esq.setStyleSheet(u"background-color: #fff")
        self.lado_esq.setFrameShape(QFrame.StyledPanel)
        self.lado_esq.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7 = QVBoxLayout(self.lado_esq)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.cabecalho = QFrame(self.lado_esq)
        self.cabecalho.setObjectName(u"cabecalho")
        self.cabecalho.setMinimumSize(QSize(0, 128))
        self.cabecalho.setMaximumSize(QSize(16777215, 128))
        self.cabecalho.setFrameShape(QFrame.StyledPanel)
        self.cabecalho.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8 = QVBoxLayout(self.cabecalho)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.label_5 = QLabel(self.cabecalho)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font9)
        self.label_5.setStyleSheet(u"color: #064A80;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.frame_51 = QFrame(self.cabecalho)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(16777215, 21))
        self.frame_51.setStyleSheet(u"#frame_51{background-color: #064A80}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(30, 14, 25, 7))
        self.frame_52.setStyleSheet(u"QFrame: {background:#ffffff;}")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setGeometry(QRect(120, 0, 25, 7))
        self.frame_53.setStyleSheet(u"QFrame: {background:#ffffff;}")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.frame_54 = QFrame(self.frame_51)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(560, 0, 25, 7))
        self.frame_54.setStyleSheet(u"QFrame: {background:#ffffff;}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_51)
        self.verticalLayout_7.addWidget(self.cabecalho)
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(self.verticalSpacer_14)

        self.meio = QFrame(self.lado_esq)
        self.meio.setObjectName(u"meio")
        self.meio.setMinimumSize(QSize(0, 320))
        self.meio.setFrameShape(QFrame.StyledPanel)
        self.meio.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout_18 = QHBoxLayout(self.meio)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(self.horizontalSpacer_27)

        self.stackedWidget = QStackedWidget(self.meio)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(260, 0))
        self.inicio = QWidget()
        self.inicio.setObjectName(u"inicio")

        self.horizontalLayout_19 = QHBoxLayout(self.inicio)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.frame_55 = QFrame(self.inicio)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(260, 0))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        
        self.btn_adm_inicio = QPushButton(self.frame_55)
        self.btn_adm_inicio.setObjectName(u"btn_adm_inicio")
        self.btn_adm_inicio.setGeometry(QRect(5, 70, 250, 50))
        self.btn_adm_inicio.setCursor(Qt.PointingHandCursor)
        self.btn_adm_inicio.setFont(font4)
        self.btn_adm_inicio.setStyleSheet(u"QPushButton:hover{font-weight: 600; border: 3px solid #08518B;} QPushButton:focus{font-weight: 600; border: 3px solid #08518B; outline: 0}"
                                            "QPushButton{border-radius: 25px; border: 2px solid #08518B; background-color: #fff; color: #064A80}")
        self.btn_int_inicio = QPushButton(self.frame_55)
        self.btn_int_inicio.setObjectName(u"btn_int_inicio")
        self.btn_int_inicio.setGeometry(QRect(5, 180, 250, 50))
        self.btn_int_inicio.setCursor(Qt.PointingHandCursor)
        self.btn_int_inicio.setFont(font4)
        self.btn_int_inicio.setStyleSheet(u"QPushButton:hover{font-weight: 600} QPushButton:focus{font-weight: 600; outline: 0}"
                                            "QPushButton{border-radius: 25px; border: 2px solid #08518B; background-color: #08518B; color: #fff;}")
        self.horizontalLayout_19.addWidget(self.frame_55)

        self.stackedWidget.addWidget(self.inicio)
        self.email = QWidget()
        self.email.setObjectName(u"email")

        self.horizontalLayout_20 = QHBoxLayout(self.email)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.frame_56 = QFrame(self.email)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(260, 0))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.btn_enviar_inicio = QPushButton(self.frame_56)
        self.btn_enviar_inicio.setObjectName(u"btn_enviar_inicio")
        self.btn_enviar_inicio.setGeometry(QRect(50, 180, 164, 43))
        self.btn_enviar_inicio.setCursor(Qt.PointingHandCursor)
        self.btn_enviar_inicio.setFont(font4)
        self.btn_enviar_inicio.setStyleSheet(u"QPushButton:hover{font-weight: 600} QPushButton:focus{font-weight: 600; outline: 0}"
                                                "QPushButton{background:#064A80;border-radius:21px; border: 4px solid#08518B; color:#fff}")
        
        self.label_email_inicio = QLabel(self.frame_56)
        self.label_email_inicio.setObjectName(u"label_email_inicio")
        self.label_email_inicio.setGeometry(QRect(20, 50, 111, 21))
        self.label_email_inicio.setFont(font7)
        self.label_email_inicio.setStyleSheet(u"color:#064A80;")
        
        self.lineEdit_email_inicio = QLineEdit(self.frame_56)
        self.lineEdit_email_inicio.setObjectName(u"lineEdit_email_inicio")
        self.lineEdit_email_inicio.setGeometry(QRect(5, 70, 250, 50))
        self.lineEdit_email_inicio.setFont(font7)
        self.lineEdit_email_inicio.setStyleSheet(u"border-radius: 25px; border: 2px solid #08518B; background-color: #fff; padding: 14px;")

        self.horizontalLayout_20.addWidget(self.frame_56)

        self.stackedWidget.addWidget(self.email)
        self.senha = QWidget()
        self.senha.setObjectName(u"senha")

        self.horizontalLayout_21 = QHBoxLayout(self.senha)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.frame_57 = QFrame(self.senha)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(260, 0))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)

        self.btn_entrar_inicio = QPushButton(self.frame_57)
        self.btn_entrar_inicio.setObjectName(u"btn_entrar_inicio")
        self.btn_entrar_inicio.setGeometry(QRect(50, 180, 164, 43))
        self.btn_entrar_inicio.setCursor(Qt.PointingHandCursor)
        self.btn_entrar_inicio.setFont(font4)
        self.btn_entrar_inicio.setStyleSheet(u"QPushButton:hover{font-weight: 600} QPushButton:focus{font-weight: 600; outline: 0}"
                                                "QPushButton{background:#064A80;border-radius:21px; border: 4px solid#08518B; color:#fff}")
        
        self.label_senha_inicio = QLabel(self.frame_57)
        self.label_senha_inicio.setObjectName(u"label_senha_inicio")
        self.label_senha_inicio.setGeometry(QRect(20, 50, 111, 21))
        self.label_senha_inicio.setFont(font7)
        self.label_senha_inicio.setStyleSheet(u"color:#064A80;")

        self.btn_esqueci_senha = QPushButton(self.frame_57)
        self.btn_esqueci_senha.setObjectName(u"btn_esqueci_senha")
        self.btn_esqueci_senha.setGeometry(QRect(110, 120, 125, 21))
        self.btn_esqueci_senha.setCursor(Qt.PointingHandCursor)
        self.btn_esqueci_senha.setFont(font8)
        self.btn_esqueci_senha.setStyleSheet(u"QPushButton:hover{text-decoration:underline;} QPushButton:focus{text-decoration: underline; outline: 0}"
                                                "QPushButton{color:rgb(6, 74, 128); border:none;}")

        self.lineEdit_senha_inicio = QLineEdit(self.frame_57)
        self.lineEdit_senha_inicio.setObjectName(u"lineEdit_senha_inicio")
        self.lineEdit_senha_inicio.setGeometry(QRect(5, 70, 250, 50))
        self.lineEdit_senha_inicio.setEchoMode(QLineEdit.Password)
        self.lineEdit_senha_inicio.setFont(font7)
        self.lineEdit_senha_inicio.setStyleSheet(u"color:#064A80; border-radius: 25px; border: 2px solid #08518B; background-color: #fff; padding: 14px;")

        self.horizontalLayout_21.addWidget(self.frame_57)
        self.stackedWidget.addWidget(self.senha)
        self.horizontalLayout_18.addWidget(self.stackedWidget)
        self.horizontalSpacer_28 = QSpacerItem(181, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(self.horizontalSpacer_28)


        self.verticalLayout_7.addWidget(self.meio)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(self.verticalSpacer_15)

        self.rodape = QFrame(self.lado_esq)
        self.rodape.setObjectName(u"rodape")
        self.rodape.setMinimumSize(QSize(0, 300))
        self.rodape.setFrameShape(QFrame.StyledPanel)
        self.rodape.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22 = QHBoxLayout(self.rodape)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)

        self.frame_58 = QFrame(self.rodape)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(240, 300))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setGeometry(QRect(0, 240, 60, 60))
        self.frame_59.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setGeometry(QRect(60, 240, 60, 60))
        self.frame_60.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setGeometry(QRect(60, 180, 60, 60))
        self.frame_61.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.frame_62 = QFrame(self.frame_58)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setGeometry(QRect(120, 180, 60, 60))
        self.frame_62.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.frame_63 = QFrame(self.frame_58)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setGeometry(QRect(180, 240, 60, 60))
        self.frame_63.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.frame_64 = QFrame(self.frame_58)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setGeometry(QRect(60, 120, 60, 60))
        self.frame_64.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.frame_65 = QFrame(self.frame_58)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setGeometry(QRect(180, 120, 60, 60))
        self.frame_65.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.frame_66 = QFrame(self.frame_58)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setGeometry(QRect(120, 60, 60, 60))
        self.frame_66.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.frame_143 = QFrame(self.frame_58)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setGeometry(QRect(0, 60, 60, 60))
        self.frame_143.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)

        self.frame_144 = QFrame(self.frame_58)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setGeometry(QRect(60, 0, 60, 60))
        self.frame_144.setStyleSheet(u"border:hidden;background-color: #DEEAFF;")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_58)
        self.horizontalSpacer_29 = QSpacerItem(237, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.frame_145 = QFrame(self.rodape)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(161, 141))
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)

        self.label_22 = QLabel(self.frame_145)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 160, 161, 141))
        self.label_22.setPixmap(QPixmap(u"logo/logo ajustada.qrc.png"))

        self.label_23 = QLabel(self.frame_145)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 170, 151, 131))
        self.label_23.setPixmap(QPixmap(u"icons/hub_key.png"))

        self.horizontalLayout_22.addWidget(self.frame_145)

        self.verticalLayout_7.addWidget(self.rodape)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(3, 1)

        self.horizontalLayout_23.addWidget(self.lado_esq)

        self.lado_dir = QFrame(self.bem_vindo)
        self.lado_dir.setObjectName(u"lado_dir")
        self.lado_dir.setStyleSheet(u"background-color:#064A80")
        self.lado_dir.setFrameShape(QFrame.StyledPanel)
        self.lado_dir.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_1 = QVBoxLayout(self.lado_dir)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setObjectName(u"verticalLayout_3")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)

        font8.setUnderline(False)

        self.label_24 = QLabel(self.lado_dir)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet("border: 3px solid #08518B; border-bottom: 0px; background-color:#064A80")
        self.label_24.setPixmap(QPixmap(u"icons/foto_turma_57.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_1.addWidget(self.label_24)

        self.horizontalLayout_23.addWidget(self.lado_dir)
        self.horizontalLayout_23.setStretch(0, 5)
        self.horizontalLayout_23.setStretch(1, 6)
       
        self.pages.addWidget(self.bem_vindo)
        self.emprestimos = QWidget()
        self.emprestimos.setObjectName(u"emprestimos")

        self.horizontalLayout = QHBoxLayout(self.emprestimos)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.planodefundo1 = QFrame(self.emprestimos)
        self.planodefundo1.setObjectName(u"planodefundo1")
        self.planodefundo1.setMaximumSize(QSize(16777215, 16777215))
        self.planodefundo1.setStyleSheet(u"QFrame#planodefundo1{background-color:#064A80}")
        self.planodefundo1.setFrameShape(QFrame.StyledPanel)
        self.planodefundo1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.planodefundo1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_146 = QFrame(self.planodefundo1)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(24, 32, 0, 0)

        self.frame_voltar_emp = QFrame(self.frame_146)
        self.frame_voltar_emp.setObjectName(u"frame_voltar_emp")
        self.frame_voltar_emp.setMinimumSize(QSize(36, 36))
        self.frame_voltar_emp.setStyleSheet(u"QFrame{border-radius: 18px; border:3px solid #fff}")
        self.frame_voltar_emp.setFrameShape(QFrame.StyledPanel)
        self.frame_voltar_emp.setFrameShadow(QFrame.Raised)
        
        self.btn_voltar_emp = QToolButton(self.frame_voltar_emp)
        self.btn_voltar_emp.setObjectName(u"btn_voltar_emp")
        self.btn_voltar_emp.setGeometry(QRect(6, 6, 24, 24))
        self.btn_voltar_emp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_emp.setStyleSheet(u"border-radius:12px; background-color: #064A80; border: hidden")
        icon = QIcon()
        icon.addFile(u"icons/arrow_back_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voltar_emp.setIcon(icon)
        self.btn_voltar_emp.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.frame_voltar_emp)
        self.horizontalSpacer_30 = QSpacerItem(621, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)

        self.verticalLayout_2.addWidget(self.frame_146)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.planodefundo1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 285))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3 = QVBoxLayout(self.frame_15)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(583, 170))
        self.frame_13.setMaximumSize(QSize(16777215, 170))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 523, 51))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:#fff")

        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 361, 55))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:#fff")

        self.verticalLayout_3.addWidget(self.frame_13)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setMaximumSize(QSize(16777215, 100))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        
        self.stackedWidget_2 = QStackedWidget(self.frame_14)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"QStackedWidget{background-color: #064A80}")
        self.page_codigo = QWidget()
        self.page_codigo.setObjectName(u"page_codigo")
        
        self.lineEdit_codigo = QLineEdit(self.page_codigo)
        self.lineEdit_codigo.setObjectName(u"lineEdit_codigo")
        self.lineEdit_codigo.setGeometry(QRect(130, 40, 200, 40))
        self.lineEdit_codigo.setFont(font7)
        self.lineEdit_codigo.setStyleSheet(u"padding-left:14px ;border-radius: 20px")

        self.label_codigo = QLabel(self.page_codigo)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(158, 16, 61, 21))
        self.label_codigo.setFont(font3)
        self.label_codigo.setStyleSheet(u"color: #fff")

        self.stackedWidget_2.addWidget(self.page_codigo)
        self.page_chave = QWidget()
        self.page_chave.setObjectName(u"page_chave")

        self.label_chave = QLabel(self.page_chave)
        self.label_chave.setObjectName(u"label_chave")
        self.label_chave.setGeometry(QRect(158, 16, 61, 21))
        self.label_chave.setFont(font3)
        self.label_chave.setStyleSheet(u"color: #fff")

        self.lineEdit_chave = QLineEdit(self.page_chave)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")
        self.lineEdit_chave.setGeometry(QRect(130, 40, 200, 40))
        self.lineEdit_chave.setFont(font7)
        self.lineEdit_chave.setStyleSheet(u"padding-left:14px ;border-radius: 20px")
        self.stackedWidget_2.addWidget(self.page_chave)

        self.verticalLayout_6.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)

        self.horizontalLayout_2.addWidget(self.frame_15)
        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addWidget(self.frame_11)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_12 = QFrame(self.planodefundo1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 300))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(180, 120, 60, 60))
        self.frame_7.setStyleSheet(u"background-color:#fff")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.frame_2 = QFrame(self.frame_12)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 180, 60, 60))
        self.frame_2.setStyleSheet(u"background-color:#fff")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.frame_4 = QFrame(self.frame_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(180, 240, 60, 60))
        self.frame_4.setStyleSheet(u"background-color:#fff")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(60, 0, 60, 60))
        self.frame_10.setStyleSheet(u"background-color:#fff")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.frame_6 = QFrame(self.frame_12)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(60, 120, 60, 60))
        self.frame_6.setStyleSheet(u"background-color:#fff")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.frame_3 = QFrame(self.frame_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 240, 60, 60))
        self.frame_3.setStyleSheet(u"background-color:#fff")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.frame_8 = QFrame(self.frame_12)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 60, 60, 60))
        self.frame_8.setStyleSheet(u"background-color:#fff")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.frame = QFrame(self.frame_12)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 240, 60, 60))
        self.frame.setStyleSheet(u"background-color:#fff")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(120, 180, 60, 60))
        self.frame_5.setStyleSheet(u"background-color:#fff")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(120, 60, 60, 60))
        self.frame_9.setStyleSheet(u"background-color:#fff")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_12)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 8)

        self.horizontalLayout.addWidget(self.planodefundo1)

        self.planodefundo2 = QFrame(self.emprestimos)
        self.planodefundo2.setObjectName(u"planodefundo2")
        self.planodefundo2.setStyleSheet(u"QFrame#planodefundo2{background-color: #F8FCFF}")
        self.planodefundo2.setFrameShape(QFrame.StyledPanel)
        self.planodefundo2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5 = QVBoxLayout(self.planodefundo2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.frame_18 = QFrame(self.planodefundo2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 210))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frame_18)
        self.verticalLayout_4.setSpacing(40)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 90, 0, 0)

        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:#064A80")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 16, 0)
        self.horizontalSpacer_3 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.search_box = QFrame(self.frame_17)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setMinimumSize(QSize(200, 0))
        self.search_box.setMaximumSize(QSize(16777215, 32))
        self.search_box.setStyleSheet(u"QFrame{border: 1px solid #c4c4c4; border-radius: 16px; background-color: #fff}QLineEdit{border-radius: 15px}")
        self.search_box.setFrameShape(QFrame.StyledPanel)
        self.search_box.setFrameShadow(QFrame.Raised)

        self.lineEdit_busca_emprestimos = LineEdit(self.search_box)
        self.lineEdit_busca_emprestimos.setObjectName(u"lineEdit_busca_emprestimos")
        self.lineEdit_busca_emprestimos.setGeometry(QRect(1, 1, 165, 30))
        self.lineEdit_busca_emprestimos.setFont(font8)
        self.lineEdit_busca_emprestimos.setStyleSheet(u"QLineEdit{border-top-right-radius:0px; border-bottom-right-radius:0px; border-right:1px solid #c4c4c4; padding-left: 14px}")
        
        self.btn_busca_emprestimos = QToolButton(self.search_box)
        self.btn_busca_emprestimos.setObjectName(u"btn_busca_emprestimos")
        self.btn_busca_emprestimos.setGeometry(QRect(170, 5, 22, 22))
        self.btn_busca_emprestimos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_busca_emprestimos.setStyleSheet(u"QToolButton{border:hidden}")
        icon1 = QIcon()
        icon1.addFile(u"icons/search_black_18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_busca_emprestimos.setIcon(icon1)
        self.btn_busca_emprestimos.setIconSize(QSize(18, 18))
        self.btn_busca_emprestimos.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btn_busca_emprestimos.setAutoRaise(False)

        self.horizontalLayout_3.addWidget(self.search_box)

        self.verticalLayout_4.addWidget(self.frame_17)
        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.planodefundo2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(56, 56, 56, 56)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(self.horizontalSpacer_26)

        self.tableEmprestimo = QTableWidget(self.frame_16)
        if (self.tableEmprestimo.columnCount() < 3):
            self.tableEmprestimo.setColumnCount(3)
        
        font4.setUnderline(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableEmprestimo.setObjectName(u"tableEmprestimo")
        self.tableEmprestimo.setMinimumSize(QSize(571, 0))

        p = self.tableEmprestimo.palette()
        p.setColor(QPalette.Base, '#F8FCFF')
        p.setColor(QPalette.AlternateBase, '#EFF4FB')
        p.setColor(QPalette.Highlight, '#D2E4FF')
        p.setColor(QPalette.HighlightedText, '#000000')
        self.tableEmprestimo.setPalette(p)

        self.tableEmprestimo.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom: 24px; background-color: #F8FCFF; border:hidden}")
        self.tableEmprestimo.setStyleSheet(u"QTableView{border: hidden}")
        self.tableEmprestimo.verticalHeader().setVisible(False)
        self.tableEmprestimo.horizontalHeader().setHighlightSections(False)
        self.tableEmprestimo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEmprestimo.setFocusPolicy(Qt.NoFocus)
        self.tableEmprestimo.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableEmprestimo.setAlternatingRowColors(True)
        self.tableEmprestimo.setShowGrid(False)
        self.tableEmprestimo.setSortingEnabled(False)
        self.tableEmprestimo.setFont(font3)

        self.horizontalLayout_17.addWidget(self.tableEmprestimo)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(self.horizontalSpacer_25)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 6)
        self.horizontalLayout_17.setStretch(2, 1)

        self.verticalLayout_5.addWidget(self.frame_16)

        self.horizontalLayout.addWidget(self.planodefundo2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.pages.addWidget(self.emprestimos)

        self.descanso = QWidget()
        self.descanso.setObjectName(u"descanso")
        self.horizontalLayout_33 = QHBoxLayout(self.descanso)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.frame_113 = QFrame(self.descanso)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(0, 0))
        self.frame_113.setStyleSheet(u"background:#064A80")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, -1, 0, -1)

        self.frame_114 = QFrame(self.frame_113)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(798, 0))
        self.frame_114.setMaximumSize(QSize(16777215, 16777215))
        self.frame_114.setStyleSheet(u"background:#006DAD")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19 = QVBoxLayout(self.frame_114)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_26 = QSpacerItem(20, 149, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(self.verticalSpacer_26)

        self.label_9 = QLabel(self.frame_114)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 64))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"color:#FFF")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_9)
        self.verticalSpacer_24 = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(self.verticalSpacer_24)

        self.frame_150 = QFrame(self.frame_114)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMaximumSize(QSize(16777215, 16777215))
        self.frame_150.setSizeIncrement(QSize(0, 0))
        self.frame_150.setBaseSize(QSize(0, 0))
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_45 = QSpacerItem(14, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_45)

        self.frame_148 = QFrame(self.frame_150)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(760, 682))
        self.frame_148.setMaximumSize(QSize(16777215, 1082))
        self.frame_148.setSizeIncrement(QSize(0, 0))
        self.frame_148.setBaseSize(QSize(0, 0))
        self.frame_148.setFont(font7)
        self.frame_148.setStyleSheet(u"QLabel{border-radius: 52px; background-color:#fff; color:#000} QLabel:hover{background-color:#F89633}")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20 = QVBoxLayout(self.frame_148)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.frame_147 = QFrame(self.frame_148)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_32.setSpacing(8)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)

        self.label_10 = QLabel(self.frame_147)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(105, 105))
        self.label_10.setMaximumSize(QSize(105, 105))
        self.label_10.setFont(font7)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_147)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(105, 105))
        self.label_11.setMaximumSize(QSize(105, 105))
        self.label_11.setFont(font7)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_147)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(105, 105))
        self.label_12.setMaximumSize(QSize(105, 105))
        self.label_12.setFont(font7)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_147)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(105, 105))
        self.label_13.setMaximumSize(QSize(105, 105))
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_147)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(105, 105))
        self.label_14.setMaximumSize(QSize(105, 105))
        self.label_14.setFont(font7)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_147)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(105, 105))
        self.label_15.setMaximumSize(QSize(105, 105))
        self.label_15.setFont(font7)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_15)

        self.verticalLayout_20.addWidget(self.frame_147)
        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.verticalSpacer_27)

        self.frame_151 = QFrame(self.frame_148)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_35 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_35.setSpacing(8)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)

        self.label_16 = QLabel(self.frame_151)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(105, 105))
        self.label_16.setMaximumSize(QSize(105, 105))
        self.label_16.setFont(font7)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_151)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(105, 105))
        self.label_17.setMaximumSize(QSize(105, 105))
        self.label_17.setFont(font7)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_151)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(105, 105))
        self.label_18.setMaximumSize(QSize(105, 105))
        self.label_18.setFont(font7)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_151)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(105, 105))
        self.label_19.setMaximumSize(QSize(105, 105))
        self.label_19.setFont(font7)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_151)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(105, 105))
        self.label_20.setMaximumSize(QSize(105, 105))
        self.label_20.setFont(font7)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_20)

        self.label_25 = QLabel(self.frame_151)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(105, 105))
        self.label_25.setMaximumSize(QSize(105, 105))
        self.label_25.setFont(font7)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_25)

        self.verticalLayout_20.addWidget(self.frame_151)
        self.verticalSpacer_28 = QSpacerItem(20, 4, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.verticalSpacer_28)

        self.frame_152 = QFrame(self.frame_148)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_36.setSpacing(8)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)

        self.label_26 = QLabel(self.frame_152)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(105, 105))
        self.label_26.setMaximumSize(QSize(105, 105))
        self.label_26.setFont(font7)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_152)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(105, 105))
        self.label_27.setMaximumSize(QSize(105, 105))
        self.label_27.setFont(font7)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_152)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(105, 105))
        self.label_28.setMaximumSize(QSize(105, 105))
        self.label_28.setFont(font7)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_152)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(105, 105))
        self.label_29.setMaximumSize(QSize(105, 105))
        self.label_29.setFont(font7)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_152)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(105, 105))
        self.label_30.setMaximumSize(QSize(105, 105))
        self.label_30.setFont(font7)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_152)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(105, 105))
        self.label_31.setMaximumSize(QSize(105, 105))
        self.label_31.setFont(font7)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_31)

        self.verticalLayout_20.addWidget(self.frame_152)
        self.verticalSpacer_29 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.verticalSpacer_29)

        self.frame_153 = QFrame(self.frame_148)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_37 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_37.setSpacing(8)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)

        self.label_32 = QLabel(self.frame_153)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(105, 105))
        self.label_32.setMaximumSize(QSize(105, 105))
        self.label_32.setFont(font7)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_153)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(105, 105))
        self.label_33.setMaximumSize(QSize(105, 105))
        self.label_33.setFont(font7)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_153)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(105, 105))
        self.label_34.setMaximumSize(QSize(105, 105))
        self.label_34.setFont(font7)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_153)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(105, 105))
        self.label_35.setMaximumSize(QSize(105, 105))
        self.label_35.setFont(font7)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_153)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(105, 105))
        self.label_36.setMaximumSize(QSize(105, 105))
        self.label_36.setFont(font7)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_153)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(105, 105))
        self.label_37.setMaximumSize(QSize(105, 105))
        self.label_37.setFont(font7)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_37)

        self.verticalLayout_20.addWidget(self.frame_153)
        self.verticalSpacer_36 = QSpacerItem(20, 4, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.verticalSpacer_36)

        self.frame_154 = QFrame(self.frame_148)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_39 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_39.setSpacing(8)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)

        self.label_38 = QLabel(self.frame_154)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(105, 105))
        self.label_38.setMaximumSize(QSize(105, 105))
        self.label_38.setFont(font7)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_154)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(105, 105))
        self.label_39.setMaximumSize(QSize(105, 105))
        self.label_39.setFont(font7)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_154)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(105, 105))
        self.label_40.setMaximumSize(QSize(105, 105))
        self.label_40.setFont(font7)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_154)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(105, 105))
        self.label_41.setMaximumSize(QSize(105, 105))
        self.label_41.setFont(font7)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_154)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(105, 105))
        self.label_42.setMaximumSize(QSize(105, 105))
        self.label_42.setFont(font7)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_154)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(105, 105))
        self.label_43.setMaximumSize(QSize(105, 105))
        self.label_43.setFont(font7)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_43)

        self.verticalLayout_20.addWidget(self.frame_154)
        self.verticalSpacer_37 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.verticalSpacer_37)

        self.frame_155 = QFrame(self.frame_148)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_38.setSpacing(8)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.label_44 = QLabel(self.frame_155)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(105, 105))
        self.label_44.setMaximumSize(QSize(105, 105))
        self.label_44.setFont(font7)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_155)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(105, 105))
        self.label_45.setMaximumSize(QSize(105, 105))
        self.label_45.setFont(font7)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_155)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(105, 105))
        self.label_46.setMaximumSize(QSize(105, 105))
        self.label_46.setFont(font7)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_155)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(105, 105))
        self.label_47.setMaximumSize(QSize(105, 105))
        self.label_47.setFont(font7)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_155)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(105, 105))
        self.label_48.setMaximumSize(QSize(105, 105))
        self.label_48.setFont(font7)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_48)

        self.label_49 = QLabel(self.frame_155)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(105, 105))
        self.label_49.setMaximumSize(QSize(105, 105))
        self.label_49.setFont(font7)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_49)
        self.verticalLayout_20.addWidget(self.frame_155)

        self.horizontalLayout_34.addWidget(self.frame_148)
        self.horizontalSpacer_46 = QSpacerItem(14, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(self.horizontalSpacer_46)

        self.verticalLayout_19.addWidget(self.frame_150)
        self.verticalSpacer_25 = QSpacerItem(20, 149, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_25)
        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(2, 2)
        self.verticalLayout_19.setStretch(4, 2)

        self.horizontalLayout_31.addWidget(self.frame_114)

        self.frame_149 = QFrame(self.frame_113)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMinimumSize(QSize(0, 0))
        self.frame_149.setMaximumSize(QSize(16777215, 16777215))
        self.frame_149.setFont(font7)
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_18 = QVBoxLayout(self.frame_149)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        
        self.label_50 = QLabel(self.frame_149)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setPixmap(QPixmap(u"icons/chave_plano_fundo.png"))
        self.label_50.setScaledContents(False)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_50.setMargin(0)
        self.label_50.setIndent(0)

        self.verticalLayout_18.addWidget(self.label_50)

        self.horizontalLayout_31.addWidget(self.frame_149)
        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 1)
        self.horizontalLayout_33.addWidget(self.frame_113)
        self.pages.addWidget(self.descanso)

        self.menu_adm = QWidget()
        self.menu_adm.setObjectName(u"menu_adm")
        self.menu_adm.setStyleSheet(u"QWidget #lista_usuarios{background-color: #F8FCFF}")

        self.horizontalLayout_4 = QHBoxLayout(self.menu_adm)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.frame_barraLateral = QFrame(self.menu_adm)
        self.frame_barraLateral.setObjectName(u"frame_barraLateral")
        self.frame_barraLateral.setMinimumSize(QSize(80, 0))
        self.frame_barraLateral.setMaximumSize(QSize(16777215, 16777215))
        self.frame_barraLateral.setStyleSheet(u"background-color: #064A80; color: #fff;")
        self.frame_barraLateral.setFont(font3)
        self.frame_barraLateral.setFrameShape(QFrame.StyledPanel)
        self.frame_barraLateral.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_10 = QVBoxLayout(self.frame_barraLateral)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.frame_quadradinhosB = QFrame(self.frame_barraLateral)
        self.frame_quadradinhosB.setObjectName(u"frame_quadradinhosB")
        self.frame_quadradinhosB.setMinimumSize(QSize(68, 64))
        self.frame_quadradinhosB.setMaximumSize(QSize(16777215, 64))
        self.frame_quadradinhosB.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinhosB.setFrameShadow(QFrame.Raised)
        self.frame_quadradinhosB.setLineWidth(0)

        self.frame_quadradinho = QFrame(self.frame_quadradinhosB)
        self.frame_quadradinho.setObjectName(u"frame_quadradinho")
        self.frame_quadradinho.setGeometry(QRect(0, 0, 16, 16))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_quadradinho.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho.setSizePolicy(sizePolicy2)
        self.frame_quadradinho.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_2 = QFrame(self.frame_quadradinhosB)
        self.frame_quadradinho_2.setObjectName(u"frame_quadradinho_2")
        self.frame_quadradinho_2.setGeometry(QRect(16, 16, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_2.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_2.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_2.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_2.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_2.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_3 = QFrame(self.frame_quadradinhosB)
        self.frame_quadradinho_3.setObjectName(u"frame_quadradinho_3")
        self.frame_quadradinho_3.setGeometry(QRect(0, 32, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_3.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_3.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_3.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_3.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_3.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_4 = QFrame(self.frame_quadradinhosB)
        self.frame_quadradinho_4.setObjectName(u"frame_quadradinho_4")
        self.frame_quadradinho_4.setGeometry(QRect(16, 48, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_4.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_4.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_4.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_4.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_4.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_5 = QFrame(self.frame_quadradinhosB)
        self.frame_quadradinho_5.setObjectName(u"frame_quadradinho_5")
        self.frame_quadradinho_5.setGeometry(QRect(32, 32, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_5.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_5.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_5.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_5.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_quadradinhosB)
        self.verticalSpacer_30 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(self.verticalSpacer_30)

        self.frame_iconesCentrais = QFrame(self.frame_barraLateral)
        self.frame_iconesCentrais.setObjectName(u"frame_iconesCentrais")
        self.frame_iconesCentrais.setMinimumSize(QSize(0, 300))
        self.frame_iconesCentrais.setFrameShape(QFrame.StyledPanel)
        self.frame_iconesCentrais.setFrameShadow(QFrame.Raised)

        self.label_iconRelatorio = QLabel(self.frame_iconesCentrais)
        self.label_iconRelatorio.setObjectName(u"label_iconRelatorio")
        self.label_iconRelatorio.setGeometry(QRect(22, 237, 36, 36))
        self.label_iconRelatorio.setMinimumSize(QSize(0, 0))
        self.label_iconRelatorio.setPixmap(QPixmap(u"icons/relatorio.svg"))
        self.label_iconRelatorio.setScaledContents(True)
        self.label_iconRelatorio.setAlignment(Qt.AlignCenter)

        self.label_iconUser = QLabel(self.frame_iconesCentrais)
        self.label_iconUser.setObjectName(u"label_iconUser")
        self.label_iconUser.setGeometry(QRect(21, 118, 38, 38))
        self.label_iconUser.setMinimumSize(QSize(0, 0))
        self.label_iconUser.setPixmap(QPixmap(u"icons/usuarios.svg"))
        self.label_iconUser.setScaledContents(True)
        self.label_iconUser.setAlignment(Qt.AlignCenter)

        self.label_iconChave = QLabel(self.frame_iconesCentrais)
        self.label_iconChave.setObjectName(u"label_iconChave")
        self.label_iconChave.setGeometry(QRect(20, 5, 38, 38))
        self.label_iconChave.setMinimumSize(QSize(0, 0))
        self.label_iconChave.setPixmap(QPixmap(u"icons/vpn_key_white_48dp.svg"))
        self.label_iconChave.setScaledContents(True)
        self.label_iconChave.setAlignment(Qt.AlignCenter)

        self.btn_menu_chave = QPushButton(self.frame_iconesCentrais)
        self.btn_menu_chave.setObjectName(u"btn_menu_chave")
        self.btn_menu_chave.setFont(font7)
        self.btn_menu_chave.setGeometry(QRect(0, 0, 79, 70))
        self.btn_menu_chave.setStyleSheet(u"QPushButton {padding-top: 34px; background-color: rgba(255,255,255,0); border-style: outset;}"
                                        "QPushButton:hover {background-color: rgba(255,255,255,15);} QPushButton:pressed{background-color: rgba(255,255,255,35);}")
        self.btn_menu_usuario = QPushButton(self.frame_iconesCentrais)
        self.btn_menu_usuario.setObjectName(u"btn_menu_usuario")
        self.btn_menu_usuario.setFont(font7)
        self.btn_menu_usuario.setGeometry(QRect(0, 112, 79, 70))
        self.btn_menu_usuario.setStyleSheet(u"QPushButton {padding-top: 32px; background-color: rgba(255,255,255,0); border-style: outset;}"
                                          "QPushButton:hover {background-color: rgba(255,255,255,15);} QPushButton:pressed{background-color: rgba(255,255,255,35);}")
        self.btn_menu_historico = QPushButton(self.frame_iconesCentrais)
        self.btn_menu_historico.setObjectName(u"btn_menu_historico")
        self.btn_menu_historico.setFont(font7)
        self.btn_menu_historico.setGeometry(QRect(0, 230, 79, 70))
        self.btn_menu_historico.setStyleSheet(u"QPushButton {padding-top: 38px; background-color: rgba(255,255,255,0); border-style: outset;}"
                                            "QPushButton:hover {background-color: rgba(255,255,255,15);} QPushButton:pressed{background-color: rgba(255,255,255,35);}")
        self.frame_selected = QFrame(self.frame_iconesCentrais)
        self.frame_selected.setObjectName(u"frame_selected")
        self.frame_selected.setGeometry(QRect(0, 0, 79, 70))
        self.frame_selected.setStyleSheet(u"background-color: rgba(255,255,255,35); border-left: 2px solid #fff;")
        self.frame_selected.setFrameShape(QFrame.StyledPanel)
        self.frame_selected.setFrameShadow(QFrame.Raised)

        self.label_iconUser.raise_()
        self.label_iconRelatorio.raise_()
        self.label_iconChave.raise_()
        self.frame_selected.raise_()

        self.btn_menu_chave.raise_()
        self.btn_menu_usuario.raise_()
        self.btn_menu_historico.raise_()

        self.verticalLayout_10.addWidget(self.frame_iconesCentrais)
        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(self.verticalSpacer_31)

        self.frame_iconeLogout = QFrame(self.frame_barraLateral)
        self.frame_iconeLogout.setObjectName(u"frame_iconeLogout")
        self.frame_iconeLogout.setMinimumSize(QSize(0, 90))
        self.frame_iconeLogout.setStyleSheet(u"")
        self.frame_iconeLogout.setFrameShape(QFrame.StyledPanel)
        self.frame_iconeLogout.setFrameShadow(QFrame.Raised)

        self.label_iconLogout = QLabel(self.frame_iconeLogout)
        self.label_iconLogout.setObjectName(u"label_iconLogout")
        self.label_iconLogout.setGeometry(QRect(25, 13, 24, 24))
        self.label_iconLogout.setPixmap(QPixmap(u"icons/logout_white_48dp.svg"))
        self.label_iconLogout.setScaledContents(True)

        self.btn_menu_sair = QPushButton(self.frame_iconeLogout)
        self.btn_menu_sair.setObjectName(u"btn_menu_sair")
        self.btn_menu_sair.setFont(font7)
        self.btn_menu_sair.setGeometry(QRect(0, 0, 79, 70))
        self.btn_menu_sair.setMinimumSize(QSize(79, 0))
        self.btn_menu_sair.setStyleSheet(u"QPushButton {padding-top: 24px; background-color: rgba(255,255,255,0); border-style: outset;}"
                                        "QPushButton:hover {background-color: rgba(255,255,255,15);} QPushButton:pressed{background-color: rgba(255,255,255,35);}")

        self.verticalLayout_10.addWidget(self.frame_iconeLogout)

        self.frame_quadradinhosB2 = QFrame(self.frame_barraLateral)
        self.frame_quadradinhosB2.setObjectName(u"frame_quadradinhosB2")
        self.frame_quadradinhosB2.setMinimumSize(QSize(68, 64))
        self.frame_quadradinhosB2.setMaximumSize(QSize(16777215, 64))
        self.frame_quadradinhosB2.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinhosB2.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_6 = QFrame(self.frame_quadradinhosB2)
        self.frame_quadradinho_6.setObjectName(u"frame_quadradinho_6")
        self.frame_quadradinho_6.setGeometry(QRect(0, 48, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_6.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_6.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_6.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_6.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_6.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_7 = QFrame(self.frame_quadradinhosB2)
        self.frame_quadradinho_7.setObjectName(u"frame_quadradinho_7")
        self.frame_quadradinho_7.setGeometry(QRect(0, 16, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_7.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_7.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_7.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_7.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_7.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_8 = QFrame(self.frame_quadradinhosB2)
        self.frame_quadradinho_8.setObjectName(u"frame_quadradinho_8")
        self.frame_quadradinho_8.setGeometry(QRect(16, 32, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_8.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_8.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_8.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_8.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_8.setFrameShadow(QFrame.Raised)

        self.frame_quadradinho_9 = QFrame(self.frame_quadradinhosB2)
        self.frame_quadradinho_9.setObjectName(u"frame_quadradinho_9")
        self.frame_quadradinho_9.setGeometry(QRect(16, 0, 16, 16))
        sizePolicy2.setHeightForWidth(self.frame_quadradinho_9.sizePolicy().hasHeightForWidth())
        self.frame_quadradinho_9.setSizePolicy(sizePolicy2)
        self.frame_quadradinho_9.setStyleSheet(u"background-color: #fff;")
        self.frame_quadradinho_9.setFrameShape(QFrame.StyledPanel)
        self.frame_quadradinho_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_quadradinhosB2)
        self.horizontalLayout_4.addWidget(self.frame_barraLateral)

        self.pages_adm = QStackedWidget(self.menu_adm)
        self.pages_adm.setObjectName(u"pages_adm")
        self.lista_chaves = QWidget()
        self.lista_chaves.setObjectName(u"lista_chaves")

        self.verticalLayout_17 = QVBoxLayout(self.lista_chaves)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.plano_fundo = QFrame(self.lista_chaves)
        self.plano_fundo.setObjectName(u"plano_fundo")
        self.plano_fundo.setMinimumSize(QSize(683, 384))
        self.plano_fundo.setFont(font)
        self.plano_fundo.setLayoutDirection(Qt.RightToLeft)
        self.plano_fundo.setStyleSheet(u"background-color: #F8FCFF;")
        self.plano_fundo.setFrameShape(QFrame.StyledPanel)
        self.plano_fundo.setFrameShadow(QFrame.Raised)
        self.plano_fundo.setLineWidth(1)

        self.horizontalLayout_27 = QHBoxLayout(self.plano_fundo)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)

        self.centro_tela_titulo = QFrame(self.plano_fundo)
        self.centro_tela_titulo.setObjectName(u"centro_tela_titulo")
        self.centro_tela_titulo.setFont(font)
        self.centro_tela_titulo.setStyleSheet(u"background-color: #F8FCFF;")
        self.centro_tela_titulo.setFrameShape(QFrame.StyledPanel)
        self.centro_tela_titulo.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_15 = QVBoxLayout(self.centro_tela_titulo)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 64, 0, 0)
        
        self.titulo = QLabel(self.centro_tela_titulo)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setStyleSheet(u"color: #064A80")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setMinimumSize(QSize(155, 70))
        self.titulo.setFont(font6)

        self.verticalLayout_15.addWidget(self.titulo)

        self.cabecario_01 = QFrame(self.centro_tela_titulo)
        self.cabecario_01.setObjectName(u"cabecario_01")
        self.cabecario_01.setMinimumSize(QSize(0, 50))
        self.cabecario_01.setStyleSheet(u"background-color: #F8FCFF;")
        self.cabecario_01.setFrameShape(QFrame.StyledPanel)
        self.cabecario_01.setFrameShadow(QFrame.Raised)
        self.cabecario_01.setLineWidth(1)

        self.verticalLayout_16 = QVBoxLayout(self.cabecario_01)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 200, 0)

        self.search_box_3 = QFrame(self.cabecario_01)
        self.search_box_3.setObjectName(u"search_box_3")
        self.search_box_3.setMinimumSize(QSize(150, 32))
        self.search_box_3.setMaximumSize(QSize(200, 32))
        self.search_box_3.setAutoFillBackground(False)
        self.search_box_3.setStyleSheet(u"QFrame{background-color: #fff; border: 1px solid #c4c4c4; border-radius: 16px} QLineEdit{border-radius: 15px}")
        self.search_box_3.setFrameShape(QFrame.StyledPanel)
        self.search_box_3.setFrameShadow(QFrame.Raised)
        
        self.lineEdit_busca_chaves = LineEdit(self.search_box_3)
        self.lineEdit_busca_chaves.setObjectName(u"lineEdit_busca_chaves")
        self.lineEdit_busca_chaves.setFont(font8)
        self.lineEdit_busca_chaves.setGeometry(QRect(1, 1, 165, 30))
        self.lineEdit_busca_chaves.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_busca_chaves.setStyleSheet(u"QLineEdit{background-color: #fff; border-top-right-radius:0px; border-bottom-right-radius:0px;"
                                        "border-right:1px solid #c4c4c4; padding-left: 14px\n}")
        self.btn_busca_chaves = QToolButton(self.search_box_3)
        self.btn_busca_chaves.setObjectName(u"btn_busca_chaves")
        self.btn_busca_chaves.setGeometry(QRect(170, 5, 22, 22))
        self.btn_busca_chaves.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_busca_chaves.setStyleSheet(u"QToolButton{background-color:#fff; border:hidden}")
        self.btn_busca_chaves.setIcon(icon1)
        self.btn_busca_chaves.setIconSize(QSize(18, 18))
        self.btn_busca_chaves.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btn_busca_chaves.setAutoRaise(False)

        self.verticalLayout_16.addWidget(self.search_box_3)
        self.verticalLayout_15.addWidget(self.cabecario_01)

        self.corpo_02 = QFrame(self.centro_tela_titulo)
        self.corpo_02.setObjectName(u"corpo_02")
        self.corpo_02.setMinimumSize(QSize(600, 350))
        self.corpo_02.setStyleSheet(u"")
        self.corpo_02.setFrameShape(QFrame.StyledPanel)
        self.corpo_02.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout_28 = QHBoxLayout(self.corpo_02)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)

        self.table_lista_chaves = QTableWidget(self.corpo_02)
        if (self.table_lista_chaves.columnCount() < 3):
            self.table_lista_chaves.setColumnCount(3)

        font4.setUnderline(True)

        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4)
        __qtablewidgetitem3.setForeground(QColor('#064A80'))
        self.table_lista_chaves.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4)
        __qtablewidgetitem4.setForeground(QColor('#064A80'))
        self.table_lista_chaves.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setForeground(QColor('#064A80'))
        self.table_lista_chaves.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        
        self.table_lista_chaves.setObjectName(u"table_lista_chaves")
        self.table_lista_chaves.setMinimumSize(QSize(600, 350))
        self.table_lista_chaves.setMaximumSize(QSize(600, 400))
        self.table_lista_chaves.setLayoutDirection(Qt.LeftToRight)

        self.table_lista_chaves.setPalette(p)

        self.table_lista_chaves.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom: 24px; background-color: #F8FCFF; border:hidden}")
        self.table_lista_chaves.setStyleSheet(u"QTableView{border: hidden;} QTableView:item{outline: 0}")
        self.table_lista_chaves.verticalHeader().setVisible(False)
        self.table_lista_chaves.horizontalHeader().setHighlightSections(False)
        self.table_lista_chaves.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_lista_chaves.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_lista_chaves.setFocusPolicy(Qt.NoFocus)
        self.table_lista_chaves.setAlternatingRowColors(True)
        self.table_lista_chaves.setShowGrid(False)
        self.table_lista_chaves.setSortingEnabled(False)
        self.table_lista_chaves.setFont(font3)
        self.table_lista_chaves.setFocus()

        self.horizontalLayout_28.addWidget(self.table_lista_chaves)
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(self.horizontalSpacer_39)

        self.verticalLayout_15.addWidget(self.corpo_02)

        self.botao_novo = QFrame(self.centro_tela_titulo)
        self.botao_novo.setObjectName(u"botao_novo")
        self.botao_novo.setMinimumSize(QSize(150, 50))
        self.botao_novo.setStyleSheet(u"background-color: #F8FCFF;")
        self.botao_novo.setFrameShape(QFrame.StyledPanel)
        self.botao_novo.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout_29 = QHBoxLayout(self.botao_novo)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(self.horizontalSpacer_40)

        self.btn_nova_chave = QPushButton(self.botao_novo)
        self.btn_nova_chave.setObjectName(u"btn_nova_chave")
        self.btn_nova_chave.setMinimumSize(QSize(145, 40))
        self.btn_nova_chave.setMaximumSize(QSize(145, 40))
        self.btn_nova_chave.setCursor(Qt.PointingHandCursor)
        self.btn_nova_chave.setFont(font)
        self.btn_nova_chave.setStyleSheet(u"QPushButton{background-color: rgb(6, 74, 128); border-radius: 20px; color: #F8FCFF} QPushButton:hover{font-weight:600; outline: 0} QPushButton:focus{font-weight:600; outline: 0}")

        self.horizontalLayout_29.addWidget(self.btn_nova_chave)
        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(self.horizontalSpacer_41)

        self.btn_imp_chave = QPushButton(self.botao_novo)
        self.btn_imp_chave.setObjectName(u"btn_imp_chave")
        self.btn_imp_chave.setMinimumSize(QSize(145, 40))
        self.btn_imp_chave.setMaximumSize(QSize(145, 40))
        self.btn_imp_chave.setCursor(Qt.PointingHandCursor)
        self.btn_imp_chave.setFont(font)
        self.btn_imp_chave.setAutoFillBackground(False)
        self.btn_imp_chave.setStyleSheet(u"QPushButton{background-color: rgb(6, 74, 128); border-radius: 20px; color: #F8FCFF;} QPushButton:hover{font-weight:600; outline: 0} QPushButton:focus{font-weight:600; outline: 0}")

        self.horizontalLayout_29.addWidget(self.btn_imp_chave)
        self.horizontalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(self.horizontalSpacer_42)

        self.btn_exc_chave = QPushButton(self.botao_novo)
        self.btn_exc_chave.setObjectName(u"btn_exc_chave")
        self.btn_exc_chave.setMinimumSize(QSize(145, 40))
        self.btn_exc_chave.setMaximumSize(QSize(145, 40))
        self.btn_exc_chave.setCursor(Qt.PointingHandCursor)
        self.btn_exc_chave.setFont(font)
        self.btn_exc_chave.setStyleSheet(u"QPushButton{border: 2px solid #064A80; border-radius: 20px; color: rgb(6, 74, 128);} QPushButton:hover{font-weight:600; outline: 0; border: 2px solid #064A80;} QPushButton:focus{font-weight:600; outline: 0; border: 2px solid #064A80;}")

        self.horizontalLayout_29.addWidget(self.btn_exc_chave)
        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(self.horizontalSpacer_43)

        self.verticalLayout_15.addWidget(self.botao_novo)

        self.rodape_2 = QFrame(self.centro_tela_titulo)
        self.rodape_2.setObjectName(u"rodape_2")
        self.rodape_2.setMinimumSize(QSize(0, 150))
        self.rodape_2.setLayoutDirection(Qt.RightToLeft)
        self.rodape_2.setStyleSheet(u"background-color: #F8FCFF;")
        self.rodape_2.setFrameShape(QFrame.StyledPanel)
        self.rodape_2.setFrameShadow(QFrame.Raised)
        self.rodape_2.setLineWidth(0)
        self.rodape_2.setMidLineWidth(0)

        self.horizontalLayout_30 = QHBoxLayout(self.rodape_2)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.art_1 = QFrame(self.rodape_2)
        self.art_1.setObjectName(u"art_1")
        self.art_1.setMinimumSize(QSize(180, 150))
        self.art_1.setMaximumSize(QSize(180, 150))
        self.art_1.setLayoutDirection(Qt.LeftToRight)
        self.art_1.setStyleSheet(u"background-color: #DEEAFF;")
        self.art_1.setFrameShape(QFrame.StyledPanel)
        self.art_1.setFrameShadow(QFrame.Raised)

        self.frame_97 = QFrame(self.art_1)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setGeometry(QRect(30, 120, 30, 30))
        self.frame_97.setMaximumSize(QSize(30, 30))
        self.frame_97.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)

        self.frame_98 = QFrame(self.art_1)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setGeometry(QRect(120, 120, 30, 30))
        self.frame_98.setMaximumSize(QSize(30, 30))
        self.frame_98.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)

        self.frame_99 = QFrame(self.art_1)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setGeometry(QRect(0, 90, 30, 30))
        self.frame_99.setMaximumSize(QSize(30, 30))
        self.frame_99.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)

        self.frame_100 = QFrame(self.art_1)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setGeometry(QRect(150, 90, 30, 30))
        self.frame_100.setMaximumSize(QSize(30, 30))
        self.frame_100.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)

        self.frame_101 = QFrame(self.art_1)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setGeometry(QRect(120, 0, 30, 30))
        self.frame_101.setMaximumSize(QSize(30, 30))
        self.frame_101.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)

        self.frame_102 = QFrame(self.art_1)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setGeometry(QRect(150, 30, 30, 30))
        self.frame_102.setMaximumSize(QSize(30, 30))
        self.frame_102.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)

        self.frame_103 = QFrame(self.art_1)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setGeometry(QRect(0, 30, 30, 30))
        self.frame_103.setMaximumSize(QSize(30, 30))
        self.frame_103.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)

        self.frame_104 = QFrame(self.art_1)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setGeometry(QRect(30, 0, 30, 30))
        self.frame_104.setMaximumSize(QSize(30, 30))
        self.frame_104.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.art_1, 0, Qt.AlignBottom)
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(self.horizontalSpacer_44)

        self.art_2 = QFrame(self.rodape_2)
        self.art_2.setObjectName(u"art_2")
        self.art_2.setMinimumSize(QSize(180, 150))
        self.art_2.setMaximumSize(QSize(180, 150))
        self.art_2.setStyleSheet(u"background-color: #DEEAFF;")
        self.art_2.setFrameShape(QFrame.StyledPanel)
        self.art_2.setFrameShadow(QFrame.Raised)

        self.frame_105 = QFrame(self.art_2)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setGeometry(QRect(30, 120, 30, 30))
        self.frame_105.setMaximumSize(QSize(30, 30))
        self.frame_105.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)

        self.frame_106 = QFrame(self.art_2)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setGeometry(QRect(120, 120, 30, 30))
        self.frame_106.setMaximumSize(QSize(30, 30))
        self.frame_106.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)

        self.frame_107 = QFrame(self.art_2)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setGeometry(QRect(0, 90, 30, 30))
        self.frame_107.setMaximumSize(QSize(30, 30))
        self.frame_107.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.frame_108 = QFrame(self.art_2)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setGeometry(QRect(150, 90, 30, 30))
        self.frame_108.setMaximumSize(QSize(30, 30))
        self.frame_108.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)

        self.frame_109 = QFrame(self.art_2)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setGeometry(QRect(120, 0, 30, 30))
        self.frame_109.setMaximumSize(QSize(30, 30))
        self.frame_109.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)

        self.frame_110 = QFrame(self.art_2)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setGeometry(QRect(150, 30, 30, 30))
        self.frame_110.setMaximumSize(QSize(30, 30))
        self.frame_110.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)

        self.frame_111 = QFrame(self.art_2)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setGeometry(QRect(0, 30, 30, 30))
        self.frame_111.setMaximumSize(QSize(30, 30))
        self.frame_111.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)

        self.frame_112 = QFrame(self.art_2)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setGeometry(QRect(30, 0, 30, 30))
        self.frame_112.setMaximumSize(QSize(30, 30))
        self.frame_112.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.art_2, 0, Qt.AlignBottom)
        self.verticalLayout_15.addWidget(self.rodape_2)
        self.horizontalLayout_27.addWidget(self.centro_tela_titulo)
        self.verticalLayout_17.addWidget(self.plano_fundo)

        self.pages_adm.addWidget(self.lista_chaves)
        self.cad_chaves = QWidget()
        self.cad_chaves.setObjectName(u"cad_chaves")

        self.verticalLayout_14 = QVBoxLayout(self.cad_chaves)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.telaBranca = QFrame(self.cad_chaves)
        self.telaBranca.setObjectName(u"telaBranca")
        self.telaBranca.setMinimumSize(QSize(166, 155))
        self.telaBranca.setMaximumSize(QSize(16777215, 16777215))
        self.telaBranca.setStyleSheet(u"background-color: #F8FCFF;")
        self.telaBranca.setFrameShape(QFrame.StyledPanel)
        self.telaBranca.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11 = QVBoxLayout(self.telaBranca)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(self.verticalSpacer_16)

        self.frame_83 = QFrame(self.telaBranca)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 91))
        self.frame_83.setMaximumSize(QSize(16777215, 16777215))
        self.frame_83.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.label_6 = QLabel(self.frame_83)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet("color:#064A80")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.verticalLayout_11.addWidget(self.frame_83)
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(self.verticalSpacer_17)

        self.frame_84 = QFrame(self.telaBranca)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 100))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(self.horizontalSpacer_31)

        self.botonNumero = QFrame(self.frame_84)
        self.botonNumero.setObjectName(u"botonNumero")
        self.botonNumero.setMinimumSize(QSize(404, 0))
        self.botonNumero.setMaximumSize(QSize(16777215, 16777215))
        self.botonNumero.setFrameShape(QFrame.StyledPanel)
        self.botonNumero.setFrameShadow(QFrame.Raised)

        self.label_chave_cad = QLabel(self.botonNumero)
        self.label_chave_cad.setObjectName(u"label_chave_cad")
        self.label_chave_cad.setGeometry(QRect(10, 0, 151, 35))
        self.label_chave_cad.setFont(font)

        self.lineEdit_chave_cad = QLineEdit(self.botonNumero)
        self.lineEdit_chave_cad.setObjectName(u"lineEdit_chave_cad")
        self.lineEdit_chave_cad.setGeometry(QRect(0, 40, 404, 30))
        self.lineEdit_chave_cad.setFont(font7)
        self.lineEdit_chave_cad.setStyleSheet(u"border-radius:15px; background-color: #DEEAFF; padding-left: 14px")

        self.horizontalLayout_16.addWidget(self.botonNumero)
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(self.horizontalSpacer_32)

        self.botonAmbiente = QFrame(self.frame_84)
        self.botonAmbiente.setObjectName(u"botonAmbiente")
        self.botonAmbiente.setMinimumSize(QSize(404, 0))
        self.botonAmbiente.setMaximumSize(QSize(16777215, 16777215))
        self.botonAmbiente.setFrameShape(QFrame.StyledPanel)
        self.botonAmbiente.setFrameShadow(QFrame.Raised)

        self.label_amb_cad = QLabel(self.botonAmbiente)
        self.label_amb_cad.setObjectName(u"label_amb_cad")
        self.label_amb_cad.setGeometry(QRect(10, 0, 151, 35))
        self.label_amb_cad.setFont(font)

        self.lineEdit_amb_cad = QLineEdit(self.botonAmbiente)
        self.lineEdit_amb_cad.setObjectName(u"lineEdit_amb_cad")
        self.lineEdit_amb_cad.setGeometry(QRect(0, 40, 404, 30))
        self.lineEdit_amb_cad.setFont(font7)
        self.lineEdit_amb_cad.setStyleSheet(u"border-radius:15px; background-color: #DEEAFF; padding-left: 14px")

        self.horizontalLayout_16.addWidget(self.botonAmbiente)
        self.horizontalSpacer_33 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(self.horizontalSpacer_33)

        self.verticalLayout_11.addWidget(self.frame_84)
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(self.verticalSpacer_22)

        self.frame_85 = QFrame(self.telaBranca)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 95))
        self.frame_85.setMaximumSize(QSize(16777215, 16777215))
        self.frame_85.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.frame_85.setLineWidth(0)

        self.horizontalLayout_25 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_34)

        self.btn_voltar_chave = QPushButton(self.frame_85)
        self.btn_voltar_chave.setObjectName(u"btn_voltar_chave")
        self.btn_voltar_chave.setMinimumSize(QSize(196, 57))
        self.btn_voltar_chave.setMaximumSize(QSize(196, 57))
        self.btn_voltar_chave.setCursor(Qt.PointingHandCursor)
        self.btn_voltar_chave.setFont(font)
        self.btn_voltar_chave.setStyleSheet(u"QPushButton:hover{font-weight: 600; border-width:3px} QPushButton:focus{font-weight:600; outline:0}"
                                                "QPushButton{border-radius:26px; color:#064a80;  border:2px solid #064a80;}")

        self.horizontalLayout_25.addWidget(self.btn_voltar_chave)
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_35)

        self.btn_salvar_chave = QPushButton(self.frame_85)
        self.btn_salvar_chave.setObjectName(u"btn_salvar_chave")
        self.btn_salvar_chave.setMinimumSize(QSize(196, 57))
        self.btn_salvar_chave.setMaximumSize(QSize(196, 57))
        self.btn_salvar_chave.setCursor(Qt.PointingHandCursor)
        self.btn_salvar_chave.setFont(font)
        self.btn_salvar_chave.setStyleSheet(u"QPushButton:hover{font-weight: 600} QPushButton:focus{font-weight:600; outline:0}"
                                                "QPushButton{border-radius:26px; background-color: #064a80; color: #fff;}")

        self.horizontalLayout_25.addWidget(self.btn_salvar_chave)
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_36)

        self.horizontalLayout_25.setStretch(0, 3)
        self.horizontalLayout_25.setStretch(2, 1)
        self.horizontalLayout_25.setStretch(4, 3)

        self.verticalLayout_11.addWidget(self.frame_85)
        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(self.verticalSpacer_23)

        self.frame_86 = QFrame(self.telaBranca)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 150))
        self.frame_86.setMaximumSize(QSize(16777215, 16777215))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(90, 0))
        self.frame_87.setMaximumSize(QSize(16777215, 16777215))
        self.frame_87.setStyleSheet(u"background-color: #DEEAFF;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)

        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setGeometry(QRect(30, 0, 30, 30))
        self.frame_88.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setGeometry(QRect(60, 90, 30, 30))
        self.frame_89.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)

        self.frame_90 = QFrame(self.frame_87)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setGeometry(QRect(60, 30, 30, 30))
        self.frame_90.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)

        self.frame_91 = QFrame(self.frame_87)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setGeometry(QRect(30, 120, 30, 30))
        self.frame_91.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_87)
        self.horizontalSpacer_37 = QSpacerItem(1111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(self.horizontalSpacer_37)

        self.frame_92 = QFrame(self.frame_86)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(90, 150))
        self.frame_92.setStyleSheet(u"background-color: #DEEAFF;")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)

        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setGeometry(QRect(30, 0, 30, 30))
        self.frame_93.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setGeometry(QRect(0, 90, 30, 30))
        self.frame_94.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)

        self.frame_95 = QFrame(self.frame_92)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setGeometry(QRect(0, 30, 30, 30))
        self.frame_95.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setGeometry(QRect(30, 120, 30, 30))
        self.frame_96.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_92)

        self.verticalLayout_11.addWidget(self.frame_86)
        self.verticalLayout_14.addWidget(self.telaBranca)

        self.pages_adm.addWidget(self.cad_chaves)
        self.lista_usuarios = QWidget()
        self.lista_usuarios.setObjectName(u"lista_usuarios")
        self.lista_usuarios.setStyleSheet(u"background-color: #F8FCFF;")

        self.verticalLayout_12 = QVBoxLayout(self.lista_usuarios)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.centro = QVBoxLayout()
        self.centro.setSpacing(6)
        self.centro.setObjectName(u"centro")
        self.verticalSpacer_4 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro.addItem(self.verticalSpacer_4)

        self.title_usuarios = QLabel(self.lista_usuarios)
        self.title_usuarios.setObjectName(u"title_usuarios")
        self.title_usuarios.setFont(font6)
        self.title_usuarios.setStyleSheet(u"color: rgb(6, 74, 128);")
        self.title_usuarios.setAlignment(Qt.AlignCenter)

        self.centro.addWidget(self.title_usuarios)

        self.mainFrame_searchBox = QFrame(self.lista_usuarios)
        self.mainFrame_searchBox.setObjectName(u"mainFrame_searchBox")
        self.mainFrame_searchBox.setMinimumSize(QSize(200, 50))
        self.mainFrame_searchBox.setStyleSheet(u"")
        self.mainFrame_searchBox.setFrameShape(QFrame.StyledPanel)
        self.mainFrame_searchBox.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5 = QHBoxLayout(self.mainFrame_searchBox)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 16, 0)
        self.horizontalSpacer_7 = QSpacerItem(1065, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.search_box_2 = QFrame(self.mainFrame_searchBox)
        self.search_box_2.setObjectName(u"search_box_2")
        self.search_box_2.setMinimumSize(QSize(200, 32))
        self.search_box_2.setMaximumSize(QSize(200, 32))
        self.search_box_2.setStyleSheet(u"QFrame{border: 1px solid #c4c4c4; border-radius: 16px; background-color: #fff} QLineEdit{border-radius: 15px; background-color: #fff}")
        self.search_box_2.setFrameShape(QFrame.StyledPanel)
        self.search_box_2.setFrameShadow(QFrame.Raised)

        self.lineEdit_busca_usuarios = LineEdit(self.search_box_2)
        self.lineEdit_busca_usuarios.setObjectName(u"lineEdit_busca_usuarios")
        self.lineEdit_busca_usuarios.setGeometry(QRect(1, 1, 165, 30))
        self.lineEdit_busca_usuarios.setMinimumSize(QSize(165, 30))
        self.lineEdit_busca_usuarios.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_busca_usuarios.setFont(font8)
        self.lineEdit_busca_usuarios.setStyleSheet(u"QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;border-right:1px solid #c4c4c4; padding-left: 14px; color: #A0A0A0;}")
        
        self.btn_busca_usuarios = QToolButton(self.search_box_2)
        self.btn_busca_usuarios.setObjectName(u"btn_busca_usuarios")
        self.btn_busca_usuarios.setCursor(Qt.PointingHandCursor)
        self.btn_busca_usuarios.setGeometry(QRect(170, 5, 22, 22))
        self.btn_busca_usuarios.setStyleSheet(u"QToolButton{background-color: #fff; border:hidden}")
        self.btn_busca_usuarios.setIcon(icon1)
        self.btn_busca_usuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.search_box_2)

        self.centro.addWidget(self.mainFrame_searchBox)
        self.verticalSpacer_5 = QSpacerItem(1293, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro.addItem(self.verticalSpacer_5)

        self.layout_table = QHBoxLayout()
        self.layout_table.setObjectName(u"layout_table")
        self.horizontalSpacer_5 = QSpacerItem(199, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_table.addItem(self.horizontalSpacer_5)

        self.table_lista_usuarios = QTableWidget(self.lista_usuarios)
        if (self.table_lista_usuarios.columnCount() < 5):
            self.table_lista_usuarios.setColumnCount(5)

        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font4)
        __qtablewidgetitem29.setForeground(QColor('#064A80'))
        self.table_lista_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font4)
        __qtablewidgetitem30.setForeground(QColor('#064A80'))
        self.table_lista_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font4)
        __qtablewidgetitem31.setForeground(QColor('#064A80'))
        self.table_lista_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font4)
        __qtablewidgetitem32.setForeground(QColor('#064A80'))
        self.table_lista_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font4)
        __qtablewidgetitem33.setForeground(QColor('#064A80'))
        self.table_lista_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        self.table_lista_usuarios.setObjectName(u"table_lista_usuarios")
        self.table_lista_usuarios.setMinimumSize(QSize(500, 500))
        self.table_lista_usuarios.setMaximumSize(QSize(800, 800))
        self.table_lista_usuarios.setStyleSheet(u"color: rgb(17, 17, 17);")
        
        self.table_lista_usuarios.setPalette(p)

        self.table_lista_usuarios.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom: 24px; background-color: #F8FCFF; border:hidden}")
        self.table_lista_usuarios.setStyleSheet(u"QTableView{border: hidden;} QTableView:item{outline: 0}")
        self.table_lista_usuarios.verticalHeader().setVisible(False)
        self.table_lista_usuarios.horizontalHeader().setHighlightSections(False)
        self.table_lista_usuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_lista_usuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_lista_usuarios.setFocusPolicy(Qt.NoFocus)
        self.table_lista_usuarios.setAlternatingRowColors(True)
        self.table_lista_usuarios.setShowGrid(False)
        self.table_lista_usuarios.setSortingEnabled(False)
        self.table_lista_usuarios.setFont(font3)


        self.layout_table.addWidget(self.table_lista_usuarios)
        self.horizontalSpacer_6 = QSpacerItem(199, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_table.addItem(self.horizontalSpacer_6)

        self.centro.addLayout(self.layout_table)
        self.verticalSpacer_6 = QSpacerItem(10, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro.addItem(self.verticalSpacer_6)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setObjectName(u"layout_btn")
        self.horizontalSpacer_4 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_btn.addItem(self.horizontalSpacer_4)

        self.frame_btns = QFrame(self.lista_usuarios)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(600, 45))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 89)

        self.btn_exc_usuarios = QPushButton(self.frame_btns)
        self.btn_exc_usuarios.setObjectName(u"btn_exc_usuarios")
        self.btn_exc_usuarios.setCursor(Qt.PointingHandCursor)
        self.btn_exc_usuarios.setFont(font)
        self.btn_exc_usuarios.setMinimumSize(QSize(163, 40))
        self.btn_exc_usuarios.setMaximumSize(QSize(163, 40))
        self.btn_exc_usuarios.setStyleSheet(u"QPushButton:hover{font-weight:600} QPushButton:focus{font-weight:600; outline:0}"
                                               "QPushButton{border-radius: 20px; border: 2px solid; color: rgb(6, 74, 128); border-color: rgb(6, 74, 128)}")

        self.horizontalLayout_13.addWidget(self.btn_exc_usuarios)
        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.btn_imp_usuarios = QPushButton(self.frame_btns)
        self.btn_imp_usuarios.setObjectName(u"btn_imp_usuarios")
        self.btn_imp_usuarios.setCursor(Qt.PointingHandCursor)
        self.btn_imp_usuarios.setFont(font)
        self.btn_imp_usuarios.setMinimumSize(QSize(163, 40))
        self.btn_imp_usuarios.setMaximumSize(QSize(163, 40))
        self.btn_imp_usuarios.setStyleSheet(u"QPushButton:hover{font-weight:600} QPushButton:focus{font-weight:600; outline:0}"
                                               "QPushButton{border-radius: 20px; color: #fff; background-color: rgb(6, 74, 128)}")

        self.horizontalLayout_13.addWidget(self.btn_imp_usuarios)
        self.horizontalSpacer_9 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.btn_cad_usuarios = QPushButton(self.frame_btns)
        self.btn_cad_usuarios.setObjectName(u"btn_cad_usuarios")
        self.btn_cad_usuarios.setCursor(Qt.PointingHandCursor)
        self.btn_cad_usuarios.setFont(font)
        self.btn_cad_usuarios.setMinimumSize(QSize(163, 40))
        self.btn_cad_usuarios.setMaximumSize(QSize(163, 40))
        self.btn_cad_usuarios.setStyleSheet(u"QPushButton:hover{font-weight:600} QPushButton:focus{font-weight:600; outline:0}"
                                               "QPushButton{border-radius: 20px; color: #fff; background-color: rgb(6, 74, 128)}")

        self.horizontalLayout_13.addWidget(self.btn_cad_usuarios)
        self.layout_btn.addWidget(self.frame_btns)
        self.horizontalSpacer_10 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_btn.addItem(self.horizontalSpacer_10)

        self.centro.addLayout(self.layout_btn)
        self.verticalSpacer_7 = QSpacerItem(1293, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro.addItem(self.verticalSpacer_7)

        self.verticalLayout_12.addLayout(self.centro)

        self.pages_adm.addWidget(self.lista_usuarios)
        self.cad_usuarios = QWidget()
        self.cad_usuarios.setObjectName(u"cad_usuarios")

        self.verticalLayout_13 = QVBoxLayout(self.cad_usuarios)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.frame_19 = QFrame(self.cad_usuarios)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(1000, 0))
        self.frame_19.setStyleSheet(u"background-color:#F8FCFF;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(0)

        self.horizontalLayout_7 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(84, 768))
        self.frame_21.setMaximumSize(QSize(1600, 16000))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame_21)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(84, 155))
        self.frame_22.setMaximumSize(QSize(84, 155))
        self.frame_22.setStyleSheet(u"background-color: #DEEAFF;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(54, 30, 31, 31))
        self.frame_23.setMinimumSize(QSize(31, 31))
        self.frame_23.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_24.setMinimumSize(QSize(31, 31))
        self.frame_24.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(23, 0, 31, 31))
        self.frame_25.setMinimumSize(QSize(31, 31))
        self.frame_25.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_26.setMinimumSize(QSize(31, 31))
        self.frame_26.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(24, 125, 31, 31))
        self.frame_27.setMinimumSize(QSize(31, 31))
        self.frame_27.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_28.setMinimumSize(QSize(31, 31))
        self.frame_28.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.frame_29 = QFrame(self.frame_22)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(55, 94, 31, 31))
        self.frame_29.setMinimumSize(QSize(31, 31))
        self.frame_29.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_30.setMinimumSize(QSize(31, 31))
        self.frame_30.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_22, 1, 0, 1, 1)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.horizontalLayout_7.addWidget(self.frame_21)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.centro_2 = QVBoxLayout()
        self.centro_2.setSpacing(0)
        self.centro_2.setObjectName(u"centro_2")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro_2.addItem(self.verticalSpacer_9)

        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 10))
        self.label_3.setMaximumSize(QSize(948, 100))
        self.label_3.setSizeIncrement(QSize(948, 0))
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color:rgb(6, 74, 128);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.centro_2.addWidget(self.label_3, 0, Qt.AlignTop)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro_2.addItem(self.verticalSpacer_10)

        self.frame_31 = QFrame(self.frame_19)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(948, 100))
        self.frame_31.setMaximumSize(QSize(800, 61))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_8.setSpacing(50)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(391, 61))
        self.frame_32.setMaximumSize(QSize(391, 61))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.label_cad_nome = QLabel(self.frame_32)
        self.label_cad_nome.setObjectName(u"label_cad_nome")
        self.label_cad_nome.setGeometry(QRect(10, 0, 81, 26))
        self.label_cad_nome.setFont(font)

        self.lineEdit_cad_nome = QLineEdit(self.frame_32)
        self.lineEdit_cad_nome.setObjectName(u"lineEdit_cad_nome")
        self.lineEdit_cad_nome.setGeometry(QRect(0, 30, 391, 30))
        self.lineEdit_cad_nome.setMinimumSize(QSize(391, 30))
        self.lineEdit_cad_nome.setMaximumSize(QSize(391, 16777215))
        self.lineEdit_cad_nome.setFont(font7)
        self.lineEdit_cad_nome.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lineEdit_cad_nome.setStyleSheet(u"border-radius:15px; background:rgb(210, 228, 255); padding-left: 14px")
        self.lineEdit_cad_nome.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.horizontalLayout_8.addWidget(self.frame_32)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(391, 61))
        self.frame_33.setMaximumSize(QSize(391, 61))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.lineEdit_cad_id = QLineEdit(self.frame_33)
        self.lineEdit_cad_id.setObjectName(u"lineEdit_cad_id")
        self.lineEdit_cad_id.setGeometry(QRect(0, 30, 391, 30))
        self.lineEdit_cad_id.setMinimumSize(QSize(391, 30))
        self.lineEdit_cad_id.setMaximumSize(QSize(391, 16777215))

        palette = QPalette()
        brush = QBrush(QColor(210, 228, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)

        self.lineEdit_cad_id.setPalette(palette)
        self.lineEdit_cad_id.setFont(font7)
        self.lineEdit_cad_id.setStyleSheet(u"border-radius:15px; background:rgb(210, 228, 255); padding-left: 14px")

        self.label_cad_id = QLabel(self.frame_33)
        self.label_cad_id.setObjectName(u"label_cad_id")
        self.label_cad_id.setGeometry(QRect(10, 0, 151, 26))
        self.label_cad_id.setFont(font)

        self.horizontalLayout_8.addWidget(self.frame_33)
        self.centro_2.addWidget(self.frame_31)

        self.frame_34 = QFrame(self.frame_19)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(948, 100))
        self.frame_34.setMaximumSize(QSize(800, 61))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(391, 0))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.cbb_cad_acesso = QComboBox(self.frame_35)
        self.cbb_cad_acesso.addItem("")
        self.cbb_cad_acesso.addItem("")
        self.cbb_cad_acesso.setObjectName(u"cbb_cad_acesso")
        self.cbb_cad_acesso.setCursor(Qt.PointingHandCursor)
        self.cbb_cad_acesso.setGeometry(QRect(0, 40, 391, 30))
        self.cbb_cad_acesso.setMinimumSize(QSize(391, 30))
        self.cbb_cad_acesso.setMaximumSize(QSize(391, 30))
        self.cbb_cad_acesso.setFont(font7)
        self.cbb_cad_acesso.setStyleSheet(u"QComboBox{border-radius:15px; background:rgb(210, 228, 255);} QComboBox:drop-down{width: 32px; border:hidden}"
                                            "QComboBox:down-arrow{image: url(icons/expand_more_black_18dp.svg); width: 18px; height: 18px; padding-right: 8px;}")
        self.cbb_cad_acesso.setMaxVisibleItems(10)
        self.cbb_cad_acesso.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.label_cad_acesso = QLabel(self.frame_35)
        self.label_cad_acesso.setObjectName(u"label_cad_acesso")
        self.label_cad_acesso.setGeometry(QRect(10, 10, 171, 26))
        self.label_cad_acesso.setFont(font)

        self.horizontalLayout_9.addWidget(self.frame_35)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(391, 61))
        self.frame_36.setMaximumSize(QSize(16777215, 61))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.lineEdit_cad_senha = QLineEdit(self.frame_36)
        self.lineEdit_cad_senha.setObjectName(u"lineEdit_cad_senha")
        self.lineEdit_cad_senha.setGeometry(QRect(0, 30, 391, 30))
        self.lineEdit_cad_senha.setMinimumSize(QSize(391, 30))
        self.lineEdit_cad_senha.setMaximumSize(QSize(391, 16777215))
        self.lineEdit_cad_senha.setFont(font7)
        self.lineEdit_cad_senha.setStyleSheet(u"border-radius:15px; background:rgb(210, 228, 255); padding-left: 14px")

        self.label_cad_senha = QLabel(self.frame_36)
        self.label_cad_senha.setObjectName(u"label_cad_senha")
        self.label_cad_senha.setGeometry(QRect(10, 0, 81, 26))
        self.label_cad_senha.setFont(font)

        self.horizontalLayout_9.addWidget(self.frame_36)
        self.centro_2.addWidget(self.frame_34)

        self.frame_37 = QFrame(self.frame_19)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(948, 100))
        self.frame_37.setMaximumSize(QSize(16777215, 61))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(10, 20, 391, 61))
        self.frame_38.setMinimumSize(QSize(391, 60))
        self.frame_38.setMaximumSize(QSize(16777215, 61))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.lineEdit_cad_email = QLineEdit(self.frame_38)
        self.lineEdit_cad_email.setObjectName(u"lineEdit_cad_email")
        self.lineEdit_cad_email.setGeometry(QRect(0, 30, 391, 30))
        self.lineEdit_cad_email.setMinimumSize(QSize(391, 30))
        self.lineEdit_cad_email.setMaximumSize(QSize(391, 16777215))
        self.lineEdit_cad_email.setFont(font7)
        self.lineEdit_cad_email.setStyleSheet(u"border-radius:15px ;background:rgb(210, 228, 255); padding-left: 14px")

        self.label_cad_email = QLabel(self.frame_38)
        self.label_cad_email.setObjectName(u"label_cad_email")
        self.label_cad_email.setGeometry(QRect(10, 0, 81, 26))
        self.label_cad_email.setFont(font)

        self.centro_2.addWidget(self.frame_37)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro_2.addItem(self.verticalSpacer_11)

        self.frame_39 = QFrame(self.frame_19)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(948, 0))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)

        self.btn_cad_cancelar = QPushButton(self.frame_39)
        self.btn_cad_cancelar.setObjectName(u"btn_cad_cancelar")
        self.btn_cad_cancelar.setCursor(Qt.PointingHandCursor)
        self.btn_cad_cancelar.setFont(font)
        self.btn_cad_cancelar.setMinimumSize(QSize(196, 60))
        self.btn_cad_cancelar.setMaximumSize(QSize(196, 60))
        self.btn_cad_cancelar.setStyleSheet(u"QPushButton:hover{font-weight: 600; border-width: 3px} QPushButton:focus{font-weight: 600; outline: 0; border-width: 3px}"
                                              "QPushButton{border: 2px solid rgb(6, 74, 128); border-radius:30px; background:#F8FCFF; color: rgb(6, 74, 128)}")

        self.horizontalLayout_10.addWidget(self.btn_cad_cancelar)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.btn_cad_salvar = QPushButton(self.frame_39)
        self.btn_cad_salvar.setObjectName(u"btn_cad_salvar")
        self.btn_cad_salvar.setCursor(Qt.PointingHandCursor)
        self.btn_cad_salvar.setFont(font)
        self.btn_cad_salvar.setMinimumSize(QSize(196, 60))
        self.btn_cad_salvar.setMaximumSize(QSize(196, 60))
        self.btn_cad_salvar.setStyleSheet(u"QPushButton:hover{font-weight: 600} QPushButton:focus{font-weight: 600; outline: 0}"
                                            "QPushButton{border-radius:30px; background:rgb(6, 74, 128); color:#F8FCFF; border-color: rgb(0, 255, 0)}")

        self.horizontalLayout_10.addWidget(self.btn_cad_salvar)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)

        self.centro_2.addWidget(self.frame_39)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centro_2.addItem(self.verticalSpacer_12)

        self.horizontalLayout_7.addLayout(self.centro_2)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.frame_40 = QFrame(self.frame_19)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(31, 31))
        self.frame_40.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_19)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(84, 768))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.gridLayout_2 = QGridLayout(self.frame_41)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(84, 155))
        self.frame_42.setMaximumSize(QSize(84, 155))
        self.frame_42.setStyleSheet(u"background-color: #DEEAFF;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(0, 30, 31, 31))
        self.frame_43.setMinimumSize(QSize(31, 31))
        self.frame_43.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_44.setMinimumSize(QSize(31, 31))
        self.frame_44.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(30, 0, 31, 31))
        self.frame_45.setMinimumSize(QSize(31, 31))
        self.frame_45.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.frame_46 = QFrame(self.frame_42)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(0, 93, 31, 31))
        self.frame_46.setMinimumSize(QSize(31, 31))
        self.frame_46.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.frame_46.setLineWidth(0)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_47.setMinimumSize(QSize(31, 31))
        self.frame_47.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(31, 124, 32, 31))
        self.frame_48.setMinimumSize(QSize(31, 31))
        self.frame_48.setStyleSheet(u"background-color: #F8FCFF;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setGeometry(QRect(-20, 30, 31, 31))
        self.frame_49.setMinimumSize(QSize(31, 31))
        self.frame_49.setStyleSheet(u"background-color: rgb(247, 250, 255);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_42, 1, 0, 1, 1)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(self.verticalSpacer_13, 0, 0, 1, 1)

        self.horizontalLayout_7.addWidget(self.frame_41)
        self.verticalLayout_13.addWidget(self.frame_19)

        self.pages_adm.addWidget(self.cad_usuarios)
        self.historico = QWidget()
        self.historico.setObjectName(u"historico")
        self.pages_adm.addWidget(self.historico)
        self.impressao = QWidget()
        self.impressao.setObjectName(u"impressao")
        self.pages_adm.addWidget(self.impressao)

        self.horizontalLayout_4.addWidget(self.pages_adm)
        self.pages.addWidget(self.menu_adm)
        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        #VALIDADORES
        #########################################################
        #self.lineEdit_email_inicio.setValidator(self.validaEmail)
        self.lineEdit_email_inicio.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_senha_inicio.setMaxLength(25)
        #-------------------------------------------------------#
        self.lineEdit_codigo.setValidator(self.validaInteiro)
        self.lineEdit_codigo.setMaxLength(4)
        #-------------------------------------------------------#
        self.lineEdit_chave.setValidator(self.validaInteiro)
        self.lineEdit_chave.setMaxLength(3)
        #-------------------------------------------------------#
        self.lineEdit_busca_emprestimos.setValidator(self.validaTexto)
        self.lineEdit_busca_emprestimos.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_busca_chaves.setValidator(self.validaTexto)
        self.lineEdit_busca_chaves.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_chave_cad.setValidator(self.validaInteiro)
        self.lineEdit_chave_cad.setMaxLength(3)
        #-------------------------------------------------------#
        self.lineEdit_amb_cad.setValidator(self.validaTexto)
        self.lineEdit_amb_cad.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_busca_usuarios.setValidator(self.validaTexto)
        self.lineEdit_busca_usuarios.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_cad_nome.setValidator(self.validaNome)
        self.lineEdit_cad_nome.setMaxLength(50)
        #-------------------------------------------------------#
        self.lineEdit_cad_id.setValidator(self.validaInteiro)
        self.lineEdit_cad_id.setMaxLength(4)
        #-------------------------------------------------------#
        self.lineEdit_cad_senha.setMaxLength(25)
        #-------------------------------------------------------#
        self.lineEdit_cad_email.setValidator(self.validaEmail)
        self.lineEdit_cad_email.setMaxLength(50)

        #########################################################
        
        self.frame_55.setFocus()
        self.pages.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"hub_key", None))
        self.btn_adm_inicio.setText(QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.btn_int_inicio.setText(QCoreApplication.translate("MainWindow", u"Integrante", None))
        self.btn_enviar_inicio.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_email_inicio.setText(QCoreApplication.translate("MainWindow", u"Digite seu email: ", None))
        self.lineEdit_email_inicio.setText("")
        self.lineEdit_email_inicio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kennia_f@hotmail.com", None))
        self.btn_entrar_inicio.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_senha_inicio.setText(QCoreApplication.translate("MainWindow", u"Digite sua senha: ", None))
        self.btn_esqueci_senha.setText(QCoreApplication.translate("MainWindow", u"Esqueci minha senha", None))
        self.lineEdit_senha_inicio.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label.setText("")
        self.btn_voltar_emp.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Entre com o c\u00f3digo da chave.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bem vindo,", None))
        self.label_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_chave.setText(QCoreApplication.translate("MainWindow", u"Chave:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimos", None))
        self.lineEdit_busca_emprestimos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.btn_busca_emprestimos.setText("")
        ___qtablewidgetitem = self.tableEmprestimo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtablewidgetitem1 = self.tableEmprestimo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Integrante", None));
        ___qtablewidgetitem2 = self.tableEmprestimo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Retirada", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CHAVES", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Espa\u00e7o\n"
"Converg\u00eancia", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"100\n"
"Asseio e \n"
"Conserva\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"101\n"
"Anatomia e \n"
"Sa\u00fade", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"102\n"
"Anatomia e \n"
"Sa\u00fade", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"103\n"
"Design de\n"
"Interiores", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"104\n"
"Laborat\u00f3rio\n"
"de Beleza I", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"105\n"
"Laborat\u00f3rio\n"
"de Beleza II", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"106\n"
"Laborat\u00f3rio\n"
"Mult. I\n"
"(Farm\u00e1cia)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"107\n"
"Laborat\u00f3rio \n"
"de Est\u00e9tica I\n"
"(Podologia)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"108\n"
"Laborat\u00f3rio\n"
"de Est\u00e9tica II", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"109\n"
"Laborat\u00f3rio\n"
"Mult. II\n"
"(Analises \n"
"Clinicas)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"110\n"
"Tecnologia da\n"
"Informa\u00e7\u00e3o", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"201\n"
"Mini\n"
"Mercado", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"202\n"
"Loja \n"
"Concei\u00e7\u00e3o", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"203\n"
"Espa\u00e7o \n"
"Empresarial", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"204\n"
"Sala", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"205\n"
"Sala", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"206\n"
"Sala", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"207\n"
"Sala\n"
"Multiuso", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"208\n"
"Tecnologia da\n"
"Informa\u00e7\u00e3o", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"209\n"
"Tecnologia da\n"
"Informa\u00e7\u00e3o", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"210\n"
"Estudio \n"
"Maker", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"211\n"
"Sala\n"
"Multiuso", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"212\n"
"Sala\n"
"Multiuso", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"213\n"
"Sala\n"
"Multiuso", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"301\n"
"Tecnologia da \n"
"Informa\u00e7\u00e3o", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"302\n"
"Tecnologia da \n"
"Informa\u00e7\u00e3o", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"303\n"
"Tecnologia da \n"
"Informa\u00e7\u00e3o", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"304\n"
"Multiuso", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"305\n"
"Multiuso", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"306\n"
"Sala de\n"
"Jogos", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"307\n"
"Manuten\u00e7\u00e3o\n"
"e Redes de\n"
"Comp.", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"308\n"
"Biblioteca", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"309\n"
"Biblioteca", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"310\n"
"Computa\u00e7\u00e3o\n"
"Grafica", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"311\n"
"Microsoft", None))
        self.label_50.setText("")
        self.label_iconRelatorio.setText("")
        self.label_iconUser.setText("")
        self.label_iconChave.setText("")
        self.btn_menu_chave.setText(QCoreApplication.translate("MainWindow", u"Chaves", None))
        self.btn_menu_usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn_menu_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.label_iconLogout.setText("")
        self.btn_menu_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Chaves", None))
        self.lineEdit_busca_chaves.setText("")
        self.lineEdit_busca_chaves.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.btn_busca_chaves.setText("")
        ___qtablewidgetitem3 = self.table_lista_chaves.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"checkbox", None));
        ___qtablewidgetitem4 = self.table_lista_chaves.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem5 = self.table_lista_chaves.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ambiente", None));
        self.btn_nova_chave.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_imp_chave.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.btn_exc_chave.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Chave", None))
        self.label_chave_cad.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_amb_cad.setText(QCoreApplication.translate("MainWindow", u"Ambiente:", None))
        self.btn_voltar_chave.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_chave.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.title_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.lineEdit_busca_usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.btn_busca_usuarios.setText("")
        ___qtablewidgetitem25 = self.table_lista_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"check_box", None));
        ___qtablewidgetitem26 = self.table_lista_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem27 = self.table_lista_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem28 = self.table_lista_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel Acesso", None));
        ___qtablewidgetitem33 = self.table_lista_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"", None));

        self.btn_exc_usuarios.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_imp_usuarios.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.btn_cad_usuarios.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_cad_nome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_cad_id.setText(QCoreApplication.translate("MainWindow", u"Identificador:", None))
        self.cbb_cad_acesso.setItemText(0, QCoreApplication.translate("MainWindow", u"  Administrador", None))
        self.cbb_cad_acesso.setItemText(1, QCoreApplication.translate("MainWindow", u"  Integrante", None))
        self.label_cad_acesso.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel de acesso:", None))
        self.label_cad_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_cad_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.btn_cad_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_cad_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

