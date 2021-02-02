def shedule():

    cabs = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'CS104': 1244, 'CS105': 1411}
    teachers = {'CS101': 'Hains', 'CS102': 'Albarado', 'CS103': 'Rich', 'NT110': 'Berk', 'CM241': 'Li'}
    times = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}
    number_of_course = input("Enter a number of course :")
    print("Number of audience | Name of teacher | Time of course")
    try:
        print(str(cabs[number_of_course]), end='')
    except KeyError:
        print('Not found', end='')
    try:
        print('\t\t\t\t' + str(teachers[number_of_course]), end='')
    except KeyError:
        print('\t\t\t\tNot found', end='')
    try:
        print('\t\t\t\t' + str(times[number_of_course]), end='')
    except KeyError:
        print('\t\t\t\tNot found', end='')


shedule()

