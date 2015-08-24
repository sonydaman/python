from Tkinter import *

class Program:

    def __init__(self):
        b1 = Button(text="click me", command=self.callback)
        b2 = Button(text="click me", command=self.callback)
        b3 = Button(text="Button 3", command=self.callback)
        b4 = Button(text="Button 4", command=self.callback)
        b1.pack(side=LEFT,padx=10)
        b2.pack(side=LEFT,padx=10)
        b3.grid(row=0, column=0)
        b4.grid(row=1, column=1)

    def callback(self):
        print "clicked!"

program = Program()

mainloop()