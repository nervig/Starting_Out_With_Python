positive_number = 0
sum_number = 0
while positive_number >= 0:
    positive_number = int(input("Enter any positive number: "))
    if positive_number >= 0:
        sum_number += positive_number
    else:
        print("Total sum: " + str(sum_number))
