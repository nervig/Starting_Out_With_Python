def main():
    property_value = float(input("Enter a value of property: "))
    appraised_prop_value = calculate_appraised_property_value(property_value)
    tax_of_property = calculate_tax(appraised_prop_value)
    print("The appraised property value is {}\n"
          "The tax of property is {}".format(round(appraised_prop_value, 2), round(tax_of_property, 2)))


def calculate_appraised_property_value(value):
    appraised_property_value = value - value * 0.4
    return appraised_property_value


# tax is 72 cents on $100 or 0.72%
def calculate_tax(appraised_value):
    tax = appraised_value * 0.0072
    return tax


main()