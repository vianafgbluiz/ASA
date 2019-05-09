class Categoria:
    __idCategoria = None
    __tituloCategoria = None
    __descricaoCategoria = None
    __fgAtivo = None

    def __init__(self, idCategoria, tituloCategoria, descricaoCategoria, fgAtivo):
        self.__idCategoria = idCategoria
        self.__tituloCategoria = tituloCategoria
        self.__descricaoCategoria = descricaoCategoria
        self.__fgAtivo = fgAtivo

    def getIdCategoria(self):
        return self.__idCategoria

    def getTituloCategoria(self):
        return self.__tituloCategoria

    def getDescricaoCategoria(self):
        return self.__descricaoCategoria

    def getAtivoCategoria(self):
        return self.__fgAtivo