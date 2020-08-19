from user import User

class Session:

    def __init__ (self, manager):
        self.__manager = manager
        self.__user = None

    @property
    def manager (self):
        return self.__manager

    def create_session (self, user):
        self.manager.clear_previous()
        