#import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
#define the RestaurantOrderManagementApp class
class RestaurantOrderManagement:
    #initialize the application
    def __init__(self, root):
        self.root = root #the main window of the app
        self.root.titlr("Restaurant Management App") #Set the title of the window
        #a dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA MEAL":4,
            "CHEESE BURGER":2.5,
            "DRINKS":1
        }
        self.exchange_rate = 82 #exchange rate for currency conversation
        self.setup_backgroung(root) #Set up the background image
        #create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #heading label
        ttk.label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}  #to store references to menu item labels
        self.menu_quantaties = {}#to store references to quantity entry widgets
        #Create labels and entry widgets for each menu item 
        for i, (item, price) in enumerate(self.menu_items.items(), star=1):
            label = ttk.Label(
                frame,
                text=f"{item}(${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_label[item] = label
            quantity_entry = ttk.entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] =  quantity_entry
            #currency selection
            self.currency_var = tk.StringVar()
            ttk.Label(
                frame,
                text="Currency:",
                font=("Arial", 12)
            ).grid(
                row=len(self.menu_items) + 1,
                column = 0,
                padx = 10,
                pady=5
            )
            #Dropdown for currency selection
            curreny_dropdown = ttk.Combox(
                frame,
                textvariable=self.currency_var,
                state="readonly",
                width=18,
                values=("USD", "INR")
            )
            currency_dropdown.grid()