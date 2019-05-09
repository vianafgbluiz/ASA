from sqlalchemy import create_engine

class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@localhost/asa"
    db_query = ""

    # --------------- SERVICE para CATEGORIA --------------- #
    def insertCategory(self, tituloCategoria, descricaoCategoria, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_categorias(tituloCategoria, descricaoCategoria, fg_ativo) VALUES (%s, %s, %s)", tituloCategoria, descricaoCategoria, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res

    def getAllCategories(self):
        db = create_engine(self.db_string)
        categorias = db.execute("SELECT * FROM project.tb_categorias")
        return categorias

    def getCategoryById(self, idCategoria):
        db = create_engine(self.db_string)
        categoria = db.execute("SELECT * FROM project.tb_categorias WHERE id_categoria = %s", idCategoria)
        return categoria

    # --------------- SERVICE para FORNECEDORES --------------- #
    def insertProvider(self, cnpj, razaoSocial, telefone, endereco, contato, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_fornecedores(cnpj, razaosocial, telefone, endereco, contato, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s)", cnpj, razaoSocial, telefone, endereco, contato, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res

    def getAllProviders(self):
        db = create_engine(self.db_string)        
        fornecedores = db.execute("SELECT * FROM project.tb_fornecedores")
        return fornecedores

    def getProviderById(self, idProvider):
        db = create_engine(self.db_string)
        categoria = db.execute("SELECT * FROM project.tb_fornecedores WHERE id_fornecedor = %s", idProvider)
        return categoria

    # --------------- SERVICE para VENDEDORES --------------- #
    def insertSalesman(self, cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_vendedores(cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s)", cpf, nome, carteiraTrabalho, telefone, dataAdmissao, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res

    def getAllSalesman(self):
        db = create_engine(self.db_string)        
        vendedores = db.execute("SELECT * FROM project.tb_vendedores")
        return vendedores

    def getSalesmanById(self, idVendedor):
        db = create_engine(self.db_string)
        vendedor = db.execute("SELECT * FROM project.tb_vendedores WHERE id_vendedor = %s", idVendedor)
        return vendedor


    # --------------- SERVICE para PRODUTOS --------------- #
    def insertProduct(self, idFornecedor, idCategoria, nomeproduto, descricaoproduto, valorunitario, quantidade, quantidademinima, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_produtos(id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valorunitario, quantidade, quantidademinima, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", idFornecedor, idCategoria, nomeproduto, descricaoproduto, valorunitario, quantidade, quantidademinima, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res

    def getAllProducts(self):
        db = create_engine(self.db_string)
        produtos = db.execute("SELECT p.id_produto, f.razaosocial, c.titulocategoria, p.nomeproduto, p.descricaoproduto, p.valorunitario, p.quantidade, p.quantidademinima, p.fg_ativo FROM project.tb_produtos p, project.tb_fornecedores f, project.tb_categorias c WHERE p.id_fornecedor = f.id_fornecedor AND p.id_categoria = c.id_categoria")
        return produtos
    
    def getProductById(self, idProduct):
        db = create_engine(self.db_string)
        try:
            product = db.execute("SELECT * FROM project.tb_produtos WHERE id_produto = %s LIMIT 1", idProduct)
            return product
        except:
            return False

    def updateQuantityProductById(self, idProduct, quantidade):
        db = create_engine(self.db_string)
        try:
            db.execute("UPDATE project.tb_produtos SET quantidade = %s WHERE id_produto = %s", quantidade, idProduct)
            res = True
        except:
            print("Problemas ao Alterar!")
            res = False
        return res

    # --------------- SERVICE para COMPRAS --------------- #
    def insertSale(self, idFornecedor, idProduto, idCategoria, valorTotal, quantidade, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_compras(id_fornecedor, id_produto, id_categoria, datacompra, valortotal, quantidade, fg_ativo) VALUES (%s, %s, %s, CURRENT_DATE, %s, %s, %s)", idFornecedor, idProduto, idCategoria, valorTotal, quantidade, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res

    def getAllSales(self):
        db = create_engine(self.db_string)
        sales = db.execute("SELECT c.id_compra, f.razaosocial, p.nomeproduto, ct.titulocategoria, c.datacompra, c.valortotal, c.quantidade, c.fg_ativo FROM project.tb_compras c, project.tb_fornecedores f, project.tb_produtos p, project.tb_categorias ct WHERE c.id_categoria = ct.id_categoria AND c.id_fornecedor = f.id_fornecedor AND c.id_produto = p.id_produto")
        return sales

    def getSaleById(self, idSale):
        db = create_engine(self.db_string)
        sale = db.execute("SELECT c.id_compra, f.razaosocial, p.nomeproduto, ct.titulocategoria, c.datacompra, c.valortotal, c.quantidade, c.fg_ativo FROM project.tb_compras c, project.tb_fornecedores f, project.tb_produtos p, project.tb_categorias ct WHERE c.id_categoria = ct.id_categoria AND c.id_fornecedor = f.id_fornecedor AND c.id_produto = p.id_produto AND c.id_compra = %s", idSale)
        return sale

    # --------------- SERVICE para VENDAS --------------- #
    def insertExit(self, idVendedor, idProduto, idCategoria, valorTotal, quantidade, fgAtivo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO project.tb_vendas(id_vendedor, id_produto, id_categoria, datavenda, valortotal, quantidade, fg_ativo) VALUES (%s, %s, %s, CURRENT_DATE, %s, %s, %s)", idVendedor, idProduto, idCategoria, valorTotal, quantidade, fgAtivo)
            res = True
        except:
            print("Problemas ao Inserir!")
            res = False
        return res
    
    def getAllExits(self):
        db = create_engine(self.db_string)
        exits = db.execute("SELECT v.id_venda, vd.nome, p.nomeproduto, c.titulocategoria, v.datavenda, v.valortotal, v.quantidade, v.fg_ativo FROM project.tb_vendas v, project.tb_vendedores vd, project.tb_produtos p, project.tb_categorias c WHERE v.id_categoria = c.id_categoria AND v.id_produto = p.id_produto AND v.id_vendedor = vd.id_vendedor")
        return exits