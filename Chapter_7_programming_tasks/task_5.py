# import random
#
#
# def main():
#     account_list = open('account_list.txt', 'w')
#     for i in range(20):
#         account_list.write(str(random.randint(1000000, 10000000)) + '\n')
#     account_list.close()
#
#
# main()

def main():
    account_list = open('account_list.txt', 'r')
    number_list = []
    for number in account_list:
        number_list.append(number.rstrip('\n'))
    print(number_list)
    account_list.close()
    account_found = input('Enter a number of account what you found: ')
    if account_found in number_list:
        print("Permissible value")
    else:
        print("Impermissible value")


main()