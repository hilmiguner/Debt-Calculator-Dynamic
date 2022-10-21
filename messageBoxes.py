from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QPoint

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

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.oldPos = None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()