from tkinter import StringVar, BooleanVar

import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton, CTkFont, CTkLabel, CTkEntry, CTkComboBox

import maths
import settings


class Calculator2(ctk.CTkFrame):
    def __init__(self, master, home_frame):
        super().__init__(master)

        # variables
        self.frame = ctk.CTkFrame(master, fg_color="transparent")
        self.home_frame = home_frame
        self.master = master
        self.clipboard = ""

        # take up entire page, 2 columns 1 row
        self.frame.rowconfigure(0, weight=1, uniform="a")
        self.frame.columnconfigure((0, 1), weight=1, uniform="a")

        # left side
        self.left_side = LeftSide(self.frame, self, self.clipboard)

        # right side
        self.right_side = RightSide(self.frame, self.left_side.actual_calculator)


    def start_second_calculator_page(self):
        self.frame.pack(expand=True, fill="both")



    def calculator_go_back(self):
        self.frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)


# LEFT SIDE
# LEFT SIDE
# LEFT SIDE
# LEFT SIDE

class LeftSide(ctk.CTkFrame):
    def __init__(self, master, calculator2, clipboard):
        super().__init__(master)

        self.running_equation = StringVar(value="4x + 4 = 8x")
        self.calculator2 = calculator2

        self.left_side_frame = CTkFrame(master, fg_color="transparent")
        self.left_side_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.left_side_frame.columnconfigure(0, weight=1, uniform="a")

        self.left_side_frame.grid(row=0, column=0, sticky="nsew")

        self.actual_calculator = ActualCalculator(self.left_side_frame, self.running_equation, self)

        self.below_calculator = BelowCalculator(self.left_side_frame, self.running_equation, self.calculator2, clipboard, self.actual_calculator)

class ActualCalculator(ctk.CTkFrame):
    def __init__(self, master, running_equation, left_side):
        super().__init__(master)

        self.left_side = left_side

        self.running_equation = running_equation
        self.answer = StringVar(value="answer")
        self.second_true = BooleanVar(value=False)

        self.bigger_font = CTkFont(family=settings.FONT_FAMILY, size=60)


        self.actual_calculator_frame = CTkFrame(master, fg_color="transparent")
        self.actual_calculator_frame.grid(row=0, rowspan=3, column=0, sticky="nsew")

        self.actual_calculator_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.actual_calculator_frame.columnconfigure(0, weight=1, uniform="a")

        self.calculator_buttons = CalculatorButtons(self.actual_calculator_frame, self)

        self.calculator_screen = CalculatorScreen(self.actual_calculator_frame, running_equation, self.answer)

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

    def set_answer_to_label(self, string):
        self.answer.set(string)

    def delete_last_character(self):
        self.running_equation.set(self.running_equation.get()[:-1])

    def midpoint_calculator(self, points):
        self.answer.set(maths.midpoint_calculator(points))

    def distance_calculator(self, points):
        self.answer.set(maths.distance_calculator(points))

    def generate_table(self, information):
        self.left_side.calculator2.right_side.right_side_above.right_side_above_table_generator.switch_to_second_page()

class CalculatorScreen(ctk.CTkFrame):
    def __init__(self, master, running_equation, answer):
        super().__init__(master)

        self.running_equation = running_equation
        self.answer = answer

        self.font = CTkFont(family=settings.FONT_FAMILY, size=36)

        self.calculator_screen_frame = CTkFrame(master, fg_color="#b2b2b2")

        self.calculator_screen_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.calculator_screen_frame.columnconfigure(0, weight=1, uniform="a")

        self.calculator_screen_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.running_equation_label = CTkLabel(self.calculator_screen_frame, textvariable=self.running_equation, font=self.font, anchor="w", padx=10)
        self.answer_label = CTkLabel(self.calculator_screen_frame, textvariable=self.answer, font=self.font, anchor="e", padx=10)

        self.running_equation_label.grid(row=0, column=0, sticky="nsew")
        self.answer_label.grid(row=1, column=0, sticky="nsew")

