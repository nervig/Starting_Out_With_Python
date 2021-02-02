import re
def read_1txt_and_write_to_list():
    read_text_file = open('test_text.txt', 'r')
    list_of_words_of_text = []
    line = read_text_file.readline()

    while line != '':
        line_clear = ''.join(re.findall(r'[а-яА-Я ]', line))
        list_of_words_of_text += line_clear.lower().split()
        line = read_text_file.readline()
    print(list_of_words_of_text)
    return list_of_words_of_text


def read_2txt_and_write_to_list():
    read_text_file = open('test_text2.txt', 'r')
    list_of_words_of_text2 = []
    line = read_text_file.readline()

    while line != '':
        line_clear = ''.join(re.findall(r'[а-яА-Я ]', line))
        list_of_words_of_text2 += line_clear.lower().split()
        line = read_text_file.readline()
    print(list_of_words_of_text2)
    return list_of_words_of_text2


def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    for word_set1 in set1:
        print(word_set1, end=' ')
    print()
    for word_set2 in set2:
        print(word_set2, end=' ')
    print()

    overlap_both_files = set1.intersection(set2)
    for word in overlap_both_files:
        print(word, end=' ')
    print()

    difference_both_files = set1.difference(set2)
    for word_diff in difference_both_files:
        print(word_diff, end=' ')
    print()

    difference_both_files2 = set2.difference(set1)
    for word_diff2 in difference_both_files2:
        print(word_diff2, end=' ')
    print()

    symmetric_both_files = set1.symmetric_difference(set2)
    for word_symmetric in symmetric_both_files:
        print(word_symmetric, end=' ')


# read_1txt_and_write_to_list()
# read_2txt_and_write_to_list()
compare_lists(read_1txt_and_write_to_list(), read_2txt_and_write_to_list())