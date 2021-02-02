"""
The file WorldSeriesWinners.txt contains the chronological list of teams winner of World Cup for baseball from
1903 to 2009 years.(The first string is a name of team, that had won in 1903, and the last string is a name of team,
that had won in 2009. Notice, what the World Cup was not carried in 1904 and 1994. Write a program, that alows to
user enter a name of team and then show an number of years, when team had been won in World Cup during a specified
time period from 1903 to 2009.
"""


# open file.txt and save a data in a list
def read_file():
    file_data = open("WorldSeriesWinners.txt", "r")
    # create a list of name
    name_list = []
    # fetched a data from file and adding to the list
    for name_team in file_data:
        name_list.append(name_team.rstrip("\n"))
    print(name_list)
    file_data.close()
    return name_list


# create a list contains years when was carried the World Cup
def create_years_list():
    # create a list
    list_years = []
    for i in range(2009 - 1902):
        list_years.append(i + 1903)
    print(list_years)
    if 1904 in list_years:
        list_years.remove(1904)
    if 1994 in list_years:
        list_years.remove(1994)
    print(list_years)
    return list_years


# get data from user and get index from list
def get_data_from_user(list1):
    name_team = input("Enter a name of team: ")
    index_list = []
    for i in range(len(list1)):
        if name_team in list1[i]:
            index_list.append(i)
    # print(index_list)
    return index_list, name_team


# the function takes index of needed team, her name and list of years
def show_year_of_win(index, name, years):
    # create a list for years
    years_of_win = []
    # add years to list through a got index
    for i in index:
        years_of_win.append(years[i])
    print(name + " had won in ")
    for x in years_of_win:
        print(x)


def main():
    name_team_list = read_file()
    years_win = create_years_list()
    index_for_year, name_of_user = get_data_from_user(name_team_list)
    show_year_of_win(index_for_year, name_of_user, years_win)


main()
