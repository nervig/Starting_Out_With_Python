def max(a, b):
    if a > b:
        return a
    else:
        return b


def main():
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(max(number_1, number_2))


main()