class CalculatorButtons(ctk.CTkFrame):
    def __init__(self, master, parent):
        super().__init__(master)

        self.font = CTkFont(family=settings.FONT_FAMILY, size=48)


        self.calculator_buttons_frame = CTkFrame(master, fg_color="transparent")
        self.calculator_buttons_frame.grid(row=1, rowspan=3, column=0, sticky="nsew", padx=5, pady=5)
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
    def __init__(self, master, running_calculation, calculator2, clipboard, actual_calculator):
        super().__init__(master)


        self.below_calculator_frame = CTkFrame(master, fg_color="transparent")
        self.below_calculator_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.below_calculator_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")

        self.below_calculator_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.back_button = BackButton(self.below_calculator_frame, calculator2)
        self.copy_and_paste = CopyAndPasteButtons(self.below_calculator_frame, running_calculation, clipboard, actual_calculator)
        self.calculator_entry = CalculatorEntry(self.below_calculator_frame, running_calculation)

class BackButton(ctk.CTkFrame):
    def __init__(self, master, calculator2):
        super().__init__(master)

        self.calculator2 = calculator2
        self.go_back_font = CTkFont(family="Calibiri", size=36)

        self.back_button_frame = CTkFrame(master, fg_color="transparent")
        self.back_button_frame.grid(row=1, column=0, sticky="nsew")
        self.back_button_frame.rowconfigure(0, weight=1, uniform="a")
        self.back_button_frame.columnconfigure(0, weight=1, uniform="a")

        self.button = ctk.CTkButton(self.back_button_frame, text="Back", font=self.go_back_font, command=lambda: calculator2.calculator_go_back())
        self.button.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

class CopyAndPasteButtons(ctk.CTkFrame):
    def __init__(self, master, running_equation, clipboard, actual_calculator):
        super().__init__(master)

        self.clipboard = clipboard
        self.actual_calculator = actual_calculator
        self.copy_and_paste_font = CTkFont(family="Calibiri", size=36)

        self.copy_and_paste_buttons_frame = CTkFrame(master, fg_color="transparent")
        self.copy_and_paste_buttons_frame.grid(row=1, column=1, columnspan=2, sticky="nsew")

        self.copy_and_paste_buttons_frame.rowconfigure(0, weight=1, uniform="a")
        self.copy_and_paste_buttons_frame.columnconfigure((0, 1), weight=1, uniform="a")

        self.copy_button = ctk.CTkButton(self.copy_and_paste_buttons_frame, text="Copy", font=self.copy_and_paste_font, command=self.set_clipboard)
        self.paste_button = ctk.CTkButton(self.copy_and_paste_buttons_frame, text="Paste", font=self.copy_and_paste_font, command=self.paste)

        self.copy_button.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.paste_button.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def set_clipboard(self):
        self.clipboard = self.actual_calculator.running_equation.get()

    def paste(self):
        self.actual_calculator.running_equation.set(self.actual_calculator.running_equation.get() + self.clipboard)

class CalculatorEntry(ctk.CTkFrame):
    def __init__(self, master, running_calculation):
        super().__init__(master)

        self.entry_font = CTkFont(family="Calibri", size=40)

        self.calculator_entry_frame = CTkFrame(master, fg_color="transparent")
        self.calculator_entry_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")


        self.calculator_entry_frame.rowconfigure(0, weight=1, uniform="a")
        self.calculator_entry_frame.columnconfigure(0, weight=1, uniform="a")

        self.calculator_entry = CTkEntry(self.calculator_entry_frame, corner_radius=20, font=self.entry_font, textvariable = running_calculation)
        self.calculator_entry.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# RIGHT SIDE
# RIGHT SIDE
# RIGHT SIDE
# RIGHT SIDE

class RightSide(ctk.CTkFrame):
    def __init__(self, master, calculator):
        super().__init__(master)

        self.current_preset_calculation = StringVar()


        self.right_side_frame = CTkFrame(master, fg_color="transparent")
        self.right_side_frame.grid(row=0, column=1, sticky="nsew")

        self.right_side_frame.rowconfigure(0, weight=3, uniform="a")
        self.right_side_frame.rowconfigure(1, weight=1, uniform="a")

        self.right_side_frame.columnconfigure(0, weight=1, uniform="a")

        self.right_side_below = RightSideBelow(self.right_side_frame, self.current_preset_calculation, calculator, self)
        self.right_side_above = RightSideAbove(self.right_side_frame, calculator, self.right_side_below, self.current_preset_calculation)

    def get_information(self):
        match self.current_preset_calculation.get():
            case "Midpoint Calculator":
                return self.right_side_above.right_side_above_midpoint_calculator.get_midpoints()
            case "Distance Calculator":
                return self.right_side_above.right_side_above_distance_calculator.get_distance_points()
            case "Table Generator":
                return self.right_side_above.right_side_above_table_generator.get_table_information()


