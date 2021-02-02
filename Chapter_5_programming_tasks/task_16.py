def calc_average(score_1, score_2, score_3, score_4, score_5):
    average_score = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
    average_score_letter = score_num_to_letter(average_score)
    return average_score_letter


def determine_grade(score_1, score_2, score_3, score_4, score_5):
    score_letter_1 = score_num_to_letter(score_1)
    score_letter_2 = score_num_to_letter(score_2)
    score_letter_3 = score_num_to_letter(score_3)
    score_letter_4 = score_num_to_letter(score_4)
    score_letter_5 = score_num_to_letter(score_5)
    return score_letter_1, score_letter_2, score_letter_3, score_letter_4, score_letter_5


def score_num_to_letter(num):
    if num >= 90:
        return 'A'
    elif 80 <= num < 90:
        return 'B'
    elif 70 <= num < 80:
        return 'C'
    elif 60 <= num < 70:
        return 'D'
    else:
        return 'F'


def main():
    score1 = int(input("Enter a first score: "))
    score2 = int(input("Enter a second score: "))
    score3 = int(input("Enter a third score: "))
    score4 = int(input("Enter a fourth score: "))
    score5 = int(input("Enter a fifth score: "))
    score_letter1, score_letter2, score_letter3, score_letter4, score_letter5 = determine_grade(score1, score2, score3, score4, score5)
    print("Your first score is " + str(score_letter1))
    print("Your second score is " + str(score_letter2))
    print("Your third score is " + str(score_letter3))
    print("Your fourth score is " + str(score_letter4))
    print("Your fifth score is " + str(score_letter5))
    average_score = calc_average(score1, score2, score3, score4, score5)
    print("Your average score is " + average_score)


main()