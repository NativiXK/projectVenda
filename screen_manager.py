from screens.login import Login
from screens.register import Register
from screens.entry import Entry
from tkinter.messagebox import showwarning
from dbConnector import Connector
from session import Session

class Manager:

    def __init__(self, master, resolution, relx, rely):
        self.__master = master
        self.__db = Connector()
        self.__curent_screen = ""
        self.__previous_screen = ""
        
        self.__screens = {
            "login" : Login(self, master, "300x250"),
            "register" : Register(self, master, "400x450"),
            "entry" : Entry(self, master, "1200x800")
            }

        self.__geometries = self.__generate_geometries(resolution, relx, rely)
        self.__user_session = Session(self)

    @property
    def master(self):
        return self.__master

    @property
    def screen(self):
        return self.__curent_screen

    @screen.setter
    def screen(self, name):

        if self.__curent_screen != "":
            self.__previous_screen = self.screen
            self.__screens[self.screen].hide()

        if name in self.__screens:
            self.__screens[name].show(self.__geometries[name])
            self.__curent_screen = name

    @property
    def previous(self):
        return self.__previous_screen

    @property
    def db(self):
        return self.__db

    def __generate_geometries(self, resolution, relx, rely):
        geometries = {}
        for screen in self.__screens:
            size = self.__screens[screen].size
            screen_res = int(size.split("x")[0]), int(size.split("x")[1])
            posx = str(int(resolution[0] * relx - (screen_res[0] / 2)))
            posy = str(int(resolution[1] * rely - (screen_res[1] / 2)))

            geometries[screen] = "{}+{}+{}".format(size, posx, posy)
        return geometries

    def clear_previous(self):
        self.__previous_screen = ""

    def inicialize(self, app_name):
        self.screen = "login"
        self.master.title(app_name)
        self.master.mainloop()

    def btnBack(self):
        self.screen = self.previous

    def exit(self):
        self.master.destroy()

    def btnRegister(self):
        self.screen = "register"

    def makeLogin(self, username, password):
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
                        self.screen = "entry"
                        self.__user_session.create_session(result)
                    else:
                        showwarning("LOGIN", "Wrong password")
                else:
                    showwarning("LOGIN", "User not found")
        else:
            showwarning("LOGIN", "User not found")

    def makeRegister(self, user):
        self.db.query(""" SELECT * FROM USER WHERE email='{}' OR username='{}' """.format(user["email"], user["username"]))
        results = self.db.cursor.fetchall()

        if results == []:
            user = (user["fullname"], user["username"], user["email"], user["password"])
            self.db.query(""" INSERT INTO USER (fullname, username, email, password) values(?, ?, ?, ?) """, user)
            self.db.commit()
            self.screen = 'login'
        else:
            showwarning("Error", "User already registered")
