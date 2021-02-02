def main():
    open_read_file = open("random_num.txt", 'r')
    sum_num = 0
    amount_num = 0
    for row in open_read_file:
        print(row.rstrip('\n'))
        sum_num += int(row)
        amount_num += 1
    print("Total sum = ", sum_num)
    print("Amount of numbers = ", amount_num)
    open_read_file.close()


main()