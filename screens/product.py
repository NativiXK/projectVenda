from .screen import Screen

class RegisterProduct (Screen):

    def __init__ (self, controls, master, size):
        super().__init__(master, size)
        self.__controls = controls

    @property
    def controls(self):
        return self.__controls

    def inicialize(self, master):
        pass

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