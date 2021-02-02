def create_answers_file():
    answers_file = open("answers.txt", "w")
    answers_file.write("1. A\n"
                       "2. C\n"
                       "3. A\n"
                       "4. A\n"
                       "5. D\n"
                       "6. B\n"
                       "7. C\n"
                       "8. A\n"
                       "9. C\n"
                       "10. B\n"
                       "11. A\n"
                       "12. D\n"
                       "13. C\n"
                       "14. A\n"
                       "15. D\n"
                       "16. C\n"
                       "17. B\n"
                       "18. B\n"
                       "19. D\n"
                       "20. A")
    answers_file.close()


def save_answers_list():
    answers = open("answers.txt", "r")
    answers_list = []
    for row in answers:
        answers_list.append(row.rstrip("\n"))
    print(answers_list)
    answers.close()
    return answers_list


def get_answer_user():
    answer_user = open("user_answer.txt", "r")
    answer_user_list = []
    for row in answer_user:
        answer_user_list.append(row.rstrip("\n"))
    print(answer_user_list)
    answer_user.close()
    return answer_user_list


def processing_answers(list1, list2):
    score = 0
    right_answer = []
    wrong_answer = []
    for i in range(20):
        if list1[i] == list2[i]:
            right_answer.append(list2[i])
            score += 1
        else:
            wrong_answer.append(list2[i])

    if score > 14:
        print("You passed exam!")
    else:
        print("You failed exam!")
    print("The numbers of right answers are " + str(score))

    print("Right answers: ")
    for row in right_answer:
        print(row)

    print("Wrong answers: ")
    for wrong_row in wrong_answer:
        print(wrong_row)


def main():
    create_answers_file()
    # save_answers_list()
    # get_answer_user()
    processing_answers(save_answers_list(), get_answer_user())


main()
