from screens.screen import Screen
import tkinter as tk

class Products :

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
        try:
            self.__master.destroy()
        except:
            return

    def btnRegisterProduct(self):
        self.controls.popupScreen = "registerProduct"
    
    def btnModifyProduct(self):
        self.controls.popupScreen = "modifyProduct"

    def btnRemoveProduct(self):
        self.controls.popupScreen = "removeProduct"

    def btnSearchProduct(self):
        self.controls.popupScreen = "searchProduct"

    def inicialize (self, geometry):
        self.__master = tk.Tk()
        self.__master.geometry(geometry)
        self.__master.title("Products control")
        self.__master.resizable(0, 0)

        self.topFrame = tk.Frame(self.__master)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")
        # register product button
        self.regProdButton = tk.Button(self.topFrame)
        self.regProdButton.place(relx=0.004, rely=0.004, relheight=0.24, relwidth=0.989)
        self.regProdButton.configure(background="WHITE")
        self.regProdButton.configure(foreground="BLACK")
        self.regProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.regProdButton.configure(relief="flat")
        self.regProdButton.configure(text='''REGISTER''')
        self.regProdButton.configure(command = self.btnRegisterProduct)
        # modify product button
        self.modProdButton = tk.Button(self.topFrame)
        self.modProdButton.place(relx=0.004, rely=0.0045 +0.25, relheight=0.24, relwidth=0.989)
        self.modProdButton.configure(background="WHITE")
        self.modProdButton.configure(foreground="BLACK")
        self.modProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.modProdButton.configure(relief="flat")
        self.modProdButton.configure(text='''MODIFY''')
        self.modProdButton.configure(command = self.btnModifyProduct)
        # remove product button
        self.remProdButton = tk.Button(self.topFrame)
        self.remProdButton.place(relx=0.004, rely=0.0055 +0.5, relheight=0.24, relwidth=0.989)
        self.remProdButton.configure(background="WHITE")
        self.remProdButton.configure(foreground="BLACK")
        self.remProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.remProdButton.configure(relief="flat")
        self.remProdButton.configure(text='''REMOVE''')
        self.remProdButton.configure(command = self.btnRemoveProduct)
        # search product button
        self.schProdButton = tk.Button(self.topFrame)
        self.schProdButton.place(relx=0.004, rely=0.0065 +0.75, relheight=0.24, relwidth=0.989)
        self.schProdButton.configure(background="WHITE")
        self.schProdButton.configure(foreground="BLACK")
        self.schProdButton.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.schProdButton.configure(relief="flat")
        self.schProdButton.configure(text='''SEARCH''')
        self.schProdButton.configure(command = self.btnSearchProduct)

class RegisterProduct:

    def __init__ (self, controls, size):
        self.__size = size
        self.__controls = controls
        self.__master = None

    @property
    def controls(self):
        return self.__controls

    @property
    def size(self):
        return self.__size

    def destroy(self):
        try:
            self.__master.destroy()
        except:
            return

    def inicialize(self, geometry):
        self.__master = tk.Tk()
        self.__master.geometry(geometry)
        self.__master.title("Adding products")
        self.__master.resizable(0, 0)

        self.topFrame = tk.Frame(self.__master)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")

         # screen design beyond here

class ModifyProduct:

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
        try:
            self.__master.destroy()
        except:
            return

    def inicialize(self, geometry):
        self.__master = tk.Tk()
        self.__master.geometry(geometry)
        self.__master.title("Adding products")
        self.__master.resizable(0, 0)

        self.topFrame = tk.Frame(self.__master)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")

         # screen design beyond here

class RemoveProduct:

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
        try:
            self.__master.destroy()
        except:
            return

    def inicialize(self, geometry):
        self.__master = tk.Tk()
        self.__master.geometry(geometry)
        self.__master.title("Adding products")
        self.__master.resizable(0, 0)

        self.topFrame = tk.Frame(self.__master)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")

         # screen design beyond here

class SearchProduct:

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
        try:
            self.__master.destroy()
        except:
            return

    def inicialize(self, geometry):
        self.__master = tk.Tk()
        self.__master.geometry(geometry)
        self.__master.title("Adding products")
        self.__master.resizable(0, 0)

        self.topFrame = tk.Frame(self.__master)
        self.topFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.topFrame.configure(background="#28a4ff")

        # screen design beyond here