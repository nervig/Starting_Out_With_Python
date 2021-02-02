import random

# read the txt file and add the data in list
def read_list_answers():
    answers_from_list = open("8_ball_responses.txt", "r")
    blank_list = []
    for row in answers_from_list:
        blank_list.append(row.rstrip("\n"))
    return blank_list


# get data from user and print a random answer from list
def get_ask_from_user(answers_list):
    # set the condition to work a loop
    condition = "yes"
    while condition == "yes":
        ask_user = input("Ask your question: ")
        print(answers_list[random.randint(0,20)])
        # checking the condition for loop
        condition = input("Do you want to continue? Enter 'yes' if you want. In different case enter 'no'")


def main():
    answer = read_list_answers()
    get_ask_from_user(answer)


main()