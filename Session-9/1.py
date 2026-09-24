def calculate_final_price(price,discount_rate):
    discount=price*discount_rate/100
    final_price=price-discount
    return final_price

print("Final price after discount: ",calculate_final_price(2500,5))
