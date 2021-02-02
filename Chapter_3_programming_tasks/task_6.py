month = int(input("Enter month "))
day = int(input("Enter day "))
year = int(input("Enter year(YY) "))
if month * day == year:
    print("Entered date is magic!")
else:
    print("Date is regular")