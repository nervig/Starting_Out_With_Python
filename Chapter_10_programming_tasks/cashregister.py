class Cashregister:
    def __init__(self, goods_list):
        self.__goods_list = goods_list

    def purchase_item(self, goods_list):
        self.__goods_list = goods_list

    def get_goods_list(self):
        return self.__goods_list

    def get_total(self):
        sum_price = 0
        goods_list = self.__goods_list
        for item in goods_list:
            sum_price += item.get_price()
        return sum_price

    def show_item(self):
        goods_list = self.__goods_list
        string_goods = ''
        for item in goods_list:
            string_goods += item.get_description() + '\n'
        return string_goods

    def list_clear(self):
        self.__goods_list.clear()
