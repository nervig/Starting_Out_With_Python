#!/usr/bin/python
FEDERAL_TAX_INDEX = 0.05
COUNTRY_TAX_INDEX = 0.025
total_number = float(input("Enter the total purchase amount: "))
federal_tax = total_number * FEDERAL_TAX_INDEX
country_tax = total_number * COUNTRY_TAX_INDEX
total_tax = federal_tax + country_tax
purchase_amount = total_number - total_tax
print("The purchase amount is: {}\nFederal tax is: {}\nRegional tax is: {}\nThe total amount is: {}"
      .format(purchase_amount, federal_tax, country_tax, total_number, '.2f'))
