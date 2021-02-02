import pet


def main():
    name = input('Name: ')
    animal_type = input('Animal type: ')
    age = input('Age: ')

    my_pet = pet.Pet(name, animal_type, age)

    print('You are entered these data:')
    print('Name: ', my_pet.get_name())
    print('Animal type: ', my_pet.get_animal_type())
    print('Age: ', my_pet.get_age())


main()
