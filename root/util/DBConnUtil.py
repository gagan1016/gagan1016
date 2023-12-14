import mysql.connector as sql
from root.util.DBPropertyUtil import DBConnUtil

class DBconnection:
    @staticmethod
    def get_connection():
        connection_string= DBConnUtil.get_property_strig()
        try:
             connection=mysql.connector.connect(connection_string)
             print("connected to the database!")
        except mysql.connector.Error as e:
            print("Failed to connect to the database: ", e)
        return DBconnection.connection