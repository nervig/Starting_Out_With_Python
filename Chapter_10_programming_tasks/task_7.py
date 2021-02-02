import employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employees.dat'


def main():
    employees = load_employee()

    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    save_employees(employees)


def load_employee():
    try:
        input_file = open(FILENAME, 'rb')

        employee_dct = pickle.load(input_file)

        input_file.close()
    except IOError:
        employee_dct = {}
    return employee_dct


def get_menu_choice():
    print()
    print('Menu')
    print('______________________________________')
    print('1. Find the employee')
    print('2. Add an employee')
    print('3. Change a data of employee')
    print('4. Delete a data of employee')
    print('5. Quit from the program')

    choice = int(input('Enter a selected item: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a selected item: '))
    return choice


def look_up(employees):
    id_employee = input('Enter an ID of employee: ')
    print(employees.get(id_employee, 'This ID not found'))


def add(employees):
    name = input('Name: ')
    id_employee = input('ID: ')
    department = input('Department: ')
    position = input('Position: ')

    entry = employee.Employee(name, id_employee, department, position)
    if id_employee not in employees:
        employees[id_employee] = entry
        print('A record added')
    else:
        print('The ID already exist')


def change(employees):
    id_employee = input('Enter the ID: ')
    if id_employee in employees:
        name = input('Enter a new name: ')
        department = input('Enter a department: ')
        position = input('Enter a position: ')

        entry = employee.Employee(name, id_employee, department, position)
        employees[id_employee] = entry
        print('Information was updated')
    else:
        print('The ID not found')


def delete(employees):
    id_employee = input('Enter the ID: ')
    if id_employee in employees:
        del employees[id_employee]
        print('The record was deleted: ')
    else:
        print('The ID not found')


def save_employees(employees):
    output_file = open(FILENAME, 'wb')

    pickle.dump(employees, output_file)

    output_file.close()


main()
