from .screen import Screen
import tkinter as tk

class Login (Screen):

    def __init__(self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.configure(background="#ffffff")
        master.resizable(0, 0)

        self.UserEntry = tk.Entry(self)
        self.UserEntry.place(relx=0.333, rely=0.12,height=34, relwidth=0.583)
        self.UserEntry.configure(background="white")
        self.UserEntry.configure(disabledforeground="#a3a3a3")
        self.UserEntry.configure(font="TkFixedFont")
        self.UserEntry.configure(foreground="#000000")
        self.UserEntry.configure(insertbackground="black")
        self.UserEntry.configure(cursor="xterm")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.037, rely=0.14, height=34, width=75)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text="Username")
        self.Label1.configure(cursor="arrow")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.033, rely=0.36, height=34, width=75)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Password''')
        self.Label2.configure(cursor="arrow")

        self.PassEntry = tk.Entry(self)
        self.PassEntry.place(relx=0.333, rely=0.36,height=34, relwidth=0.583)
        self.PassEntry.configure(background="white")
        self.PassEntry.configure(cursor="fleur")
        self.PassEntry.configure(disabledforeground="#a3a3a3")
        self.PassEntry.configure(font="TkFixedFont")
        self.PassEntry.configure(foreground="#000000")
        self.PassEntry.configure(insertbackground="black")
        self.PassEntry.configure(show="*")
        self.PassEntry.configure(cursor="xterm")

        self.btnLogin = tk.Button(self)
        self.btnLogin.place(relx=0.6, rely=0.64, height=45, width=85)
        self.btnLogin.configure(activebackground="#ececec")
        self.btnLogin.configure(activeforeground="#000000")
        self.btnLogin.configure(background="#d9d9d9")
        self.btnLogin.configure(disabledforeground="#a3a3a3")
        self.btnLogin.configure(foreground="#000000")
        self.btnLogin.configure(highlightbackground="#d9d9d9")
        self.btnLogin.configure(highlightcolor="black")
        self.btnLogin.configure(pady="0")
        self.btnLogin.configure(relief="flat")
        self.btnLogin.configure(text='''Login''')
        self.btnLogin.bind('<Button-1>',lambda e: self.controls.session.makeLogin(self.UserEntry.get(), self.PassEntry.get()))

        self.btnRegister = tk.Button(self)
        self.btnRegister.place(relx=0.133, rely=0.64, height=45, width=85)
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
        self.btnRegister.bind('<Button-1>',lambda e: self.controls.btnRegister())


        master.bind('<Key><Key-Return>', lambda e : self.controls.session.makeLogin(self.UserEntry.get(), self.PassEntry.get()))