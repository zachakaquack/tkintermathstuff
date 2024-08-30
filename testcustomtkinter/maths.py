import math

import sympy as sy
import numpy

list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]

def calculator(eq):
    return eval(eq)


def simplify_equation(eq):
    return sy.simplify(eq)

def equality_checker(eq1, eq2):

    sym = sy.symbols(list_of_letters)
    simplified_equation_1 = sy.simplify(eq1)
    simplified_equation_2 = sy.simplify(eq2)

    if simplified_equation_1 == simplified_equation_2:
        return True
    else:
        return False

def mult_matrix(mat, constant):
    for i in range(len(mat)):
        for j in range(len(mat) + 1):
            mat[i][j] *= constant
    return mat

def mult_matrix_by_matrix(a, b):
    return numpy.dot(a, b)

def make_table(x_start, x_end, equation):
    table = {}
    for i in range(x_start, x_end + 1):
        table[i] = eval(equation.replace("x", str(i)))
    return table

def distance_calculator(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

def midpoint_calculator(x_1, y_1, x_2, y_2):
    midpoint = [
        (x_1 + x_2)/2, (y_1 + y_2)/2
    ]
    return midpoint

def create_circle_equation(h, k, r):
    return f"(x-{h})^2 + (y-{k})^2 = {r}"

def find_which_quadrant(x, y):
    if x > 0:
        # Q1 / Q4
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

def find_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def find_intercepts(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)
    c = y1 - (m * x1)

    return c / m, c

