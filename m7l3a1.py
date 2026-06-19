#import necessary libraries
from tkinter import *
#create window
window = Tk()
window.title("event handler")
window.geometry("100*100")
#event handler for keypress
def handle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)
#bind keypress event to handle_keypress()
window.bind("<key>", handle_keypress)
#event handler for buttton click
def handle_click(event):
    print("\nThe button was clicked!")
button = Button(text="click me!")
button.pack()
#bind click event to handle_click()
button.bind("<Button-1>", handle_click)
#start the GUI event loop
window.mainloop()