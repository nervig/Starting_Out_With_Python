starting_number_stars = int(input("Enter starting number of stars: "))
number_of_strings = int(input("Enter a number of strings: "))
for i in range(number_of_strings):
    for x in range(starting_number_stars):
        print("*", end='')
    starting_number_stars -= 1
    print()