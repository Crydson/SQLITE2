import sqlite3 as sql


class Database:
    def __init__(self):

        pass


    @classmethod
    def connection():
        try:
            conn = sql.connect("Segundo_Database.db")
            return conn
        except:
            print("Falha ao conectar")
            return None


    #return conn
