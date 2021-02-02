import tkinter
import tkinter.messagebox

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.gallon_frame = tkinter.Frame(self.main_window)
        self.gallon_label = tkinter.Label(self.gallon_frame, text='Enter an amount of gallons', width=25)
        self.entry_gallon = tkinter.Entry(self.gallon_frame, width=10)

        self.gallon_frame.pack()
        self.gallon_label.pack(side='left')
        self.entry_gallon.pack(side='left')

        self.miles_frame = tkinter.Frame(self.main_window)
        self.miles_label = tkinter.Label(self.miles_frame, text='Enter an amount of miles', width=25)
        self.entry_miles = tkinter.Entry(self.miles_frame, width=10)

        self.miles_frame.pack()
        self.miles_label.pack(side='left')
        self.entry_miles.pack(side='left')

        self.result_frame = tkinter.Frame(self.main_window)
        self.result_label = tkinter.Label(self.result_frame, text='Miles per gallon(MPG)=')
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
        miles = int(self.entry_miles.get())
        gallons = int(self.entry_gallon.get())
        result = miles / gallons
        self.value.set(result)


my_gui = My_GUI()