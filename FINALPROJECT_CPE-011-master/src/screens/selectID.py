from PyQt5 import uic
from PyQt5.QtWidgets import *


class selectID(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        uic.loadUi(self.parent().resource_path("src\\uis\\CREATE-ID.ui"), self)
        self.DRIVERSLICENSE.clicked.connect(self.selectDriversLicense)

    def selectDriversLicense(self):
        widget = self.parent().widget(4)
        widget.clear()
        self.parent().setCurrentWidget(widget)
