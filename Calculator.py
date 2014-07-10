__author__ = 'Dilan'

from Tkinter import *


class Calculator:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.addButton = Button(frame, text = '+', command = self.add)
        self.addButton.pack(side = RIGHT)
        self.subtractButton = Button(frame, text = "-", command = frame.quit)
        self.subtractButton.pack(side = RIGHT)
        self.multiplyButton = Button(frame, text = '*', command = frame.quit)
        self.multiplyButton.pack(side = RIGHT)
        self.divideButton = Button(frame, text = "/", command = frame.quit)
        self.divideButton.pack(side = RIGHT)

    def add(self):
        x = int(raw_input("Please enter the first number to be added: "))
        y = int(raw_input("Please enter the second number to be added: "))
        return x + y


root = Tk()
Calc = Calculator(root)
root.mainloop()
try:
    root.destroy()
except Exception, e:
    print 'Error: %s' % (e)