import sys

from designFiles.appMain import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon

class mainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

        self.ui.btnMainMenu.close()

        self.setWindowIcon(QIcon("resources/debt.png"))
        self.setWindowTitle("Debt Calculator")

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

        self.ui.btnAccountSettings.clicked.connect(self.action_btnAccountSettingsClicked)

    def action_btnExitClicked(self):
        self.close()

    def action_btnMinimizeClicked(self):
        self.showMinimized()

    def action_btnAccountSettingsClicked(self):
        print("a")

def App():
    myApp = QtWidgets.QApplication(sys.argv)
    myWindow = mainMenu()
    myWindow.show()
    myApp.exec()

App()