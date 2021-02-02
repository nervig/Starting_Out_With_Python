ROWS = 3
COLS = 3


# create a two-dimensional list
def create_two_dimensional_list():
    two_dimensional_list = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
    return two_dimensional_list


# get data from user and full the list
def full_list_from_user(list1):
    # decreasing list of numbers for user
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # variables for print
    nums = ''
    for i in range(ROWS):
        for x in range(COLS):
            # remake a list to string for print
            for item in original_list:
                nums += ' ' + str(item)
            # get a number from user
            user_list = int(input("Enter any number from that list" + nums + ":"))
            # remove the number that was got from user from list for print
            original_list.remove(user_list)
            # add a number that was got from user to the two-dimensional list
            list1[i][x] = user_list
            # zeroing a variable
            nums = ''
    # print the two dimensional list that was got from user
    for row in range(ROWS):
        for col in range(COLS):
            print(list1[row][col], end=' ')
        print()
    return list1


# we add sum from the every string
def add_row_sum(list2):
    # create a variable for accumulation sum from string
    acc_sum_row = 0
    # create a list for getting the values
    row_sum = []
    # iterating over the list and sum items of string
    for i in range(ROWS):
        for x in range(COLS):
            # sum items
            acc_sum_row += int(list2[i][x])
        # add the sum
        row_sum.append(acc_sum_row)
        # zeroing the list
        acc_sum_row = 0
    return row_sum


# we add sum from the every columns
def add_col_sum(list3):
    acc_sum_col = 0
    col_sum = []
    for y in range(COLS):
        for e in range(ROWS):
            acc_sum_col += int(list3[e][y])
        col_sum.append(acc_sum_col)
        acc_sum_col = 0
    return col_sum


# is checking sum in rows and columns
def checking(sum1, sum2):
    # merge the lists
    all_sum = sum1 + sum2
    # is checking values - it should been a 6 times 15
    if all_sum.count(15) == 6:
        print("The square is magic!")
    else:
        print("The square isn't magic!")


def main():
    dimensional_list = create_two_dimensional_list()
    created_list = full_list_from_user(dimensional_list)
    list_row_sum = add_row_sum(created_list)
    list_col_sum = add_col_sum(created_list)
    checking(list_row_sum, list_col_sum)


main()