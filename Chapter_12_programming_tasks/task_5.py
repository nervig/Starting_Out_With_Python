numbers = [1, 2, 10, 4, 5, 6, 7, 8, 9]


def sum_num_of_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_num_of_list(num_list[1:])


print(sum_num_of_list(numbers))