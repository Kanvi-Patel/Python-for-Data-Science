def format_followers(number):
    if number>=1000000:
        return str(number/1000000)+"M"
    elif number>=1000:
        return str(number/1000)+"K"
    else:
        return number


follower_counts=[950, 1500, 25000, 1200000]

l1=list(map(format_followers,follower_counts))
print(l1)
