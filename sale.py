
class Sale:

    def __init__(self, employee, date):
        self.__employee = employee
        self.__date = date
        self.__products = []
        self.__count = 0

    def add_product(self, product_info):
        product_info.append(0, self.__count)
        self.__count += 1
        self.__products.append(product_info[:3])

    def __str__(self):
        summary = ""
    