class RightSideAbove(ctk.CTkFrame):
    def __init__(self, master, calculator, below, current_preset_calculation):
        super().__init__(master)

        self.current_preset_calculation = current_preset_calculation

        self.equation_example_font = CTkFont(family="Calibiri", size=48, weight="bold")
        self.enter_variable_font = CTkFont(family="Calibiri", size=32, weight="bold")

        self.right_side_above_frame = CTkFrame(master, fg_color="transparent")
        self.right_side_above_frame.grid(row=0, column=0, sticky="nsew")

        self.right_side_above_frame.rowconfigure(0, weight=1, uniform="a")
        self.right_side_above_frame.rowconfigure(1, weight=2, uniform="a")

        self.right_side_above_frame.columnconfigure(0, weight=1, uniform="a")

        self.right_side_above_dropdown = RightSideAboveDropdown(self.right_side_above_frame, self.current_preset_calculation, self)
        self.right_side_above_midpoint_calculator = RightSideAboveMidpointCalculator(self.right_side_above_frame, self.equation_example_font, self.enter_variable_font)
        self.right_side_above_distance_calculator = RightSideAboveDistanceCalculator(self.right_side_above_frame, self.equation_example_font, self.enter_variable_font)
        self.right_side_above_table_generator = RightSideAboveTableGenerator(self.right_side_above_frame, self.equation_example_font, self.enter_variable_font)


class RightSideAboveDropdown(ctk.CTkFrame):
    def __init__(self, master, current_preset_calculation, right_side_above):
        super().__init__(master)


        self.current_preset_calculation = current_preset_calculation
        self.right_side_above = right_side_above

        self.combobox_font = CTkFont(family="Calibiri", size=32, weight="bold")


        self.right_side_above_dropdown_frame = CTkFrame(master, fg_color="transparent")
        self.right_side_above_dropdown_frame.grid(row=0, column=0, sticky="nsew")

        self.right_side_above_dropdown_frame.rowconfigure(0, weight=1, uniform="a")
        self.right_side_above_dropdown_frame.columnconfigure(0, weight=1, uniform="a")

        self.right_side_dropdown = CTkComboBox(self.right_side_above_dropdown_frame,
                                               width=650, height=50, corner_radius=40, font=self.combobox_font,
                                               state="readonly",
                                               variable=self.current_preset_calculation,
                                               command=lambda x: self.do_loading(),
                                               values=[
                                                   "",
                                                   "Midpoint Calculator",
                                                   "Distance Calculator",
                                                   "Table Generator"
                                               ])

        self.right_side_dropdown.grid(row=0, column=0, sticky="n", pady=20)

    def do_loading(self):
        self.unload_all()
        match self.current_preset_calculation.get():
            case "Midpoint Calculator":
                self.right_side_above.right_side_above_midpoint_calculator.load_midpoint_calculator()
            case "Distance Calculator":
                self.right_side_above.right_side_above_distance_calculator.load_distance_calculator()
            case "Table Generator":
                self.right_side_above.right_side_above_table_generator.load_entire_table_generator()

    def unload_all(self):
        self.right_side_above.right_side_above_midpoint_calculator.unload_midpoint_calculator()
        self.right_side_above.right_side_above_distance_calculator.unload_distance_calculator()
        self.right_side_above.right_side_above_table_generator.unload_entire_table_generator()

