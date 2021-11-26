import calendar
from tkinter import *
import tkinter as tk
from tkinter.constants import W
import webbrowser
import os
from tkcalendar.calendar_ import Calendar, calendar
from datetime import datetime, date

# FONTS
ERROR = ("Segoe", 15, "bold")
LARGE = ("Segoe", 30, "bold")
SMALL = ("Segoe", 15)
DIGITS = ("Segoe", 12, "bold")
DEFAULT = ("Segoe", 15)
TOGGLER_SMALL = ("Segoe", 13, "bold")
TOGGLER_SMALL_BTN = ("Segoe", 9)
TOGGLER_SMALL_BTN_JK = ("Segoe", 7, "bold")
MAIN_FONT = ("Segoe", 20)



# COLORS
WHITE = "#f3f3f3" #DIGITS
WHITE_SHADE = "#d9dadb" #FUNCTION BTN
TK_LABEL = "#1a1a1a" #LABEL
WHITE_BG = "#bfbfbf" # CALCULATOR BG
BLUE = "#75a6ca" #BLUE EQUAL BTN

# ICONS
faviconn = ("/data/favicon/calc.ico")


# NAVBAR TOGGLER
class ToggleMenu(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=250, height=470, bg='#c5c6c7')
        self.button_callback = None
        # UI MENU
        self.create_text(50, 60, text='Calculator', anchor=tk.CENTER, font=TOGGLER_SMALL)
        self.button = tk.Button(self, text='Standard', font=TOGGLER_SMALL_BTN, command=lambda: self.button_callback())
        self.create_window(57, 100, window=self.button)
        self.button = tk.Button(self, text='Scientific', font=TOGGLER_SMALL_BTN, command=lambda: self.button_callback())
        self.create_window(57, 140, window=self.button)
        self.button = tk.Button(self, text='Programmer ', font=TOGGLER_SMALL_BTN, command=lambda: self.button_callback())
        self.create_window(69, 180, window=self.button)
        self.button = tk.Button(self, text='Charts ', font=TOGGLER_SMALL_BTN, command=lambda: self.button_callback())
        self.create_window(52, 220, window=self.button)
        self.button = tk.Button(self, text='Date ', font=TOGGLER_SMALL_BTN, command=lambda: self.button_callback())
        self.create_window(47, 260, window=self.button)
        self.button = tk.Button(self, text='Visit my GitHub!', font=TOGGLER_SMALL_BTN_JK, command=lambda: self.button_callback(webbrowser.open('https://github.com/jankupczyk')))
        self.create_window(125, 425, window=self.button)
        self.create_text(125, 447, text='Calculator 23.1011.3 ', anchor=tk.CENTER, font=TOGGLER_SMALL_BTN_JK)
        self.create_text(125, 462, text='©2021 Jan Kupczyk. All rights reserved.', anchor=tk.CENTER, font=TOGGLER_SMALL_BTN_JK)
        # standard = PhotoImage(file='src\\Calculator\\Assets\\favicon\\calc.png')

    def set_button_callback(self, callback):
        self.button_callback = callback

    def ui_start(self):
        self.place(x=0, y=0)
        
    def ui_stop(self):
        self.place_forget()
    
    # MAIN LOOP / CALCULATOR 
class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("320x470")
        self.window.resizable(0, 0)
        self.window.title("Date calculator")
        self.is_toggle_active: bool = False
        self.button_callback = None
        self.__ui_create()

        calend = Calendar(self, selectmode = 'days', year = 2021, month = 11, day = 23)
        calend.pack(pady = 15)

    converted_date = Label(text="Date--> ", bd=2, bg=WHITE_BG,
                                font=LARGE, width=40)
    converted_date.pack(pady=10)

    def add_days():
        Frame1 = Frame()
        Frame2 = Frame()
        days = Spinbox(Frame1, from_= 0, to = 10000000, font=MAIN_FONT)
        days.pack(pady=5,padx=12)
        converted_date = Label(text="Date--> ", bd=2, bg=WHITE_BG,
                                font=LARGE, width=40)
        date_1_box = datetime.datetime.strptime(calendar.get_date(), "%m/%d/%y")
        end_date = date_1_box + datetime.timedelta(days=int(days.get()))
        converted_date.config(text=f"Date--> {end_date.strftime('%m/%d/%Y')}")
 
    def subtract_days():
        Frame1 = Frame()
        Frame2 = Frame()
        days = Spinbox(Frame1, from_= 0, to = 10000000, font=MAIN_FONT)
        days.pack(pady=5,padx=12)
        converted_date = Label(text="Date--> ", bd=2, bg=WHITE_BG,
                                font=LARGE, width=40)
        date_1_box = datetime.datetime.strptime(calendar.get_date(), "%m/%d/%y")
        end_date = date_1_box - datetime.timedelta(days=int(days.get()))
        converted_date.config(text=f"Date--> {end_date.strftime('%m/%d/%Y')}")
 
    Frame1 = Frame()
    Frame2 = Frame()
 
    Frame1.pack()
    Frame2.pack()

    days = Spinbox(Frame1, from_= 0, to = 10000000, font=MAIN_FONT)
    days.pack(pady=5,padx=12)

    Button(Frame1, text = "Add Days", command = add_days, font=MAIN_FONT).pack(side=LEFT)
    Button(Frame2, text = "Subtract Days", command = subtract_days, font=MAIN_FONT).pack(padx=10)

    def run(self):
        self.window.mainloop()
        
    def ui_start(self):
        self.window.mainloop()
        
    def __ui_create(self):
        self.label = tk.Label(self.window, text='', font='Segoe 20 bold')
        self.label.pack()
        self.toggle_menu = ToggleMenu(self.window)
        self.toggle_menu.set_button_callback(self.__toggle_callback)
        self.button_toggle = tk.Button(self.window, text='\u2630', command=self.__button_toggle_handler)
        self.button_toggle.place(x=0, y=0)
        
    def __button_toggle_handler(self):
        if self.is_toggle_active:
            self.toggle_menu.ui_stop()
            self.is_toggle_active = False
        else:
            self.toggle_menu.ui_start()
            self.is_toggle_active = True
            
    def __toggle_callback(self):
        print('Test btn!')
        print('Still in development')
        os.system('python calculator_data/MenuToggler.py')

# BOILERPLATE
if __name__ == "__main__":
    calculatormain = calculator()
    calculatormain.run()
    calculatormain.ui_start()
