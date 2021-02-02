string_test = "hi! my name is John. what is your name?"
new_string = ''
position = 0
for i in range(len(string_test)):
    string_test = string_test.replace(string_test[0], string_test[0].upper(), 1)
    if string_test[i] == "." or string_test[i] == "!":
        position = i + 2
        new_string = string_test.replace(string_test[position], string_test[position].upper(), 1)
        string_test = new_string
print(new_string)

