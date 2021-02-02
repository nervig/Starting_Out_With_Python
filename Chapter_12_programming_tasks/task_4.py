numbers = [1, 2, 10, 4, 5, 6, 7, 8, 9]


# def max_value_in_list(num_list):
#     max_num = num_list[0]
#     for i in range(len(num_list)):
#         if num_list[i] > max_num:
#             max_num = num_list[i]
#     print(max_num)

def max_value_in_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        max_num = max_value_in_list(num_list[1:])
        if max_num > num_list[0]:
            return max_num
        else:
            return num_list[0]


# max_value_in_list(numbers)
print(max_value_in_list(numbers))
