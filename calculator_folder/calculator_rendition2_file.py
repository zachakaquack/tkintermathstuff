from tkinter import StringVar, BooleanVar

import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton, CTkFont, CTkLabel

import maths
import settings


class Calculator2(ctk.CTkFrame):
    def __init__(self, master, home_frame):
        super().__init__(master)

        # variables
        self.frame = ctk.CTkFrame(master, fg_color="blue")
        self.home_frame = home_frame
        self.master = master

        # take up entire page, 2 columns 1 row
        self.frame.rowconfigure(0, weight=1, uniform="a")
        self.frame.columnconfigure((0, 1), weight=1, uniform="a")

        # left side
        self.left_side = LeftSide(self.frame)

        # right side
        self.right_side = RightSide(self.frame)


    def start_second_calculator_page(self):
        self.frame.pack(expand=True, fill="both")



    def calculator_go_back(self):
        self.frame.pack_forget()


class LeftSide(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.left_side_frame = CTkFrame(master, fg_color="red")
        self.left_side_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.left_side_frame.columnconfigure(0, weight=1, uniform="a")

        self.left_side_frame.grid(row=0, column=0, sticky="nsew")

        self.actual_calculator = ActualCalculator(self.left_side_frame)

        self.below_calculator = BelowCalculator(self.left_side_frame)


class ActualCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.running_equation = StringVar(value="running equation")
        self.answer = StringVar(value="answer")
        self.second_true = BooleanVar(value=False)

        self.bigger_font = CTkFont(family=settings.FONT_FAMILY, size=60)


        self.actual_calculator_frame = CTkFrame(master, fg_color="green")
        self.actual_calculator_frame.grid(row=0, rowspan=3, column=0, sticky="nsew")

        self.actual_calculator_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.actual_calculator_frame.columnconfigure(0, weight=1, uniform="a")

        self.calculator_buttons = CalculatorButtons(self.actual_calculator_frame, self)

        self.calculator_screen = CalculatorScreen(self.actual_calculator_frame, self.running_equation, self.answer)

    def add_to_running_equation(self, entry):
        self.running_equation.set(self.running_equation.get() + entry)

    def clear(self):
        self.running_equation.set("")
        self.answer.set("")

    def answer_equation(self):
        try:
            self.set_answer_to_label(maths.calculator(self.running_equation.get()))
        except SyntaxError:
            self.set_answer_to_label("ERROR")

    def switch_second(self):
        self.second_true.set(not self.second_true.get())
        print(self.second_true.get())

    def set_answer_to_label(self, string):
        self.answer.set(string)

    def delete_last_character(self):
        self.running_equation.set(self.running_equation.get()[:-1])

class CalculatorScreen(ctk.CTkFrame):
    def __init__(self, master, running_equation, answer):
        super().__init__(master)

        self.running_equation = running_equation
        self.answer = answer

        self.font = CTkFont(family=settings.FONT_FAMILY, size=36)

        self.calculator_screen_frame = CTkFrame(master, fg_color="orange")

        self.calculator_screen_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.calculator_screen_frame.columnconfigure(0, weight=1, uniform="a")

        self.calculator_screen_frame.grid(row=0, column=0, sticky="nsew")

        self.running_equation_label = CTkLabel(self.calculator_screen_frame, textvariable=self.running_equation, font=self.font, anchor="w", padx=10)
        self.answer_label = CTkLabel(self.calculator_screen_frame, textvariable=self.answer, font=self.font, anchor="e", padx=10)

        self.running_equation_label.grid(row=0, column=0, sticky="nsew")
        self.answer_label.grid(row=1, column=0, sticky="nsew")

class CalculatorButtons(ctk.CTkFrame):
    def __init__(self, master, parent):
        super().__init__(master)

        self.font = CTkFont(family=settings.FONT_FAMILY, size=48)


        self.calculator_buttons_frame = CTkFrame(master, fg_color="blue")
        self.calculator_buttons_frame.grid(row=1, rowspan=3, column=0, sticky="nsew")
        self.calculator_buttons_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")
        self.calculator_buttons_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # row 0
        self.button_0 = CTkButton(self.calculator_buttons_frame, text="0", font=self.font, command=lambda: parent.add_to_running_equation("0"))
        self.button_period = CTkButton(self.calculator_buttons_frame, text=".", font=self.font, command=lambda: parent.add_to_running_equation("."))
        self.button_negative = CTkButton(self.calculator_buttons_frame, text="-", font=self.font, command=lambda: parent.add_to_running_equation("-"))
        self.button_enter = CTkButton(self.calculator_buttons_frame, text="ENTER", font=self.font, command=lambda: parent.answer_equation())
        self.button_second = CTkButton(self.calculator_buttons_frame, text="2ND", font=self.font, command=lambda: parent.switch_second())

        # row 1
        self.button_CLEAR = CTkButton(self.calculator_buttons_frame, text="CLEAR", font=self.font, command=lambda: parent.clear())
        self.button_1 = CTkButton(self.calculator_buttons_frame, text="1", font=self.font, command=lambda: parent.add_to_running_equation("1"))
        self.button_2 = CTkButton(self.calculator_buttons_frame, text="2", font=self.font, command=lambda: parent.add_to_running_equation("2"))
        self.button_3 = CTkButton(self.calculator_buttons_frame, text="3", font=self.font, command=lambda: parent.add_to_running_equation("3"))
        self.button_plus = CTkButton(self.calculator_buttons_frame, text="+", font=self.font, command=lambda: parent.add_to_running_equation("+"))

        # row 2
        self.button_4 = CTkButton(self.calculator_buttons_frame, text="4", font=self.font, command=lambda: parent.add_to_running_equation("4"))
        self.button_5 = CTkButton(self.calculator_buttons_frame, text="5", font=self.font, command=lambda: parent.add_to_running_equation("5"))
        self.button_6 = CTkButton(self.calculator_buttons_frame, text="6", font=self.font, command=lambda: parent.add_to_running_equation("6"))
        self.button_minus = CTkButton(self.calculator_buttons_frame, text="-", font=self.font, command=lambda: parent.add_to_running_equation("-"))
        self.button_delete = CTkButton(self.calculator_buttons_frame, text="DELETE", font=self.font, command=lambda: parent.delete_last_character())

        # row 3
        self.button_7 = CTkButton(self.calculator_buttons_frame, text="7", font=self.font, command=lambda: parent.add_to_running_equation("7"))
        self.button_8 = CTkButton(self.calculator_buttons_frame, text="8", font=self.font, command=lambda: parent.add_to_running_equation("8"))
        self.button_9 = CTkButton(self.calculator_buttons_frame, text="9", font=self.font, command=lambda: parent.add_to_running_equation("9"))
        self.button_multiply = CTkButton(self.calculator_buttons_frame, text="*", font=self.font, command=lambda: parent.add_to_running_equation("*"))
        self.button_x = CTkButton(self.calculator_buttons_frame, text="x", font=self.font, command=lambda: parent.add_to_running_equation("x"))

        # row 4
        self.button_squared = CTkButton(self.calculator_buttons_frame, text="x^2", font=self.font, command=lambda: parent.add_to_running_equation("^2"))
        self.button_open_paren = CTkButton(self.calculator_buttons_frame, text="(", font=self.font, command=lambda: parent.add_to_running_equation("("))
        self.button_closed_paren = CTkButton(self.calculator_buttons_frame, text=")", font=self.font, command=lambda: parent.add_to_running_equation(")"))
        self.button_division = CTkButton(self.calculator_buttons_frame, text="/", font=self.font, command=lambda: parent.add_to_running_equation("/"))
        self.button_equal = CTkButton(self.calculator_buttons_frame, text="=", font=self.font, command=lambda: parent.add_to_running_equation("="))

        # row 5
        self.button_sin = CTkButton(self.calculator_buttons_frame, text="sin", font=self.font, command=lambda: parent.add_to_running_equation("sin("))
        self.button_cos = CTkButton(self.calculator_buttons_frame, text="cos", font=self.font, command=lambda: parent.add_to_running_equation("cos("))
        self.button_tan = CTkButton(self.calculator_buttons_frame, text="tan", font=self.font, command=lambda: parent.add_to_running_equation("tan("))
        self.button_exponent = CTkButton(self.calculator_buttons_frame, text="^", font=self.font, command=lambda: parent.add_to_running_equation("^"))

        # placing everything
        self.button_second.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
        self.button_0.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)
        self.button_period.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)
        self.button_negative.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

        self.button_enter.grid(row=5, column=4, sticky="nsew", padx=5, pady=5)
        self.button_CLEAR.grid(row=4, column=4, sticky="nsew", padx=5, pady=5)
        self.button_delete.grid(row=3, column=4, sticky="nsew", padx=5, pady=5)

        self.button_1.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
        self.button_2.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
        self.button_3.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)
        self.button_plus.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

        self.button_4.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        self.button_5.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        self.button_6.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)
        self.button_minus.grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

        self.button_7.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.button_8.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.button_9.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        self.button_multiply.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)
        self.button_x.grid(row=2, column=4, sticky="nsew", padx=5, pady=5)

        self.button_squared.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.button_open_paren.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.button_closed_paren.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        self.button_division.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
        self.button_equal.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)

        self.button_sin.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.button_cos.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.button_tan.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.button_exponent.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)



class BelowCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.below_calculator_frame = CTkFrame(master, fg_color="yellow")
        self.below_calculator_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.below_calculator_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")

        self.below_calculator_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.back_button = BackButton(self.below_calculator_frame)
        self.copy_and_paste = CopyAndPasteButtons(self.below_calculator_frame)
        self.calculator_entry = CalculatorEntry(self.below_calculator_frame)


class BackButton(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.back_button_frame = CTkFrame(master, fg_color="purple")
        self.back_button_frame.grid(row=1, column=0, sticky="nsew")
        self.back_button_frame.rowconfigure(0, weight=1, uniform="a")
        self.back_button_frame.columnconfigure(0, weight=1, uniform="a")

        self.button = ctk.CTkButton(self.back_button_frame, command=lambda: print("test"))
        self.button.grid(row=0, column=0)

class CopyAndPasteButtons(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.copy_and_paste_buttons_frame = CTkFrame(master, fg_color="red")
        self.copy_and_paste_buttons_frame.grid(row=1, column=1, columnspan=2, sticky="nsew")

class CalculatorEntry(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.calculator_entry_frame = CTkFrame(master, fg_color="blue")
        self.calculator_entry_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

class RightSide(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.right_side_frame = CTkFrame(master, fg_color="orange")
        self.right_side_frame.grid(row=0, column=1, sticky="nsew")

        self.right_side_frame.rowconfigure(0, weight=3, uniform="a")
        self.right_side_frame.rowconfigure(1, weight=1, uniform="a")

        self.right_side_frame.columnconfigure(0, weight=1, uniform="a")

        self.right_side_above = RightSideAbove(self.right_side_frame)
        self.right_side_below = RightSideBelow(self.right_side_frame)

class RightSideAbove(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.right_side_above_frame = CTkFrame(master, fg_color="pink")
        self.right_side_above_frame.grid(row=0, column=0, sticky="nsew")
        self.right_side_above_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_above_frame.columnconfigure(0, weight=1, uniform="a")

        self.right_side_above_dropdown = RightSideAboveDropdown(self.right_side_above_frame)
        self.right_side_above_entrees = RightSideAboveEntrees(self.right_side_above_frame)

class RightSideAboveDropdown(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.right_side_above_dropdown_frame = CTkFrame(master, fg_color="brown")
        self.right_side_above_dropdown_frame.grid(row=0, column=0, sticky="nsew")

class RightSideAboveEntrees(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.right_side_above_entrees_frame = CTkFrame(master, fg_color="yellow")
        self.right_side_above_entrees_frame.grid(row=1, column=0, sticky="nsew")

class RightSideBelow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.right_side_below_frame = CTkFrame(master, fg_color="turquoise")
        self.right_side_below_frame.grid(row=1, column=0, sticky="nsew")

        self.right_side_below_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_below_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

        self.right_side_below_copy_equation_button = ctk.CTkButton(self.right_side_below_frame, command=lambda: print("copy"))
        self.right_side_below_paste_end_running = ctk.CTkButton(self.right_side_below_frame, command=lambda: print("end of running"))
        self.right_side_below_generate_idk = ctk.CTkButton(self.right_side_below_frame, command=lambda: print("generate"))
        self.right_side_below_enter = ctk.CTkButton(self.right_side_below_frame, command=lambda: print("enter"))

        self.right_side_below_copy_equation_button.grid(row=1, column=0, sticky="nsew")
        self.right_side_below_paste_end_running.grid(row=1, column=1, sticky="nsew")
        self.right_side_below_generate_idk.grid(row=1, column=2, sticky="nsew")
        self.right_side_below_enter.grid(row=1, column=3, sticky="nsew")