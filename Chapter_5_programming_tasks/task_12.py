import random

def main():
    int1 = random.randint(100, 300)
    int2 = random.randint(100, 300)
    print("  " + str(int1))
    print("+ " + str(int2))
    sum = int1 + int2
    entered_number_user = int(input("Enter the sum numbers that was shown: "))
    if entered_number_user == sum:
        print("Congratulation! You entered a right answer!")
    else:
        print("The right answer is " + str(sum))


main()