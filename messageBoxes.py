from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtWidgets

from databaseManage import database


import string

class myMessageBox(QDialog):
    def __init__(self, ui, *args):
        super().__init__()
        if ui == "warning1":
            from designFiles.warning1 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.uiManager.lblUsername.setText(f"'{args[0]}'")
            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning2":
            from designFiles.warning2 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning3":
            from designFiles.warning3 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning4":
            from designFiles.warning4 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning5":
            from designFiles.warning5 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            tempUserName = args[2]
            self.uiManager.lblInfo4.setText(f"'{tempUserName}'")

            tempUserID = args[1]
            dbManager = database()

            def action_btnYesClicked():
                dbManager.deleteTempUser(tempUserID)
                args[0].loadDatas()
                self.accept()

            self.uiManager.btnNo.clicked.connect(self.accept)
            self.uiManager.btnYes.clicked.connect(action_btnYesClicked)

        elif ui == "changePassword":
            from designFiles.changePassword import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            def action_btnPassToggleClicked(isToggled):
                if isToggled:
                    self.uiManager.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                else:
                    self.uiManager.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

            def action_btnPassToggle_2Clicked(isToggled):
                if isToggled:
                    self.uiManager.linePassword_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                else:
                    self.uiManager.linePassword_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

            def action_linePassword_2Changed(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters and char not in string.digits:
                        pos = self.uiManager.linePassword_2.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.linePassword_2.setText(text)
                        self.uiManager.linePassword_2.setCursorPosition(pos - 1)

            def action_linePasswordChanged(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters and char not in string.digits:
                        pos = self.uiManager.linePassword.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.linePassword.setText(text)
                        self.uiManager.linePassword.setCursorPosition(pos - 1)

            def action_btnChangeClicked():
                text1 = "There is no match for your \ncurrent password on the system."
                text2 = "Your password must be  \nat least 8 characters."
                currentPassword = self.uiManager.linePassword.text()
                newPassword = self.uiManager.linePassword_2.text()

                dbManager = database()
                if not dbManager.checkPassword(args[0], currentPassword):
                    self.uiManager.widget.setGeometry(0, 0, 421, 341)
                    self.uiManager.lblInfo.setText(text1)
                    return
                if len(newPassword) < 8:
                    self.uiManager.widget.setGeometry(0, 0, 421, 341)
                    self.uiManager.lblInfo.setText(text2)
                    return

                dbManager.changePassword(args[0], newPassword)
                self.accept()

            self.uiManager.btnChange.clicked.connect(action_btnChangeClicked)
            self.uiManager.btnPassToggle.clicked.connect(action_btnPassToggleClicked)
            self.uiManager.btnCancel.clicked.connect(self.accept)
            self.uiManager.btnPassToggle_2.clicked.connect(action_btnPassToggle_2Clicked)
            self.uiManager.linePassword_2.textChanged.connect(action_linePassword_2Changed)
            self.uiManager.linePassword.textChanged.connect(action_linePasswordChanged)

        elif ui == "addRelatedPerson":
            from designFiles.addRelatedPerson import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            def action_btnAddClicked():
                tempUserName = self.uiManager.lineRelatedPerson.text()

                dbManager = database()
                dbManager.addTempUser(args[1], tempUserName)

                args[0].loadDatas()

                self.accept()

            def action_lineRelatedPersonChanged(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters:
                        pos = self.uiManager.lineRelatedPerson.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineRelatedPerson.setText(text)
                        self.uiManager.lineRelatedPerson.setCursorPosition(pos - 1)

            self.uiManager.btnCancel.clicked.connect(self.accept)
            self.uiManager.btnAdd.clicked.connect(action_btnAddClicked)
            self.uiManager.lineRelatedPerson.textChanged.connect(action_lineRelatedPersonChanged)

        elif ui == "editRelatedPerson":
            from designFiles.editRelatedPerson import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            tempUserID = args[1]
            dbManager = database()
            oldUsername = dbManager.getRelatedPersonByTempUserID(tempUserID, "username")[0]
            self.uiManager.lineRelatedPerson.setText(oldUsername)

            def action_btnChangeClicked():
                newUsername = self.uiManager.lineRelatedPerson.text()

                dbManager.changeTempUsername(tempUserID, newUsername)

                args[0].loadDatas()

                self.accept()



            def action_lineRelatedPersonTextChanged(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters:
                        pos = self.uiManager.lineRelatedPerson.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineRelatedPerson.setText(text)
                        self.uiManager.lineRelatedPerson.setCursorPosition(pos - 1)

            self.uiManager.btnCancel.clicked.connect(self.accept)
            self.uiManager.btnChange.clicked.connect(action_btnChangeClicked)

            self.uiManager.lineRelatedPerson.textChanged.connect(action_lineRelatedPersonTextChanged)


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

