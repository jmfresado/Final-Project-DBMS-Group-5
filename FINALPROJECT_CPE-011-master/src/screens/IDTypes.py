from PyQt5 import uic
from PyQt5.QtCore import QDate, QBuffer, QByteArray
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *


class DriverLicense(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.__type = "Driver's License"
        self.__mode = "CREATE"
        self.__image = ""
        uic.loadUi(self.parent().resource_path("src\\uis\\Drivers-License.ui"), self)
        self.DLSubmit.clicked.connect(self.submit)
        self.DLIMAGE.clicked.connect(self.selectImage)

    def selectImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "PNG Files (*.png);;JPEG Files(*.jpg)", options=options)

        if fileName:
            image = QImage(fileName)
            self.DLIMAGE.setText(fileName.split("/").pop())
            buffer = QBuffer(QByteArray())
            buffer.open(QBuffer.ReadWrite)
            self.__image = image.save(buffer, "PNG")
            buffer.close()
            self.__image = buffer.data()

    def toDate(self, string):
        data = string.split("/")
        print(data)
        QDate()
        return QDate(int(data[2]), int(data[0]), int(data[1]))

    def prepareEditID(self, data):
        self.DLIdNumber.setDisabled(True)

        self.DLIdNumber.setText(str(data[2]))
        self.DLName.setText(str(data[0]))
        self.DLAge.setText(str(data[3]))
        self.DLBirthdate.setDate(self.toDate(data[4]))
        self.DLAddress.setText(str(data[5]))
        self.DLPhonenumber.setText(str(data[6]))
        self.__mode = "UPDATE"

    def submit(self):
        home = self.parent().widget(2)
        userID = home.getLoggedInUserID()
        id_number = self.DLIdNumber.text()
        if self.DLMcheckBox.isChecked():
            gender = 'M'
        else:
            gender = 'F'
        name = self.DLName.text()
        age = self.DLAge.text()
        birthdate = self.DLBirthdate.text()
        address = self.DLAddress.text()
        phoneNum = self.DLPhonenumber.text()
        id_type = self.__type

        if self.__mode == "CREATE":
            self.parent().createID(
                userID,
                id_type,
                id_number,
                gender,
                age,
                birthdate,
                address,
                phoneNum,
                self.__image
            )
        else:
            self.parent().updateID(
                userID,
                id_type,
                id_number,
                gender,
                age,
                birthdate,
                address,
                phoneNum,
                self.__image
            )

        home.refreshIDsFromUserID()
        self.parent().setCurrentWidget(home)
        self.clear()

    def clear(self):
        self.DLIdNumber.setEnabled(True)
        self.DLIdNumber.clear()
        self.DLName.clear()
        self.DLAge.clear()
        self.DLBirthdate.setDate(QDate(2000, 1, 1))
        self.DLAddress.clear()
        self.DLPhonenumber.clear()
        self.DLIMAGE.setText("UPLOAD IMAGE")
        self.__mode = "CREATE"
