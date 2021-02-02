test_string = "StopAndFeelTheSmellOfRoses"
new_list_of_string = test_string.split()
new_string = [test_string[0]] # add first symbol
for i in range(1, len(test_string)):
    if test_string[i].isupper():
        new_string.append(" " + test_string[i].lower())
    else:
        new_string.append(test_string[i])

print(''.join(new_string))

# new_string = ''
# for i in range(1, len(test_string)):
#     if test_string[i].isupper():
#         new_string = test_string.replace(test_string[i], " " + test_string[i].lower())
#         test_string = new_string
# print(new_string)
