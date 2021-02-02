read_text = open("text.txt", 'r')
letters_lower_case = 0
letters_upper_case = 0
number_amount = 0
space_amount = 0
for line in read_text:
    print(line)
    for symbol in line:
        if symbol.isupper():
            letters_upper_case += 1
        if symbol.islower():
            letters_lower_case += 1
        if symbol.isdigit():
            number_amount += 1
        if symbol.isspace():
            space_amount += 1
print("Amount of letters in upper case are " + str(letters_upper_case))
print("Amount of letters in lower case are " + str(letters_lower_case))
print("Amount of numbers " + str(number_amount))
print("Amount of spaces " + str(space_amount))
read_text.close()