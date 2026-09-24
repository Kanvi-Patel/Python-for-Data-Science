prices = [325,0,450,500,0,1200]

total = 0

for i in prices:
    if i == 0:
        continue

    total = total + i

    if total > 2000:
        break

print("Total:", total)
