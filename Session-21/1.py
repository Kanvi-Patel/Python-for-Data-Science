class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_discounted_price(self):
        self.price=self.price-self.price*0.1
        return self.price

p1=Product("Purse",1450)
print("Product Discounted Price after 10% discount:",p1.get_discounted_price())




