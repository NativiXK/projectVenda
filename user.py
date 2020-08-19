
class User:

    def __init__(self, user):
        self.__fullname = user["fullname"]
        self.__username = user["username"]
        self.__email = user["email"]

    @property
    def fullname (self):
        return self.__fullname
    
    @property
    def username (self):
        return self.__username

    @property
    def email (self):
        return self.__email



    