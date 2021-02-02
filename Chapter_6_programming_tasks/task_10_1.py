def main():
    read_list = open('golf.txt', 'r')
    for row in read_list:
        print(row.rstrip('\n'))
    read_list.close()


main()