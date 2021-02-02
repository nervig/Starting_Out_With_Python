import matplotlib.pyplot as plt


def read_file():
    with open("1994_Weekly_Gas_Averages.txt", "r") as gas_costs:
        # the list for weeks cost of gas
        list_week_values = []
        # the value of number of weeks
        time_list = []
        accumulate = 0
        for week_value in gas_costs:
            # add values to the list from txt file data
            list_week_values.append(week_value.strip("\n"))
            accumulate += 1
            # counting the number of weeks
            time_list.append(accumulate)
        print(list_week_values)
        print(time_list)
        return list_week_values, time_list


# build the diagram
def create_diagram(list1, list2):
    plt.bar(list2, list1)
    plt.show()


def main():
    x, y = read_file()
    create_diagram(x, y)


main()