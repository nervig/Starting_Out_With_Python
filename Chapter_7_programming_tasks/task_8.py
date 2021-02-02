import re

'''
from site "https://wjla.com/news/offbeat/most-popular-baby-names-the-decade" was copied 200 
a most popular names of boys and girls and was saved in boys_girls_names.txt. The list was in the following format:
with use a regular expressions from the file was got only names and was save in list "only names".
So list was sorted in two lists called "boys" and "girls".
'''
def sort_names():
    read_file_with_names = open("boys_girls_names.txt", "r")
    only_names = re.findall(r'([A-Z]+[a-z]+)', read_file_with_names.read())
    boys = []
    girls = []
    for i in range(len(only_names)):
        if i % 2 == 0:
            boys.append(only_names[i])
        else:
            girls.append(only_names[i])
    read_file_with_names.close()
    return boys, girls


def select_name(list1, list2):
    name_from_user = input("Enter a name of boys or girls: ")

    if name_from_user in list1:
        print("The is in list of a most popular names of boys")
    elif name_from_user in list2:
        print("The is in list of a most popular names of girls")
    else:
        print("The is not popular name of girls or boys")


def main():
    boys, girls = sort_names()
    select_name(boys, girls)


main()
