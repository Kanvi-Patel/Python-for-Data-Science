class Product():
    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

p1=Product()
p1.set_price(500)
print("Price:",p1.get_price())
