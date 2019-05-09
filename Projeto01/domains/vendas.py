class Vendas:
    __idVenda = None
    __idVendedor = None
    __idProduto = None
    __idCategoria = None
    __dataVenda = None
    __valorTotal = None
    __quantidade = None
    __fgAtivo = None

    def __init__(self, idVenda, idVendedor, idProduto, idCategoria, dataVenda, valorTotal, quantidade, fgAtivo):
        self.__idVenda = idVenda
        self.__idVendedor = idVendedor
        self.__idProduto = idProduto
        self.__idCategoria = idCategoria
        self.__dataVenda = dataVenda
        self.__valorTotal = valorTotal
        self.__quantidade = quantidade
        self.__fgAtivo = fgAtivo

    def getIdVenda(self):
        return self.__idVenda

    def getIdVendedor(self):
        return self.__idVendedor

    def getIdProduto(self):
        return self.__idProduto

    def getIdCategoria(self):
        return self.__idCategoria

    def getDataVenda(self):
        return self.__dataVenda
    
    def getValorTotal(self):
        return self.__valorTotal
    
    def getQuantidade(self):
        return self.__quantidade
    
    def getAtivo(self):
        return self.__fgAtivo