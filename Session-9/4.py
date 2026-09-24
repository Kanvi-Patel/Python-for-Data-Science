def apply_coupon(price,coupon_code=None):
    if coupon_code=="ZOMATO10":
        price=price-price*10/100
        return price
    else:
        return price

print(apply_coupon(5000))
print(apply_coupon(2000,"ZOMATO10"))
