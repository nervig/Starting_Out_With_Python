number_money_for_each_item = 1
sum_money_for_month = float(input("Enter sum of money for the month: "))
total_sum = 0
balance_of_money = 0
while number_money_for_each_item != 0:
    number_money_for_each_item = float(input("Enter the amount spent on each item. If you're done enter 0: "))
    total_sum += number_money_for_each_item
    balance_of_money = sum_money_for_month - total_sum
print(balance_of_money)
