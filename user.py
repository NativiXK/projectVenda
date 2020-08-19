
class User:

    def __init__(self, user):
        self.__fullname = user[1]
        self.__username = user[2]
        self.__email = user[3]

    @property
    def first_name (self):
        return self.__fullname.split(" ")[0]

    @property
    def last_name(self):
        return self.__fullname.split(" ")[-1]

    