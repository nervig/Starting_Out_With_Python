import os


def main():
    flag = False

    search_student = input("Enter name of student which record about you're going to update: ")
    update_value = input("Enter a new value for the string: ")
    open_list_students = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    read_string = open_list_students.readline()
    while read_string != '':
        scores = int(open_list_students.readline())
        read_string = read_string.rstrip('\n')
        if read_string == search_student:
            temp_file.write(read_string + '\n')
            temp_file.write(str(update_value) + '\n')
            flag = True
        else:
            temp_file.write(read_string + '\n')
            temp_file.write(str(scores) + '\n')
        read_string = open_list_students.readline()

    open_list_students.close()
    temp_file.close()
    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if flag:
        print("The file was update")
    else:
        print("The value wasn't found")


main()