from screens.screen import Screen
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, DoubleVar
import sys

class Entry (Screen):

    def __init__(self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls
        super().add_var("topInfoLabelVar", StringVar(self))
        super().add_var("ProductPriceVar", DoubleVar(self))
        super().add_var("ProductNameVar", StringVar(self))
        super().add_var("ProductIdVar", StringVar(self))
        super().add_var("EmployeeIdVar", StringVar(self))
        super().add_var("EmployeeNameVar", StringVar(self))
        super().add_var("LoginEmployeeVar", StringVar(self))

        super().get_var("LoginEmployeeVar").set("Login")

        # self.__inicialize(master)

    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        master.title("Point of sale")
        self.configure(background="#28a4ff")

        self.TopInfoLabel = tk.Label(self)
        self.TopInfoLabel.place(relx=0.004, rely=0.004, height=45, width=1190)
        self.TopInfoLabel.configure(activebackground="#f9f9f9")
        self.TopInfoLabel.configure(activeforeground="black")
        self.TopInfoLabel.configure(background="#d9d9d9")
        self.TopInfoLabel.configure(disabledforeground="#a3a3a3")
        self.TopInfoLabel.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
        self.TopInfoLabel.configure(foreground="#000000")
        self.TopInfoLabel.configure(textvariable=super().get_var("topInfoLabelVar"))

        self.menubar = tk.Menu(self,font="TkMenuFont",bg='#28a4ff',fg='#28a4ff')
        master.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(self,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="Products")
        self.sub_menu.add_command(
                label="Add")
        self.sub_menu.add_command(
                label="Remove")
        self.sub_menu.add_command(
                label="Modify")
        self.sub_menu.add_command(
                label="Search")
        self.sub_menu1 = tk.Menu(self,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="NewCascade")
        self.sub_menu12 = tk.Menu(self,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                label="Options")
        self.sub_menu12.add_command(
                label="History")
        self.sub_menu12.add_separator(
)

        self.FrameProduct = tk.Frame(self)
        self.FrameProduct.place(relx=0.353, rely=0.065, relheight=0.337
                , relwidth=0.643)
        self.FrameProduct.configure(relief='flat')
        self.FrameProduct.configure(borderwidth="2")
        self.FrameProduct.configure(background="#d9d9d9")
        self.FrameProduct.configure(highlightbackground="#d9d9d9")
        self.FrameProduct.configure(highlightcolor="black")

        self.LabelProduct = tk.Label(self.FrameProduct)
        self.LabelProduct.place(relx=0.0, rely=0.0, height=39, width=771)
        self.LabelProduct.configure(activebackground="#f9f9f9")
        self.LabelProduct.configure(activeforeground="black")
        self.LabelProduct.configure(background="#d9d9d9")
        self.LabelProduct.configure(disabledforeground="#a3a3a3")
        self.LabelProduct.configure(font="-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelProduct.configure(foreground="#000000")
        self.LabelProduct.configure(highlightbackground="#d9d9d9")
        self.LabelProduct.configure(highlightcolor="black")
        self.LabelProduct.configure(text='''Product''')

        self.TSeparator2 = ttk.Separator(self.FrameProduct)
        self.TSeparator2.place(relx=0.139, rely=0.16, relwidth=0.724)

        self.CanvasProduct = tk.Canvas(self.FrameProduct)
        self.CanvasProduct.place(relx=0.027, rely=0.19, relheight=0.791
                , relwidth=0.324)
        self.CanvasProduct.configure(background="#d9d9d9")
        self.CanvasProduct.configure(borderwidth="2")
        self.CanvasProduct.configure(highlightbackground="#d9d9d9")
        self.CanvasProduct.configure(highlightcolor="black")
        self.CanvasProduct.configure(insertbackground="black")
        self.CanvasProduct.configure(selectbackground="blue")
        self.CanvasProduct.configure(selectforeground="white")

        self.LabelProductName = tk.Label(self.FrameProduct)
        self.LabelProductName.place(relx=0.447, rely=0.418, height=31, width=402)

        self.LabelProductName.configure(activebackground="#f9f9f9")
        self.LabelProductName.configure(activeforeground="black")
        self.LabelProductName.configure(background="#ffffff")
        self.LabelProductName.configure(disabledforeground="#a3a3a3")
        self.LabelProductName.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelProductName.configure(foreground="#000000")
        self.LabelProductName.configure(highlightbackground="#d9d9d9")
        self.LabelProductName.configure(highlightcolor="black")
        self.LabelProductName.configure(text='''Name''')
        self.LabelProductName.configure(textvariable=super().get_var("ProductNameVar"))

        self.Label1 = tk.Label(self.FrameProduct)
        self.Label1.place(relx=0.447, rely=0.57, height=31, width=34)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''R$ :''')

        self.LabelProductPrice = tk.Label(self.FrameProduct)
        self.LabelProductPrice.place(relx=0.521, rely=0.57, height=31, width=345)

        self.LabelProductPrice.configure(activebackground="#f9f9f9")
        self.LabelProductPrice.configure(activeforeground="black")
        self.LabelProductPrice.configure(background="#ffffff")
        self.LabelProductPrice.configure(disabledforeground="#a3a3a3")
        self.LabelProductPrice.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelProductPrice.configure(foreground="#000000")
        self.LabelProductPrice.configure(highlightbackground="#d9d9d9")
        self.LabelProductPrice.configure(highlightcolor="black")
        self.LabelProductPrice.configure(text='''Price''')
        self.LabelProductPrice.configure(textvariable=super().get_var("ProductPriceVar"))

        self.LabelProductId = tk.Label(self.FrameProduct)
        self.LabelProductId.place(relx=0.447, rely=0.266, height=31, width=402)
        self.LabelProductId.configure(activebackground="#f9f9f9")
        self.LabelProductId.configure(activeforeground="black")
        self.LabelProductId.configure(background="#ffffff")
        self.LabelProductId.configure(disabledforeground="#a3a3a3")
        self.LabelProductId.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelProductId.configure(foreground="#000000")
        self.LabelProductId.configure(highlightbackground="#d9d9d9")
        self.LabelProductId.configure(highlightcolor="black")
        self.LabelProductId.configure(text='''ID''')
        self.LabelProductId.configure(textvariable=super().get_var("ProductIdVar"))

        self.FrameSummary = tk.Frame(self)
        self.FrameSummary.place(relx=0.003, rely=0.065, relheight=0.6
                , relwidth=0.348)
        self.FrameSummary.configure(relief='flat')
        self.FrameSummary.configure(borderwidth="2")
        self.FrameSummary.configure(background="#d9d9d9")
        self.FrameSummary.configure(highlightbackground="#d9d9d9")
        self.FrameSummary.configure(highlightcolor="black")

        self.LabelSummary = tk.Label(self.FrameSummary)
        self.LabelSummary.place(relx=0.0, rely=0.0, height=40, width=417)
        self.LabelSummary.configure(activebackground="#f9f9f9")
        self.LabelSummary.configure(activeforeground="black")
        self.LabelSummary.configure(background="#d9d9d9")
        self.LabelSummary.configure(disabledforeground="#a3a3a3")
        self.LabelSummary.configure(font="-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelSummary.configure(foreground="#000000")
        self.LabelSummary.configure(highlightbackground="#d9d9d9")
        self.LabelSummary.configure(highlightcolor="black")
        self.LabelSummary.configure(text='''Sale Summary''')

        self.TextSaleSummary = tk.Text(self.FrameSummary)
        self.TextSaleSummary.place(relx=0.014, rely=0.128, relheight=0.855
                , relwidth=0.971)
        self.TextSaleSummary.configure(background="white")
        self.TextSaleSummary.configure(cursor="")
        self.TextSaleSummary.configure(font="TkTextFont")
        self.TextSaleSummary.configure(foreground="black")
        self.TextSaleSummary.configure(highlightbackground="#d9d9d9")
        self.TextSaleSummary.configure(highlightcolor="black")
        self.TextSaleSummary.configure(insertbackground="black")
        self.TextSaleSummary.configure(relief="flat")
        self.TextSaleSummary.configure(selectbackground="blue")
        self.TextSaleSummary.configure(selectforeground="white")
        self.TextSaleSummary.configure(wrap="word")

        self.TSeparator1 = ttk.Separator(self.FrameSummary)
        self.TSeparator1.place(relx=0.118, rely=0.09, relwidth=0.751)

        self.FrameEmployee = tk.Frame(self)
        self.FrameEmployee.place(relx=0.353, rely=0.406, relheight=0.259
                , relwidth=0.643)
        self.FrameEmployee.configure(relief='flat')
        self.FrameEmployee.configure(borderwidth="2")
        self.FrameEmployee.configure(background="#d9d9d9")
        self.FrameEmployee.configure(highlightbackground="#d9d9d9")
        self.FrameEmployee.configure(highlightcolor="black")

        self.LabelEmployee = tk.Label(self.FrameEmployee)
        self.LabelEmployee.place(relx=0.0, rely=0.0, height=42, width=771)
        self.LabelEmployee.configure(activebackground="#f9f9f9")
        self.LabelEmployee.configure(activeforeground="black")
        self.LabelEmployee.configure(background="#d9d9d9")
        self.LabelEmployee.configure(disabledforeground="#a3a3a3")
        self.LabelEmployee.configure(font="-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelEmployee.configure(foreground="#000000")
        self.LabelEmployee.configure(highlightbackground="#d9d9d9")
        self.LabelEmployee.configure(highlightcolor="black")
        self.LabelEmployee.configure(text='''Employee''')

        self.TSeparator3 = ttk.Separator(self.FrameEmployee)
        self.TSeparator3.place(relx=0.139, rely=0.208, relwidth=0.725)

        self.CanvasEmployee = tk.Canvas(self.FrameEmployee)
        self.CanvasEmployee.place(relx=0.139, rely=0.262, relheight=0.698
                , relwidth=0.174)
        self.CanvasEmployee.configure(background="#d9d9d9")
        self.CanvasEmployee.configure(borderwidth="2")
        self.CanvasEmployee.configure(highlightbackground="#d9d9d9")
        self.CanvasEmployee.configure(highlightcolor="black")
        self.CanvasEmployee.configure(insertbackground="black")
        self.CanvasEmployee.configure(selectbackground="blue")
        self.CanvasEmployee.configure(selectforeground="white")

        self.LabelEmployeeId = tk.Label(self.FrameEmployee)
        self.LabelEmployeeId.place(relx=0.363, rely=0.262, height=31, width=386)
        self.LabelEmployeeId.configure(activebackground="#f9f9f9")
        self.LabelEmployeeId.configure(activeforeground="black")
        self.LabelEmployeeId.configure(background="#ffffff")
        self.LabelEmployeeId.configure(disabledforeground="#a3a3a3")
        self.LabelEmployeeId.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelEmployeeId.configure(foreground="#000000")
        self.LabelEmployeeId.configure(highlightbackground="#d9d9d9")
        self.LabelEmployeeId.configure(highlightcolor="black")
        self.LabelEmployeeId.configure(text='''ID''')
        self.LabelEmployeeId.configure(textvariable=super().get_var("EmployeeIdVar"))

        self.LabelEmployeeName = tk.Label(self.FrameEmployee)
        self.LabelEmployeeName.place(relx=0.363, rely=0.465, height=31
                , width=386)
        self.LabelEmployeeName.configure(activebackground="#f9f9f9")
        self.LabelEmployeeName.configure(activeforeground="black")
        self.LabelEmployeeName.configure(background="#ffffff")
        self.LabelEmployeeName.configure(disabledforeground="#a3a3a3")
        self.LabelEmployeeName.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelEmployeeName.configure(foreground="#000000")
        self.LabelEmployeeName.configure(highlightbackground="#d9d9d9")
        self.LabelEmployeeName.configure(highlightcolor="black")
        self.LabelEmployeeName.configure(text='''Name''')
        self.LabelEmployeeName.configure(textvariable=super().get_var("EmployeeNameVar"))

        self.ButtonEntraEmployee = tk.Button(self.FrameEmployee)
        self.ButtonEntraEmployee.place(relx=0.547, rely=0.693, height=44
                , width=100)
        self.ButtonEntraEmployee.configure(activebackground="#ececec")
        self.ButtonEntraEmployee.configure(activeforeground="#000000")
        self.ButtonEntraEmployee.configure(background="#5ebaff")
        self.ButtonEntraEmployee.configure(disabledforeground="#a3a3a3")
        self.ButtonEntraEmployee.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ButtonEntraEmployee.configure(foreground="#000000")
        self.ButtonEntraEmployee.configure(highlightbackground="#d9d9d9")
        self.ButtonEntraEmployee.configure(highlightcolor="black")
        self.ButtonEntraEmployee.configure(pady="0")
        self.ButtonEntraEmployee.configure(relief="flat")
        self.ButtonEntraEmployee.configure(text='''Log in''')
        self.ButtonEntraEmployee.configure(textvariable=super().get_var("LoginEmployeeVar"))

        self.FrameInput = tk.Frame(self)
        self.FrameInput.place(relx=0.003, rely=0.671, relheight=0.323
                , relwidth=0.993)
        self.FrameInput.configure(relief='flat')
        self.FrameInput.configure(borderwidth="2")
        self.FrameInput.configure(background="#d9d9d9")
        self.FrameInput.configure(highlightbackground="#d9d9d9")
        self.FrameInput.configure(highlightcolor="black")

        self.LabelInputs = tk.Label(self.FrameInput)
        self.LabelInputs.place(relx=0.0, rely=0.0, height=42, width=1191)
        self.LabelInputs.configure(activebackground="#f9f9f9")
        self.LabelInputs.configure(activeforeground="black")
        self.LabelInputs.configure(background="#d9d9d9")
        self.LabelInputs.configure(disabledforeground="#a3a3a3")
        self.LabelInputs.configure(font="-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelInputs.configure(foreground="#000000")
        self.LabelInputs.configure(highlightbackground="#d9d9d9")
        self.LabelInputs.configure(highlightcolor="black")
        self.LabelInputs.configure(text='''Input''')

        self.TSeparator4 = ttk.Separator(self.FrameInput)
        self.TSeparator4.place(relx=0.138, rely=0.167, relwidth=0.725)

        self.EntryProductID = tk.Entry(self.FrameInput)
        self.EntryProductID.place(relx=0.185, rely=0.278, height=40
                , relwidth=0.75)
        self.EntryProductID.configure(background="white")
        self.EntryProductID.configure(disabledforeground="#a3a3a3")
        self.EntryProductID.configure(font="-family {Courier New} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.EntryProductID.configure(foreground="#000000")
        self.EntryProductID.configure(highlightbackground="#d9d9d9")
        self.EntryProductID.configure(highlightcolor="black")
        self.EntryProductID.configure(insertbackground="black")
        self.EntryProductID.configure(selectbackground="blue")
        self.EntryProductID.configure(selectforeground="white")
        self.EntryProductID.bind('<Key><Key-Return>',lambda e: self.controls.session.addProduct())

        self.LabelPorductInput = tk.Label(self.FrameInput)
        self.LabelPorductInput.place(relx=0.067, rely=0.278, height=40
                , width=121)
        self.LabelPorductInput.configure(activebackground="#f9f9f9")
        self.LabelPorductInput.configure(activeforeground="black")
        self.LabelPorductInput.configure(background="#d9d9d9")
        self.LabelPorductInput.configure(disabledforeground="#a3a3a3")
        self.LabelPorductInput.configure(font="-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0")
        self.LabelPorductInput.configure(foreground="#000000")
        self.LabelPorductInput.configure(highlightbackground="#d9d9d9")
        self.LabelPorductInput.configure(highlightcolor="black")
        self.LabelPorductInput.configure(text='''Product''')

        self.ButtonNewSale = tk.Button(self.FrameInput)
        self.ButtonNewSale.place(relx=0.317, rely=0.675, height=44, width=100)
        self.ButtonNewSale.configure(activebackground="#ececec")
        self.ButtonNewSale.configure(activeforeground="#000000")
        self.ButtonNewSale.configure(background="#5ebaff")
        self.ButtonNewSale.configure(disabledforeground="#a3a3a3")
        self.ButtonNewSale.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ButtonNewSale.configure(foreground="#000000")
        self.ButtonNewSale.configure(highlightbackground="#d9d9d9")
        self.ButtonNewSale.configure(highlightcolor="black")
        self.ButtonNewSale.configure(pady="0")
        self.ButtonNewSale.configure(relief="flat")
        self.ButtonNewSale.configure(text='''New (F5)''')

        self.ButtonUndo = tk.Button(self.FrameInput)
        self.ButtonUndo.place(relx=0.456, rely=0.675, height=44, width=100)
        self.ButtonUndo.configure(activebackground="#ececec")
        self.ButtonUndo.configure(activeforeground="#000000")
        self.ButtonUndo.configure(background="#5ebaff")
        self.ButtonUndo.configure(disabledforeground="#a3a3a3")
        self.ButtonUndo.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ButtonUndo.configure(foreground="#000000")
        self.ButtonUndo.configure(highlightbackground="#d9d9d9")
        self.ButtonUndo.configure(highlightcolor="black")
        self.ButtonUndo.configure(pady="0")
        self.ButtonUndo.configure(relief="flat")
        self.ButtonUndo.configure(text='''Undo (F6)''')

        self.ButtonFinish = tk.Button(self.FrameInput)
        self.ButtonFinish.place(relx=0.589, rely=0.671, height=44, width=100)
        self.ButtonFinish.configure(activebackground="#ececec")
        self.ButtonFinish.configure(activeforeground="#000000")
        self.ButtonFinish.configure(background="#5ebaff")
        self.ButtonFinish.configure(disabledforeground="#a3a3a3")
        self.ButtonFinish.configure(font="-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ButtonFinish.configure(foreground="#000000")
        self.ButtonFinish.configure(highlightbackground="#d9d9d9")
        self.ButtonFinish.configure(highlightcolor="black")
        self.ButtonFinish.configure(pady="0")
        self.ButtonFinish.configure(relief="flat")
        self.ButtonFinish.configure(text='''Finish (F8)''')
