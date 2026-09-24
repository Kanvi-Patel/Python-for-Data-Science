def format_price(price,currency="INR"):
    if currency=="INR":
        return f"₹{price}"
    else:
        return f"${price}"


print(format_price(1000))
print(format_price(1000,"USD"))
