from screens.login import Login
from screens.register import Register
from screens.entry import Entry
from session import Session

class Manager:

    def __init__(self, master, resolution, relx, rely):
        self.__master = master
        self.__session = None
        self.__curent_screen = ""
        self.__previous_screen = ""
        self.__string_vars = {}
        
        self.__screens = {
            "login" : Login(self, master, "300x250"),
            "register" : Register(self, master, "400x450"),
            "entry" : Entry(self, master, "1200x800")
            }

        self.__geometries = self.__generate_geometries(resolution, relx, rely)
        self.__user_session = Session(self)

    @property
    def session (self):
        return self.__session

    @session.setter
    def session (self, session):
        self.__session = session

    @property
    def master(self):
        return self.__master
    # returns the actual screen object
    @property
    def screen(self):
        return self.__screens[self.__curent_screen]
    # load a screen by its name
    @screen.setter
    def screen(self, name):

        if self.__curent_screen != "":
            self.__previous_screen = self.__curent_screen
            self.__screens[self.__curent_screen].hide()

        if name in self.__screens:
            self.__screens[name].inicialize(self.master)
            self.__screens[name].show(self.__geometries[name])
            self.__curent_screen = name

    @property
    def previous(self):
        return self.__previous_screen

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
