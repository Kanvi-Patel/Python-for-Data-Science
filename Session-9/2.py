def get_delivery_charge(amount, city='Ahmedabad'):
    if city=="Ahmedabad":
        return 0
    else:
        return 50


print("Delivery charge:",get_delivery_charge(500,"ghandhinagar"))
print("Delivery charge:",get_delivery_charge(500))
