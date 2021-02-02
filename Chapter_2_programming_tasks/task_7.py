#!/usr/bin/python
covered_destination = float(input("Enter the covered destination: "))
fuel_consumption_in_liters = float(input("Enter the fuel consumption in liters: "))
fuel_consumption =float(fuel_consumption_in_liters / covered_destination)
print("The fuel consumption of your car equals {}".format(fuel_consumption))
