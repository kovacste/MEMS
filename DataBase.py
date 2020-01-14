import sqlite3
from sqlite3 import Error


class DataBase:

    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        self.connection = self.create_connection()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file_name)
            return conn
        except Error as e:
            print(e)
        return conn

    def insert(self, query, params):
        cur = self.connection.cursor()
        cur.execute(query, params)
        self.connection.commit()
        return cur.lastrowid

    def find_all(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        return cur.fetchall()

    def find_one(self, query):
        return self.find_all(query)[0]

    def close(self):
        self.connection.close()

    def execute(self, query):
        cur = self.connection.cursor()
        cur.execute(query)

    def table_exists(self, tablename):
        cur = self.connection.cursor()
        rows = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + tablename + "';").fetchall()
        return len(rows) > 0
