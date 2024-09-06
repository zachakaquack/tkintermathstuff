import customtkinter as ctk
from sympy import false

import maths
import settings


class Calculator(ctk.CTkFrame):
    def __init__(self, master, home_frame, font):
        super().__init__(master)

        # variables
        self.frame = ctk.CTkFrame(master, fg_color="transparent")
        self.home_frame = home_frame
        self.master = master

        self.default_calculator = DefaultCalculator(self.frame, self)
        self.side_buttons_row_frame = SideButtons(self.frame, self, self.default_calculator)


        # grid configuration
        self.frame.rowconfigure(0, weight=1, uniform="a")
        self.frame.columnconfigure(0, weight=1, uniform="a")
        self.frame.columnconfigure(1, weight=6, uniform="a")

        self.side_buttons_row_frame.columnconfigure(0, weight=1, uniform="a")

        self.side_buttons_row_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=2, uniform="a")
        self.side_buttons_row_frame.rowconfigure(7, weight=1, uniform="a")

        self.side_buttons_row_frame.grid(row=0, rowspan=10, column=0, sticky=ctk.NSEW)



    def start_calculator_page(self):
        self.frame.pack(expand=True, fill="both")
        self.default_calculator.load_default_calculator()



    def calculator_go_back(self):
        self.side_buttons_row_frame.unload_all()
        self.home_frame.pack(fill="both", expand=True)
        self.frame.pack_forget()



def feed_into_calculator(type_of_problem, problem=None, matrix1 = None, matrix2 = None, points=None, table_info=None):
    # simple, quadratic, has variables, mult matrix, midpoint,
    # distance, table generator, mult matrix by matrix
    match type_of_problem:
        case "simple":
            return maths.calculator(problem)
        case "quadratic":
            return maths.calculator(problem)
        case "variables":
            return maths.calculator(problem)
        case "mult_matrix":
            return maths.mult_matrix(problem, matrix1)
        case "midpoint":
            return maths.midpoint_calculator(points[0], points[1], points[2], points[3])
        case "distance":
            return maths.distance_calculator(points[0], points[1], points[2], points[3])
        case "make_table":
            return maths.make_table(table_info[0], table_info[1], table_info[2])
        case "mult_matrix_by_matrix":
            return maths.mult_matrix_by_matrix(matrix1, matrix2)


class DefaultCalculator(ctk.CTkFrame):
    def __init__(self, master, home_frame):
        super().__init__(master)
        self.master = master
        self.home_frame = home_frame

        self.default_calculator_frame = ctk.CTkFrame(master, fg_color="#719653")
        self.default_calculator_test_text = ctk.CTkLabel(self.default_calculator_frame, text="default calculator")
        self.default_calculator_test_text.grid(row=0, column=1)


    def load_default_calculator(self):
        # column 1 to get to the larger side of the screen
        self.default_calculator_frame.grid(row=0, rowspan=2, column=1, sticky=ctk.NSEW)
        #print("loading basic calculator")
    def unload_default_calculator(self):
        self.default_calculator_frame.grid_forget()
        #print("unloading basic calculator")



class SideButtons(ctk.CTkFrame):
    def __init__(self, master, calc_app, default_calc):
        super().__init__(master, fg_color="green")
        # init
        self.master = master
        self.calc_app = calc_app
        self.default_calc = default_calc

        # buttons and their frames

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")



        # quadratic, has variables, mult matrix,
        # table generator, mult matrix by matrix

        # back
        self.back_button = BackButton(self, calc_app)
        self.back_button.grid(row=7, column=0, sticky=ctk.NSEW, padx=20, pady=20)

        # basic calculator
        self.basic_calculator = BasicCalculator(master)
        self.side_basic_calculator_button = ctk.CTkButton(self, text="Calculator",
                                                          command=lambda: self.load("basic_calculator", self.basic_calculator))
        self.side_basic_calculator_button.grid(row=0, column=0)

        #  midpoint
        self.midpoint_calculator = MidpointCalculator(master)
        self.side_midpoint_calculator_button = ctk.CTkButton(self, text="Midpoint",
                                                             command=lambda: self.load("midpoint_calculator", self.midpoint_calculator))
        self.side_midpoint_calculator_button.grid(row=1, column=0)


        # # distance
        self.distance_calculator = DistanceCalculator(master)
        self.side_distance_calculator_button = ctk.CTkButton(self, text="Distance",
                                                             command=lambda: self.load("distance_calculator", self.distance_calculator))
        self.side_distance_calculator_button.grid(row=2, column=0)

        # table generator
        self.table_generator = TableGenerator(master)
        self.side_table_generator_button = ctk.CTkButton(self, text="Table Generator",
                                                         command=lambda: self.load("table_generator", self.table_generator))
        self.side_table_generator_button.grid(row=3, column=0)


    def load(self, which_to_load, obj):
        if which_to_load != "":
            self.unload_all()
        match which_to_load:
            case "basic_calculator":
                obj.load_basic_calculator()
            case "midpoint_calculator":
                obj.load_midpoint_calculator()
            case "distance_calculator":
                obj.load_distance_calculator()
            case "table_generator":
                obj.load_table_generator()

    def unload_all(self):
        self.default_calc.unload_default_calculator()
        self.basic_calculator.unload_basic_calculator()
        self.midpoint_calculator.unload_midpoint_calculator()
        self.distance_calculator.unload_distance_calculator()
        self.table_generator.unload_table_generator()

