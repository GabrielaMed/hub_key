import sys
from ui_main_window import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.showMaximized()
        self.show()

        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

if __name__ == '__main__':

	#myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	app = QApplication(sys.argv)
	#app.setWindowIcon(QIcon('icons\church_black_48dp.svg'))

	window = MainWindow()
	sys.exit(app.exec())