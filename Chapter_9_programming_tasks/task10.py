read_file = open('test_text.txt', 'r')
line = read_file.readline()
counter = 1
dict_words = {}
while line != '':
    if line == '\n':
        counter += 1
    word_list = line.split()
    for word in word_list:
        if word in dict_words:
            dict_words[word] += str(counter) + ' '
        else:
            dict_words[word] = str(counter) + ' '
    line = read_file.readline()

for item, value in dict_words.items():
    print(item + ': ' + value)