import sys
from datetime import datetime
from ui_main import *
from ui_dialog import Ui_Dialog, Ui_Dialog_2

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


class MainWindow(QMainWindow):

    timer_logout = QTimer()
    timer_descanso = QTimer()
    telaAtual = None
    
    '''emprestimos = [['302','Tatiane', '12:55'], ['304','Tatiane', '12:55'], ['306','Tatiane', '12:55'],
                    ['307','Enilda', '12:55'], ['310','Enilda', '12:55'], ['311','Enilda', '12:55']]
    '''
    emprestimos = []

    lista_chaves = [['','301', 'Lab. Informática'], ['','302', 'Sala Multiuso'], ['','303', 'Lab. Informática'], ['','304', 'Sala Multiuso'], ['','305', 'Lab. Redes']]

    usuarios = [['','4521', 'Diogo', 'Administrador'], ['', '6198', 'Enilda Aparecida', 'Integrante'], ['', '0265', 'Lucas da Silva', 'Administrador']]
    codigos = {'0264':'Diego', '2130':'Anderson', '9329':'Mariana', '1428':'Tatiana', '4287':'Enilda'}
    chaves = ['301', '302', '303', '304', '305', '306', '307', '310', '311']
    estouOrdenado = 0 

    tempo = 0
    codigo = None

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()
        
        self.showMaximized()
        self.show()

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

        #BOTÃO ADMINISTRADOR
        self.ui.btn_adm_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.email))
        self.ui.btn_adm_inicio.clicked.connect(lambda: self.ui.lineEdit_email_inicio.setFocus())

        #BOTÃO ENVIAR INICIO
        self.ui.btn_enviar_inicio.clicked.connect(self.validaEmail)
        self.ui.lineEdit_email_inicio.returnPressed.connect(self.validaEmail)
        
        #BOTÃO ENTRAR INICIO
        self.ui.btn_entrar_inicio.clicked.connect(self.validaSenha)
        self.ui.lineEdit_senha_inicio.returnPressed.connect(self.validaSenha)

        #BOTÃO ESQUECI SENHA
        self.ui.btn_esqueci_senha.clicked.connect(self.esqueciSenha)

        #BOTÃO INTEGRANTE
        self.ui.btn_int_inicio.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.emprestimos))
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

        #BOTÃO BUSCA CHAVES
        self.ui.btn_busca_chaves.clicked.connect(self.carregaChaves)
        self.ui.lineEdit_busca_chaves.returnPressed.connect(self.carregaChaves)

        #BOTÃO NOVA CHAVE
        self.ui.btn_nova_chave.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.cad_chaves))
        
        #BOTÃO EXCLUIR CHAVE
        self.ui.btn_exc_chave.clicked.connect(self.deletaChave)

        #BOTÃO VOLTAR
        self.ui.btn_voltar_chave.clicked.connect(self.limpaCampos)
        self.ui.btn_voltar_chave.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves))

        #BOTÃO SALVAR
        self.ui.btn_salvar_chave.clicked.connect(self.salvaChave)

        #BOTÃO MENU USUARIOS
        self.ui.btn_menu_usuario.clicked.connect(self.limpaCampos)
        self.ui.btn_menu_usuario.clicked.connect(lambda: self.animation(self.ui.btn_menu_usuario.y()))
        self.ui.btn_menu_usuario.clicked.connect(self.carregaUsuarios)
        self.ui.btn_menu_usuario.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios))

        #BOTÃO CADASTRAR
        self.ui.btn_cad_usuarios.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.cad_usuarios))

        #BOTÃO CANCELAR
        self.ui.btn_cad_cancelar.clicked.connect(self.limpaCampos)
        self.ui.btn_cad_cancelar.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_usuarios))

        #BOTÃO SALVAR
        self.ui.btn_cad_salvar.clicked.connect(self.salvaUsuario)

        #BOTÃO IMPRIMIR
        self.ui.btn_imp_usuarios.clicked.connect(self.show_popup_impresso)

        #BOTÃO EXCLUIR USUARIO
        self.ui.btn_exc_usuarios.clicked.connect(self.deletaUsuario)

        #BOTÃO EDITAR USUARIO
        for index in range(self.ui.table_lista_usuarios.rowCount()):
            lista_usuarios_btn_editar = QPushButton(self.ui.table)
            lista_usuarios_btn_editar.setIcon(QIcon("hub_key2\icons\edit_icon.svg"))
            lista_usuarios_btn_editar.setIconSize(QSize(16, 16))
            lista_usuarios_btn_editar.setStyleSheet("color: #111111; background-color: transparent;")
            self.ui.table.setCellWidget(index, 4, lista_usuarios_btn_editar)
            
        
        #CUSTOM SORTING
        self.ui.table_lista_usuarios.horizontalHeader().sectionClicked.connect(self.funcaoSorting)
        
        #BOTÃO MENU HISTORICO
        self.ui.btn_menu_historico.clicked.connect(self.limpaCampos)
        self.ui.btn_menu_historico.clicked.connect(lambda: self.animation(self.ui.btn_menu_historico.y()))
        self.ui.btn_menu_historico.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.historico))

        #BOTÃO SAIR
        self.ui.btn_menu_sair.clicked.connect(lambda: self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves))
        self.ui.btn_menu_sair.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.bem_vindo))

        #BOTÃO BUSCA USUARIOS
        self.ui.lineEdit_busca_usuarios.returnPressed.connect(self.carregaUsuarios)
        self.ui.btn_busca_usuarios.clicked.connect(self.carregaUsuarios)
        

        #DISPOSIÇÃO DAS TABELAS
        self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        #---------------------------------------------------------------#
        self.ui.table_lista_chaves.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table_lista_chaves.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        #---------------------------------------------------------------#
        self.ui.table_lista_usuarios.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table_lista_usuarios.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)


    def eventFilter(self, source, event):
        if (event.type() == QEvent.MouseButtonPress) or (event.type() == QEvent.KeyPress):
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

    def limpaCampos(self):
        for i in self.ui.pages.currentWidget().findChildren(QLineEdit):
            i.clear()

        for i in self.ui.pages.currentWidget().findChildren(QComboBox):
            i.setCurrentIndex(0)

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

        #conexao com banco
        self.ui.lineEdit_email_inicio.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.senha)
        self.ui.lineEdit_senha_inicio.setFocus()

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

        #conexao com banco

        self.carregaChaves()
        self.ui.pages.setCurrentWidget(self.ui.menu_adm)
        self.ui.stackedWidget.setCurrentWidget(self.ui.inicio)
        self.ui.lineEdit_senha_inicio.setText('')

    def esqueciSenha(self):
        self.ui.lineEdit_senha_inicio.setText('')

        msg = Dialog2(self)
        msg.ui.label.setText('Senha enviada para o')
        msg.ui.label_2.setText('email informado!')
        self.popup.show()
        msg.exec()
        self.popup.hide()

        #conexao com banco para conseguir a senha
        #codigo para disparo de email

        self.ui.lineEdit_senha_inicio.setFocus()

    def deslogar(self):
        self.timer_logout.stop()
        print(f'\ndeslogar\nintervalo = {self.timer_logout.interval()}\nrestante = {self.timer_logout.remainingTime()}')
        self.codigo = None

        self.ui.label.setText('Bem vindo,')
        self.ui.label_2.setText('Entre com seu código.')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_codigo)

        msg = Dialog2(self)
        msg.ui.label.setText('Usuário Deslogado!')
        self.popup.show()
        msg.exec()
        self.popup.hide()

    def voltarInicio(self):
        if self.codigo:
            self.deslogar()
        self.ui.pages_adm.setCurrentWidget(self.ui.lista_chaves)    
        self.ui.pages.setCurrentWidget(self.ui.bem_vindo)
        
    def descansoTela(self):
        if self.ui.pages.currentWidget() != self.ui.descanso:
            self.telaAtual = self.ui.pages.currentWidget()
        print(self.telaAtual.objectName())
        self.ui.pages.setCurrentWidget(self.ui.descanso)

    def devolveChave(self, pos):
        msg = Dialog(self)
        msg.ui.label.setText(f'{self.codigos[self.codigo]}, deseja devolver a chave {self.emprestimos[pos][0]}')

        msg2 = Dialog2(self)
        self.popup.show()
        if msg.exec():
            msg2.ui.label.setText(f'Chave devolvida com sucesso.')
            self.emprestimos.pop(pos)
            self.ui.tableEmprestimo.removeRow(pos)
        else:
            msg2.ui.label.setText(f'Operação cancelada!')
        msg2.exec()
        self.popup.hide()

    def carregaEmprestimo(self):
        txt = self.ui.lineEdit_busca_emprestimos.text().lower()

        if txt == '':
            emprestimos = self.emprestimos
        else:
            emprestimos = [i for i in self.emprestimos if ((i[0].find(txt)) != -1) or (i[1].lower().find(txt) != -1)]
        
        self.ui.tableEmprestimo.setRowCount(len(emprestimos))

        for row, emprestimo in enumerate(emprestimos):
            for col, dado in enumerate(emprestimo):
                self.ui.tableEmprestimo.setItem(row, col, QTableWidgetItem(dado))
                self.ui.tableEmprestimo.item(row, col).setTextAlignment(Qt.AlignCenter)
            
        #self.ui.tableEmprestimo.setColumnHidden(0, True)
    
    def loginUsuario(self):
        self.ui.lineEdit_codigo.blockSignals(True)
        self.codigo = self.ui.lineEdit_codigo.text()
        self.ui.lineEdit_codigo.setText('')

        if self.codigo not in self.codigos.keys():
            msg = Dialog2(self)
            msg.ui.label.setText('Código não encontrado!')
            self.popup.show()
            msg.exec()
            self.popup.hide()
            self.ui.lineEdit_codigo.blockSignals(False)
            return

        self.ui.label.setText(f'Olá {self.codigos[self.codigo]},')
        self.ui.label_2.setText(f'Entre com o código da chave.')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_chave)
        
        self.timer_logout.start(25000)
        print(f'timer_logout = {self.timer_logout.interval()}')
        
        self.ui.lineEdit_codigo.blockSignals(False)

    def fazEmprestimo(self):
        tempo = self.timer_logout.remainingTime()
        self.timer_logout.stop()
        print(f'\nentrei\nintervalo = {self.timer_logout.interval()}\nrestante = {tempo}\n')

        self.ui.lineEdit_chave.blockSignals(True)
        chave = self.ui.lineEdit_chave.text()
        self.ui.lineEdit_chave.setText('')

        if tempo < 1:
            self.ui.lineEdit_chave.blockSignals(False)
            return

        for pos, emprestimo in enumerate(self.emprestimos):
            if emprestimo[0] == chave:
                self.devolveChave(pos)
                self.ui.lineEdit_chave.blockSignals(False)

                self.timer_logout.start(tempo)
                print(f'reiniciou = {self.timer_logout.remainingTime()}')
                return        

        if chave  not in self.chaves:
            msg = Dialog2(self)
            msg.ui.label.setText('Chave não encontrada!')
            self.popup.show()
            msg.exec()
            self.popup.hide()
            self.ui.lineEdit_chave.blockSignals(False)
            
            self.timer_logout.start(tempo)
            print(f'reiniciou = {self.timer_logout.remainingTime()}')
            return

        msg = Dialog(self)
        msg.ui.label.setText(f'{self.codigos[self.codigo]}, deseja retirar a chave {chave}')

        msg2 = Dialog2(self)
        self.popup.show()
        if msg.exec():
            msg2.ui.label.setText(f'Chave retirada com sucesso.')
            self.emprestimos.append([chave, self.codigos[self.codigo], str(datetime.now().time())[:5]])
            self.carregaEmprestimo()
        else:
            msg2.ui.label.setText(f'Operação cancelada!')
        msg2.exec()
        self.popup.hide()
        self.ui.lineEdit_chave.blockSignals(False)

        self.timer_logout.start(tempo)
        print(f'reiniciou = {self.timer_logout.remainingTime()}')

    def carregaChaves(self):
        txt = self.ui.lineEdit_busca_chaves.text().lower()
        if txt == '':
            chaves = self.lista_chaves
        else:
            chaves = [i for i in self.lista_chaves if (i[1].find(txt) != -1) or (i[2].lower().find(txt) != -1)]
        self.ui.table_lista_chaves.setRowCount(len(chaves))
        for lin, chave in enumerate(chaves):
            for col, dado in enumerate(chave): 
                self.ui.table_lista_chaves.setItem(lin, col, QTableWidgetItem(dado))
                self.ui.table_lista_chaves.item(lin, col).setTextAlignment(Qt.AlignCenter)
        self.ui.table_lista_chaves.setColumnHidden(0, True)
        
    def deletaChave(self):
        #conexao com banco
        try:
            linha = self.ui.table_lista_chaves.selectedItems()[0].row()
        except IndexError:
            linha = None
        print(linha)        

        if linha != None:
            self.ui.table_lista_chaves.removeRow(linha)
            msg = Dialog2(self)
            msg.ui.label.setText('Chave removida')
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

        #conexao com banco
        self.limpaCampos()

        msg = Dialog2(self)
        msg.ui.label.setText('Chave cadastrada')
        msg.ui.label_2.setText('com sucesso!')
        self.popup.show()
        msg.exec()
        self.popup.hide()

    def carregaUsuarios(self):
        txt = self.ui.lineEdit_busca_usuarios.text().lower()
        if txt == '':
            usuarios = self.usuarios

        else:
            usuarios = [i for i in self.usuarios if (i[1].find(txt) != -1) or (i[2].lower().find(txt) != -1)]
    
        self.ui.table_lista_usuarios.setRowCount(len(usuarios))
        for lin, usuario in enumerate(usuarios):
            for col, dado in enumerate(usuario): 
            
                self.ui.table_lista_usuarios.setItem(lin, col, QTableWidgetItem(dado))
                self.ui.table_lista_usuarios.item(lin, col).setTextAlignment(Qt.AlignCenter)
        self.ui.table_lista_usuarios.setColumnHidden(0, True)

    def funcaoSorting(self, event):
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
    
    def deletaUsuario(self):
        #conexao com banco
        try:
            linha = self.ui.table_lista_usuarios.selectedItems()[0].row()
        except IndexError:
            linha = None
        print(linha)        

        if linha != None:
            self.ui.table_lista_usuarios.removeRow(linha)
            msg = Dialog2(self)
            msg.ui.label.setText('Usuário removido')
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
    
    def escondeCadExtras(self):
        if self.ui.cbb_cad_acesso.currentIndex():
            self.ui.label_cad_email.hide()
            self.ui.lineEdit_cad_email.hide()
            self.ui.label_cad_senha.hide()
            self.ui.lineEdit_cad_senha.hide()
        else:
            self.ui.label_cad_email.show()
            self.ui.lineEdit_cad_email.show()
            self.ui.label_cad_senha.show()
            self.ui.lineEdit_cad_senha.show()

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

        #conexao com banco
        self.limpaCampos()
        
        msg = Dialog2(self)
        msg.ui.label.setText('Usuário cadastrado')
        msg.ui.label_2.setText('com sucesso!')
        self.popup.show()
        msg.exec()
        self.popup.hide()

    def show_popup_impresso(self):
      
        self.popup.show()
        msg = Dialog2(self)
        msg.ui.label.setText("Impresso com sucesso!")
        msg.exec()
        self.popup.hide()

   
if __name__ == '__main__':

	#myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	app = QApplication(sys.argv)
	#app.setWindowIcon(QIcon('icons\church_black_48dp.svg'))

	window = MainWindow()
	sys.exit(app.exec())
	