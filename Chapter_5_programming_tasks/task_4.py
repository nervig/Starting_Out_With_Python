def main():
    loan_payment = float(input("Enter a loan payment: "))
    insurance_payment = float(input("Enter a insurance payment: "))
    payment_for_gasoline = float(input("Enter a payment for gasoline: "))
    payment_for_engine_oil = float(input("Enter a payment for engine oil"))
    tire_cost = float(input("Enter a tire cost: "))
    maintenance_payment = float(input("Enter a maintenance payment: "))
    sum_in_month, sum_in_year = calculate_sum_expenses(loan_payment, insurance_payment, payment_for_gasoline,
                                                       payment_for_engine_oil, tire_cost, maintenance_payment)
    print("The amount of payment per month is {}\n"
          "The amount of payment per year is {}".format(sum_in_month, sum_in_year))


def calculate_sum_expenses(loan, insurance, gasoline, oil, tire, maintenance):
    sum_in_month = loan + insurance + gasoline + oil + tire + maintenance
    sum_in_year = sum_in_month * 12
    return sum_in_month, sum_in_year

main()