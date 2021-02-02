start_number_organism = int(input("Enter a starting number of organisms: "))
average_daily_increase_percentage = float(input("Enter an average daily increase percentage: ")) / 100
amount_of_days = int(input("Enter a number of days: "))
print("Day\t\t\tPopulation\n"
      "1\t\t\t{}".format(start_number_organism))
for i in range(2, amount_of_days + 1):
    start_number_organism += start_number_organism * average_daily_increase_percentage
    print("{}\t\t\t{}".format(i, start_number_organism))
