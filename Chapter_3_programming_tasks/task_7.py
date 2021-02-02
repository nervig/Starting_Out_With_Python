first_color = input("Enter first color (red, blue or yellow) ")
second_color = input("Enter first color (red, blue or yellow), but not that was entered in first step ")

if (first_color == "blue" and second_color == "red") or (first_color == "red" and second_color == "blue"):
    print("Violet")
elif (first_color == "yellow" and second_color == "red") or (first_color == "red" and second_color == "yellow"):
    print("Orange")
elif (first_color == "blue" and second_color == "yellow") or (first_color == "yellow" and second_color == "blue"):
    print("Green")
else:
    print("Error")
