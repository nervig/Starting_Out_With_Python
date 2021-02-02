def main():
    # create file with the list of players
    players = open("golf.txt", "a")

    flag = 'y'
    while flag == 'y':
        # enter a data
        name = input("Enter a name of player: ")
        score = int(input("Enter a score: "))
        # write data
        players.write('Name: ' + name + '\n')
        players.write('Score: ' + str(score) + '\n')
        flag = input("Do you want to continue to enter a data? If yes enter 'y', "
                     "in different case enter any symbol: ")
    players.close()


main()
