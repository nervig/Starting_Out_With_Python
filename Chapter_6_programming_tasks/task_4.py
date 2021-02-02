def main():
    open_read_file = open('names.txt', 'r')
    total = 0
    string = open_read_file.readline()
    while string != '':
        string = string.rstrip('\n')
        print(string)
        string = open_read_file.readline()
        total += 1
    print(total)
    open_read_file.close()


main()
