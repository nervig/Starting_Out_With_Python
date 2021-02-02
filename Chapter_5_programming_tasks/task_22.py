import random


def select_thing():
    thing_num = random.randint(1, 4)
    if thing_num == 1:
        return "Stone"
    elif thing_num == 2:
        return "Scissors"
    else:
        return "Paper"


def choice_winner(robot, user):
    # stone
    if robot == 'Stone' and user == 'Paper':
        print("You win!")
    elif robot == 'Stone' and user == 'Scissors' or user == 'scissors':
        print("You lose!")
    # scissors
    elif robot == 'Scissors' and user == 'Paper':
        print("You lose!")
    elif robot == 'Scissors' and user == 'Stone':
        print("You win!")
    # paper
    elif robot == 'Paper' and user == 'Stone':
        print("You lose!")
    elif robot == 'Paper' and user == 'Scissors':
        print("You win!")
    else:
        print("Play again")
        main()


def main():
    robot = select_thing()
    selected_thing_user = input("Enter 'Stone', 'Scissors' or 'Paper' ")
    print(robot)
    choice_winner(robot, selected_thing_user)


main()
