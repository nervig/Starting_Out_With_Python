def main():
    file_name_from_user = input("Enter a name of file that you are going to open: ")
    open_file = open(file_name_from_user, 'r')
    row_number = 1
    for row in open_file:
        row = row.rstrip('\n')
        if row_number < 10:
            print(' ' + str(row_number) + ':     ' + row)

        else:
            print(str(row_number) + ':     ' + row)
        row_number += 1
    open_file.close()


main()