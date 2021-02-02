def main():
    # infile = open('numbers.txt', 'r')
    # numbers = infile.read()
    # while numbers != '':
    #
    #     print(numbers)
    #     numbers = infile.read()
    # infile.close()
    infile = open('numbers.txt', 'r')
    for i in infile:
        numbers = infile.read()
    infile.close()
    print(numbers)
main()
