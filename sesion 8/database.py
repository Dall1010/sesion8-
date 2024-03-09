import mysql.connector
import os

class MYSQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database
        self.connection = None

    def connection(self):
        try :
            if(self.connection == None):
                self.connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.pw,
                    database = self.db
                )
                os.system("color a2")
                print("la coneccion ha sido completada")   
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando9 {}". format(error))

    def disconnect(self):
        try: 
            if self.connection:
               self.connection.close
               self.connection = None
        except mysql.connector.Error as error:
            print("Error")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")

db = MYSQLDB("localhost", "root", "", "dbtesttlp")
print("conectado")


db.connect()
categorias = db.execute_query("select * drom categorias")
for reg in categorias:
    print(reg)
#db.disconnect()


