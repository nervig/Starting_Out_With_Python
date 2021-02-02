# creating a file and adding some records
def main():
    # create a variable for manage of cycle
    the_flag = 'y'
    # open the students.txt file in adding mode
    adding_students = open("students.txt", "a")
    while the_flag == 'y' or the_flag == 'Y':
        print("Enter an information are students about: ")
        name_student = input("Name of student: ")
        score_student = int(input("Enter a score of student: "))

        # add data to file
        adding_students.write(name_student + '\n')
        adding_students.write(str(score_student) + '\n')

        print("Do you want to add else data? 'y' if yes, 'n' if not: ")
        the_flag = input()

    # close the file
    adding_students.close()
    print("The data are added")

main()
