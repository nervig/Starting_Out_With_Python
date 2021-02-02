import re
capitals_open = open('capitals.txt', 'r')

capitals_list = []
capitals = capitals_open.readline()
while capitals != '':
    capitals_list.append(capitals.rstrip('\n'))
    capitals = capitals_open.readline()
# print(capitals_list)
dict_capitals = {}
for item in capitals_list:
    item_list = re.findall(r'\w[А-я/-]+', item)
    # print(item_list)
    for i in item_list:
        key = i
        for i in item_list:
            value = i
        dict_capitals[str(key)] = str(value)
        break
print(dict_capitals)
capitals_open.close()

stop_word = "Да"
right_answer = 0
wrong_answer = 0
while stop_word == "Да":
    key_dict, value_dict = dict_capitals.popitem()
    print(key_dict)
    user_value = input("Enter the name of capital of country: ")

    if value_dict == user_value:
        print("Right!")
        right_answer += 1
    else:
        print("Wrong!")
        wrong_answer += 1
    stop_word = input("Do you want to continue? Enter 'Да' if you want ")

print("The amount of right answer is " + str(right_answer))
print("The amount of wrong answer is " + str(wrong_answer))

