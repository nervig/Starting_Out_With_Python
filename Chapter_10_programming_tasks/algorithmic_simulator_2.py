class Book:
    def __init__(self, title, name_of_author, name_of_make):
        self.__title = title
        self.__name_of_author = name_of_author
        self.__name_of_make = name_of_make

    def set_title(self, title):
        self.__title = title

    def set_name_of_author(self, name_of_author):
        self.__name_of_author = name_of_author

    def set_name_of_make(self, name_of_make):
        self.__name_of_make = name_of_make

    def get_title(self):
        return self.__title

    def get_name_of_author(self):
        return self.__name_of_author

    def get_name_of_make(self):
        return self.__name_of_make

    def __str__(self):
        return "Title: " + self.__title + \
            "\nName of author: " + self.__name_of_author + \
            "\nName of maker: " + self.__name_of_make
