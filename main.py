import sys
import ctypes
import sqlite3
import smtplib, ssl
from datetime import datetime
from ui_main import *
from ui_dialog import Ui_Dialog, Ui_Dialog_2
from def_print_img import *
import code128
import os

class Overlay(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self, parent)
		palette = QPalette(self.palette())
		palette.setColor(palette.Window, Qt.transparent)
		self.setPalette(palette)
				
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.fillRect(event.rect(), QBrush(QColor(0, 0, 0, 127)))
		painter.end()


class Dialog(QDialog):
	def __init__(self, parent) -> None:
		super().__init__(parent)
		self.setAttribute(Qt.WA_DeleteOnClose)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.timer_msg = QTimer(self)
		self.timer_msg.setInterval(15000)
		self.timer_msg.timeout.connect(self.closeMsg)
		self.timer_msg.start()
	
	def closeMsg(self):
		self.close()

	def closeEvent(self, event):
		self.timer_msg.stop()
		event.accept()
		

class Dialog2(QDialog):
	def __init__(self, parent) -> None:
		super().__init__(parent)
		self.setAttribute(Qt.WA_DeleteOnClose)
		self.ui = Ui_Dialog_2()
		self.ui.setupUi(self)
		self.timer_msg = QTimer(self)
		self.timer_msg.setInterval(15000)
		self.timer_msg.timeout.connect(self.closeMsg)
		self.timer_msg.start()
	
	def closeMsg(self):
		self.timer_msg.stop()
		self.reject()

class WorkerThread(QThread):
	
	def __init__(self, email, senha):
		super().__init__()
		self.de = 'INSIRA SEU EMAIL AQUI!'
		self.para = email
		self.senha = senha

	def run(self):		
		context = ssl.create_default_context()
		try:
			server = smtplib.SMTP('INSIRA SEU SMTP DO PROVEDOR DO SEU EMAIL', 587)

			server.ehlo()
			server.starttls(context=context)
			server.ehlo()
			server.login(self.de, 'INSIRA A SENHA DO SEU EMAIL')
		except Exception as e:
			print(e)

		msg = f'Subject: hub_key - recuperacao de senha\n\nlogin: {self.para}\nsenha: {self.senha}'
		server.sendmail(self.de, self.para, msg)


