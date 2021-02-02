import random


def main():
    num_list = []
    for i in range(15):
        num_list.append(random.randint(0, 100))
    print(num_list)
    user_num = int(input('Enter a number: '))
    comparison_numbers(num_list, user_num)


def comparison_numbers(num_list, num):
    for number in num_list:
        if number > num:
            print(number)


main()