import tkinter
import tkinter.messagebox


class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.celsius_frame = tkinter.Frame(self.main_window)
        self.celsius_label = tkinter.Label(self.celsius_frame, text='Enter a value of temperature in Celsius')
        self.celsius_entry = tkinter.Entry(self.celsius_frame, width=10)

        self.celsius_frame.pack()
        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        self.result_frame = tkinter.Frame(self.main_window)
        self.result_label = tkinter.Label(self.result_frame, text='Temperature in Fahrenheit')
        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.result_frame, textvariable=self.value, width=10)

        self.result_frame.pack()
        self.result_label.pack(side='left')
        self.value_label.pack(side='left')

        self.button_frame = tkinter.Frame(self.main_window)
        self.calculate_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.exit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)

        self.button_frame.pack()
        self.calculate_button.pack(side='left')
        self.exit_button.pack(side='left')

        tkinter.mainloop()

    def calculate(self):
        celsius = int(self.celsius_entry.get())
        result = 9 / 5 * celsius + 32
        self.value.set(round(result, 1))


my_gui = My_GUI()
