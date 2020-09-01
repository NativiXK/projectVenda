from person import User, Employee
from tkinter.messagebox import showwarning, showinfo
from dbConnector import Connector

class Session:

    def __init__ (self, manager):
        self.__manager = manager
        self.__db = None
        self.__user = None
        self.__sale = None
        self.startup()
        
    @property
    def manager (self):
        return self.__manager
    
    @property
    def user (self):
        return self.__user

    @property
    def db (self):
        return self.__db

    def startup (self):
        self.__db = Connector()
        self.__manager.session = self
        self.manager.master.resizable(0, 0)
    # gives the application a user session
    def give_session (self, user):
        self.__user = User(user)
        self.manager.screen = "entry"
        self.manager.screen.get_var("topInfoLabelVar").set("Seja bem vindo {}".format(user["username"]))
    
    def makeLogin (self, username, password):
        if username == "" or password == "":
            showwarning("LOGIN", "Please fill all the fields to login")
            return

        self.db.query(""" SELECT * FROM users WHERE email='{}' OR password='{}' """.format(username, password))
        results = self.db.cursor.fetchall()

        if results != []:
            for result in results:
                dbUsername, dbPassword = (result[2], result[4])
                if username == dbUsername:
                    if password == dbPassword:
                        # create a user session
                        # (index, fullname, username, email, password)
                        user = {
                            "id" : result[0],
                            "fullname" : result[1],
                            "username" : result[2],
                            "email" : result[3],
                        }

                        self.give_session(user)
                        break
                    else:
                        showwarning("LOGIN", "Wrong password")
                else:
                    showwarning("LOGIN", "User not found")
        else:
            showwarning("LOGIN", "User not found")

    def makeRegister (self, user):
        self.db.query(""" SELECT * FROM users WHERE email='{}' OR username='{}' """.format(user["email"], user["username"]))
        results = self.db.cursor.fetchall()

        if results == []:
            user = (user["fullname"], user["username"], user["email"], user["password"])
            self.db.query(""" INSERT INTO users (fullname, username, email, password) values(?, ?, ?, ?) """, user)
            self.db.commit()
            showinfo("Register", message="Registered successfully")
            self.manager.screen = 'login'
        else:
            showwarning("Error", "User already registered")

    def addProduct (self):
        # get the product id from entry screen
        product_id = self.manager.screen.EntryProductID.get()
        # search for the product in the database
        product_info = self.db.get_product(self.user.ID, product_id)
        # clean entry id field
        self.manager.screen.EntryProductID.delete(0, 200)
        # clears all info in product frame
        self.__clear_prod_frame()
        # clear message
        self.manager.screen.clear_message()
        # check if product found
        if len(product_info) == 0:
            # display message
            self.manager.screen.show_message("Produto não encontrado")
            return
        # update product frame
        self.__update_prod_frame(product_info[0])
        
        self.__insert_record_summary()

    # clears all information retained in product frame
    def __clear_prod_frame(self):
        self.manager.screen.get_var("productIdVar").set("")
        self.manager.screen.get_var("productNameVar").set("")
        self.manager.screen.get_var("productPriceVar").set("")

    def __update_prod_frame (self, product_info):
        self.manager.screen.get_var("productIdVar").set(product_info[0])
        self.manager.screen.get_var("productNameVar").set(product_info[1])
        self.manager.screen.get_var("productPriceVar").set(product_info[2])
    
    def __insert_record_summary(self, product_info):
        pass