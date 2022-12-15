import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QStackedWidget, QApplication

from src.database import database
from src.screens.selectID import selectID
from src.screens.login import login
from src.screens.signup import signup
from src.screens.home import home
from src.screens.IDTypes import DriverLicense

from src.uis import IMAGES_rc


class IdentifierApp(QStackedWidget, database):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setWindowIcon(QtGui.QIcon(self.resource_path("src\\uis\\logo.ico")))
        self.setWindowTitle("ID-entifier")
        self.resize(364, 643)
        self.setupUi()

    def setupUi(self):
        loginWidget = login(self)
        signupWidget = signup(self)
        homeWidget = home(self)
        createIDWidget = selectID(self)
        driverLicenseWidget = DriverLicense(self)

        self.addWidget(loginWidget)
        self.addWidget(signupWidget)
        self.addWidget(homeWidget)
        self.addWidget(createIDWidget)
        self.addWidget(driverLicenseWidget)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


def main():
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)

    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    window = IdentifierApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
