print("Restart your PC and try to connect\nYou fix a problem? ")
answer = input()
if answer == "no":
    print("Restart your router and try to connect\nYou fix a problem? ")
    answer = input()
    if answer == "no":
        print("Take a new router")
    else:
        print("Have a nice day!")
else:
    print("Have a nice day!")