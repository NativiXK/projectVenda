import tkinter as tk

class Screen (tk.Frame):

    def __init__(self, master, size):
        super().__init__(master)
        self.__master = master
        self.__size = size

    @property
    def size(self):
        return self.__size

    def show(self, geometry):
        self.__master.geometry(geometry)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        #side="top", fill="both"
    def hide(self):
        self.place_forget()
