def prime_num(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False

    div = 5
    while div*div <= num:
        if num % div == 0 and num % (div + 2):
            return False
        div += 6
    return True


def main():
    num_user = int(input("Enter a number for range of numbers: "))
    for number in range(0, num_user):
        if prime_num(number):
            print(number, end=' ')


main()
