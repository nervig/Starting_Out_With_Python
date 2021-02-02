import random


def main():
    number_from_user = int(input("Enter a guess number "))
    comparison_numbers(number_from_user)


def comparison_numbers(number_from_user):
    guess_number = random.randint(1, 101)
    count = 0
    while number_from_user != guess_number:
        if number_from_user < guess_number:
            print("More!")
        else:
            print("Less!")
        count += 1
        number_from_user = int(input("Enter a new number: "))
    print("You win! You spend a {} attempt.".format(count))


main()
