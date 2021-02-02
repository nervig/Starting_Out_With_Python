import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window, text='Click me!', command=self.do_something)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Wink')
        self.label2 = tkinter.Label(self.top_frame, text='Blink')
        self.label3 = tkinter.Label(self.top_frame, text='Nod')

        self.my_button.pack()
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text='wink')
        self.label5 = tkinter.Label(self.bottom_frame, text='blink')
        self.label6 = tkinter.Label(self.bottom_frame, text='nod')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Reaction', 'Thanks, that you click the button for.')


my_gui = MyGUI()