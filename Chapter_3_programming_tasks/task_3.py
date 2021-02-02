age = int(input("Enter your age: "))
if age <= 1:
    print("You are baby!")
elif 1 < age < 13:
    print("You are child")
elif age <= 13 and age < 20:
    print("You are teenager")
elif 20 <= age < 100:
    print("You are adult")
else:
    print("You are spirit")
