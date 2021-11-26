from tkinter import *
import tkinter as tk
from tkinter.constants import W
import webbrowser
from PIL import ImageTk, Image
import os
import numpy as np
import matplotlib.pyplot as plt

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
calc_data = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccalendar.png")
calc_prog = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calcprogram.png")
calc_scient = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calcscient.png")
calc_charts = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccharts.png")


class main_window():
    self = tk.Tk()
    self.title("Charts | ©2021 Jan Kupczyk")
    self.geometry("320x470")
    self.resizable(0, 0)
    self.iconbitmap(faviconn)
    self.configure(bg = WHITE_BG)


    canvas1 = tk.Canvas(self, width = 48, height = 25, bg=WHITE_BG)
    canvas1.pack()

    titleentry = tk.Entry (self)
    canvas1.create_window(25, 25, window=titleentry)

    def stem_graph():
        stem_graphf = np.random.normal(500, 3332, 35) 
        plt.stem(stem_graphf)
        mytitle = "Your stem graph"
        plt.title(f"{mytitle}")
        plt.show()

    def polar_graph():
        polar_graphf = np.random.normal(332, 3323, 33)
        plt.polar(polar_graphf)
        mytitle = "Your polar graph"
        plt.title(f"{mytitle}")
        plt.show()

    def hist_graph():
        hist_graphf = np.random.normal(1233, 11235, 22)
        plt.hist(hist_graphf)
        mytitle = "Your hist graph"
        plt.title(f"{mytitle}")
        plt.show()

    def pie_graph():
        pie_graphf = np.random.normal(40, 22, 5)
        plt.pie(pie_graphf)
        mytitle = "Your pie graph"
        plt.title(f"{mytitle}")
        plt.show()

    charts_btn = Button(self, text="Stem graph", bg=BLUE ,command=stem_graph)
    charts_btn.pack(pady=30,padx=12)

    charts_btn = Button(self, text="Polar graph", bg=BLUE ,command=polar_graph)
    charts_btn.pack(pady=0,padx=12)

    charts_btn = Button(self, text="Hist graph", bg=BLUE ,command=hist_graph)
    charts_btn.pack(pady=30,padx=12)

    charts_btn = Button(self, text="Pie graph", bg=BLUE ,command=pie_graph)
    charts_btn.pack(pady=0,padx=12)

    self.mainloop()


# BOILERPLATE
if __name__ == "__main__":
    main_window()