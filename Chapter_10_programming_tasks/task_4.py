import employee

employee_1 = employee.Employee('Susan Myers', '47899', 'accounting', 'vice-president')
employee_2 = employee.Employee('Mark Jones', '39119', 'IT', 'programmer')
employee_3 = employee.Employee('Joy Rogers', '81774', 'production', 'developer')

print('The date of employee 1')
print('Name ' + employee_1.get_name())
print('ID ' + employee_1.get_id())
print('Department ' + employee_1.get_department())
print('Position ' + employee_1.get_position())
print()

print('The date of employee 2')
print('Name ' + employee_2.get_name())
print('ID ' + employee_2.get_id())
print('Department ' + employee_2.get_department())
print('Position ' + employee_2.get_position())
print()

print('The date of employee 3')
print('Name ' + employee_3.get_name())
print('ID ' + employee_3.get_id())
print('Department ' + employee_3.get_department())
print('Position ' + employee_3.get_position())
print()
