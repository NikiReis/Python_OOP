class Item:
    pay_rate = 0.8 #pay rate after 20% of discount
    all = []
    def __init__(self,name: str,price:float,quantity=0):

        assert price >=0, f"Price {price} is nor greather or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is nor greather or equal to zero"

        self.Name = name
        self.Price = price
        self.Quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.Quantity*self.Price

    def apply_discount(self):
        self.Price = self.Price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.Name}',{self.Price},{self.Quantity})"

item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

print(Item.all)
