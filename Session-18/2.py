import re

def check_date(string):
    pattern=r'\d{2}/\d{2}/\d{4}'
    
    if re.search(pattern, string):
        return True
    else:
        return False

print(check_date("My date is 25/09/2026"))
print(check_date("My date is 25-09-2026"))
print(check_date("My date is 25-9-2026"))
