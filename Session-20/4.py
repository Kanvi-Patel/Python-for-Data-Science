from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass

class Paytm(PaymentMethod):
    def pay(self,amount):
        print("Paytm Amount:",amount)

class PhonePe(PaymentMethod):
    def pay(self,amount):
        print("Phonepe Amount:",amount)


paytm=Paytm()
phonepe=PhonePe()
paytm.pay(200)
phonepe.pay(500)

        