class RightSideAboveMidpointCalculator(ctk.CTkFrame):
    def __init__(self, master, equation_example_font, enter_variable_font):
        super().__init__(master)

        self.equation_example_font = equation_example_font
        self.enter_variable_font = enter_variable_font

        self.x_1 = StringVar()
        self.y_1 = StringVar()
        self.x_2 = StringVar()
        self.y_2 = StringVar()

        self.right_side_above_midpoint_calculator = CTkFrame(master, fg_color="transparent")

        self.right_side_above_midpoint_calculator.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_above_midpoint_calculator.columnconfigure(0, weight=1, uniform="a")

        # example equation above
        self.midpoint_example_label = CTkLabel(self.right_side_above_midpoint_calculator, text="(x, y) = ((x.1 + x.2)/2, (y.1 + y.2)/2)", font=self.equation_example_font)
        self.midpoint_example_label.grid(row=0, column=0, sticky="nsew")

        # enter points

        self.enter_points = CTkFrame(self.right_side_above_midpoint_calculator, fg_color="transparent")

        self.enter_points.rowconfigure((0, 1), weight=1, uniform="a")
        self.enter_points.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

        self.enter_points.grid(row=1, column=0, sticky="nsew")

        # x.1
        self.midpoint_x_1_label = CTkLabel(self.enter_points, text="Enter x.1", font=self.enter_variable_font)
        self.midpoint_x_1_label.grid(row=0, column=0, sticky="nsew")

        self.midpoint_x_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_1)
        self.midpoint_x_1_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # x.1
        self.midpoint_x_1_label = CTkLabel(self.enter_points, text="Enter x.1", font=self.enter_variable_font)
        self.midpoint_x_1_label.grid(row=0, column=0, sticky="nsew")

        self.midpoint_x_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_1)
        self.midpoint_x_1_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # y.1
        self.midpoint_y_1_label = CTkLabel(self.enter_points, text="Enter y.1", font=self.enter_variable_font)
        self.midpoint_y_1_label.grid(row=0, column=1, sticky="nsew")

        self.midpoint_y_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.y_1)
        self.midpoint_y_1_entry.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # x.2
        self.midpoint_x_2_label = CTkLabel(self.enter_points, text="Enter x.2", font=self.enter_variable_font)
        self.midpoint_x_2_label.grid(row=0, column=2, sticky="nsew")

        self.midpoint_x_2_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_2)
        self.midpoint_x_2_entry.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)

        # y.2
        self.midpoint_y_2_label = CTkLabel(self.enter_points, text="Enter y.2", font=self.enter_variable_font)
        self.midpoint_y_2_label.grid(row=0, column=3, sticky="nsew")

        self.midpoint_y_2_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.y_2)
        self.midpoint_y_2_entry.grid(row=1, column=3, sticky="nsew", padx=20, pady=20)

    def get_midpoints(self):
        return self.x_1.get(), self.y_1.get(), self.x_2.get(), self.y_2.get()

    def load_midpoint_calculator(self):
        self.right_side_above_midpoint_calculator.grid(row=1, column=0, sticky="nsew")

    def unload_midpoint_calculator(self):
        self.right_side_above_midpoint_calculator.grid_forget()


