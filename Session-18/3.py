import re

text="I bought a shirt for Rs. 299, shoes for Rs. 1500 and a bag for Rs. 850."

prices=re.findall(r'Rs\. (\d+)', text)

new_prices=[]

for price in prices:
    price=int(price)
    new_prices.append(price)

print("Prices:", new_prices)
print("Total:", sum(new_prices))
