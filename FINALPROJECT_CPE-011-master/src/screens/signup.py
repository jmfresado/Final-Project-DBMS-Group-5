from PyQt5 import uic
from PyQt5.QtWidgets import *


class signup(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        uic.loadUi(self.parent().resource_path("src\\uis\\ID-entifier-Reg.ui"), self)
        self.MBACK.clicked.connect(self.goBack)
        self.MREGISTER.clicked.connect(self.register)

    def goBack(self):
        widget = self.parent().widget(0)
        self.parent().setCurrentWidget(widget)
        self.clearParameters()

    def register(self):
        username = self.RUsernamelineEdit.text()
        password = self.RPasswordlineEdit_2.text()
        email = self.RUsernamelineEdit_2.text()

        if username == "" or password == "" or email == "":
            self.RLabel.setText("Fill up missing blanks.")
            return

        result = self.parent().createUser(username, password, email)
        if result is None:
            widget = self.parent().widget(2)
            self.parent().setCurrentWidget(widget)
            widget.setLoggedInUserID(username)
            self.clearParameters()
            return
        elif result == 'email':
            self.RLabel.setText("Email was already taken!")
        else:
            self.RLabel.setText("Username was already taken!")

    def clearParameters(self):
        self.RUsernamelineEdit.setText("")
        self.RPasswordlineEdit_2.setText("")
        self.RUsernamelineEdit_2.setText("")
        self.RLabel.setText("")
