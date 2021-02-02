def main():
    amount_sale = float(input("Enter an amount of all sales per month: "))
    federal_tax = calculate_tax_federal(amount_sale)
    council_tax = calculate_tax_council(amount_sale)
    tax_sum = federal_tax + council_tax
    print("The federal tax is {}".format(federal_tax))
    print("The council tax is {}".format(council_tax))
    print("The sum of tax is {}".format(tax_sum))


def calculate_tax_federal(num):
    tax = num * 0.05
    return tax


def calculate_tax_council(num):
    tax = num * 0.025
    return tax


main()
