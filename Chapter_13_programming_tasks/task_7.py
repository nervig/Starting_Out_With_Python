import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_choice_frame = tkinter.Frame()

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.button_choice_frame,
                                       text='Daylight time (6:00 - 17:59)', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.button_choice_frame,
                                       text='Evening time (18:00 - 23:59)', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.button_choice_frame,
                                       text='Night time (00:00 - 5:59)', variable=self.radio_var, value=3)

        self.button_choice_frame.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.minutes_frame = tkinter.Frame(self.main_window)
        self.amount_of_minutes_label = tkinter.Label(self.minutes_frame, text='Enter an amount of minutes ')
        self.amount_of_minutes_entry = tkinter.Entry(self.minutes_frame, width=10)

        self.minutes_frame.pack()
        self.amount_of_minutes_label.pack(side='left')
        self.amount_of_minutes_entry.pack(side='left')

        self.button_frame = tkinter.Frame(self.main_window)
        self.show_button = tkinter.Button(self.button_frame, text='Show cost', command=self.show_cost)
        self.exit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)

        self.button_frame.pack()
        self.show_button.pack(side='left')
        self.exit_button.pack(side='left')

        tkinter.mainloop()

    def show_cost(self):
        cost = 0
        if self.radio_var.get() == 1:
            cost = int(self.amount_of_minutes_entry.get()) * 10
        elif self.radio_var.get() == 2:
            cost = int(self.amount_of_minutes_entry.get()) * 12
        elif self.radio_var.get() == 3:
            cost = int(self.amount_of_minutes_entry.get()) * 5

        message = 'Cost of call equals ' + str(cost) + ' rubles'
        tkinter.messagebox.showinfo('Select', message)


my_gui = MyGUI()