import tkinter as tk
from tkinter import *
import requests
from forex_python.converter import CurrencyRates,CurrencyCodes, _CURRENCY_FORMATTER
from tkinter.constants import W
import webbrowser
from PIL import ImageTk, Image

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
calc_curr = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccurr.png")

URL =  'http://api.exchangeratesapi.io/v1/latest?access_key=4b48b844efbfd55ed5e4621155bce7ce&format=1'
r = requests.get(url=URL)
keys_data = r.json()
currency_keys = keys_data['rates'].keys()


c = CurrencyRates()
print(c.get_rate('USD', 'PLN'))

codes = CurrencyCodes() 

class main_window(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master = master
        self.create_widgets()
        self.label = tk.Label(self)
        self.listbox = tk.Listbox(self)

    def create_widgets(self):

        self.first_curr = tk.Button(self,text='From')
        self.second_curr = tk.Button(self,text='To')

        self.symbols = tk.Button(self, text='Symbols')

        self.first_curr["command"] = self.choose_first
        self.second_curr["command"] = self.choose_second
        self.symbols["command"] = self.show_symbols

        self.first_entry = tk.Entry(width = 15)
        self.second_entry = tk.Entry(width = 15)

        self.first_curr.grid(row=0, column =0, pady=5, padx=2)
        self.second_curr.grid(row=0, column=1, pady=5, padx=20)
        self.first_entry.grid(row=1, column=0, padx=40, pady=200)
        self.second_entry.grid(row=1, column=1, padx=0)

        self.symbols.grid(row=1,column=1)

    def list_of_currencies(self, column='0', event = "<<ListboxSelect>>"):
        self.scrollbar = tk.Scrollbar()
        self.scrollbar.grid(column = column, row = 5)

        mylist = tk.Listbox(yscrollcommand=self.scrollbar.set)
        for key in currency_keys:
            mylist.insert('end', key)

        mylist.grid(column=column, row = 2)
        self.scrollbar.config(command=mylist.yview)

    def callback(self):
        selection = self.widget.curselection()
        if selection:
            index = selection[0]
            data = self.widget.get(index)
            self.label.configure(text=data)
        else:
            self.label.configure(text=' ')

    def choose_first(self):
        first = self.list_of_currencies()
        self.listbox.bind("<<ListboxSelect>>", self.callback)
        global first_symbol
        first_symbol = self.label.cget('text')


    def choose_second(self):
        second = self.list_of_currencies(column='1')
        self.listbox.bind("<<ListboxSelect>>", self.callback)
        self.label.cget('text')
        global second_symbol
        second_symbol = self.label.cget('text')


    def show_symbols(self):
        print(first_symbol)
        print(second_symbol)

self = tk.Tk()
self.title("Currency | ©2021 Jan Kupczyk")
self.geometry("320x470")
self.resizable(0, 0)
self.iconbitmap(faviconn)
self.configure(bg = WHITE_BG)

app = main_window(master=self)
app.mainloop()

# BOILERPLATE
if __name__ == "__main__":
    main_window()