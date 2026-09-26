class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_discounted_price(self):
        self.price=self.price-self.price*0.1
        return self.price

class Electronics(Product):
    def get_discounted_price(self):
        self.price=self.price-self.price*0.2
        return self.price

def show_final_price(item):
    print("Name:",item.name)
    print("Final Price:",item.get_discounted_price())

p1=Product("Purse",1450)
e1=Electronics("Laptop",60000)

show_final_price(p1)
show_final_price(e1)
