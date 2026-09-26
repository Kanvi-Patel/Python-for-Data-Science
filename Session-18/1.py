import re
string="Hello My phone number is +91-9586211554 and +91-7854123694 and my old number was +91-78945612345"

phoneno=re.findall(r'\+91-\d{10}(?!\d)',string)
print(phoneno)
