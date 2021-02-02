import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame_label = tkinter.Frame(self.main_window, width=200, height=100)
        self.frame_button = tkinter.Frame(self.main_window)

        self.variable = tkinter.StringVar()
        self.label = tkinter.Label(self.frame_label, width=30, height=5, textvariable=self.variable)
        self.button_show_info = tkinter.Button(self.frame_button, text='Show info', command=self.show_info)
        self.button_exit = tkinter.Button(self.frame_button, text='Exit', command=self.main_window.destroy)

        self.label.pack()
        self.frame_label.pack()
        self.frame_button.pack()

        self.button_show_info.pack(side='left')
        self.button_exit.pack(side='left')

        tkinter.mainloop()

    def show_info(self):
        self.variable.set('162390, Россия Вологодская обл,\nг.Великий Устюг,\nПочта Деда Мороза')


my_gui = MyGUI()
