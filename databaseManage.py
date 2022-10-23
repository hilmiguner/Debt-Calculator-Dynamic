from mysql import connector

class database:
    def __init__(self):
        try:
            self.connection = connector.connect(
                host="95.70.196.173",
                user="user1",
                password="mysql1234",
                database="debt-calculator"
            )
            self.cursor = self.connection.cursor()
        except Exception as err:
            print(err)

    def __del__(self):
        self.connection.disconnect()

    def checkLogin(self, name, password):
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM users WHERE username='{name}' and password='{password}'")
            if self.cursor.fetchone()[0] == 1:
                self.cursor.execute(f"SELECT userID FROM users WHERE username='{name}' and password='{password}'")
                ID = self.cursor.fetchone()[0]
                return True, ID
        except Exception as err:
            print(err)
        return False

    def canUserRegister(self, name):
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM users WHERE username='{name}'")
            if self.cursor.fetchone()[0] == 0:
                return True
        except Exception as err:
            print(err)
        return False

    def addUser(self, username, password):
        try:
            self.cursor.execute(f"INSERT INTO users(username,password) VALUES ('{username}','{password}')")
            self.connection.commit()

            self.cursor.execute(f"SELECT userID FROM users WHERE username='{username}'")
            userID = self.cursor.fetchone()[0]

            self.cursor.execute(f"INSERT INTO tempusers(userID, username) VALUES ({userID},'{username}')")
            self.connection.commit()
            return userID
        except Exception as err:
            print(err)
        return -1

    def getUserInfo(self, userID, *args):
        sql = f"SELECT {','.join(args)} FROM users WHERE userID={userID}"
        try:
            self.cursor.execute(sql)
            info = self.cursor.fetchone()
            return info
        except Exception as err:
            print(err)
        return -1

    def checkPassword(self, userID, password):
        sql = f"SELECT COUNT(*) FROM users WHERE userID={userID} and password='{password}'"
        try:
            self.cursor.execute(sql)
            if self.cursor.fetchone()[0] == 1:
                return True
        except Exception as err:
            print(err)
        return False

    def changePassword(self, userID, newPassword):
        sql = f"UPDATE users SET password='{newPassword}' WHERE userID={userID}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def getRelatedPerson(self, userID, *args):
        sql = f"SELECT {','.join(args)} FROM tempUsers WHERE userID={userID}"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print(err)
        return -1

    def getRelatedPersonByTempUserID(self, tempUserID, *args):
        sql = f"SELECT {','.join(args)} FROM tempUsers WHERE tempUserID={tempUserID}"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except Exception as err:
            print(err)
        return -1

    def addTempUser(self, userID, tempUserName):
        sql = f"INSERT INTO tempusers(userID, username) VALUES ({userID},'{tempUserName}')"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def deleteTempUser(self, tempUserID):
        sql = f"DELETE FROM tempUsers WHERE tempUserID={tempUserID}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def changeTempUsername(self, tempUserID, newName):
        sql = f"UPDATE tempUsers SET username='{newName}' WHERE tempUserID={tempUserID}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def getInfoForShoppingUI(self, userID):
        sql = f"SELECT * FROM shoppings WHERE userID={userID}"
        try:
            self.cursor.execute(sql)
            shoppings = self.cursor.fetchall()
            shopDict = {}

            for data in shoppings:
                shoppingID = str(data[0])

                sql = f"SELECT tempUserID FROM whichusers WHERE shoppingID={shoppingID}"
                self.cursor.execute(sql)
                for tempUser in self.cursor.fetchall():
                    tempUserID = str(tempUser[0])
                    paid = "0"

                    sql = f"SELECT payedValue FROM whopayed WHERE tempUserID={tempUserID} and shoppingID={shoppingID}"
                    self.cursor.execute(sql)
                    paid = str(self.cursor.fetchone()[0])

                    shopDict.setdefault(shoppingID, []).append((tempUserID, paid))
            return shoppings, shopDict
        except Exception as err:
            print(err)
        return -1, -1

    def getShoppingByShoppingID(self, shoppingID):
        sql = f"SELECT * FROM shoppings WHERE shoppingID={shoppingID}"
        try:
            self.cursor.execute(sql)
            shopping = self.cursor.fetchone()

            sql = f"SELECT tempUserID FROM whichusers WHERE shoppingID={shoppingID}"
            self.cursor.execute(sql)
            relatedPersons = self.cursor.fetchall()

            shoppingDict = {}

            for data in relatedPersons:
                relatedPersonID = data[0]
                sql = f"SELECT payedValue FROM whopayed WHERE shoppingID={shoppingID} and tempUserID={relatedPersonID}"
                self.cursor.execute(sql)
                paid = self.cursor.fetchone()[0]

                shoppingDict[str(relatedPersonID)] = str(paid)

            return shopping, shoppingDict
        except Exception as err:
            print(err)
        return -1, -1