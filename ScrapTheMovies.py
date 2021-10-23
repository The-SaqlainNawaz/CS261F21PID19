from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from hhhh import Ui_MainWindow

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       # u = uic.loadUi('ScrapTheFuckingMovies.ui', self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.closebutton.clicked.connect(lambda: self.close())
        self.ui.pushButton_4.clicked.connect(lambda: self.showMinimized())
        
        self.show()
       # self.close()
        

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()