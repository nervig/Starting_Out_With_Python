#!/usr/bin/python
'''
A = P * (1 + (r / n)) ** (n * t)
A - the sum of money on account after some amount of years
P - the sum that was deposited on account in begin
r - annual interest rate
n - frequency of accrual of interest income per year
t - specific number of years
'''
begin_sum = float(input("Enter the sum that was deposited in account: "))
annual_interest_rate = float(input("Enter the annual interest rate: ")) / 100
frequency_accrual_interest_per_year = int(input("Enter the frequency of accrual of interest income per year: "))
number_of_years = int(input("Enter the specific number of years: "))
total_sum_with_accrual_interest = begin_sum * (1 + (annual_interest_rate / frequency_accrual_interest_per_year)) ** (
        frequency_accrual_interest_per_year * number_of_years)
print(format(total_sum_with_accrual_interest, '.2f'))
