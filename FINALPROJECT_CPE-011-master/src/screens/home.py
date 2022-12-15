from PyQt5 import uic, QtPrintSupport, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class home(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.__userID = ""
        self.__ids = []
        uic.loadUi(self.parent().resource_path("src\\uis\\ID-entifier.ui"), self)
        self.CREATEID.clicked.connect(self.createID)
        self.UPDATEID.clicked.connect(self.updateID)
        self.DELETEID.clicked.connect(self.deleteID)
        self.PRINTID.clicked.connect(self.printID)

    def createID(self):
        widget = self.parent().widget(3)
        self.parent().setCurrentWidget(widget)

    def updateID(self):
        data = self.DELETEcomboBox.itemData(self.DELETEcomboBox.currentIndex())
        widget = self.parent().widget(4)
        widget.prepareEditID(data)
        self.parent().setCurrentWidget(widget)

    def deleteID(self):
        data = self.DELETEcomboBox.itemData(self.DELETEcomboBox.currentIndex())
        if self.parent().deleteID(data):
            self.refreshIDsFromUserID()

    def printID(self):
        data = self.DELETEcomboBox.itemData(self.DELETEcomboBox.currentIndex())
        pix = QPixmap()
        if pix.loadFromData(data[7]):
            printer = QtPrintSupport.QPrinter()
            # Create painter
            painter = QtGui.QPainter()
            # Start painter
            painter.begin(printer)
            painter.drawPixmap(pix.rect(), pix)
            painter.end()

    def getLoggedInUserID(self):
        return self.__userID

    def setLoggedInUserID(self, userID):
        self.__userID = userID
        self.refreshIDsFromUserID()

    def refreshIDsFromUserID(self):
        print("loading ids...")
        self.__ids = self.parent().loadIDs(self.__userID)
        self.DELETEcomboBox: QComboBox
        self.DELETEcomboBox.clear()
        for id_info in self.__ids:
            self.DELETEcomboBox.addItem(id_info[1], id_info)

        print(self.__ids)
