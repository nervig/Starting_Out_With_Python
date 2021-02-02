# task 1
scientists = ['Ruby', 'einstein', 'newton', 'copernicus', 'kepler']

# task 2
numbers = []
for i in range(101):
    numbers.append(i)

print(numbers)

# task 3
# numbers2 = []
# for num in numbers:
#     numbers2.append(num)

#print(numbers2)

# task 5
def get_list(list_num):
    accumulator = 0
    for integer in list_num:
        accumulator += integer
    print(accumulator)


get_list(numbers)

# task 6
def found_name(list_names):
    found_name = 'Ruby'
    if found_name in list_names:
        print("Hi " + found_name)
    else:
        print("Ruby is not here")



found_name(scientists)


def two_dimentional_list():
    COLUMN = 3
    ROWS = 5
    two_dimentional_list = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
    for i in range(ROWS):
        for e in range(COLUMN):
            two_dimentional_list[i][e] = int(input('Enter a number: '))
    print(two_dimentional_list)

two_dimentional_list()