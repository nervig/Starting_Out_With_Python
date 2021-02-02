read_file = open('free_text.txt', 'r')
my_many = set()
my_list = []
line = read_file.readline()
while line != '':
    my_list += line.split()
    line = read_file.readline()
my_many = set(my_list)
print(my_list)
print(my_many)