from Model import *


class DaoCategory:

    @classmethod
    def save(cls, category):
        with open("category.txt", "a") as f:
            f.writelines(category)
            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("category.txt", "r") as f:
            cls.category = f.readlines()
        cls.category = list(map(lambda x: x.replace("\n", ""), cls.category))
        cat = list()
        for x in cls.category:
            cat.append(Category(x))
        return cat


class DaoSells:
    @classmethod
    def save(cls, sell: Sell):
        with open("sells.txt", "a") as f:
            f.writelines(sell.itenSold.name + "|" + sell.itenSold.price + "|" +
                         sell.itenSold.category + "|" + sell.itenSold.seller + "|" + str(sell.itenSold.quantity)
                         + "|" + sell.itenSold.buyer + "|" + sell.itenSold.date
                         )
            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("sell.txt", "r") as f:
            cls.sell = f.readlines()
        cls.sell = list(map(lambda x: x.replace("\n", ""), cls.sell))
        cls.sell = list(map(lambda x: x.split("|"), cls.sell))

        set_of_sells = []
        for x in cls.sell:
            set_of_sells.append(Sell(Products(x[0], x[1], x[2]), x[3], x[4], x[5], x[6]))
        return set_of_sells


class DaoWarehouse:
    @classmethod
    def save(cls, product: Products, quantity):
        with open("warehouse.txt", "a") as f:
            f.writelines(product.nome + "|" + product.price + "|" + product.price + "|" + str(quantity))
            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("warehouse.txt", "r") as f:
            cls.warehouse = f.readlines()
        cls.warehouse = list(map(lambda x: x.replace("\n", ""), cls.warehouse))
        cls.warehouse = list(map(lambda x: x.split("|"), cls.warehouse))

        ware = []
        if len(cls.warehouse) > 0:
            for x in cls.warehouse:
                ware.append(Warehouse(Products(x[0], x[1], x[2]), x[3]))
        return ware


class DaoSupplier:
    @classmethod
    def save(cls, supplier: Supplier):
        with open("supplier.txt", "a") as f:
            cls.supplier = f.writelines(
                supplier.name + "|" +
                supplier.cnpj + "|" +
                supplier.phone + "|" +
                supplier.category
            )
            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("supplier.txt", "r") as f:
            cls.supplier = f.readlines()

        cls.supplier = list(map(lambda x: x.replace("\n", ""), cls.supplier))
        cls.supplier = list(map(lambda x: x.split("|"), cls.supplier))

        sup = []
        for x in cls.supplier:
            sup.append(Supplier(x[0], x[1], x[2], x[3]))
        return sup


class DaoPerson:
    @classmethod
    def save(cls, person: Person):
        with open("customer.txt", "a") as f:
            f.writelines(
                person.name + "|" +
                person.cpf + "|" +
                person.email + "|" +
                person.phone + "|" +
                person.address
            )

            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("customer.txt", "r") as f:
            cls.customer = f.readlines()
        cls.customer = list(map(lambda x: x.replace("\n", ""), cls.customer))
        cls.customer = list(map(lambda x: x.split("|"), cls.customer))


class DaoEmployee:
    @classmethod
    def save(cls, person: Employee):
        with open("employees.txt", "a") as f:
            f.writelines(
                person.name + "|" +
                person.cpf + "|" +
                person.email + "|" +
                person.phone + "|" +
                person.clt + "|" +
                person.address
            )
            f.writelines("\n")

    @classmethod
    def read(cls):
        with open("employees.txt", "r") as f:
            cls.employee = f.readlines()
        cls.employee = list(map(lambda x: x.replace("\n", ""), cls.employee))
        cls.employee = list(map(lambda x: x.split("|"), cls.employee))

        employee_list = []
        for x in cls.employee:
            employee_list.append(Employee(x[0], x[1], x[2], x[3], x[4], x[5]))
        return employee_list
