import sys
from designFiles.startUpWindow import Ui_MainWindow
from databaseManage import database

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

        self.setWindowIcon(QIcon("resources/debt.png"))
        self.setWindowTitle("Debt Calculator")

        self.ui.btnBack.close()

        self.initActions()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def initActions(self):
        self.ui.btnExit.clicked.connect(self.action_btnExitClicked)
        self.ui.btnMinimize.clicked.connect(self.action_btnMinimizeClicked)

        self.ui.btnLogin.clicked.connect(self.action_btnLoginClicked)
        self.ui.btnRegister.clicked.connect(self.action_btnRegisterClicked)
        self.ui.btnBack.clicked.connect(self.action_btnBackClicked)

        self.ui.btnLogin_2.clicked.connect(self.action_btnLogin_2Clicked)

    def action_btnExitClicked(self):
        self.close()

    def action_btnMinimizeClicked(self):
        self.showMinimized()

    def action_btnLoginClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLogin)
        self.ui.btnBack.show()

    def action_btnRegisterClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageRegister)
        self.ui.btnBack.show()

    def action_btnBackClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageStartUp)
        self.ui.btnBack.close()

    def action_btnLogin_2Clicked(self):
        dbManager = database()

def App():
    myApp = QtWidgets.QApplication(sys.argv)
    window = myWindow()
    window.show()
    myApp.exec()

App()