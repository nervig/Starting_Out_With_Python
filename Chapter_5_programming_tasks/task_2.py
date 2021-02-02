#!/usr/bin/python
FEDERAL_TAX_INDEX = 0.05
COUNTRY_TAX_INDEX = 0.025
def main():
    total_number = float(input("Enter the total purchase amount: "))
    federal_tax = federal_tax_calculate(total_number)
    country_tax = country_tax_calculate(total_number)
    total_tax = federal_tax + country_tax
    purchase_amount = total_number - total_tax
    print("The purchase amount is: {}\nFederal tax is: {}\nRegional tax is: {}\nThe total amount is: {}"
          .format(purchase_amount, federal_tax, country_tax, total_number, '.2f'))


def federal_tax_calculate(number):
    federal_tax = number * FEDERAL_TAX_INDEX
    return federal_tax


def country_tax_calculate(number):
    country_tax = number * COUNTRY_TAX_INDEX
    return country_tax


main()
