from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps

# Aqui temos os Imports necessarios para realizar cadastros e compras
from dbUtils import DbUtils
from domains.categoria import Categoria
from domains.fornecedores import Fornecedores
from domains.vendedor import Vendedor
from domains.produtos import Produto


app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

# --------------- SERVICE para CATEGORIA --------------- #
@app.route('/insertcategory', methods = ['POST'])
def insertcategory():
    if not request.json:
        abort(400)

    datas = request.get_json()

    tituloCategoria = datas['tituloCategoria']
    descricaoCategoria = datas['descricaoCategoria']

    dbUtils = DbUtils()

    if(dbUtils.insertCategory(tituloCategoria, descricaoCategoria, 1)):
        result = {"result" : "Categoria inserida com Sucesso!"}
    else:
        result = {"result" : "Problema ao inserir, tente novamente!"}
    return jsonify(result)

@app.route('/getallcategories', methods=['GET'])
def getAllCategories():
    categories = []
    dbUtils = DbUtils()
    categoriesData = dbUtils.getAllCategories()

    for c in categoriesData:
        a = {"Id" : c[0], "Titulo" : c[1], "Descrição" : c[2], "Ativo" : c[3]}
        categories.append(a)
    
    return jsonify(categories)

@app.route('/getcategorybyid', methods=['POST'])
def getCategoryById():
    if not request.json:
        abort(400)

    datas = request.get_json()
    dbUtils = DbUtils()

    idCategoria = datas['idCategoria']

    category = dbUtils.getCategoryById(idCategoria)

    for c in category:
        a = {"Id" : c[0], "Titulo" : c[1], "Descrição" : c[2], "Ativo" : c[3]}
    
    return jsonify(a)

# --------------- SERVICE para FORNECEDORES --------------- #
@app.route('/insertprovider', methods = ['POST'])
def insertProvider():
    if not request.json:
        abort(400)

    datas = request.get_json()

    cnpj = datas['cnpj']
    razaoSocial = datas['razaoSocial']
    telefone = datas['telefone']
    endereco = datas['endereco']
    contato = datas['contato']

    dbUtils = DbUtils()
    
    if(dbUtils.insertProvider(cnpj, razaoSocial, telefone, endereco, contato, 1)):
        result = {"result" : "Fornecedor inserido com Sucesso!"}
    else:
        result = {"result" : "Problema ao inserir, tente novamente!"}
    return jsonify(result)

@app.route('/getallproviders', methods=['GET'])
def getAllProviders():
    providers = []
    dbUtils = DbUtils()
    providersData = dbUtils.getAllProviders()

    for c in providersData:
        a = {"Id" : c[0], "CNPJ" : c[1], "Razão Social" : c[2], "Telefone" : c[3], "Endereco" : c[4], "Contato" : c[5], "Ativo" : c[6]}
        providers.append(a)
    
    return jsonify(providers)

@app.route('/getproviderbyid', methods=['POST'])
def getProviderById():
    if not request.json:
        abort(400)

    datas = request.get_json()
    dbUtils = DbUtils()

    idProvider = datas['idProvider']

    provider = dbUtils.getProviderById(idProvider)

    for c in provider:
        a = {"Id" : c[0], "CNPJ" : c[1], "Razão Social" : c[2], "Telefone" : c[3], "Endereco" : c[4], "Contato" : c[5], "Ativo" : c[6]}
    
    return jsonify(a)

# --------------- SERVICE para VENDEDORES --------------- #
@app.route('/insertsalesman', methods = ['POST'])
def insertSalesman():
    if not request.json:
        abort(400)

    datas = request.get_json()

    cpf = datas['cpf']
    nome = datas['nome']
    carteiraTrabalho = datas['carteiraTrabalho']
    telefone = datas['telefone']
    dataAdmissao = datas['dataAdmissao']

    dbUtils = DbUtils()
    
    if(dbUtils.insertSalesman(cpf, nome, carteiraTrabalho, telefone, dataAdmissao, 1)):
        result = {"result" : "Vendedor inserido com Sucesso!"}
    else:
        result = {"result" : "Problema ao inserir, tente novamente!"}
    return jsonify(result)

@app.route('/getallsalesman', methods=['GET'])
def getAllSalesman():
    salesman = []
    dbUtils = DbUtils()
    salesmanData = dbUtils.getAllSalesman()

    for c in salesmanData:
        a = {"Id" : c[0], "CPF" : c[1], "Nome" : c[2], "Carteira de Trabalho" : c[3], "Telefone" : c[4], "Data de Admissão" : c[5], "Ativo" : c[6]}
        salesman.append(a)
    
    return jsonify(salesman)

@app.route('/getsalesmanbyid', methods=['POST'])
def getSalesmanById():
    if not request.json:
        abort(400)

    datas = request.get_json()
    dbUtils = DbUtils()

    idSalesman = datas['idSalesman']

    salesman = dbUtils.getSalesmanById(idSalesman)

    for c in salesman:
        a = {"Id" : c[0], "CNPJ" : c[1], "Razão Social" : c[2], "Telefone" : c[3], "Endereco" : c[4], "Contato" : c[5], "Ativo" : c[6]}
    
    return jsonify(a)

