import tkinter as tk

class Screen (tk.Frame):

    def __init__(self, master, size):
        super().__init__(master)
        self.__master = master
        self.__size = size
        # stores all dynamic variables 
        self.__vars = {}

    #returns all keys to all created variables in te screen
    @property
    def get_vars (self):
        # print(self.__vars)
        return self.__vars.keys
    # return the instance of a variable by its key
    def get_var(self, key):
        return self.__vars[key]
    # save a new variable in the screen
    def add_var (self, key, var):
        self.__vars[key] = var

    @property
    def size(self):
        return self.__size

    def show(self, geometry):
        self.__master.geometry(geometry)
        self.__master.resizable(0, 0)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        #side="top", fill="both"

    def hide(self):
        self.place_forget()
