from task_18 import is_prime


def main():
    for i in range(1, 101):
        current_num = is_prime(i)
        if current_num == True:
            print(i, end=' ')


main()
