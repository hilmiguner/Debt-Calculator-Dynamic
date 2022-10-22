import sys

from designFiles.appMain import Ui_MainWindow
from databaseManage import database
from messageBoxes import myMessageBox

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem

class mainMenu(QtWidgets.QMainWindow):
    def __init__(self, parentWindow, userID):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.userID = userID

        self.parentWindow = parentWindow

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

        self.ui.btnMainMenu.close()

        self.ui.tableRelatedPersons.hideColumn(0)
        self.ui.tableRelatedPersons.hideColumn(1)
        self.ui.tableRelatedPersons.horizontalHeader().setVisible(False)
        self.ui.tableRelatedPersons.verticalHeader().setVisible(False)

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

        result = dbManager.getRelatedPerson(self.userID, "tempUserID", "userID", "username")
        if result != -1:
            for ix, row in enumerate(result):
                self.ui.tableRelatedPersons.setRowCount(ix + 1)
                self.ui.tableRelatedPersons.setItem(ix, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableRelatedPersons.setItem(ix, 1, QTableWidgetItem(str(row[1])))
                self.ui.tableRelatedPersons.setItem(ix, 2, QTableWidgetItem(row[2]))

    def initActions(self):
        self.ui.btnExit.clicked.connect(self.action_btnExitClicked)
        self.ui.btnMinimize.clicked.connect(self.action_btnMinimizeClicked)
        self.ui.btnMainMenu.clicked.connect(self.action_btnMainMenuClicked)

        self.ui.btnLogOut.clicked.connect(self.action_btnLogOutClicked)

        self.ui.btnAccountSettings.clicked.connect(self.action_btnAccountSettingsClicked)
        self.ui.btnChangePassword.clicked.connect(self.action_btnChangePasswordClicked)

        self.ui.btnRelatedPersons.clicked.connect(self.action_btnRelatedPersonsClicked)
        self.ui.btnAddRelated.clicked.connect(self.action_btnAddRelatedClicked)
        self.ui.btnEditRelated.clicked.connect(self.action_btnEditRelatedClicked)
        self.ui.btnRemoveRelated.clicked.connect(self.action_btnRemoveRelatedClicked)

    def action_btnExitClicked(self):
        self.close()

    def action_btnMinimizeClicked(self):
        self.showMinimized()

    def action_btnMainMenuClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMainMenu)
        self.ui.btnMainMenu.close()

    def action_btnLogOutClicked(self):
        self.close()
        self.parentWindow.show()

    def action_btnAccountSettingsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAccountSettings)
        self.ui.btnMainMenu.show()

    def action_btnChangePasswordClicked(self):
        changePasswordBox = myMessageBox("changePassword", self.userID)
        changePasswordBox.show()
        changePasswordBox.exec()

    def action_btnRelatedPersonsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageRelatedPersons)
        self.ui.btnMainMenu.show()

    def action_btnAddRelatedClicked(self):
        addRelatedPersonBox = myMessageBox("addRelatedPerson", self, self.userID)
        addRelatedPersonBox.show()
        addRelatedPersonBox.exec()

    def action_btnEditRelatedClicked(self):
        if not self.ui.tableRelatedPersons.selectedItems():
            warningBox = myMessageBox("warning4")
            warningBox.show()
            warningBox.exec()
            return
        rowNumber = self.ui.tableRelatedPersons.selectedItems()[0].row()
        tempUserID = self.ui.tableRelatedPersons.item(rowNumber, 0).text()
        editRelatedPersonBox = myMessageBox("editRelatedPerson", self, tempUserID)
        editRelatedPersonBox.show()
        editRelatedPersonBox.exec()

    def action_btnRemoveRelatedClicked(self):
        if not self.ui.tableRelatedPersons.selectedItems():
            warningBox = myMessageBox("warning4")
            warningBox.show()
            warningBox.exec()
            return
        rowNumber = self.ui.tableRelatedPersons.selectedItems()[0].row()
        tempUserID = self.ui.tableRelatedPersons.item(rowNumber, 0).text()
        dbManager = database()
        tempUsername = dbManager.getRelatedPersonByTempUserID(tempUserID, "username")[0]
        warningBox = myMessageBox("warning5", self, tempUserID, tempUsername)
        warningBox.show()
        warningBox.exec()

# def App():
#     myApp = QtWidgets.QApplication(sys.argv)
#     myWindow = mainMenu(None, 3)
#     myWindow.show()
#     myApp.exec()
#
# App()