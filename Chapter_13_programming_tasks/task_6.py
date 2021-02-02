import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_choice_frame = tkinter.Frame()

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Oil change - 500.00 ruble', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Lubrication works - 800.00 ruble', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Flushing of the radiator - 300.00 ruble', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Changing the fluid in \nthe transmission - 700.00 ruble',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Inspection - 1000.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Replacement of the exhaust muffler - 1300.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.button_choice_frame,
                                       text='Rearrangement of tires - 1300.00', variable=self.cb_var7)

        self.button_choice_frame.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.button_frame = tkinter.Frame(self.main_window)
        self.ok_button = tkinter.Button(self.button_frame, text='OK', command=self.show_choice)
        self.exit_button = tkinter.Button(self.button_frame, text='EXIT', command=self.main_window.destroy)

        self.button_frame.pack()
        self.ok_button.pack(side='left')
        self.exit_button.pack(side='left')

        tkinter.mainloop()

    def show_choice(self):
        sum_all_services = 0

        if self.cb_var1.get() == 1:
            sum_all_services += 500
        if self.cb_var2.get() == 1:
            sum_all_services += 800
        if self.cb_var3.get() == 1:
            sum_all_services += 300
        if self.cb_var4.get() == 1:
            sum_all_services += 700
        if self.cb_var5.get() == 1:
            sum_all_services += 1000
        if self.cb_var6.get() == 1:
            sum_all_services += 1300
        if self.cb_var7.get() == 1:
            sum_all_services += 1300

        message = 'Sum all services equals ' + str(sum_all_services)
        tkinter.messagebox.showinfo('Select', message)


my_gui = MyGUI()
