from flask import Flask, url_for, request, json, jsonify
from json import dumps

# Aqui temos os Imports necessarios para realizar cadastros e compras
from sales import Sale
from client import Client
from product import Product

app = Flask(__name__)

Clients = []
Products = []
Sales = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

# Rota para inserção de um client
@app.route('/insertClient', methods = ['POST'])
def insertClient():
    global Clients
    datas = request.get_json()
    id = datas['id']
    name = datas['name']
    email = datas['email']
    document = datas['document'] 
    Clients.append(Client(id, name, email, document))
    res = {'status': 'ok'}
    return jsonify(res)

# Rota para busca de um cliente pelo ID
@app.route('/getClientById', methods = ['POST'])
def getClientById():
    global Clients
    datas = request.get_json()
    print(Clients[0].getClientId())
    id = datas['id']
    res = {'status': 'Cliente nao encontrado'}
    for c in Clients:
        if(int(id) == int(c.getClientId())):
            res = {'id': id, 'nome': c.getClientName(), 'email': c.getClientEmail(), 'documento':c.getClientDocument()}
    return jsonify(res)

# Rota para retornar todos os clientes cadastrados
@app.route('/getAllClients', methods = ['GET'])
def getAllClients():
    payload = []
    content = {}
    
    for c in Clients:        
        content = {'id': str(c.getClientId()),'[Nome]': c.getClientName(), 
        '[Email]': str(c.getClientEmail()), '[Documento]': c.getClientDocument()}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)       
    return jsonify(ClientsList=res)

# Rota para criar todos os produtos de teste
@app.route('/createAllProducts', methods = ['GET'])
def createAllProducts():
    global Products 
    Products.append(Product(1, "Computador Dell", 4200.00))
    Products.append(Product(2, "Placa de Video RTX2080Ti", 7800.00))
    Products.append(Product(3, "Mouse Logitech", 110.00))
    Products.append(Product(4, "Teclado Razer", 800.00))
    res = {'status': 'ok'}
    return jsonify(res)

# Rota para inserção de um produto
@app.route('/insertProduct', methods = ['POST'])
def insertProduct():
    global Products
    datas = request.get_json()
    id = datas['id']
    name = datas['name']
    price = datas['price']
    Products.append(Product(id, name, price))
    res = {'status': 'ok'}
    return jsonify(res)

# Rota para busca de um produto pelo ID
@app.route('/getProductById', methods = ['POST'])
def getProductById():
    global Products
    datas = request.get_json()
    id = datas['id']
    res = {'status': 'Produto nao encontrado'}
    for p in Products:
        if(int(id) == int(p.getProductId())):
            res = {'[Id]': id, '[Nome]': p.getProductName(), '[Preco]': str(p.getProductPrice())}
    return jsonify(res)

# Rota para retornar todos os produtos
@app.route('/getAllProducts', methods = ['GET'])
def getAllProducts():
    payload = []
    content = {}
    for p in Products:        
        content = {'id': str(p.getProductId()),'[Nome]': p.getProductName(), '[Preco]': str(p.getProductPrice())}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)       
    return jsonify(ProductsList=res)

# Rota para inserir uma venda
@app.route('/insertSale', methods = ['POST'])
def insertSale():
    global Sales
    datas = request.get_json()
    id = datas['id']
    idClient = datas['idClient']
    idProduct = datas['idProduct']
    quantity = datas['quantity'] 
    value = 0.00
    for p in Products:
        if(int(idProduct) == int(p.getProductId())):
            value = float(p.getProductPrice()) * int(quantity)

    Sales.append(Sale(id, idClient, idProduct, quantity, value))
    res = {'status': 'ok'}
    return jsonify(res)

# Rota para retornar todas as vendas
@app.route('/getAllSales', methods = ['GET'])
def getAllSales():
    payload = []
    content = {}
    for s in Sales:        
        content = {'id': str(s.getSaleId()),'[IDCliente]': str(s.getSaleIdClient()), 
        '[IDProduto]': str(s.getSaleIdProduct()), '[Quantidade]':str(s.getSaleQuantity()), '[Total]':str(s.getSaleTotal())}
        payload.append(content)
        content = {}
    res =  json.dumps(payload)   
    return jsonify(ProductsList=res)

@app.route('/getTotalByClientId', methods=['POST'])
def getTotalByClientId():
    global Clients, Products, Sales
    cliente = None
    SalesById = []
    totalValue = 0

    datas = request.get_json()
    id = datas['id']

    # Agora iremos verificar qual o cliente
    for c in Clients:
        if(int(id) == int(c.getClientId())):
            cliente = c

    # Verificar todas as compras que esse cliente executou
    for s in Sales:
        if(int(id) == int(s.getSaleIdClient())):
            content = {'id' : s.getSaleId(), '[IDProduto]' : s.getSaleIdProduct(), '[Quantidade]' : s.getSaleQuantity(), '[Total]' : 'R$ ' + str(s.getSaleTotal())}
            SalesById.append(content)
            totalValue += float(s.getSaleTotal())
    
    totalValue = round(totalValue, 2)
    res = json.dumps(SalesById)
    return jsonify({'[Cliente]' : cliente.getClientName(), '[Compras]' : res, '[TOTAL Gasto pelo Cliente]' : 'R$ ' + str(totalValue)})

if __name__ == '__main__':
    app.run()