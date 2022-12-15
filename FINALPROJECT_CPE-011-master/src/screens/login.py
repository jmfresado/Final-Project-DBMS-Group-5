from PyQt5 import uic
from PyQt5.QtWidgets import *


class login(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        uic.loadUi(self.parent().resource_path("src\\uis\\ID-entifier-Home.ui"), self)
        self.MSIGNUP.clicked.connect(self.signup)
        self.MLOGIN.clicked.connect(self.login)

    def signup(self):
        widget = self.parent().widget(1)
        self.parent().setCurrentWidget(widget)
        self.clearParameters()

    def login(self):
        username = self.MUsernamelineEdit.text()
        password = self.MPasswordlineEdit_2.text()

        if username == "" and password == "":
            self.MLabel.setText("Fill up missing blanks.")
            return

        if self.parent().loginUser(username, password):
            widget = self.parent().widget(2)
            self.parent().setCurrentWidget(widget)
            widget.setLoggedInUserID(username)
            self.clearParameters()
            return

        self.MLabel.setText("username or password doesn't exists!")

    def clearParameters(self):
        self.MUsernamelineEdit.setText("")
        self.MPasswordlineEdit_2.setText("")
        self.MLabel.setText("")
