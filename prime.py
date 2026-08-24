month = int(input("Enter month number: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Month has 31 days")
elif month == 2:
    print("Month has 28 or 29 days on leap year")
else:
    print("Month has 30 days")