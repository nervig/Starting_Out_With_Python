def main():
    file_name_from_user = input("Enter a name of file that you are going to open: ")
    open_file = open(file_name_from_user, 'r')
    for i in range(5):
        read_line = open_file.readline()
        read_line = read_line.rstrip('\n')
        print(read_line)
    open_file.close()


main()