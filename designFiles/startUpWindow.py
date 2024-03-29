# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border: 4px solid;\n"
"border-radius: 20px;\n"
"background-image: url(:/backgrounds/resources/gradient3.jpg);\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.btnExit = QtWidgets.QToolButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(420, 10, 31, 31))
        self.btnExit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnExit.setStyleSheet("border:none;\n"
"background: rgba(255, 122, 89, 0);")
        self.btnExit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/windowButtons/resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon)
        self.btnExit.setIconSize(QtCore.QSize(25, 25))
        self.btnExit.setObjectName("btnExit")
        self.btnMinimize = QtWidgets.QToolButton(self.centralwidget)
        self.btnMinimize.setGeometry(QtCore.QRect(380, 10, 31, 31))
        self.btnMinimize.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnMinimize.setStyleSheet("border:none;\n"
"background: rgba(255, 122, 89, 0);")
        self.btnMinimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/windowButtons/resources/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimize.setIcon(icon1)
        self.btnMinimize.setIconSize(QtCore.QSize(25, 25))
        self.btnMinimize.setObjectName("btnMinimize")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 40, 631, 651))
        self.widget.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.widget.setObjectName("widget")
        self.lblIcon = QtWidgets.QLabel(self.widget)
        self.lblIcon.setGeometry(QtCore.QRect(120, 0, 221, 161))
        self.lblIcon.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);")
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/debt.png"))
        self.lblIcon.setScaledContents(True)
        self.lblIcon.setObjectName("lblIcon")
        self.lblAppName = QtWidgets.QLabel(self.widget)
        self.lblAppName.setGeometry(QtCore.QRect(30, 170, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(34)
        self.lblAppName.setFont(font)
        self.lblAppName.setStyleSheet("color: #D9F1F5;")
        self.lblAppName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppName.setObjectName("lblAppName")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 230, 461, 221))
        self.stackedWidget.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageStartUp = QtWidgets.QWidget()
        self.pageStartUp.setObjectName("pageStartUp")
        self.btnLogin = QtWidgets.QPushButton(self.pageStartUp)
        self.btnLogin.setGeometry(QtCore.QRect(150, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;")
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(self.pageStartUp)
        self.btnRegister.setGeometry(QtCore.QRect(150, 120, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;")
        self.btnRegister.setObjectName("btnRegister")
        self.stackedWidget.addWidget(self.pageStartUp)
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setObjectName("pageLogin")
        self.lineUsername = QtWidgets.QLineEdit(self.pageLogin)
        self.lineUsername.setGeometry(QtCore.QRect(70, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineUsername.setFont(font)
        self.lineUsername.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineUsername.setStyleSheet("background-color: #D1F0F3;\n"
"border-radius: 15px;\n"
"padding-left: 35px;\n"
"color: #069EAD;")
        self.lineUsername.setMaxLength(20)
        self.lineUsername.setObjectName("lineUsername")
        self.linePassword = QtWidgets.QLineEdit(self.pageLogin)
        self.linePassword.setGeometry(QtCore.QRect(70, 90, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.linePassword.setFont(font)
        self.linePassword.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linePassword.setStyleSheet("background-color: #D1F0F3;\n"
"border-radius: 15px;\n"
"padding-left: 35px;\n"
"padding-right: 35px;\n"
"color: #069EAD;")
        self.linePassword.setMaxLength(20)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.btnLogin_2 = QtWidgets.QPushButton(self.pageLogin)
        self.btnLogin_2.setGeometry(QtCore.QRect(150, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnLogin_2.setFont(font)
        self.btnLogin_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLogin_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;")
        self.btnLogin_2.setObjectName("btnLogin_2")
        self.lblUserIcon = QtWidgets.QLabel(self.pageLogin)
        self.lblUserIcon.setGeometry(QtCore.QRect(80, 40, 21, 21))
        self.lblUserIcon.setText("")
        self.lblUserIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/user.png"))
        self.lblUserIcon.setScaledContents(True)
        self.lblUserIcon.setObjectName("lblUserIcon")
        self.lblPassIcon = QtWidgets.QLabel(self.pageLogin)
        self.lblPassIcon.setGeometry(QtCore.QRect(80, 100, 21, 21))
        self.lblPassIcon.setText("")
        self.lblPassIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/key.png"))
        self.lblPassIcon.setScaledContents(True)
        self.lblPassIcon.setObjectName("lblPassIcon")
        self.btnPassToggle = QtWidgets.QToolButton(self.pageLogin)
        self.btnPassToggle.setGeometry(QtCore.QRect(350, 100, 41, 21))
        self.btnPassToggle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPassToggle.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/resources/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/Icons/resources/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnPassToggle.setIcon(icon2)
        self.btnPassToggle.setIconSize(QtCore.QSize(30, 30))
        self.btnPassToggle.setCheckable(True)
        self.btnPassToggle.setObjectName("btnPassToggle")
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageRegister = QtWidgets.QWidget()
        self.pageRegister.setObjectName("pageRegister")
        self.btnRegister_2 = QtWidgets.QPushButton(self.pageRegister)
        self.btnRegister_2.setGeometry(QtCore.QRect(150, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnRegister_2.setFont(font)
        self.btnRegister_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnRegister_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;")
        self.btnRegister_2.setObjectName("btnRegister_2")
        self.lineUsername_2 = QtWidgets.QLineEdit(self.pageRegister)
        self.lineUsername_2.setGeometry(QtCore.QRect(70, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineUsername_2.setFont(font)
        self.lineUsername_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineUsername_2.setStyleSheet("background-color: #D1F0F3;\n"
"border-radius: 15px;\n"
"padding-left: 35px;\n"
"color: #069EAD;")
        self.lineUsername_2.setMaxLength(20)
        self.lineUsername_2.setObjectName("lineUsername_2")
        self.lblPassIcon_2 = QtWidgets.QLabel(self.pageRegister)
        self.lblPassIcon_2.setGeometry(QtCore.QRect(80, 100, 21, 21))
        self.lblPassIcon_2.setText("")
        self.lblPassIcon_2.setPixmap(QtGui.QPixmap(":/Icons/resources/key.png"))
        self.lblPassIcon_2.setScaledContents(True)
        self.lblPassIcon_2.setObjectName("lblPassIcon_2")
        self.lblUserIcon_2 = QtWidgets.QLabel(self.pageRegister)
        self.lblUserIcon_2.setGeometry(QtCore.QRect(80, 40, 21, 21))
        self.lblUserIcon_2.setText("")
        self.lblUserIcon_2.setPixmap(QtGui.QPixmap(":/Icons/resources/user.png"))
        self.lblUserIcon_2.setScaledContents(True)
        self.lblUserIcon_2.setObjectName("lblUserIcon_2")
        self.linePassword_2 = QtWidgets.QLineEdit(self.pageRegister)
        self.linePassword_2.setGeometry(QtCore.QRect(70, 90, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.linePassword_2.setFont(font)
        self.linePassword_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linePassword_2.setStyleSheet("background-color: #D1F0F3;\n"
"border-radius: 15px;\n"
"padding-left: 35px;\n"
"padding-right: 35px;\n"
"color: #069EAD;")
        self.linePassword_2.setMaxLength(20)
        self.linePassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword_2.setObjectName("linePassword_2")
        self.btnPassToggle_2 = QtWidgets.QToolButton(self.pageRegister)
        self.btnPassToggle_2.setGeometry(QtCore.QRect(350, 100, 41, 21))
        self.btnPassToggle_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPassToggle_2.setText("")
        self.btnPassToggle_2.setIcon(icon2)
        self.btnPassToggle_2.setIconSize(QtCore.QSize(30, 30))
        self.btnPassToggle_2.setCheckable(True)
        self.btnPassToggle_2.setObjectName("btnPassToggle_2")
        self.btnRegister_2.raise_()
        self.lineUsername_2.raise_()
        self.lblUserIcon_2.raise_()
        self.linePassword_2.raise_()
        self.lblPassIcon_2.raise_()
        self.btnPassToggle_2.raise_()
        self.stackedWidget.addWidget(self.pageRegister)
        self.btnBack = QtWidgets.QToolButton(self.centralwidget)
        self.btnBack.setEnabled(True)
        self.btnBack.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.btnBack.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.btnBack.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnBack.setStyleSheet("background: rgba(255, 122, 89, 0);\n"
"border:none;")
        self.btnBack.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/windowButtons/resources/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon3)
        self.btnBack.setIconSize(QtCore.QSize(25, 25))
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblAppName.setText(_translate("MainWindow", "DEBT CALCULATOR"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))
        self.btnRegister.setText(_translate("MainWindow", "REGISTER"))
        self.lineUsername.setPlaceholderText(_translate("MainWindow", "Username"))
        self.linePassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btnLogin_2.setText(_translate("MainWindow", "LOGIN"))
        self.btnLogin_2.setShortcut(_translate("MainWindow", "Return"))
        self.btnRegister_2.setText(_translate("MainWindow", "REGISTER"))
        self.btnRegister_2.setShortcut(_translate("MainWindow", "Return"))
        self.lineUsername_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.linePassword_2.setPlaceholderText(_translate("MainWindow", "Password"))
import resource_rc
