steps=[7500, 8200, 9500, 10500, 9000, 12000, 11000]

day=0

while day<len(steps):
    if steps[day]>10000:
        print("First day crossed 10,000 steps:", day + 1)
        break
    else:
        day=day+1



