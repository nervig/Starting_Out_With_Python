weight_of_package = int(input("Enter a weight of package in grams: "))
if 0 < weight_of_package < 201:
    print("Cost of delivery is 150 ruble")
elif 200 < weight_of_package < 601:
    print("Cost of delivery is 300 ruble")
elif 600 < weight_of_package < 1001:
    print("Cost of delivery is 400 ruble")
elif 1000 < weight_of_package:
    print("Cost of delivery is 475 ruble")