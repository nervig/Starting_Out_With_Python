import random


def main():
    amount_random_numbers = int(input("Enter a number of random numbers: "))
    file_numbers = open("random_num.txt", "w")
    for i in range(1, amount_random_numbers + 1):
        number = random.randint(1, 501)
        file_numbers.write(str(number) + '\n')
    file_numbers.close()


main()
