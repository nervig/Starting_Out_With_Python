def main():
    my_list = []
    total_numbers = 0
    for i in range(10):
        my_list.append(int(input('Enter any number: ')))
        total_numbers += my_list[i]
    print('Minimum the number is: ' + str(min(my_list)))
    print('Maximum the number is: ' + str(max(my_list)))
    print(total_numbers)
    print(total_numbers / 10)


main()
