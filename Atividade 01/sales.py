class Sale:
    __id = None
    __idClient = None
    __idProduct = None
    __quantity = None
    __total = None
    
    def __init__(self, id, idClient, idProduct, quantity, total):
        self.__id = id
        self.__idClient = idClient
        self.__idProduct = idProduct
        self.__quantity = quantity
        self.__total = total

    def getSaleId(self):
        return self.__id

    def getSaleIdClient(self):
        return self.__idClient

    def getSaleIdProduct(self):
        return self.__idProduct

    def getSaleQuantity(self):
        return self.__quantity

    def getSaleTotal(self):
        return self.__total
    