class RightSideAboveDistanceCalculator(ctk.CTkFrame):
    def __init__(self, master, equation_example_font, enter_variable_font):
        super().__init__(master)

        self.x_1 = StringVar()
        self.y_1 = StringVar()
        self.x_2 = StringVar()
        self.y_2 = StringVar()

        self.equation_example_font = equation_example_font
        self.enter_variable_font = enter_variable_font

        self.right_side_above_distance_calculator = CTkFrame(master, fg_color="transparent")

        self.right_side_above_distance_calculator.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_above_distance_calculator.columnconfigure(0, weight=1, uniform="a")

        # example equation above

        self.distance_example_label = CTkLabel(self.right_side_above_distance_calculator,
                                               text="d = sqrt((x.2 - x.1)^2 + (y.2 - y.1)^2)",
                                               font = self.equation_example_font)
        self.distance_example_label.grid(row=0, column=0, sticky="nsew")

        # enter points

        self.enter_points = CTkFrame(self.right_side_above_distance_calculator, fg_color="transparent")

        self.enter_points.rowconfigure((0, 1), weight=1, uniform="a")
        self.enter_points.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

        self.enter_points.grid(row=1, column=0, sticky="nsew")

        # x.1
        self.distance_x_1_label = CTkLabel(self.enter_points, text="Enter x.1", font=self.enter_variable_font)
        self.distance_x_1_label.grid(row=0, column=0, sticky="nsew")

        self.distance_x_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_1)
        self.distance_x_1_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # x.1
        self.distance_x_1_label = CTkLabel(self.enter_points, text="Enter x.1", font=self.enter_variable_font)
        self.distance_x_1_label.grid(row=0, column=0, sticky="nsew")

        self.distance_x_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_1)
        self.distance_x_1_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # y.1
        self.distance_y_1_label = CTkLabel(self.enter_points, text="Enter y.1", font=self.enter_variable_font)
        self.distance_y_1_label.grid(row=0, column=1, sticky="nsew")

        self.distance_y_1_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.y_1)
        self.distance_y_1_entry.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # x.2
        self.distance_x_2_label = CTkLabel(self.enter_points, text="Enter x.2", font=self.enter_variable_font)
        self.distance_x_2_label.grid(row=0, column=2, sticky="nsew")

        self.distance_x_2_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.x_2)
        self.distance_x_2_entry.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)

        # y.2
        self.distance_y_2_label = CTkLabel(self.enter_points, text="Enter y.2", font=self.enter_variable_font)
        self.distance_y_2_label.grid(row=0, column=3, sticky="nsew")

        self.distance_y_2_entry = CTkEntry(self.enter_points, font=self.enter_variable_font, justify="center",
                                           textvariable=self.y_2)
        self.distance_y_2_entry.grid(row=1, column=3, sticky="nsew", padx=20, pady=20)

    def load_distance_calculator(self):
        self.right_side_above_distance_calculator.grid(row=1, column=0, sticky="nsew")

    def unload_distance_calculator(self):
        self.right_side_above_distance_calculator.grid_forget()

    def get_distance_points(self):
        return self.x_1.get(), self.y_1.get(), self.x_2.get(), self.y_2.get()


