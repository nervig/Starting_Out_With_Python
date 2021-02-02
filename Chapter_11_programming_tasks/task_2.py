import employee


def main():
    name_of_employee = input('Enter a name of employee: ')
    number_of_employee = input('Enter a number of employee: ')
    annual_salary = input('Enter an annual salary: ')
    annual_bonus = input('Enter an annual bonus: ')

    data_of_shift_supervisor = employee.ShiftSupervisor(name_of_employee, number_of_employee, annual_salary, annual_bonus)

    print('The data of shift supervisor: ')
    print('Name: ' + data_of_shift_supervisor.get_name_of_employee())
    print('ID: ' + data_of_shift_supervisor.get_number_of_employee())
    print('Annual salary: ' + data_of_shift_supervisor.get_annual_salary())
    print('Annual bonus: ' + data_of_shift_supervisor.get_annual_bonus())


main()