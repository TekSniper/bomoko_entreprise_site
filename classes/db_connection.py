import mysql.connector

class Db_Connection:
    def __init__(self):
        self.connectionString = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bomoko"
        )
    
    def GetConnectionString(self):
        return self.connectionString