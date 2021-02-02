def main():
    read_students = open('students.txt', 'r')
    name_student = read_students.readline()
    while name_student != '':
        score_student = int(read_students.readline())
        name_student = name_student.rstrip('\n')

        # show the record
        print("Name of students: ", name_student)
        print("Numbers of score of students: ", score_student)
        name_student = read_students.readline()

    # close the file
    read_students.close()


# call main function
main()