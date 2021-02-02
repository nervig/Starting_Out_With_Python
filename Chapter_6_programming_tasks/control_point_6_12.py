def main():
    numbers = open('numbers.txt', 'w')
    for i in range(0, 11):
        numbers.write(str(i) + '\n')

    numbers.close()


main()