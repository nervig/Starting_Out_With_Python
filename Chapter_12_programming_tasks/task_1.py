def print_num_to_n(n):
    if n == 0:
        return 1
    else:
        print_num_to_n(n - 1)
        print(n)


print_num_to_n(11)
