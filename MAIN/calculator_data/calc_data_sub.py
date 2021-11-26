from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import date
import tkinter as tk
from tkinter.constants import W
import webbrowser
from PIL import ImageTk, Image
import os

# FONTS
ERROR = ("Segoe", 15, "bold")
LARGE = ("Segoe", 30, "bold")
SMALL = ("Segoe", 15)
DIGITS = ("Segoe", 12, "bold")
DEFAULT = ("Segoe", 15)
MAIN_FONT = ("Segoe", 20)
TOGGLER_SMALL = ("Segoe", 13, "bold")
TOGGLER_SMALL_BTN = ("Segoe", 9)
TOGGLER_SMALL_BTN_JK = ("Segoe", 7, "bold")
TOGGLER_BURGER_BTN = ("Serif", 9)


# COLORS
WHITE = "#f3f3f3" #DIGITS
WHITE_SHADE = "#d9dadb" #FUNCTION BTN
TK_LABEL = "#1a1a1a" #LABEL
WHITE_BG = "#bfbfbf" # CALCULATOR BG
BLUE = "#75a6ca" #BLUE EQUAL BTN

# ICONS
faviconn = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/favicon/calc.ico")
calc_calc = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc.png")
calc_data = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc_data16.png")
calc_prog = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc_prog16.png")
calc_scient = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc_scient16.png")

def main_window():
    self = tk.Tk()
    self.title("Date Calculator | ©2021 Jan Kupczyk")
    self.geometry("320x470")
    self.resizable(0, 0)
    self.iconbitmap(faviconn)
    self.configure(bg = WHITE_BG)

    image_canvas = Canvas(self, height = 300, width =110, bg = WHITE_BG, highlightthickness = 0)
    image_canvas.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)

    Label(self, text = "From", bg = WHITE_BG, font=DIGITS).grid(row = 4, column = 8)
    first_date = DateEntry(self)
    first_date.grid(row = 5, column = 8)

    Label(self, text = "To", bg = WHITE_BG, font=DIGITS).grid(row = 6, column = 8)
    second_date = DateEntry(self)
    second_date.grid(row = 7, column = 8)

    Button(self, text = "Calculate difference", bg = BLUE, command = lambda: calculate(first_date, second_date)).grid(row = 8, column = 8)
    self.mainloop()

def calculate(second_date, first_date):
    try:
        difference = first_date.get_date() - second_date.get_date()
        messagebox.showinfo("Date calculator", f"{difference.days} days left!")
    
    except: 
        try:
            day_2, month_2, year_2 = second_date.get().split("-")
            day_1, month_1, year_1 = first_date.get().split("-")

            difference = date(int(year_2), int(month_2), int(day_2)) - date(int(year_1), int(month_1), int(day_1))
            messagebox.showinfo(f"{difference.days}")

        except ValueError as error:
            messagebox.showerror("Fatal error occurred", error)

# BOILERPLATE
if __name__ == "__main__":
    main_window()