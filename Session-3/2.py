# Question 2: Flipkart total cart amount

list_of_products=["199.99","49","350.75"]

def total_cart_amount(prices):
    total=0
    for i in prices:
        total=total+float(i)
    print("Total cart amount:",total)
total_cart_amount(list_of_products)


