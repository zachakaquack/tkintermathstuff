import math

from sympy import sympify, simplify, symbols, solve
import numpy

list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def calculator(eq):
    # TODO: ADD POSSIBILITY OF MULTIPLE X'S
    # TODO: ADD POSSIBILITY OF X JUST BEING X, AND MAKE IT 1 * X
    # TODO: ADD CASES FOR THE REST OF THE OPERATORS
    # DONE: MULTIPLICATION DIVISION ADDITION SUBTRACTION POWER
    eq = eq.replace("=", ",")
    eq = eq.replace("^", "**")
    if eq.find("x") != -1:
        # find location of x
        locs = eq.find("x")
        # insert multiplication symbol
        if eq[locs - 1] == "*":
            solved_equation = solve(sympify("Eq(" + eq+ ")"))
            return solved_equation
        if eq[locs - 1] in numbers:
            eq = eq[0:locs] + "*" + eq[locs:len(eq)]
        else:
            eq[locs] = "1*x"

        #return
        solved_equation = solve(sympify("Eq(" + eq + ")"))
        return solved_equation
    else:
        return eval(eq)


def simplify_equation(eq):
    return simplify(eq)

def equality_checker(eq1, eq2):

    sym = symbols(list_of_letters)
    simplified_equation_1 = simplify(eq1)
    simplified_equation_2 = simplify(eq2)

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

