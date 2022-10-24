import sys

from designFiles.appMain import Ui_MainWindow
from databaseManage import database
from messageBoxes import myMessageBox

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget

class mainMenu(QtWidgets.QMainWindow):
    def __init__(self, parentWindow, userID):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.userID = userID

        self.parentWindow = parentWindow

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = QDesktopWidget().availableGeometry().center()

        self.ui.btnMainMenu.close()

        self.ui.tableRelatedPersons.hideColumn(0)
        self.ui.tableRelatedPersons.hideColumn(1)
        self.ui.tableRelatedPersons.horizontalHeader().setVisible(False)
        self.ui.tableRelatedPersons.verticalHeader().setVisible(False)

        self.ui.tableShoppings.hideColumn(0)
        self.ui.tableShoppings.hideColumn(1)
        self.ui.tableShoppings.verticalHeader().setVisible(False)

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

        shoppings, shopDict = dbManager.getInfoForShoppingUI(self.userID)
        if shoppings != -1 and shopDict != -1:
            for ix, row in enumerate(shoppings):
                self.ui.tableShoppings.setRowCount(ix + 1)
                self.ui.tableShoppings.setItem(ix, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableShoppings.setItem(ix, 1, QTableWidgetItem(str(row[4])))
                self.ui.tableShoppings.setItem(ix, 2, QTableWidgetItem(row[1]))
                self.ui.tableShoppings.setItem(ix, 3, QTableWidgetItem(str(row[2])))
                self.ui.tableShoppings.setItem(ix, 4, QTableWidgetItem(row[3]))

                relatedsL = []
                for tempUserID in shopDict[str(row[0])]:
                    relatedsL.append(dbManager.getRelatedPersonByTempUserID(tempUserID[0], "username")[0])
                relateds = ", ".join(relatedsL)

                self.ui.tableShoppings.setItem(ix, 5, QTableWidgetItem(relateds))

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

        self.ui.btnShoppings.clicked.connect(self.action_btnShoppingsClicked)
        self.ui.tableShoppings.itemDoubleClicked.connect(self.action_tableShoppingsItemDoubleClicked)
        self.ui.btnAddShopping.clicked.connect(self.action_btnAddShoppingClicked)

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

    def action_btnShoppingsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageShoppings)
        self.ui.btnMainMenu.show()

    def action_tableShoppingsItemDoubleClicked(self, item):
        row = item.row()
        shoppingID = self.ui.tableShoppings.item(row, 0).text()

        dbManager = database()
        shoppingInfo, shoppingDict = dbManager.getShoppingByShoppingID(shoppingID)
        if shoppingInfo != -1 and shoppingDict != -1:
            shoppingInfoBox = myMessageBox("shoppingInfo", shoppingInfo, shoppingDict)
            shoppingInfoBox.show()
            shoppingInfoBox.exec()

    def action_btnAddShoppingClicked(self):
        dbManager = database()
        result = dbManager.getRelatedPerson(self.userID, "tempUserID", "username")

        tempUserID_to_tempUserName = {}

        for tempUser in result:
            tempUserID_to_tempUserName[str(tempUser[0])] = tempUser[1]

        addShoppingBox = myMessageBox("addShopping", tempUserID_to_tempUserName)
        addShoppingBox.show()
        addShoppingBox.exec()

# def App():
#     myApp = QtWidgets.QApplication(sys.argv)
#     myWindow = mainMenu(None, 3)
#     myWindow.show()
#     myApp.exec()
#
# App()