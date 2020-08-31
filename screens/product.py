from screens.screen import Screen
import tkinter as tk

class Products (Screen):

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
        self.__topLevel.destroy()

    def btnRegister(self):
        self.controls.screen = "registerProduct"

    def inicialize (self, geometry):
        self.__topLevel = tk.Tk()
        self.__topLevel.geometry(geometry)
        self.__topLevel.title("Products control")
        self.__topLevel.resizable(0, 0)

        self.topFrame = tk.Frame(self.__topLevel)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")
        # register product button
        self.regProdButton = tk.Button(self.topFrame)
        self.regProdButton.configure(background="WHITE")
        self.regProdButton.configure(foreground="BLACK")
        self.regProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.regProdButton.configure(relief="flat")
        self.regProdButton.configure(text='''REGISTER''')
        self.regProdButton.place(relx=0.004, rely=0.004, relheight=0.246, relwidth=0.995)
        # modify product button
        self.modProdButton = tk.Button(self.topFrame)
        self.modProdButton.configure(background="WHITE")
        self.modProdButton.configure(foreground="BLACK")
        self.modProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.modProdButton.configure(relief="flat")
        self.modProdButton.configure(text='''MODIFY''')
        self.modProdButton.place(relx=0.004, rely=0.004, relheight=0.246, relwidth=0.995)

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
        self.__topLevel.destroy()

    def inicialize(self, geometry):
        self.__topLevel = tk.Tk()
        self.__topLevel.geometry(geometry)
        self.__topLevel.title("Products control")
        self.__topLevel.resizable(0, 0)

        self.top_frame = tk.Frame(self.__topLevel)
        self.top_frame.configure(background="#28a4ff")

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