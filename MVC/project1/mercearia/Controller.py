from Model import Category, Products, Warehouse, Supplier, Person, Sell, Employee
from Dao import DaoCategory, DaoSells, DaoWarehouse, DaoSupplier, DaoPerson, DaoEmployee
from datetime import datetime


class ControllerCategory:
    def register_category(self, new_category):
        exist = False
        ver = DaoCategory.read()
        for i in ver:
            if i.category == new_category:
                exist = True

        if not exist:
            DaoCategory.save(new_category)
            print("The category was saved successfully")
        else:
            print("The category already exists")

    def remove_category(self, remove_category):
        rmvar = DaoCategory.read()
        cat = list(filter(lambda rmvar: rmvar.category == remove_category, rmvar))

        if len(cat) <= 0:
            print("The category doesn't exists")
        else:
            for i in range(len(rmvar)):
                if rmvar[i].category == remove_category:
                    del rmvar[i]
                    break
            print("The category was removed successfully")

            with open("category.txt", "w") as f:
                for i in cat:
                    f.writelines(i.category)
                    f.writelines("\n")

    def alter_category(self, category_to_alter, category_changed):
        catgr = DaoCategory.read()
        cat = list(filter(lambda catgr: catgr.category_to_alter == category_to_alter, catgr))

        if len(cat) > 0:
            cat2 = list(filter(lambda catgr: catgr.category_to_alter == category_changed, catgr))
            if len(cat2) == 0:
                catgr = list(map(lambda catgr: Category(category_changed) if (
                        catgr.category == category_to_alter) else catgr, catgr))
            else:
                print("The category that you´re trying to change already exist")
        else:
            print("The category that you´re trying to change doesn't exist")

        with open("category.txt", "w") as f:
            for i in catgr:
                f.writelines(i.category)
                f.writelines("\n")


    def show_category(self):
        categories = DaoCategory.read()
        if len(categories) == 0:
            print("Empty Category")
        else:
            for x in categories:
                print(f"Category:{x.categories}")
