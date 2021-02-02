import question

question_dct = {}

question_1 = question.Question('Question 1', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '1')
question_dct['Question 1'] = question_1
question_2 = question.Question('Question 2', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '3')
question_dct['Question 2'] = question_2
question_3 = question.Question('Question 3', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '2')
question_dct['Question 3'] = question_3
question_4 = question.Question('Question 4', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '4')
question_dct['Question 4'] = question_4
question_5 = question.Question('Question 5', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '3')
question_dct['Question 5'] = question_5
question_6 = question.Question('Question 6', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '4')
question_dct['Question 6'] = question_6
question_7 = question.Question('Question 7', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '1')
question_dct['Question 7'] = question_7
question_8 = question.Question('Question 8', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '1')
question_dct['Question 8'] = question_8
question_9 = question.Question('Question 9', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '2')
question_dct['Question 9'] = question_9
question_10 = question.Question('Question 10', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', '4')
question_dct['Question 10'] = question_10


for x in range(1, 3):
    print('________________________________________________________')
    print("Player number " + str(x))
    score = 0
    for i in question_dct:
        print(question_dct[i].get_question())
        print('Select number of answer: ')
        print(question_dct[i].get_answer_1())
        print(question_dct[i].get_answer_2())
        print(question_dct[i].get_answer_3())
        print(question_dct[i].get_answer_4())
        number_answer = input("Enter number of answer: ")
        if number_answer == question_dct[i].get_right_answer_num():
            score += 1
    print("Your score are " + str(score))
    print('________________________________________________________')



