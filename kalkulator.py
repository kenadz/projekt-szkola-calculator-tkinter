import tkinter as tk
from tkinter import *
import math

LIGHT_COLOR = "#ffffff"

FONT_STYLE = ("Consolas", 20,"bold")

BG_DARK = "#323232"

DARK_BTN_HOVER = "#191919"
DARK_BTN_NORMAL = "#323232"

BTN_HOVER = DARK_BTN_HOVER
BTN_NORMAL = DARK_BTN_NORMAL

ACTIVE_BG = BG_DARK
FONT_COLOR = LIGHT_COLOR


class Calculator:
    def __init__(self):
        # tworzenie okna
        self.window = tk.Tk()
        self.window.iconbitmap("ikona/ikona.ico")
        self.window.geometry("660x660")
        self.window.minsize(500, 400)
        self.window.resizable(height=True, width=True)
        self.window.title("Kalkulator")
        # tworzenie UI
        self.interface_create()

    def interface_start(self):
        self.window.mainloop()
        
    def interface_create(self):
        self.ostatnie_dzialanie = ""
        self.aktualne_dzialanie = ""
        # pokazywanie aplikacji
        self.display_frame = self.create_display_frame()
        # okno wyniku
        self.total_label, self.label = self.create_display_labels()
        # przypisywanie miejsca danej cyfry
        self.digits = { 7:(1,1), 8:(1,2), 9:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 1:(3,1), 2:(3,2), 3:(3,3), 0:(4,2), ".":(4,1) }
        # przypisanie przycisków
        self.operators = {"/": "\u00F7", "*": "\u00D7","-": "-", "+": "+", "%": "%"}
        # tworzenie przycisków
        self.buttons = self.create_buttons_frame()
        # konfiguracja przycisków w wierszach
        self.buttons.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons.rowconfigure(x, weight=1)
            self.buttons.columnconfigure(x, weight=1)
        # wywołanie innych funkcji
        self.create_digit_buttons()
        self.create_op_buttons()
        self.create_buttons()
        self.bind_keys()

    # keybinding
    def bind_keys(self):
        # bindowanie przycisków
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        self.window.bind("<c>", lambda event: self.clear())
        # przycisk = cyfra
        for key in self.digits:
            self.window.bind(str(key), lambda event, digits = key: self.add_to_expressions(digits))
        # przycisk = operator
        for key in self.operators:
            self.window.bind(key, lambda event, operator = key: self.append_operator(operator))

    # tworzenie przycisków
    def create_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_delete_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_pi_button()
        self.create_plus_min_button()
        self.create_tan_button()
        self.create_sin_button()
        self.create_tau_button()
        self.create_tanh_button()
        self.create_sinh_button()
        self.create_log_button()
        self.create_exp_button()
        self.create_log2_button()
        self.create_E_button()
        self.create_log_button()
        self.create_gamma_button()
        self.create_title()

    # wypisywanie działań na ekran
    def create_display_labels(self):
       total_label=tk.Label(self.display_frame, text=self.ostatnie_dzialanie, anchor=tk.E, bg=ACTIVE_BG, fg=FONT_COLOR, padx=24, font=("Consolas", 24))
       total_label.pack(expand=True, fill="both")

       label=tk.Label(self.display_frame, text=self.aktualne_dzialanie, anchor=tk.E, bg=ACTIVE_BG, fg=FONT_COLOR, padx=24, font=("Consolas", 40, "bold"))
       label.pack(expand=True, fill="both")
            
       return total_label, label

    # pokazywanie okna
    def create_display_frame(self):
        Frame = tk.Frame(self.window, height=220, bg=ACTIVE_BG)
        Frame.pack(expand=True, fill="both")
        return Frame
    # dodawanie do działania
    def add_to_expressions(self, value):
        self.aktualne_dzialanie += str(value)
        self.update_label()
    # tworzenie przycisków cyfr
    def create_digit_buttons(self):
        # zmiana koloru przycisków kiedy się na niego najedzie
        def changedgt_on_hovering(event):
          event.widget["bg"]=BTN_HOVER
        # powrót do normalnego wyglądu przycisku
        def returndgt_to_normalstate(event):
          event.widget["bg"]=BTN_NORMAL
        
        for digit, grid_value in self.digits.items():
            Button =  tk.Button(self.buttons, text=str(digit), bg=ACTIVE_BG, fg=FONT_COLOR, font=("Consolas", 24, "bold"), borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=lambda x=digit: self.add_to_expressions(x))
            Button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            Button.bind("<Enter>", changedgt_on_hovering)
            Button.bind("<Leave>",returndgt_to_normalstate)
    # dodawanie operatorów
    def append_operator(self, operator):
        self.aktualne_dzialanie += operator
        self.ostatnie_dzialanie += self.aktualne_dzialanie
        self.aktualne_dzialanie = ""
        self.update_total_label()
        self.update_label()
