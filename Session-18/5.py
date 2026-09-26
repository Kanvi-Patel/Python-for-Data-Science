import re

text = """
Great photo! @kanvi_55
Amazing! @jay123
Nice post @parth_22
Love this! @priya
Follow @kanvi_55
Hello @mansi_123
Great work @jay
Wow @tisha_45
Nice @priya
Thanks @hetvi_99
"""

usernames=re.findall(r'@[A-Za-z0-9_]{3,}', text)

unique_usernames = set(usernames)

print("Instagram Usernames:", unique_usernames)
