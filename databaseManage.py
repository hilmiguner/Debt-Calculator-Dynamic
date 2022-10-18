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
        except Exception as err:
            print(err)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.disconnect()
