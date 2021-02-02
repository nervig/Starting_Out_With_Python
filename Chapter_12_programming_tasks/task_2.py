def recursive_multiplication(x, y):
    if y == 1 or x == 1:
        return x
    else:
        return x + recursive_multiplication(x, y - 1)


print(recursive_multiplication(7, 4))
