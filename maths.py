import math
from webbrowser import Error

from sympy import sympify, simplify, symbols, solve
import numpy
from sympy.series.formal import solve_de

list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

operands = ["+", "-", "*", "/", "**"]

def change_x_multiplication(eq):
    new_eq = ""
    for i in range(eq.count("x")):
        # find location of x
        loc = eq.find("x")

        if loc == 0:  # case if equation starts with x, like x + 12 becomes 1*x + 12
            new_eq += eq[:loc] + "1*x"

        elif eq[loc - 1] not in numbers:  # case where it's just x in the middle of the equation
            new_eq += eq[:loc] + "1*x"


        else:  # case where it is something like 12x, becomes 12 * x
            # add from the beginning of the equation to the character before x, + "*x"
            new_eq += eq[:loc] + "*x"


        # remove x just iterated upon
        eq = eq[loc + 1:]
    new_eq += eq
    return new_eq

def calculator(eq):
    # TODO: ADD SIN COS TAN WITH MATH
    try:
        eq = eq.replace(" ", "").replace("=", ",").replace("^", "**")

        # THERE IS NO =
        if eq.find(",") == -1:
            eq += ",0"
        #print("none")

        if eq[eq.find(",") + 1] != "0":
            answer_side = eq[eq.find(",") + 1:]

            locations = []
            for i in range(len(answer_side)):
                 if answer_side[i] in operands:
                     locations.append(i)
            locations.append(len(answer_side))


            # if there are terms on the other side, split all of them into a list
            terms = []

            if len(locations) > 0:
                for i in range(len(locations)):
                    # start to first operand
                    if i == 0:
                        terms.append(answer_side[:locations[i]])
                    else:
                        # operand to operand
                        terms.append(answer_side[locations[i - 1]:locations[i]])
                        # if last entry, do last operand to end of string
                        if i + 1 == len(locations):
                            terms.append(answer_side[locations[i]:])
            else:
                terms.append(answer_side)


            # remove all instances of "" in the answers
            while "" in terms:
                terms.remove("")


            # add + to the beginning of a term if it's not there
            for i in range(len(terms)):
                if terms[i][0] not in operands:
                    terms[i] = "+" + terms[i]

            # inverse the terms

            for i in range(len(terms)):
                # inverse
                match terms[i][0]:
                    case "+":
                        terms[i] = "-" + terms[i][1:]
                    case "-":
                        terms[i] = "+" + terms[i][1:]
                    case "*":
                        terms[i] = "/" + terms[i][1:]
                    case "/":
                        terms[i] = "*" + terms[i][1:]

            # make terms into one string
            terms_to_add = ""
            for term in terms:
                terms_to_add += term

            # setup left side of new equation
            left_equation_side = eq.replace("," + answer_side, "")
            left_equation_side += terms_to_add


            # setup new equation
            new_eq = change_x_multiplication(left_equation_side + ",0")


            # finish equation
            solved_equation = solve(sympify("Eq(" + new_eq + ")"))

            return solved_equation

        # ELSE, THERE ARE NO TERMS ON THE RIGHT SIDE OF THE EQUATION
        else:
            new_eq = change_x_multiplication(eq)
            solved_equation = solve(sympify("Eq(" + new_eq + ")"))
            return solved_equation

    #CATCH ERROR
    except TypeError:
            return "ERROR"



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


def distance_calculator(points):
    # points = [x.1, y.1, x.2, y.2]
    points = list(points)

    # convert all from string to int, once again, because of python bullshittery
    for i in range(len(points)):
        points[i] = int(points[i])

    return math.sqrt((points[2] - points[0])**2 + (points[3] - points[1])**2)

def midpoint_calculator(points):
    # points = [x.1, y.1, x.2, y.2]

    # convert to list because of python bullshittery
    points = list(points)

    # convert all from string to int, once again, because of python bullshittery
    for i in range(len(points)):
        points[i] = int(points[i])

    # actually do the math
    midpoint = [
        (points[0] + points[2])/2, (points[1] + points[3])/2
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

