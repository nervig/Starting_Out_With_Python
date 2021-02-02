vegetarian = input("Will there be a vegetarian? ")
vegan = input("Will there be a vegan? ")
gluten_free = input("Will a gluten-free diet follower? ")
if vegetarian == "yes" and gluten_free == "yes" and vegan == "yes":
    print("Your choice the\n 'Cafe around the corner'\n'Chef\'s kitchen'")
else:
    if vegetarian == "yes" and gluten_free == "yes":
        print("Your choice the 'Central pizzeria'")
    else:
        if vegetarian == "yes":
            print("Your choice central pizzeria , Dishes from an Italian mom, cafe around the corner, chef's kitchen.")
        elif vegan == "yes":
            print("Your choice cafe around the corner, chef's kitchen.")
        elif gluten_free == "yes":
            print("Your choice central pizzeria, cafe around the corner, chef's kitchen.")
        else:
            print("Your choice gourmet burgers from Joe")