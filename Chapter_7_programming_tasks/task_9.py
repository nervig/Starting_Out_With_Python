"""
The file USPopulation.txt contains a data about annual population change for period 1950 - 1990. The first string contains the data for 1950 year, second string 1951 and ets. You should to develop a program that reads the data into the list from a file. The program must to show as well:
average annual population changes for a slice of period of time,
the year that had have maximum growth between a specified of period of years,
the year that had have minimum growth between a specified of period of years.
"""


# fetching data into a list
def save_amount_list():
    # reading file txt
    read_file = open("USPopulation.txt", "r")
    # create list for save data from file txt
    folk_population = []
    # adding the data with deleting "\n"
    for amount in read_file:
        folk_population.append(amount.rstrip("\n"))
    # closing a file
    read_file.close()
    # print(len(folk_population))
    return folk_population


# pass in list a data for a slice of time period
def make_slice_time(list_uspopulation):
    # get from user a start year of period
    start_period = int(input("Enter a beginning of time: "))
    # get from user a end year of period
    end_period = int(input("Enter a end of time: "))
    # create a list for slice time of period
    slice_time_list = []
    # to pass the parameters of the function range, we discard the year of the beginning of the range set in the task
    for i in range(start_period - 1950, end_period - 1949):
        slice_time_list.append(list_uspopulation[i])
    print(slice_time_list)
    # the function return a list contains a slice of time period and year of start period that user was set
    return slice_time_list, start_period


# average annual population change
def calculate_average_annual_change(list1):
    # calculate a average annual population change for the year
    average_annual_population_change = (int(list1[-1]) - int(list1[0])) / len(list1)
    return average_annual_population_change


# calculate a difference between years
def calculate_maximum_minimum_population_growth(list2, start_year):
    # create a list for a record the difference
    difference_between_years = []
    # add the difference that was calculated
    for i in range(len(list2)-1):
        difference_between_years.append(int(list2[i+1]) - int(list2[i]))
    # take a minimum and maximum value from list
    maximum_population_growth = max(difference_between_years)
    minimum_population_growth = min(difference_between_years)
    # fetching data for calculate year using the value
    max_year = difference_between_years.index(maximum_population_growth) + start_year + 1
    min_year = difference_between_years.index(minimum_population_growth) + start_year + 1
    print(difference_between_years)
    return max_year, min_year


def main():
    population = save_amount_list()
    slice_time, start_year = make_slice_time(population)
    print(calculate_average_annual_change(slice_time))
    maximum_year, minimum_year = calculate_maximum_minimum_population_growth(slice_time, start_year)
    print("Maximum population in year " + str(maximum_year))
    print("Minimum population in year " + str(minimum_year))


main()
