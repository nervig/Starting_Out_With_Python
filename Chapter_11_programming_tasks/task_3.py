import person

def main():
    name = input('Enter a name: ')
    address = input('Enter an address: ')
    phone_number = input('Enter a phone number: ')
    id_num = input('Enter an ID of person: ')
    mailing = bool(input('Mailing - yes(Space) or no(Enter): '))

    person_data = person.Customer(name, address, phone_number, id_num, mailing)

    print('Name: ' + person_data.get_name())
    print('Address: ' + person_data.get_address())
    print('Phone number: ' + person_data.get_phone_number())
    print('ID: ' + person_data.get_id_num())
    print('Mailing: ' + str(person_data.get_mailing()))


main()