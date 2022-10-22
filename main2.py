import sys

from designFiles.appMain import Ui_MainWindow
from databaseManage import database
from messageBoxes import myMessageBox

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon

class mainMenu(QtWidgets.QMainWindow):
    def __init__(self, userID):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.userID = userID

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

        self.ui.btnMainMenu.close()

        self.setWindowIcon(QIcon("resources/debt.png"))
        self.setWindowTitle("Debt Calculator")

        self.loadDatas()

        self.initActions()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def loadDatas(self):
        dbManager = database()
        respond = dbManager.getUserInfo(self.userID, "username")
        if respond != -1:
            self.ui.lblUserInfo.setText(f"You logged in as '{respond[0]}'")
            self.ui.lblUsername.setText(f"Username: {respond[0]}")

    def initActions(self):
        self.ui.btnExit.clicked.connect(self.action_btnExitClicked)
        self.ui.btnMinimize.clicked.connect(self.action_btnMinimizeClicked)
        self.ui.btnMainMenu.clicked.connect(self.action_btnMainMenuClicked)

        self.ui.btnAccountSettings.clicked.connect(self.action_btnAccountSettingsClicked)
        self.ui.btnChangePassword.clicked.connect(self.action_btnChangePasswordClicked)

    def action_btnExitClicked(self):
        self.close()

    def action_btnMinimizeClicked(self):
        self.showMinimized()

    def action_btnMainMenuClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMainMenu)
        self.ui.btnMainMenu.close()

    def action_btnAccountSettingsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAccountSettings)
        self.ui.btnMainMenu.show()

    def action_btnChangePasswordClicked(self):
        changePasswordBox = myMessageBox("changePassword", self.userID)
        changePasswordBox.show()
        changePasswordBox.exec()



# def App():
#     myApp = QtWidgets.QApplication(sys.argv)
#     myWindow = mainMenu(4)
#     myWindow.show()
#     myApp.exec()
#
# App()