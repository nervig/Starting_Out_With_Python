import re
def read_txt_and_write_to_list():
    read_text_file = open('test_text.txt', 'r')
    list_of_words_of_text = []
    line = read_text_file.readline()

    while line != '':
        line_clear = ''.join(re.findall(r'[а-яА-Я ]', line))
        list_of_words_of_text += line_clear.lower().split()
        line = read_text_file.readline()
    return list_of_words_of_text


def filling_dictionary(list_words):
    my_dict = {}
    for item in list_words:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    return my_dict


def print_dict(dict):
    for key, value in dict.items():
        print(key + ": " + str(value))


print_dict(filling_dictionary(read_txt_and_write_to_list()))
