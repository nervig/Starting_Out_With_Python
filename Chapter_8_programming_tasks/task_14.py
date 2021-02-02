read_file = open("GasPrices.txt", "r")

# calculate the average value in year
def calculate_average_in_year(r_file):
    # create a list of years
    years = "93 94 95 96 97 98 99 00 01 02 03 04 05 06 07 08 09 10 11 12 13"
    years_list = years.split()

    # iterating over the years
    for year in years_list:
        month_count = 0
        sum_price_gas_93 = 0
        line = r_file.readline()
        while line[8:10] == year:
            # count sum prices gas per months of the every year
            sum_price_gas_93 += float(line[11:].rstrip())
            month_count += 1
            line = r_file.readline()
        print("The year " + year)
        average_price = sum_price_gas_93 / month_count
        print(round(average_price, 2))


def calculate_average_in_month_of_year(r_file):
    years = "93 94 95 96 97 98 99 00 01 02 03 04 05 06 07 08 09 10 11 12 13"
    years_list = years.split()
    for year in years_list:
        print("Year " + str(year))
        month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        for month in month_list:
            month_count = 0
            month_price_sum = 0
            line = r_file.readline()
            if line[0:2] in month_list:
                month_price_sum += float(line[11:].rstrip())
                month_count += 1
                line = r_file.readline()
            print("Month " + str(month))
            average_price_count = month_price_sum / month_count
            print(average_price_count)


def calculate_max_and_min_price_in_year(r_file):
    years = "93 94 95 96 97 98 99 00 01 02 03 04 05 06 07 08 09 10 11 12 13"
    years_list = years.split()

    for year in years_list:
        years_count = 0
        temporary_values_max_price = 0
        temporary_values_min_price = 5.11
        month_count_max = 0
        month_count_min = 0
        line = r_file.readline()
        print("The year " + year)
        while line[8:10] == year:
            if temporary_values_max_price < float(line[11:].rstrip()):
                temporary_values_max_price = float(line[11:].rstrip())
                month_count_max = line[0:2]
            if temporary_values_min_price > float(line[11:].rstrip()):
                temporary_values_min_price = float(line[11:].rstrip())
                month_count_min = line[0:2]
            line = r_file.readline()
        print("Month " + month_count_max + ", max price " + str(temporary_values_max_price))
        print("Month " + month_count_min + ", min price " + str(temporary_values_min_price))


def sort_list_ascending_descending(r_file):
    list_of_price = []
    line = r_file.readline()

    def keyFunc(item):
        return item[11:16]

    while line != '':
        list_of_price.append(line.rstrip())
        line = r_file.readline()
    list_of_price.sort(key=keyFunc)
    for i in list_of_price:
        print(i)
    print()
    list_of_price.sort(key=keyFunc, reverse=True)
    for e in list_of_price:
        print(e)


calculate_average_in_year(read_file)
# calculate_average_in_month_of_year(read_file)
# calculate_max_and_min_price_in_year(read_file)
# sort_list_ascending_descending(read_file)

read_file.close()
