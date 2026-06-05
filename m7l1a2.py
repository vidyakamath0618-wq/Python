#import necessary libraries
from tkinter import *
from datetime import date
#create window
root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')
#add widgets
#add label
lbl = Label(text = "hey there!", fg="white", bg="#0722F5F", height = 1, width = 300)
#add label from getting name as input from user
#Use entry widget to create text box for user to enter details
name_lbl = Label(text = "Full name", bg="#3895D3")
name_entry = Entry()
#function to display a message
def display():
    #read input given by user
    name = name_entry.get()
    #declaring a global variable
    #to make it accessible anywhere in the program
    global Message
    message = "welcome to the application! \nToday's date is:"
    greet = "hello"+name+"\n"
    #display details in a text box
    #specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    #add a text widget to display information/messages
    text_box = Text(height = 3)
    #add button and give value of command as name of the function
    #press button, display function will be called automatically
    btn = Button(text="begin", command = display, height = 1, bg="#1261AO", fg="white")
    #organise all the widgets in the window
    lbl.pack()
    name_lbl.pack()
    name_entry.pack()
    btn.pack()
    text_box.pack()
    #start the GUI event loop
    root.mainloop()