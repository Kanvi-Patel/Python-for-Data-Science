import re

text="Contact me at kanvi@gmail.com or jay123@yahoo.com for more information."

new_text=re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', '[hidden email]', text)

print(new_text)
