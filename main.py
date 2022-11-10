import sys
import string
from designFiles.startUpWindow import Ui_MainWindow
from messageBoxes import myMessageBox
from databaseManage import database

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDialog, QDesktopWidget

class myWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = QDesktopWidget().availableGeometry().center()

        self.myMainMenu = None

        self.userID = None

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

        self.ui.lineUsername_2.textChanged.connect(self.action_lineUsername_2Changed)
        self.ui.lineUsername.textChanged.connect(self.action_lineUsernameChanged)

        self.ui.linePassword_2.textChanged.connect(self.action_linePassword_2Changed)
        self.ui.linePassword.textChanged.connect(self.action_linePasswordChanged)

        self.ui.btnPassToggle.clicked.connect(self.action_btnPassToggleClicked)
        self.ui.btnPassToggle_2.clicked.connect(self.action_btnPassToggle_2Clicked)

        self.ui.btnRegister_2.clicked.connect(self.action_btnRegister_2Clicked)
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

    def action_lineUsername_2Changed(self, text):
        for ix, char in enumerate(text):
            if char not in string.ascii_letters and char not in string.digits:
                pos = self.ui.lineUsername_2.cursorPosition()
                text = text[:ix] + text[ix + 1:]
                self.ui.lineUsername_2.setText(text)
                self.ui.lineUsername_2.setCursorPosition(pos - 1)

    def action_lineUsernameChanged(self, text):
        for ix, char in enumerate(text):
            if char not in string.ascii_letters and char not in string.digits:
                pos = self.ui.lineUsername.cursorPosition()
                text = text[:ix] + text[ix + 1:]
                self.ui.lineUsername.setText(text)
                self.ui.lineUsername.setCursorPosition(pos - 1)

    def action_linePassword_2Changed(self, text):
        for ix, char in enumerate(text):
            if char not in string.ascii_letters and char not in string.digits:
                pos = self.ui.linePassword_2.cursorPosition()
                text = text[:ix] + text[ix + 1:]
                self.ui.linePassword_2.setText(text)
                self.ui.linePassword_2.setCursorPosition(pos - 1)

    def action_linePasswordChanged(self, text):
        for ix, char in enumerate(text):
            if char not in string.ascii_letters and char not in string.digits:
                pos = self.ui.linePassword.cursorPosition()
                text = text[:ix] + text[ix + 1:]
                self.ui.linePassword.setText(text)
                self.ui.linePassword.setCursorPosition(pos - 1)

    def action_btnPassToggleClicked(self, isToggled):
        if isToggled:
            self.ui.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.ui.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def action_btnPassToggle_2Clicked(self, isToggled):
        if isToggled:
            self.ui.linePassword_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.ui.linePassword_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def action_btnLogin_2Clicked(self):
        username = self.ui.lineUsername.text()
        password = self.ui.linePassword.text()

        dbManager = database()
        result = dbManager.checkLogin(username, password)
        if not result:
            warningBox = myMessageBox("warning3")
            warningBox.show()
            warningBox.exec()
        elif result[0]:
            self.userID = result[1]
            from main2 import mainMenu
            self.close()
            self.myMainMenu = mainMenu(self, self.userID)
            self.myMainMenu.show()

    def action_btnRegister_2Clicked(self):
        username = self.ui.lineUsername_2.text()
        password = self.ui.linePassword_2.text()

        dbManager = database()
        if dbManager.canUserRegister(username):
            if len(password) < 8:
                warningBox = myMessageBox("warning2")
                warningBox.show()
                warningBox.exec()
                return
            self.userID = dbManager.addUser(username, password)
            from main2 import mainMenu
            self.close()
            self.myMainMenu = mainMenu(self, self.userID)
            self.myMainMenu.show()

        else:
            warningBox = myMessageBox("warning1", username)
            warningBox.show()
            warningBox.exec()
            return

def App():
    myApp = QtWidgets.QApplication(sys.argv)
    window = myWindow(myApp)
    window.show()
    myApp.exec()

App()