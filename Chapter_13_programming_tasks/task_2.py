import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.word = tkinter.StringVar()
        self.label_answer = tkinter.Label(self.main_window, textvariable=self.word)
        self.button_word1 = tkinter.Button(self.main_window, text='sinister', command=self.get_word1)
        self.button_word2 = tkinter.Button(self.main_window, text='dexter', command=self.get_word2)
        self.button_word3 = tkinter.Button(self.main_window, text='medium', command=self.get_word3)

        # self.word2 = tkinter.StringVar()
        # self.word3 = tkinter.StringVar()

        self.label_answer.pack()
        self.button_word1.pack(side='left')
        self.button_word2.pack(side='left')
        self.button_word3.pack(side='left')

        tkinter.mainloop()

    def get_word1(self):
        self.word.set('Левый')

    def get_word2(self):
        self.word.set('Правый')

    def get_word3(self):
        self.word.set('Центральный')


my_gui = MyGUI()
