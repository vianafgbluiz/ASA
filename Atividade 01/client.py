class Client:
    __id = None
    __name = None
    __email = None
    __document = None

    def __init__(self, id, name, email, document):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__document = document

    def getClientId(self):
        return self.__id

    def getClientName(self):
        return self.__name

    def getClientEmail(self):
        return self.__email

    def getClientDocument(self):
        return self.__document
