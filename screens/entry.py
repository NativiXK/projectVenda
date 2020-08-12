from screens.screen import Screen
import tkinter as tk

class Entry (Screen):

    def __init__(self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls
        self.__inicialize()

    @property
    def controls(self):
        return self.__controls

    def __inicialize(self):
        pass
