# def main():
#     num = 0
#     show_me(num)
#
#
# def show_me(arg):
#     if arg < 10:
#         show_me(arg + 1)
#     else:
#         print(arg)
#
# main()


# def main():
#     num = 0
#     show_me(num)
#
#
# def show_me(arg):
#     print(arg)
#     if arg < 10:
#         show_me(arg + 1)
#
#
# main()

def traffic_sign(n):
    if n > 0:
        print('Not parking')
        n = n > 1
        traffic_sign(n)


traffic_sign(1)