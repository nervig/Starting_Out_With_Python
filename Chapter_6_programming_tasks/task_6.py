def main():
    open_read_file = open('numbers.txt', 'r')
    total = 0
    for numbers in open_read_file:
        total += int(numbers)
        print(numbers, end='')
    print('Average of numbers: ', total / 2)
    open_read_file.close()


main()