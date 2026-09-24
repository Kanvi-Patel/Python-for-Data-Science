total_cart_amount=int(input("Enter your total cart amount:"))
item_count=int(input("Enter you item count:"))

try:
    division=total_cart_amount/item_count
    print("Price per item:", division)
    
except ZeroDivisionError as e:
    print("Item count cannot be zero.")
