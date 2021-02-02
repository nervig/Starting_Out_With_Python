audited_year = int(input("Enter an audited year: "))
if audited_year % 100 == 0:
    if audited_year % 400 == 0:
        print("Audited year is leap")
elif audited_year % 100 != 0:
    if audited_year % 4 == 0:
        print("Audited year is leap")
else:
    print("The checked year is normal")
