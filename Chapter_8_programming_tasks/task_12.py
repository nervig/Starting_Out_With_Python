test_string = 'Stop and feel the smell of roses'
test_string_list = test_string.split()
test_list = []
for item in test_string_list:
    for i in range(1, len(item)):
        test_list.append(item[i])
    test_list.append(item[0] + "ki ")
print(''.join(test_list))