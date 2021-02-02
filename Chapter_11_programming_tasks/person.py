class Person():
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number


class Customer(Person):
    def __init__(self, name, address, phone_number, id_num, mailing):
        Person.__init__(self, name, address, phone_number)
        self.__id_num = id_num
        self.__mailing = mailing

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_mailing(self, mailing):
        self.__mailing = mailing

    def get_id_num(self):
        return self.__id_num

    def get_mailing(self):
        return self.__mailing