# --------------- SERVICE para PRODUTOS --------------- #
@app.route('/insertproduct', methods = ['POST'])
def insertProduct():
    if not request.json:
        abort(400)

    datas = request.get_json()

    idFornecedor = datas['idFornecedor']
    idCategoria = datas['idCategoria']
    nomeProduto = datas['nomeProduto']
    descricaoProduto = datas['descricaoProduto']
    valorUnitario = datas['valorUnitario']
    quantidade = datas['quantidade']
    quantidadeMinima = datas['quantidadeMinima']

    dbUtils = DbUtils()
    
    if(dbUtils.insertProduct(idFornecedor, idCategoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima, 1)):
        result = {"result" : "Produto inserido com Sucesso!"}
    else:
        result = {"result" : "Problema ao inserir o produto, tente novamente!"}
    return jsonify(result)

@app.route('/getallproducts', methods=['GET'])
def getAllProducts():
    products = []
    dbUtils = DbUtils()
    productsData = dbUtils.getAllProducts()

    for c in productsData:
        a = {"Id" : c[0], "Fornecedor" : c[1], "Categoria" : c[2], "Nome" : c[3], "Descrição" : c[4], "Valor" : str(c[5]), "Quantidade" : c[6], "Quantidade Minima" : c[7], "Ativo" : c[8]}
        products.append(a)
    
    return jsonify(products)

@app.route('/getproductbyid', methods=['POST'])
def getProductById():
    if not request.json:
        abort(400)

    datas = request.get_json()
    dbUtils = DbUtils()

    idProduto = datas['idProduto']

    produto = dbUtils.getProductById(idProduto)

    for c in produto:
        a = {"Id" : c[0], "Fornecedor" : c[1], "Categoria" : c[2], "Nome" : c[3], "Descrição" : c[4], "Valor" : str(c[5]), "Quantidade" : c[6], "Quantidade Minima" : c[7], "Ativo" : c[8]}
    
    return jsonify(a)

# --------------- SERVICE para COMPRAS --------------- #
@app.route('/insertsale', methods = ['POST'])
def inserSale():
    if not request.json:
        abort(400)

    dbUtils = DbUtils()
    datas = request.get_json()

    idFornecedor = datas['idFornecedor']
    idProduto = datas['idProduto']
    quantidade = datas['quantidade']

    produto = dbUtils.getProductById(idProduto)

    for p in produto:
        valorTotal = int(quantidade) * float(p[5])
        idCategoria = p[2]
        # Adicionando ao estoque
        quantidadeProduto = int(p[6]) + int(quantidade)

    if(quantidadeProduto > 0):
        if(dbUtils.insertSale(idFornecedor, idProduto, idCategoria, valorTotal, quantidade, 1)):
            if(dbUtils.updateQuantityProductById(idProduto, quantidadeProduto)):
                result = {"result" : "Compra efetuada com sucesso", "update" : "Ok"}
            else:
                result = {"update" : "False"}
        else:
            result = {"result" : "Problema ao efetuar a compra, tente novamente!"}
    else:
        result = {"return" : "Não é possivel, pois nao temos prudutos no estoque"}
    
    return jsonify(result)

@app.route('/getallsales', methods=['GET'])
def getAllSales():
    sales = []
    dbUtils = DbUtils()
    salesData = dbUtils.getAllSales()

    for c in salesData:
        a = {"Id" : c[0], "Fornecedor" : c[1], "Produto" : c[2], "Categoria" : c[3], "Data de Compra" : c[4], "Valor" : str(c[5]), "Quantidade" : c[6], "Ativo" : c[7]}
        sales.append(a)
    
    return jsonify(sales)

@app.route('/getsalebyid', methods=['POST'])
def getSalesById():
    if not request.json:
        abort(400)

    datas = request.get_json()
    dbUtils = DbUtils()

    idSale = datas['idSale']

    sale = dbUtils.getSaleById(idSale)

    for c in sale:
        a = {"Id" : c[0], "Fornecedor" : c[1], "Produto" : c[2], "Categoria" : c[3], "Data de Compra" : c[4], "Valor" : str(c[5]), "Quantidade" : c[6], "Ativo" : c[7]}
    
    return jsonify(a)

# --------------- SERVICE para VENDAS --------------- #
@app.route('/insertexit', methods = ['POST'])
def insertExit():
    if not request.json:
        abort(400)

    dbUtils = DbUtils()
    datas = request.get_json()

    idVendedor = datas['idVendedor']
    idProduto = datas['idProduto']
    quantidade = datas['quantidade']

    produto = dbUtils.getProductById(idProduto)

    for p in produto:
        valorTotal = int(quantidade) * float(p[5])
        idCategoria = p[2]
        # Adicionando ao estoque
        quantidadeProduto = int(p[6]) - int(quantidade)

    if(quantidadeProduto > 0):
        if(dbUtils.insertExit(idVendedor, idProduto, idCategoria, valorTotal, quantidade, 1)):
            if(dbUtils.updateQuantityProductById(idProduto, quantidadeProduto)):
                result = {"result" : "Venda efetuada com Sucesso", "update" : "Ok"}
            else:
                result = {"update" : "False"}
        else:
            result = {"result" : "Problema ao efetuar a venda, tente novamente!"}
    else:
        result = {"return" : "Não é possivel, pois nao temos prudutos no estoque"}
    
    return jsonify(result)


# Main
if __name__ == '__main__':
    app.run()