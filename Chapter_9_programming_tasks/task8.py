import pickle
output_file = open('email_data.dat', 'wb')
select = int(input("Enter 1 if you would be find an email address of persona\n"
               "Enter 2 if you would be add new email address\n"
               "Enter 3 if you would be rename name of person of rename name of email address\n"
               "Enter 4 if you would be delete email address\n:"))


dict_of_users = {"ankern@mail.ru": "Andrew"}
flag_word = "yes"
while flag_word == "yes":
    if select == 1:
        value = input("Enter a name of person: ")
        for email, name in dict_of_users.items():
            if name == value:
                print(email)
    if select == 2:
        key = input("Enter a name of email address: ")
        value = input("Enter a name of new person: ")
        dict_of_users[key] = value
        print("New person is added!")
    if select == 3:
        value = input("Enter a name of person: ")
        new_value = input("Enter a new name of person: ")
        for email, name in dict_of_users.items():
            if name == value:
                dict_of_users.update({email: new_value})
                print(dict_of_users)
    if select == 4:
        value = input("Enter a name of person for deleting: ")
        delete_person = dict_of_users.pop(value, "The record not found")
        print("The record " + delete_person + "had deleted")

    flag_word = input("Do you would be to continue? Enter 'yes' if yes, enter 'no' if not: ")
pickle.dump(dict_of_users, output_file)
output_file.close()
