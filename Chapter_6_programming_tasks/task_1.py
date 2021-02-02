def main():
    file_read = open('numbers.txt', 'r')
    print(file_read.read())
    file_read.close()


main()