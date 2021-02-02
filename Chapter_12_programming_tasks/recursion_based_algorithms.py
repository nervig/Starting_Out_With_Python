# sum of numbers from to in list numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


num_sum = range_sum(numbers, 3, 7)
print(num_sum)
#
#
# # Fibonacci numbers. After 2th number every next number equal sum 2 previous numbers.
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# for num in range(1, 11):
#     print(fib(num))
#
#
# # Greatest Common Divisor
# def gcd(x, y):
#     if x % y == 0:
#         return y
#     else:
#         return gcd(y, x % y)
#
#
# print(gcd(28, 49))

# towers of hanoi
# def main():
#     num_discs = 3
#     from_peg = 1
#     to_peg = 3
#     temp_peg = 2
#
#     move_discs(num_discs, from_peg, to_peg, temp_peg)
#
#
# def move_discs(num, from_peg, to_peg, temp_peg):
#     if num > 0:
#         move_discs(num - 1, from_peg, temp_peg, to_peg)
#         print('Move a ring from', from_peg, 'to', to_peg)
#         move_discs(num - 1, temp_peg, to_peg, from_peg)
#
#
# main()
