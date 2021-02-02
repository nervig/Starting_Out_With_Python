#!/usr/bin/python
''' 1,5 glass of sugar }
    1 glass of oil     } = 48 cookies
    2.75 glass of flour }
'''
glass_of_sugar = 0.028
glass_of_oil = 0.021
glass_of_flour = 0.057
amount_of_cookies = int(input("Please, enter the amount of cookies: "))
amount_sugar = amount_of_cookies * glass_of_sugar
amount_oil = glass_of_oil * amount_of_cookies
amount_flour = glass_of_flour * amount_of_cookies
print("For maiking {} amount of cookies you need: \n {} glass of sugar\n {} glass of oil\n {} glass of flour".format(amount_of_cookies, amount_sugar, amount_oil, amount_flour, 1))
