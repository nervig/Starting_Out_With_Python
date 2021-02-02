class Employee:
    def __init__(self, name_of_employee, number_of_employee):
        self.__name_of_employee = name_of_employee
        self.__number_of_employee = number_of_employee

    def set_name_of_employee(self, name_of_employee):
        self.__name_of_employee = name_of_employee

    def set_number_of_employee(self, number_of_employee):
        self.__number_of_employee = number_of_employee

    def get_name_of_employee(self):
        return self.__name_of_employee

    def get_number_of_employee(self):
        return self.__number_of_employee


class ProductionWorker(Employee):
    def __init__(self, name_of_employee, number_of_employee, shift_number, hourly_rate):
        Employee.__init__(self, name_of_employee, number_of_employee)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate


    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_rate


class ShiftSupervisor(Employee):
    def __init__(self, name_of_employee, number_of_employee, annual_salary, annual_bonus):
        Employee.__init__(self, name_of_employee, number_of_employee)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus
