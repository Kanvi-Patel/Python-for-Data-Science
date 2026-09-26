class Ticket():
    def __init__(self, price):
        self.price = price
    def get_final_price(self):
        print("Ticket Price:",self.price)


class PremiumTicket(Ticket):
    def get_final_price(self):
        super().get_final_price()
        self.price=self.price+50
        print("Premium Ticket Price:",self.price)
        
t1=Ticket(500)
t1.get_final_price()

p1=PremiumTicket(500)
p1.get_final_price()


        
