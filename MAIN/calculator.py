from tkinter import *
import tkinter as tk
from tkinter.constants import W
import webbrowser
from PIL import ImageTk, Image
import os
from tkinter import messagebox

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
GH_BG = "#464646" #GitHub BTN
LI_BG = "#417dcd" #LinkedIn BTN
TW_BG = "#00b7ff" #Twitter BTN
WB_BG = "#2e2e2e" #Website BTN

# ICONS
faviconn = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/favicon/calc.ico")
calc_calc = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc.png")
calc_data = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccalendar.png")
calc_prog = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calcprogram.png")
calc_scient = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calcscient.png")
calc_charts = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccharts.png")
calc_curr = ("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccurr.png")

# NAVBAR TOGGLER
class ToggleMenu(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=250, height=470, bg='#c5c6c7')
        self.button_callback = None
        # UI MENU
        self.create_text(50, 60, text='Calculator', anchor=tk.CENTER, font=TOGGLER_SMALL)
        self.button = tk.Button(self, text='Standard', font=TOGGLER_SMALL_BTN, bg=BLUE, command=lambda: self.button_callback(os.system('python MAIN/calculator.py')))
        self.create_window(70, 100, window=self.button)
        self.button = tk.Button(self, text='Programmer ', font=TOGGLER_SMALL_BTN, bg=BLUE, command=lambda: self.button_callback())
        self.create_window(84, 140, window=self.button)
        self.button = tk.Button(self, text='Charts ', font=TOGGLER_SMALL_BTN, bg=BLUE, command=lambda: self.button_callback(os.system('python MAIN/calculator_data/calc_charts_sub.py')))
        self.create_window(67, 180, window=self.button)
        self.button = tk.Button(self, text='Date ', font=TOGGLER_SMALL_BTN, bg=BLUE, command=lambda: self.button_callback(os.system('python MAIN/calculator_data/calc_data_sub.py')))
        self.create_window(62, 220, window=self.button)
        self.button = tk.Button(self, text="Currency", font=TOGGLER_SMALL_BTN, bg=BLUE, command=lambda: self.button_callback(os.system('python tempdata/calc_curr_sub.py')))
        self.create_window(72, 260, window=self.button)
        self.button = tk.Button(self, text='GitHub repo!', font=TOGGLER_SMALL_BTN_JK, command=lambda: self.button_callback(webbrowser.open('https://github.com/jankupczyk/Calculator')))
        self.create_window(125, 425, window=self.button)
        self.button = tk.Button(self, text='', font=TOGGLER_SMALL_BTN_JK, bg=GH_BG, command=lambda: self.button_callback(webbrowser.open('https://github.com/jankupczyk')))
        self.create_window(81, 368, window=self.button)
        self.button = tk.Button(self, text='', font=TOGGLER_SMALL_BTN_JK, bg=LI_BG, command=lambda: self.button_callback(webbrowser.open('https://www.linkedin.com/in/jan-kupczyk')))
        self.create_window(111, 368, window=self.button)
        self.button = tk.Button(self, text='', font=TOGGLER_SMALL_BTN_JK, bg=TW_BG, command=lambda: self.button_callback(webbrowser.open('https://twitter.com/Jan57965221')))
        self.create_window(141, 368, window=self.button)
        self.button = tk.Button(self, text='', font=TOGGLER_SMALL_BTN_JK, bg=WB_BG, command=lambda: self.button_callback(webbrowser.open('https://jankupczyk.github.io/KUPCZYK/')))
        self.create_window(171, 368, window=self.button)
        self.create_text(125, 447, text='Calculator 30.1011.3 ', anchor=tk.CENTER, font=TOGGLER_SMALL_BTN_JK)
        self.create_text(125, 462, text='©2021 Jan Kupczyk. All rights reserved.', anchor=tk.CENTER, font=TOGGLER_SMALL_BTN_JK)
        loadimg1 = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calc.png")
        renderimg1 = ImageTk.PhotoImage(loadimg1)
        img = Label(self, image=renderimg1)
        img.image = renderimg1
        img.place(x=3, y=82)
        loadimg2 = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calcprogram.png")
        renderimg2 = ImageTk.PhotoImage(loadimg2)
        img = Label(self, image=renderimg2)
        img.image = renderimg2
        img.place(x=3, y=122)
        loadimg3 = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccharts.png")
        renderimg3 = ImageTk.PhotoImage(loadimg3)
        img = Label(self ,image=renderimg3)
        img.image = renderimg3
        img.place(x=3, y=162)
        loadimg4 = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccalendar.png")
        renderimg4 = ImageTk.PhotoImage(loadimg4)
        img = Label(self, image=renderimg4)
        img.image = renderimg4
        img.place(x=3, y=202)
        loadimg5 = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/iconsm/calccurr.png")
        renderimg5 = ImageTk.PhotoImage(loadimg5)
        img = Label(self, image=renderimg5)
        img.image = renderimg5
        img.place(x=3, y=242)

        loadimg1_media = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/media/github.png")
        loadimg1_media = ImageTk.PhotoImage(loadimg1_media)
        img = Label(self, image=loadimg1_media)
        img.image = loadimg1_media
        img.place(x=67, y=370)

        loadimg2_media = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/media/linkedin.png")
        loadimg2_media = ImageTk.PhotoImage(loadimg2_media)
        img = Label(self, image=loadimg2_media)
        img.image = loadimg2_media
        img.place(x=97, y=370)

        loadimg3_media = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/media/twitter.png")
        loadimg3_media = ImageTk.PhotoImage(loadimg3_media)
        img = Label(self, image=loadimg3_media)
        img.image = loadimg3_media
        img.place(x=127, y=370)

        loadimg4_media = Image.open("H:/VSC/PROJEKTY/Calculator/src/Calculator/Assets/media/website.png")
        loadimg4_media = ImageTk.PhotoImage(loadimg4_media)
        img = Label(self, image=loadimg4_media)
        img.image = loadimg4_media
        img.place(x=157, y=370)


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
        self.window.title("Calculator | ©2021 Jan Kupczyk")
        self.window.iconbitmap(faviconn)
        self.is_toggle_active: bool = False
        self.button_callback = None
        self.__ui_create()

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '¬':(4, 1), 0: (4, 2), ',': (4, 3)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.__ui_create()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_negation_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=WHITE_BG,
                               fg=TK_LABEL, padx=24, font=SMALL)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=WHITE_BG,
                         fg=TK_LABEL, padx=24, font=ERROR)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=WHITE_BG)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=TK_LABEL, font=DIGITS,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=WHITE_SHADE, fg=TK_LABEL, font=DEFAULT,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
        
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg=WHITE_SHADE, fg=TK_LABEL, font=DEFAULT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=WHITE_SHADE, fg=TK_LABEL, font=DEFAULT,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=WHITE_SHADE, fg=TK_LABEL, font=DEFAULT,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def negation(self):
        self.current_expression = str(eval(f"-{self.current_expression}"))
        self.update_label()

    def create_negation_button(self):
        button = tk.Button(self.buttons_frame, text="\u00ac", bg=WHITE_SHADE, fg=TK_LABEL, font=DEFAULT,
                           borderwidth=0, command=self.negation)
        button.grid(row=4, column=1, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "ERR"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=BLUE, fg=TK_LABEL, font=DEFAULT,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, columnspan=1, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()
        
    def ui_start(self):
        self.window.mainloop()
        
    def __ui_create(self):
        self.label = tk.Label(self.window, text='', font='Segoe 20 bold')
        self.label.pack()
        self.toggle_menu = ToggleMenu(self.window)
        self.toggle_menu.set_button_callback(self.__toggle_callback)
        self.button_toggle = tk.Button(self.window, text='\u2630', font = TOGGLER_BURGER_BTN, command=self.__button_toggle_handler)
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


# BOILERPLATE
if __name__ == "__main__":
    calculatormain = calculator()
    calculatormain.run()
    calculatormain.ui_start()
