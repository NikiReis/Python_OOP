import datetime


class Category:
    def __init__(self, category):
        self.category = category


class Products:
    def __init__(self, nome, price, category):
        self.nome = nome
        self.price = price
        self.category = category


class Warehouse:
    def __init__(self, product: Products, quantity):
        self.product = product,
        self.quantity = quantity


class Sell:
    def __init__(self, itenSold: Products, seller, buyer, QuantitySold,
                 date=datetime.datetime.now().strftime("%d-%m-%Y")
                 ):

        self.itenSold = itenSold,
        self.seller = seller,
        self.buyer = buyer,
        self.quantitysold = QuantitySold
        self.Date = date


class Supplier:
    def __init__(self, name, cnpj, phone, category):
        self.name = name
        self.category = category
        self.cnpj = cnpj
        self.phone = phone


class Person:
    def __init__(self, name, cpf, email, address, phone):
        self.name = name,
        self.cpf = cpf,
        self.address = address,
        self.phone = phone,
        self.email = email


class Employee(Person):
    def __init__(self, name, email, cpf, phone, address, clt):
        self.clt = clt
        super(Employee, self).__init__(name, cpf, email, address, phone)