# tworzenie przycisków i ich funkcje
    def create_op_buttons(self):
        i = 0
        def changeop_on_hovering(event):
          event.widget["bg"]=BTN_HOVER
        def returnop_to_normalstate(event):
          event.widget["bg"]=BTN_NORMAL

        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons, text=symbol, bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=lambda x=operator:self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            button.bind("<Enter>", changeop_on_hovering)
            button.bind("<Leave>", returnop_to_normalstate)
            i += 1

    def clear(self):
        self.aktualne_dzialanie = ""
        self.ostatnie_dzialanie = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons, text="C", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        
        def changecl_on_hovering(event):
          global create_clear_button
          button["bg"]=BTN_HOVER
        
        def returncl_to_normalstate(event):
          global create_clear_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changecl_on_hovering)
        button.bind("<Leave>",returncl_to_normalstate)

    def delete(self):
      self.aktualne_dzialanie =  self.aktualne_dzialanie[:-1]
      self.update_label()

    def create_delete_button(self):
        button = tk.Button(self.buttons, text="⌫", bg = BTN_NORMAL, fg=FONT_COLOR, font=("Consolas", 20, "bold"), borderwidth=0, activebackground=BTN_NORMAL,command=self.delete)
        button.grid(row=4, column=3, sticky=tk.NSEW)

        def changedel_on_hovering(event):
          global create_delete_button
          button["bg"]=BTN_HOVER
        
        def returndel_to_normalstate(event):
          global create_delete_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changedel_on_hovering)
        button.bind("<Leave>",returndel_to_normalstate)
        
    def square(self):
        self.aktualne_dzialanie = str(eval(f"{self.aktualne_dzialanie}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons, text="x\u00b2", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        
        def changesq_on_hovering(event):
          global create_square_button
          button["bg"]=BTN_HOVER
        
        def returnsq_to_normalstate(event):
          global create_square_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changesq_on_hovering)
        button.bind("<Leave>",returnsq_to_normalstate)     

    def sqrt(self):
        self.aktualne_dzialanie = str(eval(f"{self.aktualne_dzialanie}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons, text="\u221ax", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

        def changesqrt_on_hovering(event):
          global create_sqrt_button
          button["bg"]=BTN_HOVER
        
        def returnsqrt_to_normalstate(event):
          global create_sqrt_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changesqrt_on_hovering)
        button.bind("<Leave>",returnsqrt_to_normalstate)

    def create_title(self):
        button = tk.Button(self.buttons, text="↓ Więcej funkcji ↓", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR)
        button.grid(row=0, column=5, columnspan=3, sticky=tk.NSEW)

    def pi(self):
        self.aktualne_dzialanie = str(math.pi)
        self.update_label()

    def create_pi_button(self):
        button = tk.Button(self.buttons, text="pi", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.pi)
        button.grid(row=1, column=5, sticky=tk.NSEW)
        
        def changepi_on_hovering(event):
          global create_pi_button
          button["bg"]=BTN_HOVER
        
        def returnpi_to_normalstate(event):
          global create_pi_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changepi_on_hovering)
        button.bind("<Leave>",returnpi_to_normalstate) 

    def plus_min(self):
        self.aktualne_dzialanie = str(-(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_plus_min_button(self):
        button = tk.Button(self.buttons, text="+/-", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.plus_min)
        button.grid(row=1, column=6, sticky=tk.NSEW)
        
        def changeplus_min_on_hovering(event):
          global create_plus_min_button
          button["bg"]=BTN_HOVER
        
        def returnplus_min_to_normalstate(event):
          global create_plus_min_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changeplus_min_on_hovering)
        button.bind("<Leave>",returnplus_min_to_normalstate) 

    def tan(self):
        self.aktualne_dzialanie = str(math.tan(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_tan_button(self):
        button = tk.Button(self.buttons, text="tan", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.tan)
        button.grid(row=1, column=7, sticky=tk.NSEW)
        
        
        def changetan_on_hovering(event):
          global create_tan_button
          button["bg"]=BTN_HOVER
        
        def returntan_to_normalstate(event):
          global create_tan_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changetan_on_hovering)
        button.bind("<Leave>",returntan_to_normalstate)

    def sin(self):
        self.aktualne_dzialanie = str(math.sin(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_sin_button(self):
        button = tk.Button(self.buttons, text="sin", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.sin)
        button.grid(row=2, column=5, sticky=tk.NSEW)
        
        
        def changesin_on_hovering(event):
          global create_sin_button
          button["bg"]=BTN_HOVER
        
        def returnsin_to_normalstate(event):
          global create_sin_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changesin_on_hovering)
        button.bind("<Leave>",returnsin_to_normalstate) 

    def tau(self):
        self.aktualne_dzialanie = str(math.tau)
        self.update_label()

    def create_tau_button(self):
        button = tk.Button(self.buttons, text="tau", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.tau)
        button.grid(row=2, column=6, sticky=tk.NSEW)
        
        
        def changetau_on_hovering(event):
          global create_tau_button
          button["bg"]=BTN_HOVER
        
        def returntau_to_normalstate(event):
          global create_tau_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changetau_on_hovering)
        button.bind("<Leave>",returntau_to_normalstate) 

    def tanh(self):
        self.aktualne_dzialanie = str(math.tanh(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_tanh_button(self):
        button = tk.Button(self.buttons, text="tanh", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.tanh)
        button.grid(row=2, column=7, sticky=tk.NSEW)
        
        
        def changetauh_on_hovering(event):
          global create_tanh_button
          button["bg"]=BTN_HOVER
        
        def returntauh_to_normalstate(event):
          global create_tanh_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changetauh_on_hovering)
        button.bind("<Leave>",returntauh_to_normalstate) 

    def sinh(self):
        self.aktualne_dzialanie = str(math.sinh(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_sinh_button(self):
        button = tk.Button(self.buttons, text="sinh", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.sinh)
        button.grid(row=3, column=5, sticky=tk.NSEW)
        
        
        def changesinh_on_hovering(event):
          global create_sinh_button
          button["bg"]=BTN_HOVER
        
        def returnsinh_to_normalstate(event):
          global create_sinh_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changesinh_on_hovering)
        button.bind("<Leave>",returnsinh_to_normalstate) 

    def log(self):
        self.aktualne_dzialanie = str(math.log(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_log_button(self):
        button = tk.Button(self.buttons, text="log", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.log)
        button.grid(row=3, column=6, sticky=tk.NSEW)
        
        
        def changelog_on_hovering(event):
          global create_log_button
          button["bg"]=BTN_HOVER
        
        def returnlog_to_normalstate(event):
          global create_log_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changelog_on_hovering)
        button.bind("<Leave>",returnlog_to_normalstate) 

    def exp(self):
        self.aktualne_dzialanie = str(math.exp(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_exp_button(self):
        button = tk.Button(self.buttons, text="exp", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.exp)
        button.grid(row=3, column=7, sticky=tk.NSEW)
        
        def changeexp_on_hovering(event):
          global create_exp_button
          button["bg"]=BTN_HOVER
        
        def returnexp_to_normalstate(event):
          global create_exp_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changeexp_on_hovering)
        button.bind("<Leave>",returnexp_to_normalstate) 

    def log2(self):
        self.aktualne_dzialanie = str(math.log2(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_log2_button(self):
        button = tk.Button(self.buttons, text="log2", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.log2)
        button.grid(row=4, column=5, sticky=tk.NSEW)
        
        def changelog2_on_hovering(event):
          global create_log2_button
          button["bg"]=BTN_HOVER
        
        def returnlog2_to_normalstate(event):
          global create_log2_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changelog2_on_hovering)
        button.bind("<Leave>",returnlog2_to_normalstate) 

    def E(self):
        self.aktualne_dzialanie = str(math.e)
        self.update_label()

    def create_E_button(self):
        button = tk.Button(self.buttons, text="E", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.E)
        button.grid(row=4, column=6, sticky=tk.NSEW)
        
        def changeE_on_hovering(event):
          global create_E_button
          button["bg"]=BTN_HOVER
        
        def returnE_to_normalstate(event):
          global create_E_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changeE_on_hovering)
        button.bind("<Leave>",returnE_to_normalstate) 

    def gamma(self):
        self.aktualne_dzialanie = str(math.gamma(float(self.aktualne_dzialanie)))
        self.update_label()

    def create_gamma_button(self):
        button = tk.Button(self.buttons, text="gamma", bg=ACTIVE_BG, fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground=BTN_NORMAL,activeforeground=FONT_COLOR,command=self.gamma)
        button.grid(row=4, column=7, sticky=tk.NSEW)
        
        def changegamma_on_hovering(event):
          global create_gamma_button
          button["bg"]=BTN_HOVER
        
        def returngamma_to_normalstate(event):
          global create_gamma_button
          button["bg"]=BTN_NORMAL
        
        button.bind("<Enter>", changegamma_on_hovering)
        button.bind("<Leave>",returngamma_to_normalstate) 

    def evaluate(self):
        self.ostatnie_dzialanie += self.aktualne_dzialanie
        self.update_total_label()
        try:
            self.aktualne_dzialanie = str(eval(self.ostatnie_dzialanie))

            self.ostatnie_dzialanie = ""
        except Exception as error:
            self.aktualne_dzialanie = ("Błąd")
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons, text="=", bg="#4ec0ff", fg=FONT_COLOR, font= FONT_STYLE, borderwidth=0, activebackground="#B8E6FF",activeforeground=FONT_COLOR,command=self.evaluate)
        button.grid(row=5, column=1, columnspan=7, rowspan=5, sticky=tk.NSEW)

        def changeeql_on_hovering(event):
          global create_equals_button
          button["bg"]="#4e9fff"


        def returneql_to_normalstate(event):
          global create_equals_button
          button["bg"]="#4ec0ff"
        
        button.bind("<Enter>", changeeql_on_hovering)
        button.bind("<Leave>",returneql_to_normalstate)
    # funkcja, która tworzy przyciski
    def create_buttons_frame(self):
        Frame= tk.Frame(self.window)
        Frame.pack(expand=True, fill="both")
        return Frame
    # aktualizowanie wyniku
    def update_total_label(self):
        expression = self.ostatnie_dzialanie
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f"{symbol}")
        self.total_label.config(text=expression)

    def update_label(self):   
        self.label.config(text=self.aktualne_dzialanie[:12])


if __name__.__eq__("__main__"):
    app = Calculator()
    app.interface_start()