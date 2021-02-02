import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text='Hello word!')
        self.label2 = tkinter.Label(self.main_window, text='This is my program with GUI')

        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()


my_gui = MyGUI()