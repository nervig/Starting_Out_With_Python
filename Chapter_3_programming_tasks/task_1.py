#!/usr/bin/python
number = int(input("Enter a number in range from 1 to 7: "))

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Thursday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
elif number > 7 or number < 1:
    print("You entered a number in incorrect range!")