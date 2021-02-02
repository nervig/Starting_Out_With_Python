#!/usr/bin/python
cost_of_food = float(input("Enter the cost of food: "))
tax_of_sales = cost_of_food * 0.07
tips = cost_of_food * 0.18
total_sum = cost_of_food + tax_of_sales + tips
print("Cost of food: {}\nTax of sales: {}\nTips: {}\nTotal sum: {}".format(cost_of_food, tax_of_sales, tips, total_sum, '.2f'))
