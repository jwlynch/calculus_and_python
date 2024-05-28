
# make function that takes coords for two points and returns equation
# of line that passes through those two points

from sympy import *

def equation_of_line(e, f, g, h):
    # first calculate m (of y = mx + b)

    m = (f - h) / (e - g)

    # now calc b

    b = f - m * e

    # make sympy symbols for line equations

    x, y = symbols('x, y')

    # now return equation of line

    return Eq(y , m * x + b)

