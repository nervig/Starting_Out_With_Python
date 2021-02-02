#!/usr/bin/python
boys_amount = int(input("Enter boys amount: "))
girls_amount = int(input("Enter girl amount: "))
number_of_students = boys_amount + girls_amount
percentage_of_girls = float(girls_amount / number_of_students) * 100
percentage_of_boys = 100 - percentage_of_girls
print("Percentage of girls equal {}".format(percentage_of_girls))
print("Percentage of boys equal {}".format(percentage_of_boys))
