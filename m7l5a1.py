#import necessary libraries
from tkinter import *
#setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")
#function to open new (Top Level) window
def topwin():
    #setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #adding label widget to Top Window
    l2 = Label(top, text="This is top level window")
    l2.pack()
    top.mainloop()
    #adding a label and button Widget to Root (Main)window
    l = Label(root, text="This is root window")
    btn = Button(root, text="click here to open another window", command=topwin)
    #arrangind widgets
    l.pack()
    btn.pack()
    root.mainloop()