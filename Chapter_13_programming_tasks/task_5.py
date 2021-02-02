import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.cost_of_property_label = tkinter.Label(self.top_frame, text='Enter a cost of property:')
        self.cost_of_property_entry = tkinter.Entry(self.top_frame, width=10)

        self.top_frame.pack()
        self.cost_of_property_label.pack(side='left')
        self.cost_of_property_entry.pack(side='left')

        self.middle_frame = tkinter.Frame(self.main_window)
        self.estimate_cost_label = tkinter.Label(self.middle_frame, text='Estimate cost:')
        self.estimate_cost = tkinter.StringVar()
        self.estimate_cost_calc_label = tkinter.Label(self.middle_frame, textvariable=self.estimate_cost)

        self.middle_frame.pack()
        self.estimate_cost_label.pack(side='left')
        self.estimate_cost_calc_label.pack(side='left')

        self.bottom_frame = tkinter.Frame(self.main_window)
        self.tax_label = tkinter.Label(self.bottom_frame, text='Estimate cost:')
        self.tax = tkinter.StringVar()
        self.tax_calc_label = tkinter.Label(self.bottom_frame, textvariable=self.tax)

        self.bottom_frame.pack()
        self.tax_label.pack(side='left')
        self.tax_calc_label.pack(side='left')

        self.button_frame = tkinter.Frame()
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.exit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)

        self.button_frame.pack()
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        tkinter.mainloop()

    def calculate(self):
        cost_of_property = int(self.cost_of_property_entry.get())
        estimate_cost = cost_of_property * 0.60
        tax = estimate_cost * 0.0075
        self.estimate_cost.set(estimate_cost)
        self.tax.set(tax)


my_gui = MyGUI()