all_period_days = int(input("Enter a number of days: "))
sum_of_day = 2
sum_all_day = 0.03
print("Day\t\t\tSum\n"
      "-------------\n"
      "1\t\t\t0.01\n"
      "2\t\t\t0.02")
for i in range(3, all_period_days + 1):
    sum_of_day *= 2
    sum_all_day += sum_of_day
    print("{}\t\t\t{}".format(i, round(sum_of_day, 2) / 100))
print("-------------\nSum\t\t\t{}".format(round(sum_all_day, 2)))