class RightSideAboveTableGenerator(ctk.CTkFrame):
    def __init__(self, master, equation_example_font, enter_variable_font):
        super().__init__(master)

        self.x_values = []
        self.y_values = []
        self.rows = []
        self.equation_example_font = equation_example_font
        self.enter_variable_font = enter_variable_font
        self.button_font = CTkFont(family="Calibri", size=24)

        self.low_value = StringVar(value="0")
        self.high_value = StringVar(value="0")
        self.equation = StringVar(value="y=x")

        self.right_side_above_entire_table_generator = CTkFrame(master, fg_color="transparent")
        self.right_side_above_entire_table_generator.rowconfigure(0, weight=1, uniform="a")
        self.right_side_above_entire_table_generator.columnconfigure(0, weight=1, uniform="a")


        self.right_side_above_table_generator = CTkFrame(self.right_side_above_entire_table_generator, fg_color="transparent")
        self.right_side_above_table_generator.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_above_table_generator.columnconfigure((0, 1, 2), weight=1, uniform="a")

        self.low_value_label = CTkLabel(self.right_side_above_table_generator, text="Low Value", font=self.enter_variable_font)
        self.low_value_label.grid(row=0, column=0, sticky="nsew")

        self.low_value_entry = CTkEntry(self.right_side_above_table_generator, textvariable=self.low_value, font=self.enter_variable_font, justify="center")
        self.low_value_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)


        self.high_value_label = CTkLabel(self.right_side_above_table_generator, text="High Value", font=self.enter_variable_font)
        self.high_value_label.grid(row=0, column=1, sticky="nsew")

        self.high_value_entry = CTkEntry(self.right_side_above_table_generator, textvariable=self.high_value, font=self.enter_variable_font, justify="center")
        self.high_value_entry.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)


        self.equation_label = CTkLabel(self.right_side_above_table_generator, text="Equation", font=self.enter_variable_font)
        self.equation_label.grid(row=0, column=2, sticky="nsew")

        self.equation_entry = CTkEntry(self.right_side_above_table_generator, textvariable=self.equation, font=self.enter_variable_font, justify="center")
        self.equation_entry.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)


        # -------- PAGE 2 --------


        self.table_generator_frame = CTkFrame(self.right_side_above_entire_table_generator, fg_color="#b2b2b2")

        self.table_generator_frame.columnconfigure((0, 1), weight=1, uniform="a")


        self.back_from_table_button = CTkButton(self.table_generator_frame, command=self.switch_to_first_page,
                                                text="Input New Equation", font=self.button_font)


    def unload_entire_table_generator(self):
        self.right_side_above_entire_table_generator.grid_forget()

    def load_entire_table_generator(self):
        self.right_side_above_entire_table_generator.grid(row=1, column=0, sticky="nsew")
        self.switch_to_first_page()

    def switch_to_first_page(self):
        self.table_generator_frame.grid_forget()
        self.right_side_above_table_generator.grid(row=0, column=0, sticky="nsew")

    def switch_to_second_page(self):
        self.right_side_above_table_generator.grid_forget()
        self.table_generator_frame.grid(row=0, column=0, sticky="nsew")
        self.make_second_page()

    def get_table_information(self):
        return self.low_value.get(), self.high_value.get(), self.equation.get()

    def make_second_page(self):

        # reset for new page
        self.x_values = []
        self.y_values = []
        self.rows = []

        # generate x values (range from lowest value to highest value)
        for i in range(int(self.low_value.get()), int(self.high_value.get()) + 1):
            self.x_values.append(str(i))

        # generate answers (substitute x value in for equation and add to list)
        for i in range(len(self.x_values)):
            self.y_values.append(self.solve_for(self.x_values[i], self.equation.get().replace("y=", "")))

        # generate amount of rows
        for i in range(len(self.x_values)):
            self.rows.append(i)

        # configure rows to amount needed
        self.table_generator_frame.rowconfigure(self.rows, weight=1, uniform="a")

        # generate each entry in row
        for i in range(len(self.x_values)):
            x_data = StringVar(value="x = " + self.x_values[i])
            y_data = StringVar(value="y = " + self.y_values[i])
            CTkLabel(self.table_generator_frame, textvariable=x_data, font=self.enter_variable_font).grid(row=i,
                                                                                                          column=0,
                                                                                                          sticky="nsew")
            CTkLabel(self.table_generator_frame, textvariable=y_data, font=self.enter_variable_font).grid(row=i,
                                                                                                          column=1,
                                                                                                          sticky="nsew")

        # make back button
        self.back_from_table_button.grid(row=len(self.x_values), column=1, sticky="nsew", padx=50, pady=10)

    def solve_for(self, value, eq):
        new_eq = maths.change_x_multiplication(eq).replace("x", value)
        answer = str(eval(new_eq))
        return answer



class RightSideBelow(ctk.CTkFrame):
    def __init__(self, master, current_preset_calculation, calculator, right_side):
        super().__init__(master)

        self.current_preset_calculation = current_preset_calculation
        self.calculator = calculator
        self.right_side = right_side

        self.right_side_below_frame = CTkFrame(master, fg_color="transparent")
        self.right_side_below_frame.grid(row=1, column=0, sticky="nsew")

        self.right_side_below_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.right_side_below_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")

        self.right_side_below_copy_equation_button = CTkButton(self.right_side_below_frame,text="Copy Equation", command=lambda: print("copy"))
        self.right_side_below_paste_end_running = CTkButton(self.right_side_below_frame,text="Paste To End", command=lambda: print("end of running"))
        self.right_side_below_generate_idk = CTkButton(self.right_side_below_frame,text="Generate Equation", command=lambda: print("generate"))
        self.right_side_below_enter = CTkButton(self.right_side_below_frame, text="Calculate", command=self.send_to_calculator)

        self.right_side_below_copy_equation_button.grid(row=1, column=0, sticky="nsew")
        self.right_side_below_paste_end_running.grid(row=1, column=1, sticky="nsew")
        self.right_side_below_generate_idk.grid(row=1, column=2, sticky="nsew")
        self.right_side_below_enter.grid(row=1, column=3, sticky="nsew")

    def send_to_calculator(self):
        match self.current_preset_calculation.get():
            case "Midpoint Calculator":
                self.calculator.midpoint_calculator(self.right_side.get_information())
            case "Distance Calculator":
                self.calculator.distance_calculator(self.right_side.get_information())
            case "Table Generator":
                self.calculator.generate_table(self.right_side.get_information())
