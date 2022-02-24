import sys
from ui_main_window import *
from ui_dialog import Ui_Dialog_2

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

class Dialog2(QDialog):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.setAttribute(Qt.WA_DeleteOnClose)
            self.ui = Ui_Dialog_2()
            self.ui.setupUi(self)

class MainWindow(QMainWindow):

    usuarios = [['','4521', 'Diogo', 'Administrador'], ['', '6198', 'Enilda Aparecida', 'Integrante'], ['', '0265', 'Lucas da Silva', 'Administrador']]
    estouOrdenado = 0 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.carregaUsuarios()

        self.showMaximized()
        self.show()
        #BOTÃO BUSCA
        self.ui.search_icon.clicked.connect(self.carregaUsuarios)

        #APERTA ENTER
        self.ui.buscar.returnPressed.connect(self.carregaUsuarios)
        
        #BOTÃO CADASTRAR
        self.ui.btn_cadastrar.clicked.connect(self.show_popup_cadastrar)

        #BOTÃO IMPRIMIR
        self.ui.btn_imprimir.clicked.connect(self.show_popup_impresso)

        #BOTÃO EXCLUIR
        self.ui.btn_excluir.clicked.connect(lambda: self.ui.table.removeRow(self.ui.table.selectedItems()[0].row()))
        
        #Sorting
        self.ui.table.horizontalHeader().sectionClicked.connect(self.lalala)
        #BOTÃO EDITAR
        #self. ___qtablewidgetitem1.doubleClicked.connect(self.show_popup_editar)

    def lalala(self, event):
        if event < 2:
            self.ui.table.horizontalHeader().setSortIndicatorShown(False)
            return

        match self.estouOrdenado:
            case 0:
                self.ui.table.sortByColumn(event, Qt.AscendingOrder)
                self.ui.table.horizontalHeader().setSortIndicatorShown(True)
                self.estouOrdenado = 1
            case 1:
                self.ui.table.sortByColumn(event, Qt.DescendingOrder)
                self.ui.table.horizontalHeader().setSortIndicatorShown(True)
                self.estouOrdenado = 2
            case 2:
                self.carregaUsuarios()
                self.ui.table.horizontalHeader().setSortIndicatorShown(False)
                self.estouOrdenado = 0

    def carregaUsuarios(self):
        txt = self.ui.buscar.text().lower()
        #print('entrei1')
        if txt == '':
            usuarios = self.usuarios

        else:
            usuarios = [i for i in self.usuarios if (i[1].find(txt) != -1) or (i[2].lower().find(txt) != -1)]
    
        self.ui.table.setRowCount(len(usuarios))
        for lin, usuario in enumerate(usuarios):
            for col, dado in enumerate(usuario): 
            
                self.ui.table.setItem(lin, col, QTableWidgetItem(dado))
                self.ui.table.item(lin, col).setTextAlignment(Qt.AlignCenter)
        

        self.ui.table.setColumnHidden(0, True)
    

    def show_popup_cadastrar(self):
        self.popup.show()
        msg = Dialog2(self)
        msg.ui.label.setText('Usuário cadastrado com sucesso!')
        msg.exec()
        self.popup.hide()

    def show_popup_impresso(self):
        if not self.ui.table.selectedItems():
            self.ui.table.showColumn(0)
            return
        else:
            self.ui.table.hideColumn(0)

        self.popup.show()
        msg = Dialog2(self)
        msg.ui.label.setText("Impresso com sucesso!")
        msg.exec()
        self.popup.hide()



    def show_popup_editar(self):
        msg = Dialog2()
        msg.setWindowTitle("Editar Usuário")
        msg.setText("Usuário editado com sucesso!")
        msg.defaultButton(u"border-radius: 20px;\n"
"font: 16pt \"Aldrich\";\n"
"color: #fff;\n"
"background-color: rgb(6, 74, 128);")
        msg.setStyleSheet(u"border-radius: 20px;\n""font: 16pt \"Aldrich\";\n""border: 2px solid;\n""color: rgb(6, 74, 128);\n""border-color: rgb(6, 74, 128);")

        msg.exec()

if __name__ == '__main__':

	#myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	app = QApplication(sys.argv)
	#app.setWindowIcon(QIcon('icons\church_black_48dp.svg'))

	window = MainWindow()
	sys.exit(app.exec())