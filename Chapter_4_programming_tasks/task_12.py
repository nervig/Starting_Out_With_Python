factorial_number = int(input("Enter any positive number: "))
factorial = 1
for i in range(2, factorial_number + 1):
    factorial *= i
print(factorial)