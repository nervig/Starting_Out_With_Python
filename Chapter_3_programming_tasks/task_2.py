length_rectangle_1 = int(input("Enter length of rectangle 1: "))
height_rectangle_1 = int(input("Enter height of rectangle 1: "))
s_rectangle_1 = length_rectangle_1 * height_rectangle_1
length_rectangle_2 = int(input("Enter length of rectangle 2: "))
height_rectangle_2 = int(input("Enter height of rectangle 2: "))
s_rectangle_2 = length_rectangle_2 * height_rectangle_2
if s_rectangle_1 == s_rectangle_2:
    print("The rectangles are equal!")
elif s_rectangle_1 > s_rectangle_2:
    print("The first rectangle is more than second")
else:
    print("The second rectangle is more than first")