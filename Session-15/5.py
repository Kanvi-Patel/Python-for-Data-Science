def safe_divide_for_zomato(bill_amount,no_of_people):
    return bill_amount/no_of_people
    

bill_amount=int(input("Enter your bill amount:"))
no_of_people=int(input("Enter no of people:"))

try:
    print("Bill Per Person:",safe_divide_for_zomato(bill_amount,no_of_people))
except ZeroDivisionError as e:
    print("No of people can't be zero!")
else:
    print("Calculation successful!")
finally:
    print("Split calculation done")
