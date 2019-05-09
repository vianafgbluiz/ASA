class Produto:
    __idProduto = None
    __idFornecedor = None
    __idCategoria = None
    __nomeProduto = None
    __descricaoProduto = None
    __valorUnitario = None
    __quantidade = None
    __quantidadeMinima = None
    __fgAtivo = None

    def __init__(self, idProduto, idFornecedor, idCategoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, fgAtivo):
        self.__idProduto = idProduto
        self.__idFornecedor = idFornecedor
        self.__idCategoria = idCategoria
        self.__nomeProduto = nomeProduto
        self.__descricaoProduto = descricaoProduto
        self.__valorUnitario = valorUnitario
        self.__quantidade = quantidade
        self.__quantidadeMinima = quantidadeMinima
        self.__fgAtivo = fgAtivo

    def getIdProduto(self):
        return self.__idProduto

    def getIdFornecedor(self):
        return self.__idFornecedor

    def getIdCategoria(self): 
        return self.__idCategoria
    
    def getNomeProduto(self):
        return self.__nomeProduto

    def getDescricaoProduto(self):
        return self.__descricaoProduto

    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getQuantidade(self):
        return self.__quantidade

    def getQuantidadeMinima(self):
        return self.__quantidadeMinima
    
    def getAtivo(self):
        return self.__fgAtivo

