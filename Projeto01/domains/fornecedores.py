class Fornecedores:
    __idFornecedor = None
    __cnpj = None
    __razaoSocial = None
    __telefone = None
    __endereco = None
    __contato = None
    __fgAtivo = None
    
    def __init__(self, idFornecedor, cnpj, razaosocial, telefone, endereco, contato, fgAtivo):
        self.__idFornecedor = idFornecedor
        self.__cnpj = cnpj
        self.__razaoSocial = razaosocial
        self.__telefone = telefone
        self.__endereco = endereco
        self.__contato = contato
        self.__fgAtivo = fgAtivo

    def getIdFornecedor(self):
        return self.__idFornecedor

    def getCnpj(self):
        return self.__cnpj

    def getRazaoSocial(self):
        return self.__razaoSocial

    def getTelefone(self):
        return self.__telefone

    def getEndereco(self):
        return self.__endereco

    def getContato(self):
        return self.__contato

    def getAtivoFornecedor(self):
        return self.__fgAtivo