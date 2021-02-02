number_book_purchased = int(input("Enter a number of book purchased: "))
points = 0
if 0 < number_book_purchased < 3:
    points = 5
elif 3 < number_book_purchased < 6:
    points = 15
elif 5 < number_book_purchased < 8:
    points = 30
elif 7 < number_book_purchased:
    points = 60
print("Your number of points equals " + str(points))
