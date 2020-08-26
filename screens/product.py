from screens.screen import Screen
import tkinter as tk

class RegisterProduct:

    def __init__ (self, controls, size):
        self.__size = size
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    @property
    def size(self):
        return self.__size

    def destroy(self):
        self.__toplevel.destroy()

    def inicialize(self, geometry):
        self.__toplevel = tk.Tk()
        self.__toplevel.geometry(geometry)
        self.__toplevel.title("Products control")

class ModifyProduct (Screen):

    def __init__ (self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):
        pass

class RemoveProduct (Screen):

    def __init__ (self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):
        pass

class SearchProduct (Screen):

    def __init__ (self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls
    
    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):
        pass