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
        self.BtnRegistrar = tk.Button(self.topFrame)
        self.BtnRegistrar.place(relx=0.25, rely=0.8, height=44, width=100)
        self.BtnRegistrar.configure(activebackground="#ececec")
        self.BtnRegistrar.configure(activeforeground="#000000")
        self.BtnRegistrar.configure(background="#ffffff")
        self.BtnRegistrar.configure(disabledforeground="#a3a3a3")
        self.BtnRegistrar.configure(foreground="#000000")
        self.BtnRegistrar.configure(highlightbackground="#d9d9d9")
        self.BtnRegistrar.configure(highlightcolor="black")
        self.BtnRegistrar.configure(pady="0")
        self.BtnRegistrar.configure(relief="flat")
        self.BtnRegistrar.configure(text='''Registrar''')

        self.BtnCancelar = tk.Button(self.topFrame)
        self.BtnCancelar.place(relx=0.6, rely=0.8, height=44, width=100)
        self.BtnCancelar.configure(activebackground="#ececec")
        self.BtnCancelar.configure(activeforeground="#000000")
        self.BtnCancelar.configure(background="#ffffff")
        self.BtnCancelar.configure(disabledforeground="#a3a3a3")
        self.BtnCancelar.configure(foreground="#000000")
        self.BtnCancelar.configure(highlightbackground="#ffffff")
        self.BtnCancelar.configure(highlightcolor="#ffffff")
        self.BtnCancelar.configure(pady="0")
        self.BtnCancelar.configure(relief="flat")
        self.BtnCancelar.configure(text='''Cancelar''')

        self.EntryID = tk.Entry(self.topFrame)
        self.EntryID.place(relx=0.18, rely=0.156,height=44, relwidth=0.7)
        self.EntryID.configure(background="white")
        self.EntryID.configure(disabledforeground="#a3a3a3")
        self.EntryID.configure(font="TkFixedFont")
        self.EntryID.configure(foreground="#000000")
        self.EntryID.configure(highlightbackground="#d9d9d9")
        self.EntryID.configure(highlightcolor="black")
        self.EntryID.configure(insertbackground="black")
        self.EntryID.configure(selectbackground="blue")
        self.EntryID.configure(selectforeground="white")

        self.LabelID = tk.Label(self.topFrame)
        self.LabelID.place(relx=0.05, rely=0.169, height=30, width=42)
        self.LabelID.configure(activebackground="#f9f9f9")
        self.LabelID.configure(activeforeground="black")
        self.LabelID.configure(background="#d9d9d9")
        self.LabelID.configure(disabledforeground="#a3a3a3")
        self.LabelID.configure(foreground="#000000")
        self.LabelID.configure(highlightbackground="#d9d9d9")
        self.LabelID.configure(highlightcolor="black")
        self.LabelID.configure(justify='center')
        self.LabelID.configure(text='''ID''')

        self.EntryDescription = tk.Entry(self.topFrame)
        self.EntryDescription.place(relx=0.18, rely=0.292, height=44
                , relwidth=0.7)
        self.EntryDescription.configure(background="white")
        self.EntryDescription.configure(disabledforeground="#a3a3a3")
        self.EntryDescription.configure(font="TkFixedFont")
        self.EntryDescription.configure(foreground="#000000")
        self.EntryDescription.configure(highlightbackground="#d9d9d9")
        self.EntryDescription.configure(highlightcolor="black")
        self.EntryDescription.configure(insertbackground="black")
        self.EntryDescription.configure(selectbackground="blue")
        self.EntryDescription.configure(selectforeground="white")

        self.LabelDescription = tk.Label(self.topFrame)
        self.LabelDescription.place(relx=0.015, rely=0.311, height=26, width=82)
        self.LabelDescription.configure(activebackground="#f9f9f9")
        self.LabelDescription.configure(activeforeground="black")
        self.LabelDescription.configure(background="#d9d9d9")
        self.LabelDescription.configure(disabledforeground="#a3a3a3")
        self.LabelDescription.configure(foreground="#000000")
        self.LabelDescription.configure(highlightbackground="#d9d9d9")
        self.LabelDescription.configure(highlightcolor="black")
        self.LabelDescription.configure(text='''Description''')

        self.EntryPrice = tk.Entry(self.topFrame)
        self.EntryPrice.place(relx=0.433, rely=0.428,height=44, relwidth=0.233)
        self.EntryPrice.configure(background="white")
        self.EntryPrice.configure(disabledforeground="#a3a3a3")
        self.EntryPrice.configure(font="TkFixedFont")
        self.EntryPrice.configure(foreground="#000000")
        self.EntryPrice.configure(highlightbackground="#d9d9d9")
        self.EntryPrice.configure(highlightcolor="black")
        self.EntryPrice.configure(insertbackground="black")
        self.EntryPrice.configure(selectbackground="blue")
        self.EntryPrice.configure(selectforeground="white")

        self.LabelPrice = tk.Label(self.topFrame)
        self.LabelPrice.place(relx=0.283, rely=0.45, height=26, width=53)
        self.LabelPrice.configure(activebackground="#f9f9f9")
        self.LabelPrice.configure(activeforeground="black")
        self.LabelPrice.configure(background="#d9d9d9")
        self.LabelPrice.configure(disabledforeground="#a3a3a3")
        self.LabelPrice.configure(foreground="#000000")
        self.LabelPrice.configure(highlightbackground="#d9d9d9")
        self.LabelPrice.configure(highlightcolor="black")
        self.LabelPrice.configure(text='''Price $''')

        self.Entry1 = tk.Entry(self.topFrame)
        self.Entry1.place(relx=0.4, rely=0.564,height=44, relwidth=0.45)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.BtnImagem = tk.Button(self.topFrame)
        self.BtnImagem.place(relx=0.18, rely=0.565, height=44, width=100)
        self.BtnImagem.configure(activebackground="#ececec")
        self.BtnImagem.configure(activeforeground="#000000")
        self.BtnImagem.configure(background="#ffffff")
        self.BtnImagem.configure(disabledforeground="#a3a3a3")
        self.BtnImagem.configure(foreground="#000000")
        self.BtnImagem.configure(highlightbackground="#d9d9d9")
        self.BtnImagem.configure(highlightcolor="black")
        self.BtnImagem.configure(pady="0")
        self.BtnImagem.configure(relief="flat")
        self.BtnImagem.configure(text='''Selecionar imagem''')
        self.BtnImagem.configure(wraplength="100")

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