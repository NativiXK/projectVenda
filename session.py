from person import User, Employee
from tkinter.messagebox import showwarning, showinfo
from dbConnector import Connector

class Session:

    def __init__ (self, manager):
        self.__manager = manager
        self.__db = None
        self.__user = None
        self.startup()
        
    @property
    def manager (self):
        return self.__manager
    
    @property
    def user (self):
        return self.__user

    @property
    def db (self):
        return self.__db

    def startup (self):
        self.__db = Connector()
        self.__manager.session = self
    # gives the application a user session
    def give_session (self, user):
        self.__user = user
        self.manager.screen = "entry"
    
    def makeLogin (self, username, password):
        if username == "" or password == "":
            showwarning("LOGIN", "Please fill all the fields to login")
            return

        self.db.query(""" SELECT * FROM USER WHERE email='{}' OR password='{}' """.format(username, password))
        results = self.db.cursor.fetchall()

        if results != []:
            for result in results:
                dbUsername, dbPassword = (result[2], result[4])
                if username == dbUsername:
                    if password == dbPassword:
                        # create a user session
                        # (index, fullname, username, email, password)
                        user = {
                            "fullname" : result[1],
                            "username" : result[2],
                            "email" : result[3],
                        }

                        self.give_session(user)
                    else:
                        showwarning("LOGIN", "Wrong password")
                else:
                    showwarning("LOGIN", "User not found")
        else:
            showwarning("LOGIN", "User not found")

    def makeRegister (self, user):
        self.db.query(""" SELECT * FROM USER WHERE email='{}' OR username='{}' """.format(user["email"], user["username"]))
        results = self.db.cursor.fetchall()

        if results == []:
            user = (user["fullname"], user["username"], user["email"], user["password"])
            self.db.query(""" INSERT INTO USER (fullname, username, email, password) values(?, ?, ?, ?) """, user)
            self.db.commit()
            showinfo("Register", message="Registered successfully")
            self.manager.screen = 'login'
        else:
            showwarning("Error", "User already registered")

    def addProduct (self):
        print(self.manager.screen.EntryProductID.get())
        