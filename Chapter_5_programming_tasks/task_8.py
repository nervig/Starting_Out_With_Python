def main():
    surface_area = int(input("Enter an area of surface: "))
    cost_one_container_pain = float(input("Enter a cost of one container of paint: "))

    amount_pain_containers = calculate_number_paint_containers(surface_area)
    print("The amount of containers of paint is {}".format(amount_pain_containers))

    amount_hours_work = calculate_number_hours_work(surface_area)
    print("The number of hours for work is {}".format(round(amount_hours_work)))

    cost_of_pains = amount_pain_containers * cost_one_container_pain
    print("The cost of containers of paint is {}".format(cost_of_pains))

    # The cost of one hour of work equals 2000 ruble/hour
    cost_of_works = amount_hours_work * 2000
    print("The cost of all works equals {}".format(cost_of_works))

    total_cost = cost_of_pains + cost_of_works
    print("Total cost is {}".format(total_cost))


# 10 square meters requires 8 hours. 1 square meter requires 0.8 hour or 60 * 0.8 = 48 min.
def calculate_number_hours_work(num):
    if (num * 48) % 60 == 0:
        amount_hours = (num * 48 / 60)
    else:
        amount_hours = (num * 48 // 60) + 1
    return amount_hours


# the one container contains 5 liter. 10 square meters requires 5 liters. For 1 square meters is needed 0.5 L
def calculate_number_paint_containers(num):
    if num % 10 == 0:
        amount_containers = (num * 0.5) / 5
    else:
        amount_containers = ((num * 0.5) // 5) + 1
    return amount_containers


main()
