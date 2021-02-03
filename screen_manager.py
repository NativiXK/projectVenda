from screens.login import Login
from screens.register import Register
from screens.entry import Entry
from screens.product import Products, RegisterProduct, ModifyProduct, RemoveProduct, SearchProduct
from session import Session
import tkinter as tk

class Manager:

    def __init__(self, master, resolution, relx, rely):
        self.__master = master
        self.__session = None
        self.__curent_screen = ""
        self.__previous_screen = ""
        self.__string_vars = {}
        self.__current_popupScreen = ""
        """ size = %W x %H """
        self.__screens = {
            "login" : Login(self, master, "0.2x0.3"),
            "register" : Register(self, master, "0.3x0.47"),
            "entry" : Entry(self, master, "0.9x0.9"),
            "popup" : {
                "products" : Products(self, "0.2x0.35"),
                "registerProduct" : RegisterProduct(self, "0.3x0.45"),
                "modifyProduct" : ModifyProduct(self, "0.3x0.45"),
                "removeProduct" : RemoveProduct(self, "0.3x0.45"),
                "searchProduct" : SearchProduct(self, "0.3x0.45"),
                # "Employees" : Employees(self, "400x400")
                }
            }

        self.__geometries = self.__generate_geometries(resolution, relx, rely)

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
            self.__screens[name].show()
            self.master.geometry(self.__geometries[name])
            self.__curent_screen = name

    @property
    def popupScreen(self):
        return self.__screens["popup"][self.__current_popupScreen]

    @popupScreen.setter
    def popupScreen(self, name):

        if self.__current_popupScreen != "":
            self.__screens["popup"][self.__current_popupScreen].destroy()

        if name in self.__screens["popup"]:
            self.__screens["popup"][name].inicialize(self.__geometries["popup"][name])
            self.__current_popupScreen = name

    @property
    def previous(self):
        return self.__previous_screen
    """ 
    A function that takes the resolution of the screen and the ratio of X and Y
    to generate the geometries for the screens
    """
    def __generate_geometries(self, resolution, relx, rely):
        geometries = {}
        for screen in self.__screens:
            if screen == "popup":
                popups = {}
                for screen in self.__screens["popup"]:
                    size = self.__screens["popup"][screen].size
                    screen_res = int(resolution[0] * float(size.split("x")[0])), int(resolution[1] * float(size.split("x")[1]))
                    posx = str(int(resolution[0] * relx - (screen_res[0] / 2)))
                    posy = str(int(resolution[1] * rely - (screen_res[1] / 2)))
                        
                    popups[screen] = "{}x{}+{}+{}".format(screen_res[0], screen_res[1], posx, posy)
                geometries["popup"] = popups
            else:
                size = self.__screens[screen].size
                screen_res = int(resolution[0] * float(size.split("x")[0])), int(resolution[1] * float(size.split("x")[1]))
                
                posx = str(int(resolution[0] * relx - (screen_res[0] / 2)))
                posy = str(int(resolution[1] * rely - (screen_res[1] / 2)))

                geometries[screen] = "{}x{}+{}+{}".format(screen_res[0], screen_res[1], posx, posy)
        return geometries

    """
    Clear the previous screen
    """
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


    