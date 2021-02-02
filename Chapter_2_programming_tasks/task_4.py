#!/usr/bin/python
item_1 = float(input("Enter the product price: "))
item_2 = float(input("Enter the product price: "))
item_3 = float(input("Enter the product price: "))
item_4 = float(input("Enter the product price: "))
item_5 = float(input("Enter the product price: "))
cost_of_all_products = item_1 + item_2 + item_3 + item_4 + item_5
tax = cost_of_all_products * 0.07
total_cost = cost_of_all_products + tax
print("Cost of all products is: {}\n tax is: {}\n total cost: {}".format(cost_of_all_products, tax, total_cost, '.2f'))
