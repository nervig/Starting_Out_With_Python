import matplotlib.pyplot as plt
import re


def read_data():
    # list for string data
    result_line = []
    # list for numeric data
    result_digit_line = []
    # read the txt file
    with open("costs_last_month.txt", "r") as file:
        for line in file:
            # with regular expression find to numeric data in text
            digit_line = re.findall(r"\d", line)
            # with regular expression find to string data in text
            string_line = re.findall(r"[A-X ]*[a-z]", line)
            # add string data to the list
            result_line.append(''.join(string_line))
            # add numeric data to the list
            result_digit_line.append("".join(digit_line))

    return result_line, result_digit_line


# build the diagram
def built_pie_diagram(list1, list2):
    plt.pie(list2, labels=list1)
    plt.title("Expenses")
    plt.show()


def main():
    labels, numbers = read_data()
    built_pie_diagram(labels, numbers)


main()