class BackButton(ctk.CTkFrame):
    def __init__(self, master, calc_app):
        super().__init__(master, fg_color="brown")

        self.master = master
        self.calc_app = calc_app

        # go back
        self.back_button = ctk.CTkButton(master, text="Back", command=calc_app.calculator_go_back)
        self.back_button.grid(row=7, column=0, sticky=ctk.NSEW, padx=20, pady=20)


class BasicCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="turquoise")

        self.font = ctk.CTkFont(family="Calibiri", size=36)

        # VARIABLES
        self.running_equation = ctk.StringVar(value="x-5=0")
        self.finished_calculation = ctk.StringVar(value="test")



        # the frame the calculator and everything relating to it is kept inside
        self.calculator_content_frame = ctk.CTkFrame(master, fg_color="yellow")
        self.calculator_content_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.calculator_content_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="a")


        # entry at the bottom for the calculator
        self.calculator_entry_frame = ctk.CTkFrame(self.calculator_content_frame, fg_color="blue")
        self.calculator_entry_frame.rowconfigure(0, weight=1, uniform="a")
        self.calculator_entry_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.calculator_entry_frame.grid(row=5, column=0, columnspan=3, sticky=ctk.NSEW, padx=20, pady=20)


        # actual entry
        self.basic_calculator_entry = ctk.CTkEntry(self.calculator_entry_frame, height=100, font=self.font, textvariable=self.running_equation)
        self.basic_calculator_entry.grid(row=0, column=0, columnspan=3, sticky=ctk.NSEW, padx=70, pady=50)

        # copy and paste buttons
        self.calculator_copy_button = ctk.CTkButton(self.calculator_entry_frame, text="copy", corner_radius=50, command=lambda: print("copy"))
        self.calculator_paste_button = ctk.CTkButton(self.calculator_entry_frame, text="paste", corner_radius=50, command=lambda: print("paste"))

        self.calculator_copy_button.grid(row=0, column=3, sticky=ctk.NSEW, padx=50, pady=50)
        self.calculator_paste_button.grid(row=0, column=4, sticky=ctk.NSEW, padx=50, pady=50)


        # entirety of the calculator
        self.basic_calculator_frame = ctk.CTkFrame(self.calculator_content_frame, fg_color="green")
        self.basic_calculator_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.basic_calculator_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        # row zero (middle) rowspan=3 (fully middle) column 1 (to be in right location)
        self.basic_calculator_frame.grid(row=0, rowspan=4, column=1, columnspan=1, sticky=ctk.NSEW, pady=50)

        # buttons
        # lowest row
        self.calculator_button_zero = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                    text="0", command=lambda: self.add_to_current_calculation("0"))
        self.calculator_button_period = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                      text=".", command=lambda: self.add_to_current_calculation("."))
        self.calculator_button_enter = ctk.CTkButton(self.basic_calculator_frame, font=self.font, text="Enter", command=self.load_calculation)
        self.calculator_button_addition = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                        text="+", command=lambda: self.add_to_current_calculation("+"))


        # bottom row
        self.calculator_button_one = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                   text="1",  command=lambda: self.add_to_current_calculation("1"))
        self.calculator_button_two = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                   text="2",  command=lambda: self.add_to_current_calculation("2"))
        self.calculator_button_three = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                     text="3",  command=lambda: self.add_to_current_calculation("3"))
        self.calculator_button_subtraction = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                           text="-",  command=lambda: self.add_to_current_calculation("-"))

        # middle row
        self.calculator_button_four = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                    text="4",  command=lambda: self.add_to_current_calculation("4"))
        self.calculator_button_five = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                    text="5",  command=lambda: self.add_to_current_calculation("5"))
        self.calculator_button_six = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                   text="6",  command=lambda: self.add_to_current_calculation("6"))
        self.calculator_button_multiplication = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                              text="*",  command=lambda: self.add_to_current_calculation("*"))


        # top row
        self.calculator_button_seven = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                     text="7",  command=lambda: self.add_to_current_calculation("7"))
        self.calculator_button_eight = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                     text="8",  command=lambda: self.add_to_current_calculation("8"))
        self.calculator_button_nine = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                    text="9",  command=lambda: self.add_to_current_calculation("9"))
        self.calculator_button_division = ctk.CTkButton(self.basic_calculator_frame, font=self.font,
                                                        text="/",  command=lambda: self.add_to_current_calculation("/"))

        # delete button
        self.calculator_delete_button = ctk.CTkButton(self.calculator_content_frame, font=self.font, height=50,
                                                      text="Delete", command=self.delete_from_calculation)
        self.calculator_delete_button.grid(row=3, column=2, sticky=ctk.NSEW, padx=100, pady=20)

        # clear button
        self.calculator_clear_button = ctk.CTkButton(self.calculator_content_frame, font=self.font, height=50,
                                                      text="Clear", command=self.clear_calculation)
        self.calculator_clear_button.grid(row=2, column=2, sticky=ctk.NSEW, padx=100, pady=20)

        # answer section
        self.calculator_answer_label = ctk.CTkLabel(self.calculator_content_frame, font=self.font,
                                                    fg_color="#b2b2b2", corner_radius=25, textvariable=self.finished_calculation)
        self.calculator_answer_label.grid(row=1, column=2, sticky=ctk.NSEW, padx=100, pady=20)

        # text at the top
        self.calculator_window = ctk.CTkLabel(self.basic_calculator_frame,
                                              textvariable=self.running_equation,
                                              fg_color="#b2b2b2",
                                              anchor="w",
                                              font=self.font,
                                              corner_radius=20)
        self.calculator_window.grid(row=0, column=0, columnspan=5, sticky=ctk.NSEW, padx=20, pady=20)

        # placement
        # lowest row
        self.calculator_button_zero.grid(row=4, column=0, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_period.grid(row=4, column=1, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_enter.grid(row=4, column=2, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_addition.grid(row=4, column=3, sticky=ctk.NSEW, padx=5, pady=5)

        # bottom row
        self.calculator_button_one.grid(row=3, column=0, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_two.grid(row=3, column=1, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_three.grid(row=3, column=2, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_subtraction.grid(row=3, column=3, sticky=ctk.NSEW, padx=5, pady=5)

        # middle row
        self.calculator_button_four.grid(row=2, column=0, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_five.grid(row=2, column=1, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_six.grid(row=2, column=2, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_multiplication.grid(row=2, column=3, sticky=ctk.NSEW, padx=5, pady=5)

        # top row
        self.calculator_button_seven.grid(row=1, column=0, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_eight.grid(row=1, column=1, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_nine.grid(row=1, column=2, sticky=ctk.NSEW, padx=5, pady=5)
        self.calculator_button_division.grid(row=1, column=3, sticky=ctk.NSEW, padx=5, pady=5)


    def load_basic_calculator(self):
        # column 1 to get to the larger side of the screen
        self.calculator_content_frame.grid(row=0, column=1, sticky=ctk.NSEW)
    def unload_basic_calculator(self):
        self.calculator_content_frame.grid_forget()

    def add_to_current_calculation(self, button):
        self.running_equation.set(self.running_equation.get() + button)

    def delete_from_calculation(self):
        self.running_equation.set(self.running_equation.get()[:-1])

    def clear_calculation(self):
        self.running_equation.set("")

    def load_calculation(self):
        self.finished_calculation.set(maths.calculator(self.running_equation.get()))

class MidpointCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="brown")

        self.midpoint_content_frame = ctk.CTkFrame(master, fg_color="orange")
        self.midpoint_test_text = ctk.CTkLabel(self.midpoint_content_frame, text="midpoint calculator")
        self.midpoint_test_text.grid(row=0, column=1)

    def load_midpoint_calculator(self):
        self.midpoint_content_frame.grid(row=0, rowspan=2, column=1, sticky=ctk.NSEW)

    def unload_midpoint_calculator(self):
        self.midpoint_content_frame.grid_forget()

class DistanceCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="gray")

        self.distance_calculator_frame = ctk.CTkFrame(master, fg_color="gray")

        self.distance_test_text = ctk.CTkLabel(self.distance_calculator_frame, text="distance calculator")
        self.distance_test_text.grid(row=0, column=1)

    def load_distance_calculator(self):
        self.distance_calculator_frame.grid(row=0, rowspan=2, column=1, sticky=ctk.NSEW)

    def unload_distance_calculator(self):
        self.distance_calculator_frame.grid_forget()

class TableGenerator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=settings.BACKGROUND)

        self.table_generator_frame = ctk.CTkFrame(master, fg_color=settings.BACKGROUND)

        self.table_generator_test_text = ctk.CTkLabel(self.table_generator_frame, text="table generator")
        self.table_generator_test_text.grid(row=0, column=1)

    def load_table_generator(self):
        self.table_generator_frame.grid(row=0, rowspan=2, column=1, sticky=ctk.NSEW)

    def unload_table_generator(self):
        self.table_generator_frame.grid_forget()