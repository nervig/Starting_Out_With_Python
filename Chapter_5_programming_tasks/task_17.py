import random
def main():
    even_number = 0
    odd_number = 0
    for i in range(100):
        current_number = random.randint(1, 101)
        print(current_number, end=' ')
        if current_number % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    print()
    print("Even number: " + str(even_number))
    print("Odd number: " + str(odd_number))

main()