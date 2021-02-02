class Vegetable:
    def __init__(self, vegtype):
        self.__vegtype = vegtype

    def message(self):
        print('I am vegetable')

    def print_type(self):
        print(self.__vegtype)


class Potato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self, 'potato')

    def message(self):
        print('I am potato')


v = Vegetable('Vegetable product')
p = Potato()
v.message()
p.message()
v.print_type()
p.print_type()
