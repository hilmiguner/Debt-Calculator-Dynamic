# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/resources/debt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        Dialog.setModal(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -1, 431, 281))
        self.widget.setStyleSheet("border: 4px solid;\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"border-radius: 20px;\n"
"background-image: url(:/backgrounds/resources/gradient3.jpg);\n"
"")
        self.widget.setObjectName("widget")
        self.btnOk = QtWidgets.QPushButton(self.widget)
        self.btnOk.setGeometry(QtCore.QRect(130, 210, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;\n"
"border:none;\n"
"")
        self.btnOk.setObjectName("btnOk")
        self.lbl1 = QtWidgets.QLabel(self.widget)
        self.lbl1.setGeometry(QtCore.QRect(20, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl1.setFont(font)
        self.lbl1.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(self.widget)
        self.lbl2.setGeometry(QtCore.QRect(20, 160, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl2.setFont(font)
        self.lbl2.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl2.setObjectName("lbl2")
        self.lblWarningIcon = QtWidgets.QLabel(self.widget)
        self.lblWarningIcon.setGeometry(QtCore.QRect(160, 10, 111, 111))
        self.lblWarningIcon.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblWarningIcon.setText("")
        self.lblWarningIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/warning.png"))
        self.lblWarningIcon.setScaledContents(True)
        self.lblWarningIcon.setObjectName("lblWarningIcon")
        self.lblUsername = QtWidgets.QLabel(self.widget)
        self.lblUsername.setGeometry(QtCore.QRect(150, 130, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblUsername.setText("")
        self.lblUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUsername.setObjectName("lblUsername")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.lbl1.setText(_translate("Dialog", "Username"))
        self.lbl2.setText(_translate("Dialog", "has been taken by another user !"))
import resource_rc
