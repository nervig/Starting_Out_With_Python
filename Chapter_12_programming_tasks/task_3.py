def print_stars(n):
    if n > 0:
        print_stars(n - 1)
        print('*' * n)


print_stars(7)
