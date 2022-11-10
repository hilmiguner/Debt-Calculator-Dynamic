from PyQt5.QtWidgets import QDialog, QDesktopWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtWidgets

from databaseManage import database

from datetime import date


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

        elif ui == "warning6":
            from designFiles.warning6 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning7":
            from designFiles.warning7 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning8":
            from designFiles.warning8 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.lbl2_2.setText(args[0])
            self.uiManager.lbl2_4.setText(str(args[1]))

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning9":
            from designFiles.warning9 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.lbl2.setText(args[0])

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning10":
            from designFiles.warning10 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning11":
            from designFiles.warning11 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnOk.clicked.connect(self.accept)

        elif ui == "warning12":
            from designFiles.warning12 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.lblInfo4.setText(f"{args[1]} and {args[2]}")

            def action_btnYesClicked():
                db = database()
                db.deleteShoppingByShoppingID(args[0])
                args[3].loadDatas()
                self.accept()

            self.uiManager.btnYes.clicked.connect(action_btnYesClicked)
            self.uiManager.btnNo.clicked.connect(self.accept)

        elif ui == "warning13":
            from designFiles.warning13 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)


            self.uiManager.btnNo.clicked.connect(self.accept)

        elif ui == "warning14":
            from designFiles.warning14 import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnYes.clicked.connect(self.accept)
            self.uiManager.btnNo.clicked.connect(self.reject)

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

                db = database()
                if not db.checkPassword(args[0], currentPassword):
                    self.uiManager.widget.setGeometry(0, 0, 421, 341)
                    self.uiManager.lblInfo.setText(text1)
                    return
                if len(newPassword) < 8:
                    self.uiManager.widget.setGeometry(0, 0, 421, 341)
                    self.uiManager.lblInfo.setText(text2)
                    return

                db.changePassword(args[0], newPassword)
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
                userName = self.uiManager.lineRelatedPerson.text()

                db = database()
                relatedPersons = db.getRelatedPerson(args[1], "username")
                for relatedPerson in relatedPersons:
                    if relatedPerson[0] == userName:
                        warningBox = myMessageBox("warning11")
                        warningBox.show()
                        warningBox.exec()
                        return
                db.addTempUser(args[1], userName)

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
                relatedPersons = dbManager.getRelatedPerson(args[1], "username")
                for relatedPerson in relatedPersons:
                    if relatedPerson[0] == newUsername:
                        warningBox = myMessageBox("warning11")
                        warningBox.show()
                        warningBox.exec()
                        return

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

        elif ui == "shoppingInfo":
            from designFiles.shoppingInfo import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)

            self.uiManager.btnOk.clicked.connect(self.accept)

            shoppingInfo = args[0]
            shoppingDict = args[1]

            self.uiManager.lblShoppingName.setText(f"Shopping Name: {shoppingInfo[1]}")
            self.uiManager.lblShoppingCost.setText(f"Shopping Cost: {shoppingInfo[2]}")
            self.uiManager.lblShoppingDate.setText(f"Shopping Date: {shoppingInfo[3]}")

            labelFont = self.uiManager.lblShoppingName.font()

            verticalLayout = QtWidgets.QVBoxLayout()

            for tempUserID in shoppingDict:
                label = QtWidgets.QLabel()
                label.setStyleSheet("""color: #D9F1F5;""")

                dbManager = database()
                tempUserName = dbManager.getRelatedPersonByTempUserID(tempUserID, "username")[0]

                label.setText(f"'{tempUserName}' paid {shoppingDict[tempUserID]}.")
                label.setFont(labelFont)

                verticalLayout.addWidget(label)

            widget = QtWidgets.QWidget()
            widget.setLayout(verticalLayout)
            self.uiManager.scrollArea.setWidget(widget)

        elif ui == "addShopping":
            from designFiles.addShopping import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.setWindowTitle("Add Shopping")

            tempUserID_to_tempUserName = args[0]

            def action_lineShoppingNameTextChanged(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters and char not in string.digits and char != " ":
                        pos = self.uiManager.lineShoppingName.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineShoppingName.setText(text)
                        self.uiManager.lineShoppingName.setCursorPosition(pos - 1)

            def action_lineShoppingCostTextChanged(text):
                for ix, char in enumerate(text):
                    if char != "." and char not in string.digits:
                        pos = self.uiManager.lineShoppingCost.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineShoppingCost.setText(text)
                        self.uiManager.lineShoppingCost.setCursorPosition(pos - 1)

            def action_btnAddRelatedPersonClicked():
                if len(comboBoxes) == len(tempUserID_to_tempUserName):
                    box = myMessageBox("warning6")
                    box.show()
                    box.exec()
                    return

                comboBox = QtWidgets.QComboBox()
                comboBox.setFont(self.uiManager.btnAdd.font())
                policy = comboBox.sizePolicy()
                policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                comboBox.setSizePolicy(policy)
                comboBox.setMaximumSize(200, 50)
                comboBox.setStyleSheet("""color: #D9F1F5;
background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
border-radius: 5px;""")
                comboBoxes.append(comboBox)
                for key in tempUserID_to_tempUserName:
                    comboBox.addItem(tempUserID_to_tempUserName[key])

                def action_lineTextChanged(text):
                    for ix, char in enumerate(text):
                        if char != "." and char not in string.digits:
                            pos = line.cursorPosition()
                            text = text[:ix] + text[ix + 1:]
                            line.setText(text)
                            line.setCursorPosition(pos - 1)

                line = QtWidgets.QLineEdit()
                line.setPlaceholderText("Paid Value")
                policy = line.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                line.setSizePolicy(policy)
                line.setMaximumSize(500, 50)
                line.setStyleSheet("""background-color: #D1F0F3;
border-radius: 15px;
padding-left: 5px;
color: #069EAD;""")
                line.textChanged.connect(action_lineTextChanged)
                lineEdits.append(line)

                button = QtWidgets.QPushButton()
                button.setStyleSheet("""background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
color: #D9F1F5;
border:none;
padding: 5px;""")
                button.setFont(self.uiManager.btnAdd.font())
                policy = button.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                button.setSizePolicy(policy)
                button.setText("Remove Person")
                button.setMaximumSize(400, 50)
                buttons.append(button)
                buttonGroup.addButton(button)

                row = gridLayout.rowCount()
                gridLayout.addWidget(comboBox, row + 1, 0)
                gridLayout.addWidget(line, row + 1, 1)
                gridLayout.addWidget(button, row + 1, 2)

            def action_buttonGroupClicked(btn):
                ix = buttons.index(btn)
                comboBoxes[ix].deleteLater()
                lineEdits[ix].deleteLater()
                buttons[ix].deleteLater()

                comboBoxes.pop(ix)
                lineEdits.pop(ix)
                buttons.pop(ix)

            def action_btnAddClicked():
                if len(comboBoxes) == 0:
                    warningBox = myMessageBox("warning10")
                    warningBox.show()
                    warningBox.exec()
                    return

                tempListForComboText = set()
                for comboBox in comboBoxes:
                    tempListForComboText.add(comboBox.currentText())
                if len(comboBoxes) != len(tempListForComboText):
                    warningBox = myMessageBox("warning11")
                    warningBox.show()
                    warningBox.exec()
                    return

                isBlank = False
                if self.uiManager.lineShoppingName.text() == "":
                    isBlank = True
                else:
                    if self.uiManager.lineShoppingCost.text() == "":
                        isBlank = True
                    else:
                        if self.uiManager.lineShoppingDate.text() == "":
                            isBlank = True
                        else:
                            for lineEdit in lineEdits:
                                if lineEdit.text() == "":
                                    isBlank = True
                                    break
                if isBlank:
                    warningBox = myMessageBox("warning7")
                    warningBox.show()
                    warningBox.exec()
                    return

                try:
                    float(self.uiManager.lineShoppingCost.text())
                except ValueError:
                    warningBox = myMessageBox("warning9", "Shopping cost")
                    warningBox.show()
                    warningBox.exec()
                    return

                for ix, lineEdit in enumerate(lineEdits):
                    try:
                        float(lineEdit.text())
                    except ValueError:
                        parameter1 = comboBoxes[ix].currentText()
                        warningBox = myMessageBox("warning9", f"{parameter1} value")
                        warningBox.show()
                        warningBox.exec()
                        return

                totalPaid = 0
                for lineEdit in lineEdits:
                    totalPaid += float(lineEdit.text())
                if totalPaid != float(self.uiManager.lineShoppingCost.text()):
                    warningBox = myMessageBox("warning8", self.uiManager.lineShoppingCost.text(), totalPaid)
                    warningBox.show()
                    warningBox.exec()
                    return

                shoppingName = self.uiManager.lineShoppingName.text()
                shoppingCost = self.uiManager.lineShoppingCost.text()
                shoppingDate = self.uiManager.lineShoppingDate.text()
                userID = args[1]

                tempUserID_to_paidValue = {}
                for temp in tempUserID_to_tempUserName.keys():
                    for ix, cmbBox in enumerate(comboBoxes):
                        if cmbBox.currentText() == tempUserID_to_tempUserName[temp] and lineEdits[ix].text() != "":
                            tempUserID_to_paidValue[temp] = float(lineEdits[ix].text())
                            break
                costPerPerson = float(shoppingCost)/len(comboBoxes)
                isThereDebt = False
                for key in list(tempUserID_to_paidValue.keys()):
                    if float(tempUserID_to_paidValue[key]) != costPerPerson:
                        isThereDebt = True
                        break
                if not isThereDebt:
                    warningBox = myMessageBox("warning14")
                    warningBox.show()
                    response = warningBox.exec()
                    if int(response) == 1:
                        db = database()
                        db.addShopping(shoppingName, shoppingCost, shoppingDate, userID, tempUserID_to_paidValue)
                        args[2].loadDatas()
                        self.accept()
                    elif int(response) == 0:
                        return
                db = database()
                db.addShopping(shoppingName, shoppingCost, shoppingDate, userID, tempUserID_to_paidValue)
                args[2].loadDatas()
                self.accept()

            self.uiManager.btnCancel.clicked.connect(self.accept)
            self.uiManager.lineShoppingName.textChanged.connect(action_lineShoppingNameTextChanged)
            self.uiManager.lineShoppingCost.textChanged.connect(action_lineShoppingCostTextChanged)
            self.uiManager.btnAddRelatedPerson.clicked.connect(action_btnAddRelatedPersonClicked)
            self.uiManager.btnAdd.clicked.connect(action_btnAddClicked)

            self.uiManager.lineShoppingDate.setText(str(date.today()))

            gridLayout = QtWidgets.QGridLayout()

            comboBoxes = []
            lineEdits = []
            buttons = []
            buttonGroup = QtWidgets.QButtonGroup()
            buttonGroup.buttonClicked.connect(action_buttonGroupClicked)

            widget = QtWidgets.QWidget()
            widget.setLayout(gridLayout)
            self.uiManager.scrollArea.setWidget(widget)

        elif ui == "editShopping":
            from designFiles.editShopping import Ui_Dialog
            self.uiManager = Ui_Dialog()
            self.uiManager.setupUi(self)
            self.setWindowTitle("Edit Shopping")

            tempUserID_to_tempUserName = args[0]

            def action_lineShoppingNameTextChanged(text):
                for ix, char in enumerate(text):
                    if char not in string.ascii_letters and char not in string.digits and char != " ":
                        pos = self.uiManager.lineShoppingName.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineShoppingName.setText(text)
                        self.uiManager.lineShoppingName.setCursorPosition(pos - 1)

            def action_lineShoppingCostTextChanged(text):
                for ix, char in enumerate(text):
                    if char != "." and char not in string.digits:
                        pos = self.uiManager.lineShoppingCost.cursorPosition()
                        text = text[:ix] + text[ix + 1:]
                        self.uiManager.lineShoppingCost.setText(text)
                        self.uiManager.lineShoppingCost.setCursorPosition(pos - 1)

            def action_btnAddRelatedPersonClicked():
                if len(comboBoxes) == len(tempUserID_to_tempUserName):
                    box = myMessageBox("warning6")
                    box.show()
                    box.exec()
                    return

                comboBox = QtWidgets.QComboBox()
                comboBox.setFont(self.uiManager.btnAdd.font())
                policy = comboBox.sizePolicy()
                policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                comboBox.setSizePolicy(policy)
                comboBox.setMaximumSize(200, 50)
                comboBox.setStyleSheet("""color: #D9F1F5;
            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            border-radius: 5px;""")
                comboBoxes.append(comboBox)
                for key in tempUserID_to_tempUserName:
                    comboBox.addItem(tempUserID_to_tempUserName[key])

                def action_lineTextChanged(text):
                    for ix, char in enumerate(text):
                        if char != "." and char not in string.digits:
                            pos = line.cursorPosition()
                            text = text[:ix] + text[ix + 1:]
                            line.setText(text)
                            line.setCursorPosition(pos - 1)

                line = QtWidgets.QLineEdit()
                line.setPlaceholderText("Paid Value")
                policy = line.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                line.setSizePolicy(policy)
                line.setMaximumSize(500, 50)
                line.setStyleSheet("""background-color: #D1F0F3;
            border-radius: 15px;
            padding-left: 5px;
            color: #069EAD;""")
                line.textChanged.connect(action_lineTextChanged)
                lineEdits.append(line)

                button = QtWidgets.QPushButton()
                button.setStyleSheet("""background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            color: #D9F1F5;
            border:none;
            padding: 5px;""")
                button.setFont(self.uiManager.btnAdd.font())
                policy = button.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                button.setSizePolicy(policy)
                button.setText("Remove Person")
                button.setMaximumSize(400, 50)
                buttons.append(button)
                buttonGroup.addButton(button)

                row = gridLayout.rowCount()
                gridLayout.addWidget(comboBox, row + 1, 0)
                gridLayout.addWidget(line, row + 1, 1)
                gridLayout.addWidget(button, row + 1, 2)

            def createRelatePerson(cmbBoxText, paidValue):
                comboBox = QtWidgets.QComboBox()
                comboBox.setFont(self.uiManager.btnAdd.font())
                policy = comboBox.sizePolicy()
                policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                comboBox.setSizePolicy(policy)
                comboBox.setMaximumSize(200, 50)
                comboBox.setStyleSheet("""color: #D9F1F5;
            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            border-radius: 5px;""")
                comboBoxes.append(comboBox)
                for key in tempUserID_to_tempUserName:
                    comboBox.addItem(tempUserID_to_tempUserName[key])
                comboBox.setCurrentText(cmbBoxText)

                def action_lineTextChanged(text):
                    for ix, char in enumerate(text):
                        if char != "." and char not in string.digits:
                            pos = line.cursorPosition()
                            text = text[:ix] + text[ix + 1:]
                            line.setText(text)
                            line.setCursorPosition(pos - 1)

                line = QtWidgets.QLineEdit()
                line.setPlaceholderText("Paid Value")
                policy = line.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                line.setSizePolicy(policy)
                line.setMaximumSize(500, 50)
                line.setStyleSheet("""background-color: #D1F0F3;
            border-radius: 15px;
            padding-left: 5px;
            color: #069EAD;""")
                line.textChanged.connect(action_lineTextChanged)
                line.setText(str(paidValue))
                lineEdits.append(line)

                button = QtWidgets.QPushButton()
                button.setStyleSheet("""background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));
            color: #D9F1F5;
            border:none;
            padding: 5px;""")
                button.setFont(self.uiManager.btnAdd.font())
                policy = button.sizePolicy()
                policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
                button.setSizePolicy(policy)
                button.setText("Remove Person")
                button.setMaximumSize(400, 50)
                buttons.append(button)
                buttonGroup.addButton(button)

                row = gridLayout.rowCount()
                gridLayout.addWidget(comboBox, row + 1, 0)
                gridLayout.addWidget(line, row + 1, 1)
                gridLayout.addWidget(button, row + 1, 2)

            def action_buttonGroupClicked(btn):
                ix = buttons.index(btn)
                comboBoxes[ix].deleteLater()
                lineEdits[ix].deleteLater()
                buttons[ix].deleteLater()

                comboBoxes.pop(ix)
                lineEdits.pop(ix)
                buttons.pop(ix)

            def action_btnAddClicked():
                if len(comboBoxes) == 0:
                    warningBox = myMessageBox("warning10")
                    warningBox.show()
                    warningBox.exec()
                    return

                tempListForComboText = set()
                for comboBox in comboBoxes:
                    tempListForComboText.add(comboBox.currentText())
                if len(comboBoxes) != len(tempListForComboText):
                    warningBox = myMessageBox("warning11")
                    warningBox.show()
                    warningBox.exec()
                    return

                isBlank = False
                if self.uiManager.lineShoppingName.text() == "":
                    isBlank = True
                else:
                    if self.uiManager.lineShoppingCost.text() == "":
                        isBlank = True
                    else:
                        if self.uiManager.lineShoppingDate.text() == "":
                            isBlank = True
                        else:
                            for lineEdit in lineEdits:
                                if lineEdit.text() == "":
                                    isBlank = True
                                    break
                if isBlank:
                    warningBox = myMessageBox("warning7")
                    warningBox.show()
                    warningBox.exec()
                    return

                try:
                    float(self.uiManager.lineShoppingCost.text())
                except ValueError:
                    warningBox = myMessageBox("warning9", "Shopping cost")
                    warningBox.show()
                    warningBox.exec()
                    return

                for ix, lineEdit in enumerate(lineEdits):
                    try:
                        float(lineEdit.text())
                    except ValueError:
                        parameter1 = comboBoxes[ix].currentText()
                        warningBox = myMessageBox("warning9", f"{parameter1} value")
                        warningBox.show()
                        warningBox.exec()
                        return

                totalPaid = 0
                for lineEdit in lineEdits:
                    totalPaid += float(lineEdit.text())
                if totalPaid != float(self.uiManager.lineShoppingCost.text()):
                    warningBox = myMessageBox("warning8", self.uiManager.lineShoppingCost.text(), totalPaid)
                    warningBox.show()
                    warningBox.exec()
                    return

                dbManager.deleteShoppingByShoppingID(args[3])

                shoppingName = self.uiManager.lineShoppingName.text()
                shoppingCost = self.uiManager.lineShoppingCost.text()
                shoppingDate = self.uiManager.lineShoppingDate.text()
                userID = args[1]

                tempUserID_to_paidValue = {}
                for temp in tempUserID_to_tempUserName.keys():
                    for ix, cmbBox in enumerate(comboBoxes):
                        if cmbBox.currentText() == tempUserID_to_tempUserName[temp] and lineEdits[ix].text() != "":
                            tempUserID_to_paidValue[temp] = float(lineEdits[ix].text())
                            break

                db = database()
                db.addShopping(shoppingName, shoppingCost, shoppingDate, userID, tempUserID_to_paidValue)
                args[2].loadDatas()
                self.accept()

            self.uiManager.btnCancel.clicked.connect(self.accept)
            self.uiManager.lineShoppingName.textChanged.connect(action_lineShoppingNameTextChanged)
            self.uiManager.lineShoppingCost.textChanged.connect(action_lineShoppingCostTextChanged)
            self.uiManager.btnAddRelatedPerson.clicked.connect(action_btnAddRelatedPersonClicked)
            self.uiManager.btnAdd.clicked.connect(action_btnAddClicked)


            gridLayout = QtWidgets.QGridLayout()

            comboBoxes = []
            lineEdits = []
            buttons = []
            buttonGroup = QtWidgets.QButtonGroup()
            buttonGroup.buttonClicked.connect(action_buttonGroupClicked)

            self.uiManager.lineShoppingName.setText(args[4])
            self.uiManager.lineShoppingCost.setText(args[5])
            self.uiManager.lineShoppingDate.setText(args[6])

            dbManager = database()
            whichUsers = dbManager.getWhichUsersByShoppingID(args[3])
            for data in whichUsers:
                tempUserID = data[1]
                tempUserName = dbManager.getRelatedPersonByTempUserID(tempUserID, "username")[0]
                payedValue = dbManager.getWhoPayedByTempUserIDandShoppingID(tempUserID, args[3])[3]
                createRelatePerson(tempUserName, payedValue)

            widget = QtWidgets.QWidget()
            widget.setLayout(gridLayout)
            self.uiManager.scrollArea.setWidget(widget)


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = QDesktopWidget().availableGeometry().center()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
