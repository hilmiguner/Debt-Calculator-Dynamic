# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning14.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 402)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/resources/debt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        Dialog.setModal(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.widget.setStyleSheet("border: 4px solid;\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.1875 rgba(0, 210, 255, 255), stop:1 rgba(0, 255, 173, 255));\n"
"border-radius: 20px;\n"
"background-image: url(:/backgrounds/resources/gradient3.jpg);\n"
"")
        self.widget.setObjectName("widget")
        self.btnYes = QtWidgets.QPushButton(self.widget)
        self.btnYes.setGeometry(QtCore.QRect(40, 310, 171, 51))
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
        self.lbl1 = QtWidgets.QLabel(self.widget)
        self.lbl1.setGeometry(QtCore.QRect(40, 170, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl1.setFont(font)
        self.lbl1.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1.setObjectName("lbl1")
        self.lblWarningIcon = QtWidgets.QLabel(self.widget)
        self.lblWarningIcon.setGeometry(QtCore.QRect(180, 10, 111, 111))
        self.lblWarningIcon.setStyleSheet("background-image: url();\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lblWarningIcon.setText("")
        self.lblWarningIcon.setPixmap(QtGui.QPixmap(":/Icons/resources/warning.png"))
        self.lblWarningIcon.setScaledContents(True)
        self.lblWarningIcon.setObjectName("lblWarningIcon")
        self.lbl1_2 = QtWidgets.QLabel(self.widget)
        self.lbl1_2.setGeometry(QtCore.QRect(40, 210, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl1_2.setFont(font)
        self.lbl1_2.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1_2.setObjectName("lbl1_2")
        self.lbl1_3 = QtWidgets.QLabel(self.widget)
        self.lbl1_3.setGeometry(QtCore.QRect(20, 130, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl1_3.setFont(font)
        self.lbl1_3.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1_3.setObjectName("lbl1_3")
        self.lbl1_4 = QtWidgets.QLabel(self.widget)
        self.lbl1_4.setGeometry(QtCore.QRect(20, 250, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.lbl1_4.setFont(font)
        self.lbl1_4.setStyleSheet("color: #D9F1F5;\n"
"background: rgba(0,0,0,0);\n"
"border:none;")
        self.lbl1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1_4.setObjectName("lbl1_4")
        self.btnNo = QtWidgets.QPushButton(self.widget)
        self.btnNo.setGeometry(QtCore.QRect(260, 310, 171, 51))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.btnYes.setText(_translate("Dialog", "YES"))
        self.lbl1.setText(_translate("Dialog", "so adding this shopping"))
        self.lbl1_2.setText(_translate("Dialog", "won\'t affect debt table."))
        self.lbl1_3.setText(_translate("Dialog", "No one has debt from this shopping"))
        self.lbl1_4.setText(_translate("Dialog", "Are you sure to add this shopping ?"))
        self.btnNo.setText(_translate("Dialog", "NO"))
import resource_rc
