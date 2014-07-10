__author__ = 'Dilan'

from Tkinter import *


class Calculator:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Button(frame, text = "/", command = self.divide).grid(row = 0, column = 0)
        Button(frame, text = '*', command = self.multiply).grid(row = 1, column = 0)
        Button(frame, text = "-", command = self.subtract).grid(row = 2, column = 0)
        Button(frame, text = '+', command = self.add).grid(row = 3, column = 0)


    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass


root = Tk()
Calc = Calculator(root)
root.mainloop()
try:
    root.destroy()
except Exception:
    pass