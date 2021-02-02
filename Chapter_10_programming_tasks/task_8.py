import retailitem
import cashregister

STOP_PROGRAM = 0

print('Enter a data about goods: ')
choice = 1
object_list = []
while choice != STOP_PROGRAM:
    description = input('Enter a description of goods: ')
    amount = input('Enter an amount of goods: ')
    price = float(input('Enter a price of goods: '))
    print()

    goods = retailitem.RetailItem(description, amount, price)
    object_list.append(goods)
    goods_list = cashregister.Cashregister(object_list)

    choice = int(input('If you want continue enter 1, in opposite way enter 0: '))

print('Total of all purchases: ' + str(round(goods_list.get_total(), 2)))
print('List of all purchases: \n' + goods_list.show_item())
goods_list.list_clear()
