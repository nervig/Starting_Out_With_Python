number_years = int(input("Enter number of years: "))
total_number_precipitation = 0
average_mm_precipitation_per_month = 0
for i in range(number_years):
    amount_month = 1
    for x in range(1, 3):
        mm_precipitation_in_month = int(input("Enter amount of mm of precipitation per month: "))
        amount_month += x
        total_number_precipitation += mm_precipitation_in_month
average_mm_precipitation_per_month = total_number_precipitation / amount_month
print("Total number of month: {}".format(amount_month))
print("Total number of mm of precipitation: {}".format(total_number_precipitation))
print("Average mm of precipitation per month: {}".format(average_mm_precipitation_per_month))
