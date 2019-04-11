class Product:
    __id = None
    __name = None
    __price = None
    
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def getProductId(self):
        return self.__id

    def getProductName(self):
        return self.__name

    def getProductPrice(self):
        return self.__price
