from functools import reduce

prices=[499, 1299, 299, 799]

total=reduce(lambda a,b:a+b,prices)

print("Total:",total)

