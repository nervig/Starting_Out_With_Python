class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, right_answer_num):
        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__right_answer_num = right_answer_num

    def set_question(self, question):
        self.__question = question

    def set_answer_1(self, answer_1):
        self.__answer_1 = answer_1

    def set_answer_2(self, answer_2):
        self.__answer_2 = answer_2

    def set_answer_3(self, answer_3):
        self.__answer_3 = answer_3

    def set_answer_4(self, answer_4):
        self.__answer_4 = answer_4

    def set_right_answer_num(self, right_answer_num):
        self.__right_answer_num = right_answer_num

    def get_question(self):
        return self.__question

    def get_answer_1(self):
        return self.__answer_1

    def get_answer_2(self):
        return self.__answer_2

    def get_answer_3(self):
        return self.__answer_3

    def get_answer_4(self):
        return self.__answer_4

    def get_right_answer_num(self):
        return self.__right_answer_num
