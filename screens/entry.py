from screens.screen import Screen
import tkinter as tk
from tkinter import StringVar

class Entry (Screen):

    def __init__(self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls
        super().add_var("username", StringVar(self))
        
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
        font9 = "-family {Segoe UI Black} -size 14 -weight bold"

        self.configure(background="#4ab3ff")
 
        self.greetingsLabel = tk.Label(self)
        self.greetingsLabel.place(relx=0.0, rely=0.0, height=47, width=1200)
        self.greetingsLabel.configure(background="#d9d9d9")
        self.greetingsLabel.configure(disabledforeground="#a3a3a3")
        self.greetingsLabel.configure(font=font9)
        self.greetingsLabel.configure(foreground="#000000")
        self.greetingsLabel.configure(justify='left')
        self.greetingsLabel.configure(anchor='w')
        self.greetingsLabel.configure(textvariable=self.get_var("username"))

        self.menubar = tk.Menu(self,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
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
        self.sub_menu12.add_command(
                label="New")
