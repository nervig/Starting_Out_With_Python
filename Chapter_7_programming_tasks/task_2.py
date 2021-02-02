import random


def main():
    numbers_list = []
    for i in range(7):
        numbers_list.append(random.randint(0, 10))
    for number in numbers_list:
        print(number)


main()
