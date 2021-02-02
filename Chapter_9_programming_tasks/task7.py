read_file_win_teams = open('WorldSeriesWinners.txt', 'r')
line = read_file_win_teams.readline()
dictionary_win_teams = {}
dictionary_win_years = {}
years = 1903
while line != '':
    # print(line.rstrip('\n'))
    if line.rstrip('\n') not in dictionary_win_teams:
        dictionary_win_teams[line.rstrip('\n')] = 1
    else:
        dictionary_win_teams[line.rstrip('\n')] += 1
    line = read_file_win_teams.readline()
# print(dictionary_win_teams)


read_file_win_teams = open('WorldSeriesWinners.txt', 'r')

while years < 2009:
    stop_list = [1904, 1994]
    if years not in stop_list:
        line = read_file_win_teams.readline()
        dictionary_win_years[years] = line.rstrip('\n')
    years += 1
# print(dictionary_win_years)
read_file_win_teams.close()

users_question = int(input("Enter the year: "))
print("In " + str(users_question) + " year won " + dictionary_win_years[users_question])
print("In World Series the " + dictionary_win_years[users_question] + " has won " + str(dictionary_win_teams[dictionary_win_years[users_question]])+ " times")