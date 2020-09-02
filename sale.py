
class Sale:

    def __init__(self, employee, date):
        self.__employee = employee
        self.__date = date
        self.__total = 0.0
        self.__products = []
        self.__count = 0

    def add_product(self, product_info):
        product = list(product_info)
        product.insert(0, str(self.__count))
        self.__total += product_info[2]
        self.__count += 1
        self.__products.append(product)

    def __str__(self):
        summary = ""

        for product in self.__products:
            #product index in sale
            summary += "  " + product[0] + ((len(product[0]) - 3) * -1 * " ") 
            # product description
            summary += product[2] + ("\t\t\t\t\t")
            # product price
            summary += "R$ " + str(product[3]) + ((len(str(product[3])) - 5) * -1 * " ")
            summary += "\n"
        summary += "TOTAL: \t\t\t\t\t R$" + str(self.__total) 
        return summary