import csv

class Item:
    pay_rate = 0.8 #pay rate after 20% of discount
    all = []
    def __init__(self,name: str,price:float,quantity=0):

        assert price >=0, f"Price {price} is nor greather or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is nor greather or equal to zero"

        self.Name = name
        self.Price = price
        self.Quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.Quantity*self.Price

    def apply_discount(self):
        self.Price = self.Price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for x in items:
            Item(
                name=x.get('name'),
                price=float(x.get('price')),
                quantity=int(x.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero 
        if isinstance(num,float):
            #Count ou the floats that are point zero 
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.Name}',{self.Price},{self.Quantity})"
        
print(Item.is_integer())


