def main():
    amount_ticket_a = int(input("Enter a number of tickets of A category: "))
    amount_ticket_b = int(input("Enter a number of tickets of B category: "))
    amount_ticket_c = int(input("Enter a number of tickets of C category: "))
    a, b, c = calculate_profit_from_a_b_c_sale(amount_ticket_a, amount_ticket_b, amount_ticket_c)
    sum_profit = a + b + c
    print("The sum of profit is {}".format(sum_profit))


def calculate_profit_from_a_b_c_sale(a, b, c):
    a_profit = a * 20
    b_profit = b * 15
    c_profit = c * 10
    return a_profit, b_profit, c_profit

main()