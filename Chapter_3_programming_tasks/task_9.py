number = int(input("Enter a number: "))
if 0 < number < 11:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif 10 < number < 19:
    if number % 2 == 0:
        print("Red")
    else:
        print("Black")
elif 18 < number < 29:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif 28 < number < 37:
    if number % 2 == 0:
        print("Red")
    else:
        print("Black")
elif number == 0:
    print("Green")
elif number < 0 or number > 36:
    print("Error")