from .screen import Screen
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter import ttk
import sys

class Register(Screen):

    def __init__(self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    def makeRegister(self, user):
        if user["password"] != user["passwordConf"]:
            showwarning("Error","Passwords do not match")
            return
        elif "" in user.values():
            showwarning("Info", "Fullfil all the fields!")
            return
        else:
            self.controls.session.makeRegister(user)

    def inicialize(self, master):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Franklin Gothic Heavy} -size 16"

        self.configure(background="#ffffff")
        master.resizable(0, 0)

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.0, rely=0.0, height=44, relwidth=1)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font9)
        self.Label1.configure(relief="flat")
        self.Label1.configure(anchor='center')
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Register''')

        """FULLNAME"""
        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.05, rely=0.15, height=34, width=85)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(font="TkDefaultFont")
        self.Label6.configure(relief="flat")
        self.Label6.configure(anchor='w')
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''Full Name:''')
        self.Label6.configure(cursor="arrow")

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(relx=0.3, rely=0.15,height=35, relwidth=0.563)
        self.nameEntry.configure(background="#ffffff")
        self.nameEntry.configure(cursor="xterm")
        self.nameEntry.configure(disabledforeground="#a3a3a3")
        self.nameEntry.configure(font="TkFixedFont")
        self.nameEntry.configure(foreground="#000000")
        self.nameEntry.configure(insertbackground="black")
        self.nameEntry.configure(relief="flat")

        self.TSeparator1 = ttk.Separator(self)
        self.TSeparator1.place(relx=0.3, rely=0.22, relwidth=0.563)

        """USERNAME"""
        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.05, rely=0.3, height=34, width=85)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(font="TkDefaultFont")
        self.Label6.configure(relief="flat")
        self.Label6.configure(anchor='w')
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''Username:''')
        self.Label6.configure(cursor="arrow")

        self.userEntry = tk.Entry(self)
        self.userEntry.place(relx=0.3, rely=0.3,height=35, relwidth=0.563)
        self.userEntry.configure(background="#ffffff")
        self.userEntry.configure(cursor="xterm")
        self.userEntry.configure(disabledforeground="#a3a3a3")
        self.userEntry.configure(font="TkFixedFont")
        self.userEntry.configure(foreground="#000000")
        self.userEntry.configure(insertbackground="black")
        self.userEntry.configure(relief="flat")

        self.TSeparator5 = ttk.Separator(self)
        self.TSeparator5.place(relx=0.3, rely=0.36, relwidth=0.563)

        """EMAIL"""
        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.05, rely=0.425, height=34, width=85)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(font="TkDefaultFont")
        self.Label3.configure(relief="flat")
        self.Label3.configure(anchor='w')
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''E-mail:''')
        self.Label3.configure(cursor="arrow")

        self.emailEntry = tk.Entry(self)
        self.emailEntry.place(relx=0.3, rely=0.42,height=34, relwidth=0.563)
        self.emailEntry.configure(background="white")
        self.emailEntry.configure(cursor="xterm")
        self.emailEntry.configure(disabledforeground="#a3a3a3")
        self.emailEntry.configure(font="TkFixedFont")
        self.emailEntry.configure(foreground="#000000")
        self.emailEntry.configure(insertbackground="black")
        self.emailEntry.configure(relief="flat")

        self.TSeparator2 = ttk.Separator(self)
        self.TSeparator2.place(relx=0.3, rely=0.486, relwidth=0.563)
        self.TSeparator2.configure(cursor="fleur")

        """PASSWORD"""
        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.05, rely=0.56, height=34, width=85)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(font="TkDefaultFont")
        self.Label6.configure(relief="flat")
        self.Label6.configure(anchor='w')
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''Password:''')
        self.Label6.configure(cursor="arrow")

        self.passwordEntry = tk.Entry(self)
        self.passwordEntry.place(relx=0.3, rely=0.56, height=34, relwidth=0.563)
        self.passwordEntry.configure(background="white")
        self.passwordEntry.configure(cursor="xterm")
        self.passwordEntry.configure(disabledforeground="#a3a3a3")
        self.passwordEntry.configure(font="TkFixedFont")
        self.passwordEntry.configure(foreground="#000000")
        self.passwordEntry.configure(insertbackground="black")
        self.passwordEntry.configure(relief="flat")
        self.passwordEntry.configure(show="*")

        self.TSeparator3 = ttk.Separator(self)
        self.TSeparator3.place(relx=0.3, rely=0.63, relwidth=0.563)

        """PASSWORD CONFIRMATION"""
        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.05, rely=0.66, height=64, width=95)
        self.Label5.configure(background="#FFFFFF")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(font="TkDefaultFont")
        self.Label5.configure(relief="flat")
        self.Label5.configure(anchor='w')
        self.Label5.configure(justify='left')
        self.Label5.configure(wraplength="90")
        self.Label5.configure(text='''Password confirmation:''')
        self.Label5.configure(cursor="arrow")

        self.passwordConfEntry = tk.Entry(self)
        self.passwordConfEntry.place(relx=0.3, rely=0.7, height=34
                , relwidth=0.563)
        self.passwordConfEntry.configure(background="white")
        self.passwordConfEntry.configure(disabledforeground="#a3a3a3")
        self.passwordConfEntry.configure(font="TkFixedFont")
        self.passwordConfEntry.configure(foreground="#000000")
        self.passwordConfEntry.configure(insertbackground="black")
        self.passwordConfEntry.configure(relief="flat")
        self.passwordConfEntry.configure(show="*")
        self.passwordConfEntry.configure(cursor="xterm")

        self.TSeparator4 = ttk.Separator(self)
        self.TSeparator4.place(relx=0.3, rely=0.77, relwidth=0.563)

        self.btnBack = tk.Button(self)
        self.btnBack.place(relx=0.175, rely=0.822, height=45, width=85)
        self.btnBack.configure(activebackground="#ececec")
        self.btnBack.configure(activeforeground="#000000")
        self.btnBack.configure(background="#d9d9d9")
        self.btnBack.configure(cursor="hand2")
        self.btnBack.configure(disabledforeground="#a3a3a3")
        self.btnBack.configure(foreground="#000000")
        self.btnBack.configure(highlightbackground="#d9d9d9")
        self.btnBack.configure(highlightcolor="black")
        self.btnBack.configure(pady="0")
        self.btnBack.configure(relief="flat")
        self.btnBack.configure(text='''Back''')
        self.btnBack.bind('<Button-1>',lambda e: self.controls.btnBack())

        self.btnRegister = tk.Button(self)
        self.btnRegister.place(relx=0.575, rely=0.822, height=45, width=85)
        self.btnRegister.configure(activebackground="#ececec")
        self.btnRegister.configure(activeforeground="#000000")
        self.btnRegister.configure(background="#d9d9d9")
        self.btnRegister.configure(disabledforeground="#a3a3a3")
        self.btnRegister.configure(foreground="#000000")
        self.btnRegister.configure(highlightbackground="#d9d9d9")
        self.btnRegister.configure(highlightcolor="black")
        self.btnRegister.configure(pady="0")
        self.btnRegister.configure(relief="flat")
        self.btnRegister.configure(text='''Register''')
        self.btnRegister.configure(cursor="hand2")
        self.btnRegister.bind('<Button-1>',lambda e: self.makeRegister(
        {
        "fullname" : self.nameEntry.get(),
        "username" : self.userEntry.get(),
        "email" : self.emailEntry.get(),
        "password" : self.passwordEntry.get(),
        "passwordConf" : self.passwordConfEntry.get()}
        ))
