from Tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def NewFile():
    print "New File!"
def OpenFile():
    name = askopenfilename()
    print name
def About():
    print "This is a simple example of a menu"   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
 
filemenuData =[{"Lable":"New","Command":"NewFile"},{"Lable":"Open","Command":"OpenFile"},{"Lable":"Save","Command":"donothing"},{"Lable":"Save as...","Command":"donothing"},{"Lable":"Close","Command":"donothing"}]

for i in range(len(filemenuData)):
	filemenu.add_command(label=filemenuData[i]["Lable"], command=filemenuData[i]["Command"])
filemenu.add_command(label="New", command=NewFile)


	
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

# fileMenuMainData = [{"Lable":"File","Command":"filemenu"},{"Lable":"Edit","Command":"editmenu"},{"Lable":"Help","Command":"helpmenu"}]
# for k in range(len(fileMenuMainData)):
	# menubar.add_cascade(label=fileMenuMainData[k]["Lable"], menu=fileMenuMainData[k]["Command"])



editmenu = Menu(menubar, tearoff=0)

editmenuData = [{"Lable":"Undo","Command":"donothing"},{"Lable":"Cut","Command":"donothing"},{"Lable":"Copy","Command":"donothing"},{"Lable":"Paste","Command":"donothing"},{"Lable":"Delete","Command":"donothing"},{"Lable":"Select All","Command":"donothing"}]
for k in range(len(editmenuData)):
	editmenu.add_cascade(label=editmenuData[k]["Lable"], menu=editmenuData[k]["Command"])

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenuData = [{"Lable":"Help Index","Command":"donothing"},{"Lable":"About...","Command":"About"},{"Lable":"Help","Command":"donothing"}]
for k in range(len(helpmenuData)):
	helpmenu.add_command(label=helpmenuData[k]["Lable"], command=helpmenuData[k]["Command"])
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()