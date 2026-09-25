def format_number_short(n,unit=""):
    if n<1000:
        return str(n)+unit
    if n>=1000000:
        return format_number_short(n/1000000,"M")
    else:
        return format_number_short(n/1000,"K")


print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(500))
