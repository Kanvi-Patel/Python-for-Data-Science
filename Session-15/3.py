class NoOffersApplied(Exception):
    message="No Offers were applied!"

total_spend=int(input("Enter your total spend:"))
offers=int(input("Enter the number of offers applied:"))

try:
    if offers==0:
        raise NoOffersApplied()
    else:
        division=total_spend/offers
        print("Average cashback per offer:", division)
    
except NoOffersApplied as e:
    print("Error:",e.message)
