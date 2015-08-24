from Tkinter import *

def callback(number):
   print "button", number

b = Button(text="click me", command=callback)
#print b.cget("command")
b.pack()

Button(text="one",   command=lambda: callback(1)).pack()
Button(text="two",   command=lambda: callback(2)).pack()
Button(text="three", command=lambda: callback(3)).pack()


mainloop()