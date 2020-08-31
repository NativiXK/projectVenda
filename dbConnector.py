import sqlite3 as db

class Connector:

    def __init__(self):
        self.__db = db.connect("database.db")
        self.__cursor = self.db.cursor()
        if not self.tablesExists():
            self.create_tables()

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
        self.query("""SELECT count(name) 
            FROM sqlite_master 
            WHERE type='table' 
            AND name= 'users'
            OR name= 'products'
            OR name= 'employees'
            OR name= 'costumers'
            """)
        result = self.cursor.fetchone()

        if result[0] == 4:
            return True
        else:
            return False

    def create_tables(self):
        self.query("""
        pragma foreign_keys = ON;

        CREATE TABLE users (
            user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );

        CREATE TABLE products (
            product_id VARCHAR(50) PRIMARY KEY NOT NULL,
            description TEXT NOT NULL,
            price DOUBLE NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        );

        CREATE TABLE employees (
            employee_id VARCHAR(50) PRIMARY KEY NOT NULL,
            fullname TEXT NOT NULL,
            emp_role INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        );


        """)

    def get_product(self, user_id, prod_id):
        self.query("SELECT * FROM products WHERE user_id = '{}' AND product_id = '{}' ".format(user_id, prod_id))
        results = self.cursor.fetchall()
        if len(results) == 0:
            return []
        else:
            return results