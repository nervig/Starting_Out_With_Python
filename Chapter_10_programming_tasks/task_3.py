import information

def main():
    my_data = information.Information('Andrew', 'Lugovaya 18', '37', '+79181112233')

    print('The information is about me: ')
    print('Name: ' + my_data.get_name())
    print('Address: ' + my_data.get_address())
    print('Age: ' + my_data.get_age())
    print('Phone number: ' + my_data.get_phone_number())
    print()

    son_data = information.Information('Antony', 'Lugovaya 18', '13', '+79184561214')

    print('The information is about my son: ')
    print('Name: ' + son_data.get_name())
    print('Address: ' + son_data.get_address())
    print('Age: ' + son_data.get_age())
    print('Phone number: ' + son_data.get_phone_number())
    print()

    wife_data = information.Information('Svetlana', 'Lugovaya 18', '38', '+79187892839')

    print('The information is about my son: ')
    print('Name: ' + wife_data.get_name())
    print('Address: ' + wife_data.get_address())
    print('Age: ' + wife_data.get_age())
    print('Phone number: ' + wife_data.get_phone_number())
    print()

main()