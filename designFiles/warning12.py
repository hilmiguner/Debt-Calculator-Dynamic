# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning12.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/resources/debt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        Dialog.setModal(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -1, 431, 361))
        self.widget.setStyleSheet("border: 4px solid;\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"border-radius: 20px;\n"
"background-image: url(:/backgrounds/resources/gradient3.jpg);\n"
"")
        self.widget.setObjectName("widget")
        self.btnNo = QtWidgets.QPushButton(self.widget)
        self.btnNo.setGeometry(QtCore.QRect(230, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnNo.setFont(font)
        self.btnNo.setStyleSheet("background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;\n"
"border:none;\n"
"")
        self.btnNo.setObjectName("btnNo")
        self.lblInfo1 = QtWidgets.QLabel(self.widget)
        self.lblInfo1.setGeometry(QtCore.QRect(20, 130, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lblInfo1.setFont(font)
        self.lblInfo1.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblInfo1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo1.setObjectName("lblInfo1")
        self.lblWarningIcon = QtWidgets.QLabel(self.widget)
        self.lblWarningIcon.setGeometry(QtCore.QRect(160, 10, 111, 111))
        self.lblWarningIcon.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblWarningIcon.setText("")
        self.lblWarningIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/warning.png"))
        self.lblWarningIcon.setScaledContents(True)
        self.lblWarningIcon.setObjectName("lblWarningIcon")
        self.btnYes = QtWidgets.QPushButton(self.widget)
        self.btnYes.setGeometry(QtCore.QRect(30, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnYes.setFont(font)
        self.btnYes.setStyleSheet("background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"color: #D9F1F5;\n"
"border:none;\n"
"")
        self.btnYes.setObjectName("btnYes")
        self.lblInfo3 = QtWidgets.QLabel(self.widget)
        self.lblInfo3.setGeometry(QtCore.QRect(20, 210, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lblInfo3.setFont(font)
        self.lblInfo3.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblInfo3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo3.setObjectName("lblInfo3")
        self.lblInfo4 = QtWidgets.QLabel(self.widget)
        self.lblInfo4.setGeometry(QtCore.QRect(20, 250, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lblInfo4.setFont(font)
        self.lblInfo4.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblInfo4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo4.setObjectName("lblInfo4")
        self.lblInfo2 = QtWidgets.QLabel(self.widget)
        self.lblInfo2.setGeometry(QtCore.QRect(20, 170, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lblInfo2.setFont(font)
        self.lblInfo2.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblInfo2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo2.setObjectName("lblInfo2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.btnNo.setText(_translate("Dialog", "NO"))
        self.lblInfo1.setText(_translate("Dialog", "Are you sure"))
        self.btnYes.setText(_translate("Dialog", "YES"))
        self.lblInfo3.setText(_translate("Dialog", "shopping named and cost are"))
        self.lblInfo4.setText(_translate("Dialog", "shopping name and cost"))
        self.lblInfo2.setText(_translate("Dialog", "want to delete"))
import resource_rc
