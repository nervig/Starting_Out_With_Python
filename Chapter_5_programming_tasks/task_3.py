def main():
    building_cost = float(input("Enter a cost of building: "))
    minimum_cost_of_insurance = minimum_cost_of_insurance_calculate(building_cost)
    print("Minimum cost of insurance equals {:.2f}".format(minimum_cost_of_insurance))


def minimum_cost_of_insurance_calculate(num):
    minimum_cost_of_insurance = num - (num * 0.2)
    return minimum_cost_of_insurance


main()