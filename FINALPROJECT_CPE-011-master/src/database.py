import sqlite3


class database:
    def __init__(self):
        self.__db = sqlite3.connect('identifier.db')
        print("Creating db...")
        cursor = self.__db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (userID INTEGER PRIMARY KEY,
               username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                CONSTRAINT UC_Email UNIQUE (email),
                CONSTRAINT UC_Username UNIQUE (username));""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS ids(
        userID INT NOT NULL,
        IdType VARCHAR(64) NOT NULL,
        IdNumber VARCHAR(64) NOT NULL,
        age INT NOT NULL,
        birthdate DATE NOT NULL,
        address VARCHAR(255) NOT NULL,
        phoneNum INT NOT NULL,
        image BLOB,
        FOREIGN KEY(userID) REFERENCES users(userID));""")
        self.__db.commit()

    def createUser(self, username, password, email):
        cursor = self.__db.cursor()
        try:
            cursor.execute("""INSERT INTO users(username,password,email)
            VALUES (?, ?, ?);""",
                           [username, password, email])
            self.__db.commit()
        except sqlite3.IntegrityError as er:
            error = er.args[0][-5:]
            print(error)
            if error == 'email':
                return 'email'
            else:
                return 'username'
        return None

    def loginUser(self, username, password) -> bool:
        cursor = self.__db.cursor()
        cursor.execute("""
        SELECT * FROM users WHERE username=? AND password=?""",
                       [username, password])

        if cursor.fetchone() is None:
            return False
        return True

    def loadIDs(self, userID):
        cursor = self.__db.cursor()
        cursor.execute("""SELECT * FROM ids WHERE userID=?""", [userID])
        return cursor.fetchall()

    def createID(self, userID, id_type, id_number, gender, age, birthdate, address, phone_number, image=""):
        cursor = self.__db.cursor()
        cursor.execute("""INSERT INTO ids(userID, IdType, IdNumber, age, birthdate, address, phoneNum, image)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);""",
                       [userID, id_type, id_number, age, birthdate, address, phone_number, image])
        self.__db.commit()

    def updateID(self, userID, id_type, id_number, gender, age, birthdate, address, phone_number, image=""):
        cursor = self.__db.cursor()
        cursor.execute("""UPDATE ids SET age=?, birthdate=?, address=?, phoneNum=?, image=?
        WHERE userID=? AND IdType=? AND IdNumber=?;""",
                       [age, birthdate, address, phone_number, image, userID, id_type, id_number])
        self.__db.commit()

    def deleteID(self, data):
        cursor = self.__db.cursor()
        cursor.execute("""DELETE FROM ids WHERE userID=? AND IdType=? AND IdNumber=?
        AND age=? AND birthdate=? AND address=? AND phoneNum=? AND image=?;""",
                       [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]])
        self.__db.commit()
        return True

    def close(self):
        print("closing db...")
        self.__db.close()
