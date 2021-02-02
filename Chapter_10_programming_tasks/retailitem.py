class RetailItem:
    def __init__(self, description, amount, price):
        self.__description = description
        self.__amount = amount
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_amount(self, amount):
        self.__amount = amount

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_amount(self):
        return self.__amount

    def get_price(self):
        return self.__price
