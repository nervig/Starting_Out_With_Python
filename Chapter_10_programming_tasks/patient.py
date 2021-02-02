class Patient:
    def __init__(self, name, address, phone, emergency_name):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__emergency_name = emergency_name

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency_name(self, emergency_name):
        self.__emergency_name = emergency_name

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_emergency_name(self):
        return self.__emergency_name

