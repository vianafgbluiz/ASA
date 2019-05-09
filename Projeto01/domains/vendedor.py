class Vendedor:
    __idVendedor = None
    __cpf = None
    __nome = None
    __carteiraTrabalho = None
    __telefone = None
    __dataAdmissao = None
    __fgAtivo = None

    def __init__(self, idVendedor, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fgAtivo):
        self.__idVendedor = idVendedor
        self.__cpf = cpf
        self.__nome = nome
        self.__carteiraTrabalho = carteiraTrabalho
        self.__telefone = telefone
        self.__dataAdmissao = dataAdmissao
        self.__fgAtivo = fgAtivo

    def getIdVendedor(self):
        return self.__idVendedor

    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

    def getCarteiraTrabalho(self):
        return self.__carteiraTrabalho

    def getTelefone(self):
        return self.__telefone

    def getDataAdmissao(self):
        return self.__dataAdmissao

    def getAtivo(self):
        return self.__fgAtivo