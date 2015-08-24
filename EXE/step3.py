from Tkinter import *

class Program:

    def __init__(self):
        
        b1 = Label( text="This is a label")
        
        b2 = Button(text="click me", command=self.callback)
        b3 = Button(text="Button 3", command=self.callback)
        b4 = Button(text="Get", command=self.callback)
        v = StringVar()
        e = Entry(textvariable=v)
        e.pack()
        b1.pack(padx=30)
        b2.pack(padx=10)
        b3.pack()
        b4.pack()
        b1.grid(row=0, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=0)
        b4.grid(row=2, column=1)
        e.grid(row=2, column=0)


    def callback(self):
        print "clicked!"
        v.get()

program = Program()

mainloop()