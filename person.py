
class User:

    def __init__(self, user):
        """
        Expects a user dict {
            "fullname" : value,
            "username" : value,
            "email" : value
        }
        """
        check_values = lambda key : user[key] if (key in user.keys()) else ""
    
        self.__fullname = check_values("fullname")
        self.__username = check_values("username")
        self.__email = check_values("email")

    @property
    def fullname (self):
        return self.__fullname
    
    @property
    def username (self):
        return self.__username

    @property
    def email (self):
        return self.__email


class Employee:

    def __init__ (self, employee):
        pass        


