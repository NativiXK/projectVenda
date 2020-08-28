from screen_manager import Manager
import ctypes
import tkinter as tk
from session import Session

user32 = ctypes.windll.user32
resolution = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
master = tk.Tk()
manager = Manager(master, resolution, 0.48, 0.46)
this_session = Session(manager)
this_session.manager.inicialize("Vendas")
