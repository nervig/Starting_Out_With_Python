number_of_strings = int(input("Enter a number of strings: "))
for i in range(number_of_strings):
    print("#", end='')
    for x in range(i):
        print(" ", end='')
    print("#")