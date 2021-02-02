import employee

def main():
    name_of_employee = input('Enter a name of employee: ')
    number_of_employee = input('Enter a number of employee: ')
    shift_number = input('Enter a shift number: ')
    hourly_rate = input('Enter a hourly rate: ')

    data_of_product_worker = employee.ProductionWorker(name_of_employee, number_of_employee, shift_number, hourly_rate)

    print('Data of product worker: ')
    print('Name: ' + data_of_product_worker.get_name_of_employee())
    print('ID: ' + data_of_product_worker.get_number_of_employee())
    print('Shift number: ' + data_of_product_worker.get_shift_number())
    print('Hourly rate: ' + data_of_product_worker.get_hourly_rate())


main()