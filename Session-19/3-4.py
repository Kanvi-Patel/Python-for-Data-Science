#Task:3
class FoodOrder():
    def __init__(self,restaurant_name,items,total_price):
        self.restaurant_name=restaurant_name
        self.items=items
        self.total_price=total_price
        print("Restaurant Name:",self.restaurant_name)
        print("Items:",self.items)
        print("Total:",self.total_price)
#Task:4
    def add_item(self,item_name,item_price):
        self.item_name=item_name
        self.item_price=item_price
        self.items.append(self.item_name)
        self.total_price=self.total_price+self.item_price
        print("Total Items:",self.items)
        print("Total Price:",self.total_price)

items=["Farmhouse Pizza","Garlic Bread"]
f1=FoodOrder("La Pino's Pizza",items, 499)
f1.add_item("Coke", 100)
f1.add_item("Lasagna", 400)
