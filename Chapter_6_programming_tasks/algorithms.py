# import random
# def simple_num_found(num):
#     if num < 2:
#         return False
#     else:
#         for x in range(2, num - 1):
#             if num % x == 0:
#                 return False
#         else:
#             return print(num, end=' ')
#
# def main():
#     for i in range(1, 101):
#         simple_num_found(i)
# main()
# algorithm 1
# def main():
#     file_output = open('my_name.txt', 'w')
#     file_output.write('Andrey')
#     file_output.close()
#
#
# main()

# algorithm 2
# def main():
#     file_read = open('my_name.txt', 'r')
#     print(file_read.read())
#     file_read.close()
#
#
# main()

# algorithm 3
# def main():
#     file_output = open('number_list.txt', 'w')
#     for i in range(1, 101):
#         file_output.write(str(i) + ' ')
#     file_output.close()
#
#
# main()

# algorithm 4
# def main():
#     read_number_list = open('number_list.txt', 'r')
#     for numbers in read_number_list:
#         print(numbers)
#
#     read_number_list.close()
#
#
# main()

# algorithm 5
# def main():
#     total = 0
#     sum_numbers_from_list = open('number_list.txt', 'r')
#     read_numbers = sum_numbers_from_list.read()
#     read_numbers = read_numbers.replace(' ', '')
#     for numbers in read_numbers:
#         total += int(numbers)
#     print(total)
#     sum_numbers_from_list.close()
#
#
# main()

# algorithm 6
# def main():
#     read_file = open('number_list.txt', 'r')
#     read_file.close()
#
# main()

# algorithm 7
