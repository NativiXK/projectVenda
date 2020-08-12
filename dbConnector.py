import sqlite3 as db

class Connector:

    def __init__(self):
        self.__db = db.connect("database.db")
        self.__cursor = self.db.cursor()
        if not self.tablesExists():
            self.createTables()

    @property
    def db(self):
        return self.__db

    @property
    def cursor(self):
        return self.__cursor

    def query(self, command, data = []):
        self.cursor.execute(command, data)

    def commit(self):
        self.db.commit()

    def tablesExists(self):
        self.query("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USER' """)
        result = self.cursor.fetchone()

        if result[0] == 1:
            return True
        else:
            return False

    def createTables(self):
        self.query("""CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            username TEXT,
            email TEXT,
            password TEXT
        );""")