class MainWindow(QMainWindow):

	timer_logout = QTimer()
	timer_descanso = QTimer()
	telaAtual = None
	
	estouOrdenado = 0
	all_pages = []
	lista_impressao_historico = []
	turnoManha = '+7 hours'
	turnoTarde = '+12 hours'
	turnoNoite = '+18 hours'
	
	tempo = 0
	limit = 30
	count = 0
	total = 0
	sessao_usuario = None

	def __init__(self):
		super().__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.popup = Overlay(self)
		self.popup.setMinimumWidth(1920)
		self.popup.setMinimumHeight(1080)
		self.popup.hide()
		
		self.showMaximized()
		self.fazBackUp()

		self.timer_descanso.start(40000)

		# FILTRO DE EVENTOS
		self.ui.centralwidget.installEventFilter(self)
		self.ui.btn_adm_inicio.installEventFilter(self)
		self.ui.lineEdit_email_inicio.installEventFilter(self)
		self.ui.lineEdit_senha_inicio.installEventFilter(self)
		self.ui.btn_enviar_inicio.installEventFilter(self)
		self.ui.btn_esqueci_senha.installEventFilter(self)
		self.ui.btn_entrar_inicio.installEventFilter(self)
		self.ui.btn_int_inicio.installEventFilter(self)
		self.ui.lineEdit_codigo.installEventFilter(self)
		self.ui.lineEdit_chave.installEventFilter(self)
		self.ui.btn_voltar_emp.installEventFilter(self)
		self.ui.lineEdit_busca_emprestimos.installEventFilter(self)
		self.ui.btn_busca_emprestimos.installEventFilter(self)
		self.ui.btn_menu_chave.installEventFilter(self)
		self.ui.btn_busca_chaves.installEventFilter(self)
		self.ui.lineEdit_busca_chaves.installEventFilter(self)
		self.ui.btn_nova_chave.installEventFilter(self)
		self.ui.btn_imp_chave.installEventFilter(self)
		self.ui.btn_exc_chave.installEventFilter(self)
		self.ui.lineEdit_chave_cad.installEventFilter(self)
		self.ui.lineEdit_amb_cad.installEventFilter(self)
		self.ui.btn_voltar_chave.installEventFilter(self)
		self.ui.btn_salvar_chave.installEventFilter(self)
		self.ui.btn_menu_usuario.installEventFilter(self)
		self.ui.lineEdit_busca_usuarios.installEventFilter(self)
		self.ui.btn_busca_usuarios.installEventFilter(self)
		self.ui.btn_cad_usuarios.installEventFilter(self)
		self.ui.btn_imp_usuarios.installEventFilter(self)
		self.ui.btn_exc_usuarios.installEventFilter(self)
		self.ui.lineEdit_cad_nome.installEventFilter(self)
		self.ui.lineEdit_cad_id.installEventFilter(self)
		self.ui.cbb_cad_acesso.installEventFilter(self)
		self.ui.lineEdit_cad_senha.installEventFilter(self)
		self.ui.lineEdit_cad_email.installEventFilter(self)
		self.ui.btn_cad_cancelar.installEventFilter(self)
		self.ui.btn_cad_salvar.installEventFilter(self)
		self.ui.btn_menu_historico.installEventFilter(self)
		self.ui.btn_menu_sair.installEventFilter(self)


		#SINAIS DE CONTROLE
		#---------------------------------------------------------------#
		self.ui.lineEdit_codigo.editingFinished.connect(self.loginUsuario)
		#---------------------------------------------------------------#
		self.ui.lineEdit_chave.editingFinished.connect(self.fazEmprestimo)
		#---------------------------------------------------------------#
		self.timer_logout.timeout.connect(self.deslogar)
		#---------------------------------------------------------------#
		self.timer_descanso.timeout.connect(self.descansoTela)
		#---------------------------------------------------------------#
		self.ui.cbb_cad_acesso.currentIndexChanged.connect(self.escondeCadExtras)
		#---------------------------------------------------------------#
		self.ui.btn_visibilidade_cad.clicked.connect(self.visibilidadeSenha)
		#---------------------------------------------------------------#
		self.ui.btn_visibilidade_inicio.clicked.connect(self.visibilidadeSenha)
		#---------------------------------------------------------------#
		self.ui.pages_adm.currentChanged.connect(self.resetaCount)
		#---------------------------------------------------------------#
		self.ui.dateEdit_InicialDate.editingFinished.connect(lambda: self.ui.dateEdit_EndDate.setFocus())
		#---------------------------------------------------------------#
		self.ui.dateEdit_EndDate.editingFinished.connect(self.load_search_date_historic)
		#---------------------------------------------------------------#
		self.ui.spinBox_num_copies.valueChanged.connect(self.spinBoxValueChanged, Qt.QueuedConnection)
		
		
		#BOTÃO ADMINISTRADOR
		self.ui.btn_adm_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.email))
		self.ui.btn_adm_inicio.clicked.connect(lambda: self.ui.lineEdit_email_inicio.setFocus())
		self.ui.btn_adm_inicio.clicked.connect(lambda: self.ui.frame_voltar_login.show())

		#BOTÃO ENVIAR INICIO
		self.ui.btn_enviar_inicio.clicked.connect(self.validaEmail)
		self.ui.lineEdit_email_inicio.inputRejected.connect(lambda: print('sinal enviado!'))
		self.ui.lineEdit_email_inicio.returnPressed.connect(self.validaEmail)
		
		#BOTÃO ENTRAR INICIO
		self.ui.btn_entrar_inicio.clicked.connect(self.validaSenha)
		self.ui.lineEdit_senha_inicio.returnPressed.connect(self.validaSenha)
		self.ui.btn_entrar_inicio.clicked.connect(self.set_default_position) # Arrumando a posica da barra lateral
		self.ui.lineEdit_senha_inicio.returnPressed.connect(self.set_default_position)

		#BOTÃO ESQUECI SENHA
		self.ui.btn_esqueci_senha.clicked.connect(self.esqueciSenha)
		
		#BOTAO VOLTAR INICIO
		self.ui.btn_voltar_login.clicked.connect(self.voltaInicio)

		#BOTÃO INTEGRANTE
		self.ui.btn_int_inicio.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.emprestimos))
		self.ui.btn_int_inicio.clicked.connect(self.carregaEmprestimo)
		self.ui.btn_int_inicio.clicked.connect(lambda: self.ui.lineEdit_codigo.setFocus())

		#BOTÃO VOLTAR
		self.ui.btn_voltar_emp.clicked.connect(self.limpaCampos)
		self.ui.btn_voltar_emp.clicked.connect(self.voltarInicio)
		
		#BOTÃO BUSCA EMPRESTIMO
		self.ui.btn_busca_emprestimos.clicked.connect(self.carregaEmprestimo)
		self.ui.lineEdit_busca_emprestimos.returnPressed.connect(self.carregaEmprestimo)

		#BOTÃO MENU CHAVES
		self.ui.btn_menu_chave.clicked.connect(self.limpaCampos)
		self.ui.btn_menu_chave.clicked.connect(lambda: self.animation(self.ui.btn_menu_chave.y()))
		self.ui.btn_menu_chave.clicked.connect(self.carregaChaves)
		self.ui.btn_menu_chave.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves))
		self.ui.btn_menu_chave.clicked.connect(self.clear_table)

		#BOTÃO BUSCA CHAVES
		self.ui.btn_busca_chaves.clicked.connect(self.carregaChaves)
		self.ui.lineEdit_busca_chaves.returnPressed.connect(self.carregaChaves)

		#BOTÃO CADASTRAR CHAVE
		self.ui.btn_nova_chave.clicked.connect(lambda: self.ui.lineEdit_chave_cad.setFocus())
		self.ui.btn_nova_chave.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.cad_chaves))
		self.ui.btn_nova_chave.clicked.connect(self.default_title)

		#BOTÃO IMPRIMIR CHAVE
		self.ui.btn_imp_chave.clicked.connect(lambda: self.show_tela_impressao(self.ui.table_lista_chaves.selectedItems(), 2)) #Ratu
		
		#BOTÃO EXCLUIR CHAVE
		self.ui.btn_exc_chave.clicked.connect(self.deletaChave)
		
		#BOTÃO CANCELAR CHAVE
		self.ui.btn_voltar_chave.clicked.connect(self.limpaCampos)
		self.ui.btn_voltar_chave.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves))
		self.ui.btn_voltar_chave.clicked.connect(self.carregaChaves)

		#BOTÃO SALVAR CHAVE
		self.ui.btn_salvar_chave.clicked.connect(self.salvaChave)
		
		#CUSTOM SORTING
		self.ui.table_lista_chaves.horizontalHeader().sectionClicked.connect(self.funcaoSorting)

		#BOTÃO MENU USUARIOS
		self.ui.btn_menu_usuario.clicked.connect(self.limpaCampos)
		self.ui.btn_menu_usuario.clicked.connect(lambda: self.animation(self.ui.btn_menu_usuario.y()))
		self.ui.btn_menu_usuario.clicked.connect(self.carregaUsuarios)
		self.ui.btn_menu_usuario.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios))
		self.ui.btn_menu_usuario.clicked.connect(self.clear_table)

		#BOTÃO BUSCA USUARIOS
		self.ui.lineEdit_busca_usuarios.returnPressed.connect(self.carregaUsuarios)
		self.ui.btn_busca_usuarios.clicked.connect(self.carregaUsuarios)

		#BOTÃO CADASTRAR USUARIO
		self.ui.btn_cad_usuarios.clicked.connect(lambda: self.ui.lineEdit_cad_nome.setFocus())
		self.ui.btn_cad_usuarios.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.cad_usuarios))
		self.ui.btn_cad_usuarios.clicked.connect(self.default_title)

		#BOTÃO IMPRIMIR
		self.ui.btn_imp_usuarios.clicked.connect(lambda: self.show_tela_impressao(self.ui.table_lista_usuarios.selectedItems(), 3))

		#BOTÃO EXCLUIR USUARIO
		self.ui.btn_exc_usuarios.clicked.connect(self.deletaUsuario)
		
		#BOTÃO CANCELAR USUARIO
		self.ui.btn_cad_cancelar.clicked.connect(self.limpaCampos)
		self.ui.btn_cad_cancelar.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios))
		self.ui.btn_cad_cancelar.clicked.connect(self.carregaUsuarios)

		#BOTÃO SALVAR USUARIO
		self.ui.btn_cad_salvar.clicked.connect(self.salvaUsuario)
		
		#CUSTOM SORTING
		self.ui.table_lista_usuarios.horizontalHeader().sectionClicked.connect(self.funcaoSorting)
		
		#BOTÃO MENU HISTORICO
		self.ui.btn_menu_historico.clicked.connect(self.limpaCampos)
		self.ui.btn_menu_historico.clicked.connect(lambda: self.animation(self.ui.btn_menu_historico.y()))
		self.ui.btn_menu_historico.clicked.connect(self.loadData)
		self.ui.btn_menu_historico.clicked.connect(self.clear_table)

		#BOTÃO BUSCA HISTORICO
		self.ui.lineEdit_searchBar.returnPressed.connect(self.clear_for_search)
		self.ui.btn_searchBar.clicked.connect(self.clear_for_search)

		#BOTAO IMPRIMIR HISTORICO
		self.ui.radio_selection_PrintPV.toggled.connect(lambda: self.radio_btn_selection(self.ui.radio_selection_PrintPV.isChecked()))
		self.ui.btn_back_PrintPV.clicked.connect(self.hide_tela_impressao)
		self.ui.pushButton_print.clicked.connect(lambda: self.show_tela_impressao(self.lista_impressao_historico, 4))
		self.ui.btn_back_PrintPV.clicked.connect(self.clear_scrollArea)
		self.ui.btn_back_PrintPV.clicked.connect(self.delete_imgs)
		self.ui.btn_print_PrintPV.clicked.connect(lambda: print_img(self.all_pages, self.ui.combo_box_device_PrintPV.currentText(), self.ui.lineEdit_pages_PrintPV.text(), self.ui.spinBox_num_copies.value()))
		self.ui.btn_print_PrintPV.clicked.connect(self.dialog_impresso)
		
		#BOTAO VER HISTORICO
		self.ui.pushButton_show.clicked.connect(self.load_search_date_historic)

		#BOTÃO SAIR
		self.ui.btn_menu_sair.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves))
		self.ui.btn_menu_sair.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.bem_vindo))
		self.ui.btn_menu_sair.clicked.connect(self.clear_table)

		#BOTAO MENU AJUDA
		self.ui.btn_menu_ajuda.clicked.connect(lambda: os.startfile('manual hub key.pdf'))
		self.ui.btn_menu_ajuda.clicked.connect(lambda: self.ui.pages_adm.currentWidget().setFocus())

		#DISPOSIÇÃO DAS TABELAS
		self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
		#---------------------------------------------------------------#
		self.ui.table_lista_chaves.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.table_lista_chaves.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
		#---------------------------------------------------------------#
		self.ui.table_lista_usuarios.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.table_lista_usuarios.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
		#---------------------------------------------------------------#
		self.ui.table_relatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.table_relatorio.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
		self.ui.table_relatorio.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
		self.ui.table_relatorio.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
		self.ui.table_relatorio.horizontalHeader().resizeSection(2, 185)
		self.ui.table_relatorio.horizontalHeader().resizeSection(3, 185)


	def eventFilter(self, source, event):
		chaves_selecionadas = self.ui.table_lista_chaves.selectionModel().selectedRows()
		usuarios_selecionados = self.ui.table_lista_usuarios.selectionModel().selectedRows()

		if (event.type() == QEvent.MouseButtonPress) or (event.type() == QEvent.KeyPress):
			if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Delete:
				print('entrei key delete')
				if chaves_selecionadas:
					print('entrei index 0')				
					self.deletaChave()
				elif usuarios_selecionados:
					print('entrei index 2')				
					self.deletaUsuario()

			print("pressed")
			print(self.timer_descanso.remainingTime())
			self.timer_descanso.stop()
			if self.ui.pages.currentWidget() == self.ui.descanso:
				self.ui.pages.setCurrentWidget(self.telaAtual)
			self.timer_descanso.start(40000)
			print(self.timer_descanso.remainingTime())
		return super().eventFilter(source, event)

	def animation(self, where):
		self.animator = QPropertyAnimation(self.ui.frame_selected, b'geometry')
		self.animator.setDuration(150)
		self.animator.setStartValue(QRect(0, self.ui.frame_selected.y(), 79, 70))
		self.animator.setEndValue(QRect(0, where, 79, 70))
		self.animator.start()
	
	def set_default_position(self): #Volta o frame de selecao para a posicao inicial ao entrar no sistema
		self.ui.frame_selected.setGeometry(0, 0, 79, 70)

	def clear_table(self): # Tira o foco das linhas das tabelas quando trocado de tela
		self.ui.table_lista_chaves.clearSelection()
		self.ui.table_lista_usuarios.clearSelection()
		self.ui.table_relatorio.clearSelection()

	def default_title(self):
		self.ui.label_6.setText('Cadastrar Chave')
		self.ui.label_3.setText('Cadastrar Usuário')

	def limpaCampos(self):
		for i in self.ui.pages.currentWidget().findChildren(QLineEdit):
			i.clear()

		for i in self.ui.pages.currentWidget().findChildren(QComboBox):
			i.setCurrentIndex(0)

		if self.ui.stackedWidget.currentIndex() == 2:
			self.ui.lineEdit_senha_inicio.setEchoMode(QLineEdit.Password)
			self.ui.btn_visibilidade_inicio.setIcon(QIcon("icons/visibility_blue_18dp.svg"))

		if self.ui.pages_adm.currentIndex() == 3:
			self.ui.lineEdit_cad_senha.setEchoMode(QLineEdit.Password)
			self.ui.btn_visibilidade_cad.setIcon(QIcon("icons/visibility_blue_18dp.svg"))

	def voltaInicio(self):
		self.limpaCampos()
		self.ui.stackedWidget.setCurrentWidget(self.ui.inicio)
		self.ui.frame_voltar_login.hide()

	def validaEmail(self):
		email = self.ui.validaEmail.validate(self.ui.lineEdit_email_inicio.text(), 0)
		if email[1] == '':
			msg = Dialog2(self)
			msg.ui.label.setText('Campo Obrigatório!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			self.ui.lineEdit_email_inicio.setFocus()
			return

		if email[0] != QValidator.Acceptable:
			self.ui.lineEdit_email_inicio.setText('')
			msg = Dialog2(self)
			msg.ui.label.setText('Campo preenchido')
			msg.ui.label_2.setText('incorretamente!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			self.ui.lineEdit_email_inicio.setFocus()
			return

		self.ui.lineEdit_email_inicio.setText('')
		try:
			cursor.execute('SELECT email FROM usuario')
			usuarios = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		for usuario in usuarios:
			if usuario[0] == email[1]:
				self.ui.lineEdit_email_inicio.setText('')
				self.sessao_usuario = email[1]
				self.ui.stackedWidget.setCurrentWidget(self.ui.senha)
				self.ui.lineEdit_senha_inicio.setFocus()
				return
		msg = Dialog2(self)
		msg.ui.label.setText('O email informado')
		msg.ui.label_2.setText('não existe!')
		self.popup.show()
		msg.exec()
		self.popup.hide()
		self.ui.lineEdit_email_inicio.setFocus()

	def validaSenha(self):
		senha = self.ui.lineEdit_senha_inicio.text()
		if senha == '':
			msg = Dialog2(self)
			msg.ui.label.setText('Campo Obrigatório!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			self.ui.lineEdit_senha_inicio.setFocus()
			return

		self.ui.lineEdit_senha_inicio.setText('')
		try:
			cursor.execute(f"SELECT rowid, id_usuario, nome, senha FROM usuario WHERE email = '{self.sessao_usuario}'")	
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		login_usuario = cursor.fetchone()
		if not login_usuario:
			return

		if login_usuario[3] == senha:
			self.sessao_usuario = login_usuario[:-2]
			print(self.sessao_usuario)
			self.carregaChaves()
			self.ui.frame_voltar_login.hide()
			self.ui.pages.setCurrentWidget(self.ui.menu_adm)
			self.ui.stackedWidget.setCurrentWidget(self.ui.inicio)
			self.ui.frame_voltar_login.hide()
			self.limpaCampos()
			return
		msg = Dialog2(self)
		msg.ui.label.setText('O email ou senha')
		msg.ui.label_2.setText('estão incorretos!')
		self.popup.show()
		msg.exec()
		self.popup.hide()
		self.ui.lineEdit_senha_inicio.setFocus()

	def esqueciSenha(self):
		self.ui.lineEdit_senha_inicio.setText('')

		try:
			cursor.execute(f"SELECT senha FROM usuario WHERE email = '{self.sessao_usuario}'")	
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		senha = cursor.fetchone()
		if senha:
			senha = senha[0]

		self.worker = WorkerThread(self.sessao_usuario, senha)
		self.worker.start()
		self.worker.finished.connect(lambda: print('e-mail enviado.'))

		msg = Dialog2(self)
		msg.ui.label.setText('Senha enviada para')
		msg.ui.label_2.setText(f'{self.sessao_usuario}')
	
		self.popup.show()
		msg.exec()
		self.popup.hide()
	
		self.ui.lineEdit_senha_inicio.setFocus()
 
	def voltarInicio(self):
		if self.sessao_usuario:
			self.deslogar()
		self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves)    
		self.ui.pages.setCurrentWidget(self.ui.bem_vindo)
		
	def loginUsuario(self):
		self.ui.lineEdit_codigo.blockSignals(True)
		codigo = self.ui.lineEdit_codigo.text()

		self.ui.lineEdit_codigo.setText('')
		try:
			cursor.execute('SELECT rowid, id_usuario, nome FROM usuario')
			usuarios = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		for usuario in usuarios:
			if usuario[1] == codigo:
				self.ui.lineEdit_email_inicio.setText('')
				self.sessao_usuario = usuario

				self.ui.label.setText(f'Olá {self.sessao_usuario[2].split(" ")[0]},')
				self.ui.label_2.setText(f'Entre com o código da chave.')
				self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_chave)

				self.timer_logout.start(25000)
				print(f'timer_logout = {self.timer_logout.interval()}')
				self.ui.lineEdit_codigo.blockSignals(False)
				return
		msg = Dialog2(self)
		msg.ui.label.setText('Código não encontrado!')
		self.popup.show()
		msg.exec()
		self.popup.hide()
		self.ui.lineEdit_codigo.blockSignals(False)

	def deslogar(self):
		self.timer_logout.stop()
		print(f'\ndeslogar\nintervalo = {self.timer_logout.interval()}\nrestante = {self.timer_logout.remainingTime()}')
		self.sessao_usuario = None

		self.ui.label.setText('Bem vindo,')
		self.ui.label_2.setText('Entre com seu código.')
		self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_codigo)

		msg = Dialog2(self)
		msg.ui.label.setText('Usuário Deslogado!')
		self.popup.show()
		msg.exec()
		self.popup.hide()

	def fazEmprestimo(self):
		tempo = self.timer_logout.remainingTime()
		self.timer_logout.stop()
		print(f'\nentrei\nintervalo = {self.timer_logout.interval()}\nrestante = {tempo}\n')
		
		self.ui.lineEdit_chave.blockSignals(True)
		_chave = self.ui.lineEdit_chave.text()
		self.ui.lineEdit_chave.setText('')

		if tempo < 1:
			self.ui.lineEdit_chave.blockSignals(False)
			return

		try:
			cursor.execute('SELECT * FROM chave')
			chaves = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
			
		for chave in chaves:
			if chave[1] == _chave:
				if chave[3]:
					self.devolveChave(chave[0], _chave)
					self.ui.lineEdit_chave.blockSignals(False)
					self.timer_logout.start(tempo)
					print(f'reiniciou = {self.timer_logout.remainingTime()}')
					return

				msg = Dialog(self)
				msg.ui.label.setText(f'{self.sessao_usuario[2].split(" ")[0]}, deseja retirar')
				msg.ui.label_2.setText(f'a chave {chave[1]}')
				msg2 = Dialog2(self)
				self.popup.show()
				if msg.exec():
					args = (self.sessao_usuario[0], chave[0], str(datetime.now())[:-7])
					try:
						cursor.execute('INSERT INTO emprestimo(usuario_ret, id_sala, data_hora_retirada) VALUES ((select nome from usuario where rowid = ?), (select id_sala from chave where rowid = ?), ?)', args)
						cursor.execute(f'UPDATE usuario SET pendencia = 1 WHERE rowid = {self.sessao_usuario[0]}')
						cursor.execute(f'UPDATE chave SET estado = {self.sessao_usuario[0]} WHERE rowid = {chave[0]}')
						banco.commit()
					except sqlite3.Error as erro:
						print('Erro com o banco de dados: ', erro)
						return
					msg2.ui.label.setText(f'Chave retirada com sucesso.')
					self.carregaEmprestimo()
				else:
					msg2.ui.label.setText(f'Operação cancelada!')
				msg2.exec()
				self.popup.hide()
				self.ui.lineEdit_chave.blockSignals(False)
				self.timer_logout.start(tempo)
				print(f'reiniciou = {self.timer_logout.remainingTime()}')
				return

		msg = Dialog2(self)
		msg.ui.label.setText('Chave não encontrada!')
		self.popup.show()
		msg.exec()
		self.popup.hide()
		self.ui.lineEdit_chave.blockSignals(False)
		
		self.timer_logout.start(tempo)
		print(f'reiniciou = {self.timer_logout.remainingTime()}')

	def encontraPosItem(self, chave):
		for row in range(self.ui.tableEmprestimo.rowCount()):
			item = self.ui.tableEmprestimo.item(row, 1)
			if chave == item.text().lower():
				print(f"row = {row}")
				return row

	def devolveChave(self, pos, chave):	
		row = self.encontraPosItem(chave)
		if row == None:
			try:
				cursor.execute(f'SELECT rowid FROM emprestimo WHERE id_sala = {chave} ORDER BY rowid DESC')
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

			rowid = cursor.fetchone()
			if rowid:
				rowid = rowid[0]

		else:
			rowid = self.ui.tableEmprestimo.item(row, 0).text()

		msg = Dialog(self)
		msg.ui.label.setText(f'{self.sessao_usuario[2].split(" ")[0]}, deseja devolver')
		msg.ui.label_2.setText(f'a chave {chave}')

		msg2 = Dialog2(self)
		self.popup.show()
		if msg.exec():

			args = (self.sessao_usuario[0], str(datetime.now())[:-7], rowid)
			try:
				cursor.execute(f'SELECT COUNT() FROM chave WHERE estado = (SELECT estado FROM chave WHERE rowid = {pos})')
				pendencias = cursor.fetchone()[0]
				if pendencias == 1:
					cursor.execute(f'UPDATE usuario SET pendencia = 0 WHERE rowid = (SELECT estado FROM chave WHERE rowid = {pos})')
				cursor.execute('UPDATE emprestimo SET usuario_dev = (SELECT nome FROM usuario WHERE rowid = ?), data_hora_devolucao = ? WHERE rowid = ?', args)
				cursor.execute(f'UPDATE chave SET estado = 0 WHERE rowid = {pos}')
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return
			msg2.ui.label.setText(f'Chave devolvida com sucesso.')
			if row != None:
				self.ui.tableEmprestimo.removeRow(row)
		else:
			msg2.ui.label.setText(f'Operação cancelada!')
		msg2.exec()
		self.popup.hide()

	def carregaEmprestimo(self):
		txt = self.ui.lineEdit_busca_emprestimos.text().lower()
		hora_atual = int(str(datetime.now().time())[:2])
		print('hora_atual = ', hora_atual)

		if hora_atual >= 7 and hora_atual < 13:
			turno = self.turnoManha
			contra_turno = self.turnoTarde
		elif hora_atual >= 13 and hora_atual < 18:
			turno = self.turnoTarde
			contra_turno = self.turnoNoite
		else:
			turno = self.turnoNoite
			contra_turno = '+23 hours'
		print(f"{turno}~{contra_turno}")

		if txt == '':		
			query = f'''SELECT emprestimo.rowid, emprestimo.id_sala, usuario_ret, data_hora_retirada FROM emprestimo WHERE
						(data_hora_retirada BETWEEN datetime('now','localtime', 'start of day', '{turno}') AND datetime('now', 'localtime', 'start of day', '{contra_turno}')) AND 
						data_hora_devolucao IS NULL	ORDER BY data_hora_retirada ASC'''
		else:
			query = f'''SELECT emprestimo.rowid, emprestimo.id_sala, usuario_ret, data_hora_retirada FROM emprestimo WHERE 
						(data_hora_retirada BETWEEN datetime('now','localtime', 'start of day', '{turno}') AND datetime('now', 'localtime', 'start of day', '{contra_turno}')) AND
						data_hora_devolucao IS NULL AND (usuario_ret LIKE "%{txt}%" OR emprestimo.id_sala LIKE "%{txt}%") ORDER BY data_hora_retirada ASC'''

		try:
			cursor.execute(query)
			emprestimos = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		self.ui.tableEmprestimo.setRowCount(len(emprestimos))

		for row, emprestimo in enumerate(emprestimos):
			for col, dado in enumerate(emprestimo):
				if col == 3:
					self.ui.tableEmprestimo.setItem(row, col, QTableWidgetItem(dado[11:-3]))	
				else:
					self.ui.tableEmprestimo.setItem(row, col, QTableWidgetItem(str(dado)))
				self.ui.tableEmprestimo.item(row, col).setTextAlignment(Qt.AlignCenter)
		self.ui.tableEmprestimo.setColumnHidden(0, True)
	
	def carregaChaves(self):
		self.estouOrdenado = 0
		
		txt = self.ui.lineEdit_busca_chaves.text().lower()
		if txt == '':		
			query = f'''SELECT rowid, id_sala, nome, estado FROM chave ORDER BY id_sala ASC'''
		else:
			query = f'''SELECT rowid, id_sala, nome, estado FROM chave WHERE id_sala LIKE "%{txt}%" OR nome LIKE "%{txt}%" ORDER BY id_sala ASC'''

		try:
			cursor.execute(query)
			chaves = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.table_lista_chaves.setRowCount(len(chaves))
		for lin, chave in enumerate(chaves):
			for col, dado in enumerate(chave):
				if col == 3:
					self.ui.table_lista_chaves.setItem(lin, col, QTableWidgetItem('Disponível' if dado == 0 else 'Em uso'))
				else:
					self.ui.table_lista_chaves.setItem(lin, col, QTableWidgetItem(str(dado)))
				self.ui.table_lista_chaves.item(lin, col).setTextAlignment(Qt.AlignCenter)
			self.lista_chaves_btn_editar = QPushButton(self.ui.table_lista_chaves)
			self.lista_chaves_btn_editar.setObjectName(u"btn_edit_chave")
			self.lista_chaves_btn_editar.setFocusPolicy(Qt.ClickFocus)
			self.lista_chaves_btn_editar.setCursor(Qt.PointingHandCursor)
			self.lista_chaves_btn_editar.setIcon(QIcon("icons\edit_black_48dp.svg"))
			self.lista_chaves_btn_editar.setIconSize(QSize(16, 16))
			self.lista_chaves_btn_editar.clicked.connect(lambda: self.editarChave(self.ui.table_lista_chaves.currentRow()))
			self.lista_chaves_btn_editar.setStyleSheet("QPushButton {color: #111111; background-color: transparent;} QPushButton:hover {background-color: #DEEAFF; border: none;}") #Rati
			self.ui.table_lista_chaves.setCellWidget(lin, 4, self.lista_chaves_btn_editar)
		self.ui.table_lista_chaves.setColumnHidden(0, True)
		self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves)

	def deletaChave(self):
		rows = sorted(self.ui.table_lista_chaves.selectionModel().selectedRows(), key=lambda row: row.row(), reverse=True)

		for row in rows:
			if self.ui.table_lista_chaves.item(row.row(), 3).text() == 'Em uso':
				msg = Dialog2(self)
				msg.ui.label.setText('Chave emprestada')
				msg.ui.label_2.setText('não pode ser removida!')
				self.popup.show()
				msg.exec()
				self.popup.hide()
				return

			try:
				rowid = int(self.ui.table_lista_chaves.item(row.row(), 0).text())
				cursor.execute(f'DELETE FROM chave WHERE rowid = {rowid}')
				banco.commit()
				self.ui.table_lista_chaves.removeRow(row.row())
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

		if rows:
			msg = Dialog2(self)
			msg.ui.label.setText('Chave(s) removida(s)')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
		else:
			msg = Dialog2(self)
			msg.ui.label.setText('Selecione uma chave')
			msg.ui.label_2.setText('a ser removida!')
			self.popup.show()
			msg.exec()
			self.popup.hide()

	def salvaChave(self):
		chave = self.ui.validaInteiro.validate(self.ui.lineEdit_chave_cad.text(), 0)
		ambiente = self.ui.validaTexto.validate(self.ui.lineEdit_amb_cad.text(), 0)
		
		campoBranco = False
		campoInvalido = False

		if chave[1] == '':
			campoBranco = True
		if chave[0] != QValidator.Acceptable:
			self.ui.lineEdit_cad_nome.setText('')
			campoInvalido = True
		if ambiente[1] == '':
			campoBranco = True
		if ambiente[0] != QValidator.Acceptable:
			self.ui.lineEdit_cad_id.setText('')
			campoInvalido = True
		
		if campoBranco:
			msg = Dialog2(self)
			msg.ui.label.setText('Preencha todos os')
			msg.ui.label_2.setText('campos!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			return

		if campoInvalido:
			msg = Dialog2(self)
			msg.ui.label.setText('Campos preenchidos')
			msg.ui.label_2.setText('incorretamente!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			return
		
		args = (chave[1].strip(), ambiente[1].strip())
		if 'Cadastrar' in self.ui.label_6.text():
			try:
				cursor.execute(f'INSERT INTO chave(id_sala, nome) VALUES(?, ?)', args)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				if 'UNIQUE' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! essa chave')
					msg.ui.label_2.setText('ja foi cadastrada.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_chave_cad.setText('')
				return
		
			self.limpaCampos()

			msg = Dialog2(self)
			msg.ui.label.setText('Chave cadastrada')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
		else:
			args = (chave[1].strip(), ambiente[1].strip(), self.ui.table_lista_chaves.item(self.ui.table_lista_chaves.selectedItems()[0].row(), 0).text())
			try:
				cursor.execute(f'UPDATE chave set id_sala = ?, nome = ? where rowid = ?', args)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				if 'UNIQUE' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! essa chave')
					msg.ui.label_2.setText('ja foi cadastrada.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_chave_cad.setText('')
				return
			
			self.limpaCampos()

			msg = Dialog2(self)
			msg.ui.label.setText('Chave editada')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			self.carregaChaves()


	def carregaUsuarios(self):
		self.estouOrdenado = 0
		
		txt = self.ui.lineEdit_busca_usuarios.text().lower()
		if txt == '':		
			query = f'''SELECT rowid, id_usuario, nome, admin, pendencia FROM usuario ORDER BY nome ASC'''
		else:
			query = f'''SELECT rowid, id_usuario, nome, admin, pendencia FROM usuario WHERE id_usuario LIKE "%{txt}%" OR nome LIKE "%{txt}%" ORDER BY nome ASC'''

		try:
			cursor.execute(query)
			usuarios = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.table_lista_usuarios.setRowCount(len(usuarios))
		for lin, usuario in enumerate(usuarios):
			for col, dado in enumerate(usuario):
				if col == 3:
					if dado:
						self.ui.table_lista_usuarios.setItem(lin, col, QTableWidgetItem('Administrador'))
					else:
						self.ui.table_lista_usuarios.setItem(lin, col, QTableWidgetItem('Integrante'))
				else:
					self.ui.table_lista_usuarios.setItem(lin, col, QTableWidgetItem(str(dado)))
				self.ui.table_lista_usuarios.item(lin, col).setTextAlignment(Qt.AlignCenter)
			self.lista_usuarios_btn_editar = QPushButton(self.ui.table_lista_usuarios)
			self.lista_usuarios_btn_editar.setObjectName(u"btn_nova_chave")
			self.lista_usuarios_btn_editar.setFocusPolicy(Qt.ClickFocus)
			self.lista_usuarios_btn_editar.setCursor(Qt.PointingHandCursor)
			self.lista_usuarios_btn_editar.setIcon(QIcon("icons\edit_black_48dp.svg"))
			self.lista_usuarios_btn_editar.setIconSize(QSize(16, 16))
			self.lista_usuarios_btn_editar.clicked.connect(lambda: self.editarUsuario(self.ui.table_lista_usuarios.currentRow()))
			self.lista_usuarios_btn_editar.setStyleSheet("QPushButton { color: #111111; background-color: transparent;} QPushButton:hover {background-color: #DEEAFF; border: none;} QPushButton:focus {font-weight:600; outline:0} ")
			self.ui.table_lista_usuarios.setCellWidget(lin, 5, self.lista_usuarios_btn_editar)
		self.ui.table_lista_usuarios.setColumnHidden(0, True)
		self.ui.table_lista_usuarios.setColumnHidden(4, True)
		self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios)

	def funcaoSorting(self, event):
		if self.ui.pages_adm.currentIndex() == 2:
			if event < 2:
				self.ui.table_lista_usuarios.horizontalHeader().setSortIndicatorShown(False)
				return

			match self.estouOrdenado:
				case 0:
					self.ui.table_lista_usuarios.sortByColumn(event, Qt.AscendingOrder)
					self.ui.table_lista_usuarios.horizontalHeader().setSortIndicatorShown(True)
					self.estouOrdenado = 1
				case 1:
					self.ui.table_lista_usuarios.sortByColumn(event, Qt.DescendingOrder)
					self.ui.table_lista_usuarios.horizontalHeader().setSortIndicatorShown(True)
					self.estouOrdenado = 2
				case 2:
					self.carregaUsuarios()
					self.ui.table_lista_usuarios.horizontalHeader().setSortIndicatorShown(False)
					self.estouOrdenado = 0
		else:
			match self.estouOrdenado:
				case 0:
					self.ui.table_lista_chaves.sortByColumn(event, Qt.AscendingOrder)
					self.ui.table_lista_chaves.horizontalHeader().setSortIndicatorShown(True)
					self.estouOrdenado = 1
				case 1:
					self.ui.table_lista_chaves.sortByColumn(event, Qt.DescendingOrder)
					self.ui.table_lista_chaves.horizontalHeader().setSortIndicatorShown(True)
					self.estouOrdenado = 2
				case 2:
					self.carregaChaves()
					self.ui.table_lista_chaves.horizontalHeader().setSortIndicatorShown(False)
					self.estouOrdenado = 0

	def deletaUsuario(self):
		rows = sorted(self.ui.table_lista_usuarios.selectionModel().selectedRows(), key=lambda row: row.row(), reverse=True)

		for row in rows:
			print(int(self.ui.table_lista_usuarios.item(row.row(), 4).text()))
			if int(self.ui.table_lista_usuarios.item(row.row(), 4).text()):
				msg = Dialog2(self)
				msg.ui.label.setText('Usuário com chave')
				msg.ui.label_2.setText('não pode ser removido!')
				self.popup.show()
				msg.exec()
				self.popup.hide()
				return

			try:
				rowid = int(self.ui.table_lista_usuarios.item(row.row(), 0).text())	
				cursor.execute(f'DELETE FROM usuario WHERE rowid = {rowid}')
				banco.commit()
				self.ui.table_lista_usuarios.removeRow(row.row())
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

		if rows:
			msg = Dialog2(self)
			msg.ui.label.setText('Usuário(s) removido(s)')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
		else:
			msg = Dialog2(self)
			msg.ui.label.setText('Selecione um usuário')
			msg.ui.label_2.setText('a ser removido!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
	
	def visibilidadeSenha(self):
		if self.ui.pages.currentIndex() == 0:
			if self.ui.lineEdit_senha_inicio.echoMode() == QLineEdit.Password:
				self.ui.lineEdit_senha_inicio.setEchoMode(QLineEdit.Normal)
				self.ui.btn_visibilidade_inicio.setIcon(QIcon("icons/visibility_off_blue_18dp.svg"))
			else:
				self.ui.lineEdit_senha_inicio.setEchoMode(QLineEdit.Password)
				self.ui.btn_visibilidade_inicio.setIcon(QIcon("icons/visibility_blue_18dp.svg"))
		else:
			if self.ui.lineEdit_cad_senha.echoMode() == QLineEdit.Password:
				self.ui.lineEdit_cad_senha.setEchoMode(QLineEdit.Normal)
				self.ui.btn_visibilidade_cad.setIcon(QIcon("icons/visibility_off_black_18dp.svg"))
			else:
				self.ui.lineEdit_cad_senha.setEchoMode(QLineEdit.Password)
				self.ui.btn_visibilidade_cad.setIcon(QIcon("icons/visibility_black_18dp.svg"))

	def escondeCadExtras(self):
		if self.ui.cbb_cad_acesso.currentIndex():
			self.ui.label_cad_email.show()
			self.ui.lineEdit_cad_email.show()
			self.ui.label_cad_senha.show()
			self.ui.frame_cad_senha.show()
		else:
			self.ui.label_cad_email.hide()
			self.ui.lineEdit_cad_email.hide()
			self.ui.label_cad_senha.hide()
			self.ui.frame_cad_senha.hide()

	def salvaUsuario(self):
		nome = self.ui.validaNome.validate(self.ui.lineEdit_cad_nome.text(), 0)
		id_usuario = self.ui.validaInteiro.validate(self.ui.lineEdit_cad_id.text(), 0)
		senha = self.ui.lineEdit_cad_senha.text()
		email = self.ui.validaEmail.validate(self.ui.lineEdit_cad_email.text(), 0)
		
		campoBranco = False
		campoInvalido = False

		if nome[1] == '':
			campoBranco = True
		if nome[0] != QValidator.Acceptable:
			self.ui.lineEdit_cad_nome.setText('')
			campoInvalido = True
		if id_usuario[1] == '':
			campoBranco = True
		if id_usuario[0] != QValidator.Acceptable:
			self.ui.lineEdit_cad_id.setText('')
			campoInvalido = True
		if self.ui.lineEdit_cad_senha.isVisible():
			if (senha == ''):
				campoBranco = True
			if email[1] == '':
				campoBranco = True
			if email[0] != QValidator.Acceptable:
				self.ui.lineEdit_cad_email.setText('')
				campoInvalido = True

		if campoBranco:
			msg = Dialog2(self)
			msg.ui.label.setText('Preencha todos os')
			msg.ui.label_2.setText('campos!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			return

		if campoInvalido:
			msg = Dialog2(self)
			msg.ui.label.setText('Campos preenchidos')
			msg.ui.label_2.setText('incorretamente!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			return
		args = (id_usuario[1].strip(), nome[1].strip(), self.ui.cbb_cad_acesso.currentIndex(), email[1].strip(), senha.strip())
		if 'Cadastrar' in self.ui.label_3.text():
			try:
				if self.ui.cbb_cad_acesso.currentIndex():
					cursor.execute(f'INSERT INTO usuario(id_usuario, nome, admin, email, senha) VALUES(?, ?, ?, ?, ?)', args)
				else:
					cursor.execute(f'INSERT INTO usuario(id_usuario, nome, admin) VALUES(?, ?, ?)', args[:-2])
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				if 'UNIQUE' in erro.args[0] and 'id_usuario' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! esse identificador')
					msg.ui.label_2.setText('ja foi cadastrado.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_cad_id.setText('')
				elif 'UNIQUE' in erro.args[0] and 'email' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! esse email')
					msg.ui.label_2.setText('ja foi cadastrado.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_cad_email.setText('')
				return
		
			self.limpaCampos()
			
			msg = Dialog2(self)
			msg.ui.label.setText('Usuário cadastrado')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
		else:
			args = (id_usuario[1].strip(), nome[1].strip(), self.ui.cbb_cad_acesso.currentIndex(), email[1].strip(), senha.strip(), self.ui.table_lista_usuarios.item(self.ui.table_lista_usuarios.selectedItems()[0].row(), 0).text())
			try:
				cursor.execute(f'UPDATE usuario set id_usuario = ?, nome = ?, admin = ?, email = ?, senha = ? where rowid = ?', args)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				if 'UNIQUE' in erro.args[0] and 'id_usuario' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! esse identificador')
					msg.ui.label_2.setText('ja foi cadastrado.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_cad_id.setText('')
				elif 'UNIQUE' in erro.args[0]  and 'email' in erro.args[0]:
					msg = Dialog2(self)
					msg.ui.label.setText('Oops! esse email')
					msg.ui.label_2.setText('ja foi cadastrado.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
					self.ui.lineEdit_cad_email.setText('')
				return
			
			self.limpaCampos()
			
			msg = Dialog2(self)
			msg.ui.label.setText('Usuário editado')
			msg.ui.label_2.setText('com sucesso!')
			self.popup.show()
			msg.exec()
			self.popup.hide()
			self.carregaUsuarios()

	def editarChave(self, row_source):
		self.ui.label_6.setText("Editar Chave")
		self.ui.lineEdit_chave_cad.setText(self.ui.table_lista_chaves.item(row_source, 1).text())
		self.ui.lineEdit_amb_cad.setText(self.ui.table_lista_chaves.item(row_source, 2).text())
		self.ui.pages_adm.setCurrentWidget(self.ui.cad_chaves)

	def editarUsuario(self, row_source):
		self.ui.label_3.setText("Editar Usu\u00e1rios")
		self.ui.lineEdit_cad_nome.setText(self.ui.table_lista_usuarios.item(row_source, 2).text())
		self.ui.lineEdit_cad_id.setText(self.ui.table_lista_usuarios.item(row_source, 1).text())
		self.ui.cbb_cad_acesso.setCurrentIndex(0 if self.ui.table_lista_usuarios.item(row_source, 3).text() == 'Integrante' else 1)
		self.ui.pages_adm.setCurrentWidget(self.ui.cad_usuarios)

	def show_popup_impresso(self):
		self.popup.show()
		msg = Dialog2(self)
		msg.ui.label.setText("Impresso com sucesso!")
		msg.exec()
		self.popup.hide()
	
	def dialog_impresso(self):
		msg = Dialog2(self)
		msg.ui.label.setText('Impresso com sucesso!')
		self.popup.show()
		msg.exec()
		self.popup.hide()

	def dialog_selecione_itens(self):
		msg = Dialog2(self)
		msg.ui.label.setText('Selecione os itens')
		msg.ui.label_2.setText('para imprimir!')
		self.popup.show()
		msg.exec()
		self.popup.hide()

	def show_tela_impressao(self, list_to_print, cha_user_rela):
		if list_to_print == []:
			self.dialog_selecione_itens()
			return
		
		if not os.path.isdir('temp'):
			os.mkdir('temp')
		
		if cha_user_rela < 4:
			lista_selecionados = []
			lista_selecionados2 = []
			for i in list_to_print: 
				if i.text() != 'Disponível' and i.text() != 'Em uso': lista_selecionados.append(i.text())

			for i in self.chunks(lista_selecionados, cha_user_rela):
				code128.image(i[0]).save(f'temp/codigo_barra_{i[0]}.png')

				i[0] = f'temp/codigo_barra_{i[0]}'
				lista_selecionados2.append(i)
			self.papers(lista_selecionados2)
			self.ui.frame_barraLateral.hide()
			self.ui.pages_adm.setCurrentWidget(self.ui.impressao)
		else:
			self.user_paper(list_to_print)
			self.ui.frame_barraLateral.hide()
			self.ui.pages_adm.setCurrentWidget(self.ui.impressao)

	def hide_tela_impressao(self):
		self.ui.radio_all_pages_PrintPV.setChecked(True)
		self.ui.frame_barraLateral.show()
		if self.ui.frame_selected.y() == 0: 
			self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves)
		elif self.ui.frame_selected.y() == 112:
			self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios)
		else:
			self.ui.pages_adm.setCurrentWidget(self.ui.historico)

	def chunks(self, lst, n):
		splited_list = []
		for i in range(0, len(lst), n):
			splited_list.append(lst[i:i + n])
		return splited_list

	def radio_btn_selection(self, checked): # Acoes dos radio btn
		if checked:
			self.ui.lineEdit_pages_PrintPV.setEnabled(True)
			self.ui.lineEdit_pages_PrintPV.setStyleSheet(u"border-bottom: 2px solid #064A80;\n"
				"border-top-left-radius: 5px;\n"
				"padding-top: 1px;"
				"border-top-right-radius: 5px;\n"
			"")
			self.ui.lineEdit_pages_PrintPV.setFocus()
		else:
			self.ui.lineEdit_pages_PrintPV.setEnabled(False)
			self.ui.lineEdit_pages_PrintPV.setStyleSheet(u"border-bottom: 2px solid #D3CDCD;\n"
				"border-top-left-radius: 5px;\n"
				"padding-top: 1px;"
				"border-top-right-radius: 5px;\n"
			"")

	def clear_scrollArea(self):
		self.all_pages = []
		for i in reversed(range(self.ui.horizontalLayout_8_PrintPV.count())):
			self.ui.horizontalLayout_8_PrintPV.itemAt(i).widget().setParent(None)

	def user_paper(self, list_to_print): # Gerar folhas de impressao
		splited_list = self.chunks(list_to_print, 25)

		validator_PrintPV = QRegularExpressionValidator(f"[0-{len(splited_list)}-,]*")
		self.ui.lineEdit_pages_PrintPV.setValidator(validator_PrintPV)

		for i in range(len(splited_list)): #Gera a quantidade de folhas necessarias
			rodape = Roda_and_pe(len(splited_list), i)
			self.class_paper = Ui_Paper_Users()

			for x in splited_list[i]: # Aplica os 5 usuarios em cada folha.
				if len(x) < 4:
					x.append("Sem devolução.")
				user_bar_line = Ui_Line_Users(x[0], x[1], x[2], x[3])
				self.class_paper.verticalLayout_2.addWidget(user_bar_line.frame_line_ULU)
			self.class_paper.verticalLayout_2.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
			self.class_paper.verticalLayout_2.addWidget(rodape.roda_pe_RP)
			self.ui.horizontalLayout_8_PrintPV.addWidget(self.class_paper.background_papel)

			# Gerar as imgs para imprimir
			pix = QPixmap(self.class_paper.background_papel.size())
			self.class_paper.background_papel.render(pix)

			img_path = f'temp/page_{i+1}.png'
			self.all_pages.append(img_path)
			pix.save(img_path)

	def papers(self, list_to_print): # Gerar folhas de impressao
		splited_list = self.chunks(list_to_print, 6)

		validator_PrintPV = QRegularExpressionValidator(f"[0-{len(splited_list)}-,]*")
		self.ui.lineEdit_pages_PrintPV.setValidator(validator_PrintPV)

		for i in range(len(splited_list)): #Gera a quantidade de folhas necessarias
			rodape = Roda_and_pe(len(splited_list), i)
			self.class_paper = Ui_Paper()

			for x in splited_list[i]: # Aplica os 5 usuarios em cada folha.
				user_bar_line = Ui_Line(x[1], x[0])
				self.class_paper.verticalLayout_P.addWidget(user_bar_line.linha_01_ULI)
			self.class_paper.verticalLayout_P.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
			self.class_paper.verticalLayout_P.addWidget(rodape.roda_pe_RP)
			self.ui.horizontalLayout_8_PrintPV.addWidget(self.class_paper.paper_P)

			# Gerar as imgs para imprimir
			pix = QPixmap(self.class_paper.paper_P.size())
			self.class_paper.paper_P.render(pix)

			img_path = f'temp/page_{i+1}.png'
			self.all_pages.append(img_path)
			pix.save(img_path)

	def load_search_date_historic(self):
		self.lista_impressao_historico = []
		self.ui.table_relatorio.removeRow(self.ui.table_relatorio.rowCount()-1)
		
		# Junta todos os valores de datas para poder fazer a conta.
		inicial_date = '-'.join(self.ui.dateEdit_InicialDate.text().split('/')[::-1])
		end_date = '-'.join(self.ui.dateEdit_EndDate.text().split('/')[::-1])

		query = f'''SELECT id_sala, usuario_ret, usuario_dev, data_hora_retirada, data_hora_devolucao FROM  emprestimo
						WHERE data_hora_retirada BETWEEN date('{inicial_date}')
						AND date('{end_date}', '+1 day') ORDER BY data_hora_retirada ASC'''
		try:
			cursor.execute(query)
			emprestimos = cursor.fetchall()
			self.emprestimos = emprestimos
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		lista = []
		self.ui.table_relatorio.setRowCount(len(emprestimos))
		for row, emprestimo in enumerate(emprestimos):
			sublista = []
			for col, dado in enumerate(emprestimo):
				if dado:
					if col < 2:
						self.ui.table_relatorio.setItem(row, col, QTableWidgetItem(str(dado)))
						self.ui.table_relatorio.item(row, col).setTextAlignment(Qt.AlignCenter)
						sublista.append(str(dado))
					elif col == 2:
						self.ui.table_relatorio.item(row, col-1).setText(emprestimo[col-1] + ' / ' + emprestimo[col])
						sublista[-1] = emprestimo[col-1] + ' / ' + emprestimo[col]
					else:
						self.ui.table_relatorio.setItem(row, col-1, QTableWidgetItem('/'.join(dado.split()[0].split('-')[::-1]) +'  '+str(dado.split()[1][:-3])))
						self.ui.table_relatorio.item(row, col-1).setTextAlignment(Qt.AlignCenter)
						sublista.append('/'.join(dado.split()[0].split('-')[::-1]) +'  '+str(dado.split()[1][:-3]))

			lista.append(sublista)
			self.lista_impressao_historico.append(sublista)
			del sublista

	def delete_imgs(self):
		print('entrei')
		for filename in os.listdir('temp'):
			os.remove(f'temp/{filename}')
	
	def add_show_more(self):
		rowCount = self.ui.table_relatorio.rowCount()
		self.ui.table_relatorio.insertRow(rowCount)
		self.ui.table_relatorio.setSpan(rowCount, 0, 1, 4)

		self.lista_relatorio_btn_ver_mais = QPushButton(self.ui.table_relatorio)
		self.lista_relatorio_btn_ver_mais.setObjectName(u"lista_relatorio_btn_ver_mais")
		self.lista_relatorio_btn_ver_mais.setCursor(Qt.PointingHandCursor)
		self.lista_relatorio_btn_ver_mais.setText("Ver mais")
		self.lista_relatorio_btn_ver_mais.clicked.connect(self.ver_mais)
		self.lista_relatorio_btn_ver_mais.setStyleSheet("#lista_relatorio_btn_ver_mais { background-color: transparent; border: none; color: #111111; font-family: Aldrich; font-size: 18px;}\n"
		"#lista_relatorio_btn_ver_mais:hover { background-color: #DEEAFF;}")
		self.ui.table_relatorio.setCellWidget(rowCount, 0, self.lista_relatorio_btn_ver_mais)

	def clear_for_search(self):
		self.lista_impressao_historico = []
		self.loadData()

	def loadData(self):
		self.ui.table_relatorio.removeRow(self.ui.table_relatorio.rowCount()-1)
		txt = self.ui.lineEdit_searchBar.text().lower()
		if txt == '':		
			try:
				cursor.execute("SELECT COUNT(rowid) FROM emprestimo")
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

			self.total = cursor.fetchone()
			if self.total:
				self.total = self.total[0]

			query = f'''SELECT id_sala, usuario_ret, usuario_dev, data_hora_retirada, data_hora_devolucao FROM  emprestimo 
								ORDER BY data_hora_retirada ASC LIMIT {self.limit} OFFSET {self.limit*self.count}'''
		else:
			try:
				cursor.execute(f'''SELECT COUNT(*) FROM (SELECT id_sala, usuario_ret, usuario_dev, data_hora_retirada, data_hora_devolucao FROM  emprestimo 
								WHERE usuario_ret LIKE "%{txt}%" OR usuario_dev LIKE "%{txt}%" OR id_sala LIKE "%{txt}%")''')
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return			

			self.total = cursor.fetchone()
			if self.total:
				self.total = self.total[0]
			
			self.resetaCount()
			query = f'''SELECT id_sala, usuario_ret, usuario_dev, data_hora_retirada, data_hora_devolucao FROM  emprestimo 
						WHERE usuario_ret LIKE "%{txt}%" OR usuario_dev LIKE "%{txt}%" OR id_sala LIKE "%{txt}%"
						ORDER BY data_hora_retirada ASC LIMIT {self.limit} OFFSET {self.limit*self.count}'''
		
		try:
			cursor.execute(query)
			emprestimos = cursor.fetchall()
			self.emprestimos = emprestimos
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		lista = []
		self.ui.table_relatorio.setRowCount(self.limit*self.count)
		print(f"count e limite: {self.count}, {self.limit}")

		for emprestimo in emprestimos:
			sublista = []
			rowCount = self.ui.table_relatorio.rowCount()
			self.ui.table_relatorio.insertRow(rowCount)
			for col, dado in enumerate(emprestimo):
				if dado:
					if col < 2:
						self.ui.table_relatorio.setItem(rowCount, col, QTableWidgetItem(str(dado)))
						self.ui.table_relatorio.item(rowCount, col).setTextAlignment(Qt.AlignCenter)
						sublista.append(str(dado))
					elif col == 2:
						self.ui.table_relatorio.item(rowCount, col-1).setText(emprestimo[col-1] + ' / ' + emprestimo[col])
						sublista[-1] = emprestimo[col-1] + ' / ' + emprestimo[col]
					else:
						self.ui.table_relatorio.setItem(rowCount, col-1, QTableWidgetItem('/'.join(dado.split()[0].split('-')[::-1]) +'  '+str(dado.split()[1][:-3])))
						self.ui.table_relatorio.item(rowCount, col-1).setTextAlignment(Qt.AlignCenter)
						sublista.append('/'.join(dado.split()[0].split('-')[::-1]) +'  '+str(dado.split()[1][:-3]))
			lista.append(sublista)
			self.lista_impressao_historico.append(sublista)
			del sublista
		if self.total > self.ui.table_relatorio.rowCount():
			self.add_show_more()

		self.ui.pages_adm.setCurrentWidget(self.ui.historico)
		self.ui.dateEdit_InicialDate.setDate(QDate.currentDate())
		self.ui.dateEdit_EndDate.setDate(QDate.currentDate())
		self.ui.dateEdit_InicialDate.setSelectedSection(QDateEdit.NoSection)
		self.ui.dateEdit_EndDate.setSelectedSection(QDateEdit.NoSection)

	def ver_mais(self):
		if self.ui.table_relatorio.rowCount() > self.limit:
			self.count += 1
			self.loadData()
			self.ui.table_relatorio.clearSelection()

	def resetaCount(self):
		self.count = 0

	def divideString(self, string):	 
		strings = [x+'.' for x in string.split('.')]
		strings[-1] = strings[-1].strip('.')

		temp = []
		for item in strings:	
			
			tam = len(item)
			if tam > 11:
				
				i = n = 0
				while tam-i > 11:			
					if n == 1:
						extra = 3
					elif n == 2:
						extra = 2
					else:
						extra = 0

					if item[i] == ' ':
						i += 1

					if item[i+9] == ' ':
						temp.append(item[i:i+extra+9])
						i += (9 + extra)
					elif item[i+10] == ' ':
						temp.append(item[i:i+extra+10])
						i += (10 + extra)
					else:
						temp.append(item[i:i+extra+11])
						i += (11 + extra)
					n+=1
				temp.append(item[i:].strip())
			else:
				temp.append(item.strip())
		string = ''
		for item in temp[:4]:
			string = string + '\n' + item
		return string

	def spinBoxValueChanged(self):
		campo = self.ui.spinBox_num_copies.findChild(QLineEdit)
		campo.deselect()
		campo.clearFocus()

	def carregaDescanso(self):
		font = QFont()
		font.setFamilies([u"Aldrich"])
		font.setPointSize(10)
		
		try:
			cursor.execute('SELECT id_sala, nome, estado FROM chave ORDER BY id_sala ASC')
			chaves = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		chaves = [chaves[i:i + 5] for i in range(0, len(chaves), 5)]
		for row, linha in enumerate(chaves):
			for col, coluna in enumerate(linha):

				bolota = QLabel(self.ui.frame_148)
				bolota.setObjectName(f"label_1{row}{col}")
				bolota.setMinimumSize(QSize(105, 105))
				bolota.setMaximumSize(QSize(105, 105))

				string = self.divideString(coluna[1])
				bolota.setText(f"{coluna[0]}{string}")
				
				if coluna[2]:
					bolota.setStyleSheet(u"color:#000; background-color:#f89633")
				else:
					bolota.setStyleSheet(u"color:#000; background-color:#fff")
				
				bolota.setFont(font)
				bolota.setAlignment(Qt.AlignCenter)
				self.ui.gridLayout_3.addWidget(bolota, row, col, 1, 1)
		
		self.ui.pages.setCurrentWidget(self.ui.descanso)
		
	def descansoTela(self):
		self.timer_descanso.stop()
		if self.ui.pages.currentWidget() != self.ui.descanso:
			self.telaAtual = self.ui.pages.currentWidget()
		print(self.telaAtual.objectName())
		self.carregaDescanso()

	def fazBackUp(self):
		diaAtual = (str(datetime.now())[:10], )

		files = next(os.walk('./db'))[2]
		print(files)

		for file in files:
			if 'backup_' in file:
				print(file[7:-4])
				d1 = datetime.fromisoformat(diaAtual[0])
				d2 = datetime.fromisoformat(file[7:-4])
				print((d1-d2).days)
				if (d1-d2).days > 6:
					print(f'removi {file}')
					os.remove('./db/'+file)
		try:
			query = f"SELECT rowid FROM backup WHERE data = ?"
			cursor.execute(query, diaAtual)
			ult_backup = cursor.fetchone()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)

		print(f'res da query = {ult_backup}')
		if not ult_backup:
			try:
				query = f"INSERT INTO backup (data) VALUES (?)"
				cursor.execute(query, diaAtual)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

			print(f'fiz backup do dia {diaAtual[0]}')
			with open(f'db/backup_{diaAtual[0]}.sql', 'w') as f:
				for line in banco.iterdump():
					f.write(f'{line}\n')

	 
if __name__ == '__main__':

	myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	try:
		banco = sqlite3.connect('db\hub_key.db')
		cursor = banco.cursor()
	except sqlite3.Error as erro:
		print('Erro com o banco de dados: ', erro)

	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon('icons/hub_key.ico'))

	window = MainWindow()
	app.exec()
	banco.close()
