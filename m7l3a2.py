#import necessary libraries
from tkinter import *
from tkinter import messagebox
#SetUp tkinter window
root = Tk()
root.geometry("200x200")
#function for displaying warning message
#this will be called once the button is clicked
#messagebox.showwarning("window name", "text to be displayed")
def msg():
    messagebox.showwarning("Alert", "stop virus is found!")
#adding button widget to window
button = Button(root, text="scan for virus", command = msg)
button.place(x = 40, y = 80)
#entering main event loop
root.mainloop()