def main():
    current_sum = float(input("Enter a current sum: "))
    interest_rate = (float(input("Enter a interest rate per month: "))) / 100
    amount_of_month = float(input("Enter an amount of month: "))
    print("Your sum will be " + str(round(calculate_future_sum(current_sum, interest_rate, amount_of_month), 2)))


# future sum = current sum * (1 + interest rate)**2
def calculate_future_sum(current_sum, interest_rate, amount_month):
    future_sum = (current_sum * (1 + interest_rate) ** 2) * amount_month
    return future_sum

main()