import tkinter
import tkinter.messagebox


# 1
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.label = tkinter.Label(self.main_window, text='Programming is cool!')
#
#         self.label.pack()
#
#         self.main_window.mainloop()
#
#
# my_gui = MyGUI()


# 2
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.label1 = tkinter.Label(self.main_window, text='Element 1')
#         self.label2 = tkinter.Label(self.main_window, text='Element 2')
#
#         self.label1.pack(side='left')
#         self.label2.pack(side='left')
#
#         self.main_window.mainloop()
#
#
# my_gui = MyGUI()


# 3
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.frame = tkinter.Frame(self.main_window)
#         self.label = tkinter.Label(self.frame, text='Frame///')
#
#         self.frame.pack()
#         self.label.pack()
#
#         self.main_window.mainloop()
#
#
# my_gui = MyGUI()


# 4
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.frame = tkinter.Frame(self.main_window)
#         self.label1 = tkinter.Label(self.frame, text='The program is suspended')
#         self.label2 = tkinter.Label(self.frame, text='Click OK, when you will be ready')
#
#         self.frame.pack()
#         self.label1.pack()
#         self.label2.pack()
#
#         self.main_window.mainloop()
#
#
# my_gui = MyGUI()

# 5
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.button_frame = tkinter.Frame(self.main_window)
#         self.button1 = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
#
#         self.button_frame.pack()
#         self.button1.pack()
#
#         self.main_window.mainloop()
#
#     def calculate(self):
#         pass
#
#
# my_gui = MyGUI()

# 6
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.button_frame = tkinter.Frame(self.main_window)
#         self.button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)
#
#         self.button_frame.pack()
#         self.button.pack()
#
#         self.main_window.mainloop()
#
#
# my_gui = MyGUI()


# 7
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         self.data_entry = tkinter.Entry(self.main_window, width=10)
#
#         self.data_entry.pack()
#
#         self.var = tkinter.StringVar()
#         self.label = tkinter.Label(self.main_window, textvariable=self.var)
#
#         self.label.pack()
#
#         self.assign_button = tkinter.Button(self.main_window, text='Assign',
#                                             command=self.assign)
#
#         self.assign_button.pack()
#
#         self.main_window.mainloop()
#
#     def assign(self):
#         self.var.set(self.data_entry.get())
#
#
# my_gui = MyGUI()


# 8
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame_line = tkinter.Frame(self.main_window)
        self.canvas_line = tkinter.Canvas(self.frame_line, width=200, height=200)
        self.canvas_line.create_line(0, 0, 199, 199, width=3)

        self.frame_line.pack(side='left')
        self.canvas_line.pack()

        self.frame_rectangle = tkinter.Frame(self.main_window)
        self.canvas_rectangle = tkinter.Canvas(self.frame_rectangle, width=200, height=200)
        self.canvas_rectangle.create_rectangle(50, 50, 100, 100, fill='black', outline='red')

        self.frame_rectangle.pack(side='left')
        self.canvas_rectangle.pack()

        self.frame_oval = tkinter.Frame(self.main_window)
        self.canvas_oval = tkinter.Canvas(self.frame_oval, width=200, height=200)
        self.canvas_oval.create_oval(50, 50, 150, 150, outline='green', width=2)

        self.frame_oval.pack(side='left')
        self.canvas_oval.pack()

        self.frame_arc = tkinter.Frame(self.main_window)
        self.canvas_arc = tkinter.Canvas(self.frame_arc, width=200, height=200)
        self.canvas_arc.create_arc(20, 20, 180, 180, start=0, extent=90, outline='blue', width=2)

        self.frame_arc.pack(side='left')
        self.canvas_arc.pack()

        tkinter.mainloop()


my_gui = MyGUI()