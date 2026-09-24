def calculate_average_rating(total_rating,num_reviews):
        return total_rating/num_reviews
try:
    print(calculate_average_rating(500, 0))
    
except ZeroDivisionError as e:
    print("Cannot divide by zero.")

finally:
    print("Thank you for using the calculator")


