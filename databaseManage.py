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
            self.cursor = self.connection.cursor(buffered=True)
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

    def getWhichUsersByShoppingID(self, shoppingID):
        sql = f"SELECT * FROM whichusers WHERE shoppingID={shoppingID}"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print(err)

    def getWhoPayedByTempUserIDandShoppingID(self, tempUserID, shoppingID):
        sql = f"SELECT * FROM whopayed WHERE tempUserID={tempUserID} AND shoppingID={shoppingID}"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except Exception as err:
            print(err)

    def addWhichUsersEntry(self, tempUserID, shoppingID):
        sql = f"INSERT INTO whichusers(tempUserID,shoppingID) VALUES({tempUserID},{shoppingID})"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def addWhoPayedEntry(self, tempUserID, shoppingID, payedValue):
        sql = f"INSERT INTO whopayed(tempUserID,shoppingID,payedValue) VALUES({tempUserID},{shoppingID},{payedValue})"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(err)

    def addShopping(self, shoppingName, shoppingCost, shoppingDate, userID, whichTempUserPaidHowMuch):
        sql = f"INSERT INTO shoppings(shoppingName,shoppingCost,shoppingDate,userID) VALUES('{shoppingName}',{shoppingCost},'{shoppingDate}',{userID})"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.execute("SELECT LAST_INSERT_ID() FROM shoppings")
            lastShoppingID = self.cursor.fetchone()[0]
            for tempUserID in whichTempUserPaidHowMuch.keys():
                self.addWhichUsersEntry(tempUserID, lastShoppingID)
                self.addWhoPayedEntry(tempUserID, lastShoppingID, whichTempUserPaidHowMuch[tempUserID])
        except Exception as err:
            print(err)

    def deleteShoppingByShoppingID(self, shoppingID):
        sql1 = f"DELETE FROM whopayed WHERE shoppingID={shoppingID}"
        sql2 = f"DELETE FROM whichusers WHERE shoppingID={shoppingID}"
        sql3 = f"DELETE FROM shoppings WHERE shoppingID={shoppingID}"
        try:
            self.cursor.execute(sql1)
            self.connection.commit()
            self.cursor.execute(sql2)
            self.connection.commit()
            self.cursor.execute(sql3)
            self.connection.commit()
        except Exception as err:
            print("hata", err)

    def checkIsUserRelatedAnyShoppingByTempUserID(self, tempUserID):
        sql = f"SELECT COUNT(*) FROM whichusers WHERE tempUserID={tempUserID}"
        try:
            self.cursor.execute(sql)
            return int(self.cursor.fetchone()[0])
        except Exception as err:
            print(err)

    def calculateDebtsByUserID(self, userID):
        sql = f"SELECT shoppingID FROM shoppings WHERE userID={userID}"
        debtDict = {}
        try:
            self.cursor.execute(sql)
            shoppingIDs = self.cursor.fetchall()
            for shoppingID in shoppingIDs:
                self.cursor.execute(f"SELECT tempUserID FROM whichusers WHERE shoppingID={shoppingID[0]}")
                userIDs = self.cursor.fetchall()
                self.cursor.execute(f"SELECT shoppingCost FROM shoppings WHERE shoppingID={shoppingID[0]}")
                shoppingTotalCost = float(self.cursor.fetchone()[0])
                debtDict[str(shoppingID[0])] = []
                debtDict[str(shoppingID[0])].append(shoppingTotalCost)
                for tempUserID in userIDs:
                    self.cursor.execute(f"SELECT payedValue FROM whopayed WHERE tempUserID={tempUserID[0]} AND shoppingID={shoppingID[0]}")
                    paidValue = self.cursor.fetchone()[0]
                    debtDict[str(shoppingID[0])].append((str(tempUserID[0]), paidValue))
            debtors_to_payes = {}
            for debtKey in debtDict.keys():
                debtors = {}
                payees = {}
                relatedPersonNum = len(debtDict[debtKey][1:])
                costPerPerson = debtDict[debtKey][0]/relatedPersonNum
                for i in debtDict[debtKey][1:]:
                    if i[1] < costPerPerson:
                        debtors.setdefault(i[0], 0)
                        debtors[i[0]] += costPerPerson - i[1]
                    elif i[1] > costPerPerson:
                        payees.setdefault(i[0], 0)
                        payees[i[0]] += i[1] - costPerPerson
                for debtorKey in list(debtors.keys()):
                    while True:
                        if debtors[debtorKey] == payees[list(payees.keys())[0]]:
                            debtors_to_payes.setdefault(f"{debtorKey},{list(payees.keys())[0]}", 0)
                            debtors_to_payes[f"{debtorKey},{list(payees.keys())[0]}"] += debtors[debtorKey]
                            payees.pop(list(payees.keys())[0])
                            debtors.pop(debtorKey)
                            break
                        elif debtors[debtorKey] < payees[list(payees.keys())[0]]:
                            debtors_to_payes.setdefault(f"{debtorKey},{list(payees.keys())[0]}", 0)
                            debtors_to_payes[f"{debtorKey},{list(payees.keys())[0]}"] += debtors[debtorKey]
                            payees[list(payees.keys())[0]] -= debtors[debtorKey]
                            debtors.pop(debtorKey)
                            break
                        elif debtors[debtorKey] > payees[list(payees.keys())[0]]:
                            debtors_to_payes.setdefault(f"{debtorKey},{list(payees.keys())[0]}", 0)
                            debtors_to_payes[f"{debtorKey},{list(payees.keys())[0]}"] += payees[list(payees.keys())[0]]
                            debtors[debtorKey] -= payees[list(payees.keys())[0]]
                            payees.pop(list(payees.keys())[0])
                            continue
            sql = f"DELETE FROM debts WHERE userID={userID}"
            self.cursor.execute(sql)
            self.connection.commit()
            for key in list(debtors_to_payes.keys()):
                tempUser1ID, tempUser2ID = key.split(",")
                sql = f"INSERT INTO debts(tempUser1ID,tempUser2ID,debt,userID) VALUES({tempUser1ID},{tempUser2ID},{debtors_to_payes[key]},{userID})"
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception as err:
            print(err)


    def getDebtsForTableByUserID(self, userID):
        sql = f"SELECT debts.debtID, debts.tempUser1ID, debts.tempUser2ID, debts.debt, debts.userID FROM tempusers JOIN debts ON debts.tempUser1ID=tempusers.tempUserID WHERE debts.userID={userID}"
        try:
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()
            result = []
            for data in datas:
                data = list(data)
                data.insert(3, self.getRelatedPersonByTempUserID(data[1], "username")[0])
                data.insert(4, self.getRelatedPersonByTempUserID(data[2], "username")[0])
                result.append(data)
            return result
        except Exception as err:
            print(err)