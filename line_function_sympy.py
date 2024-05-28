
# make function that takes coords for two points and returns equation
# of line that passes through those two points

from sympy import *

def equation_of_line(a, b, c, d):
    # first calculate m (of y = mx + b)

    m = (b - d) / (a - c)

    # now calc b

    b = b - m * a

    # make sympy symbols for line equations

    x, y = symbols('x, y')

    # now return equation of line

    return y = m * x + b

