class Compras:
    __idCompra = None
    __idFornecedor = None
    __idProduto = None
    __idCategoria = None
    __dataCompra = None
    __valorTotal = None
    __quantidade = None
    __fgAtivo = None

    def __init__(self, idCompra, idFornecedor, idProduto, idCategoria, dataCompra, valorTotal, quantidade, fgAtivo):
        self.__idCompra = idCompra
        self.__idFornecedor = idFornecedor
        self.__idProduto = idProduto
        self.__idCategoria = idCategoria
        self.__dataCompra = dataCompra
        self.__valorTotal = valorTotal
        self.__quantidade = quantidade
        self.__fgAtivo = fgAtivo

    def getIdCompra(self):
        return self.__idCompra

    def getIdFornecedor(self):
        return self.__idFornecedor

    def getIdProduto(self):
        return self.__idProduto
    
    def getIdCategoria(self):
        return self.__idCategoria

    def getDataCompra(self):
        return self.__dataCompra

    def getValorTotal(self):
        return self.__valorTotal
    
    def getQuantidade(self):
        return self.__quantidade
    
    def getAtivo(self):
        return self.__fgAtivo