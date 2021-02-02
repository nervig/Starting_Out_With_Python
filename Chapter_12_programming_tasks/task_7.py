def exponentiation_of_numbers(num, expnt):
    if expnt == 0:
        return 1
    else:
        return num * exponentiation_of_numbers(num, expnt - 1)


print(exponentiation_of_numbers(14, 6))