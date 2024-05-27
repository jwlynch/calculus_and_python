#
# Write a python function that takes three inputs.
#
# The function should add these three numbers and return the sum.
#
# Write a python statement that will execute the function.
#
# Use '#' to add a brief description of what your function is doing.

# this function, add_three_numbers, takes three numbers as input to
# the function, adds them together and returns their sum.

def add_three_numbers(x, y, z):
    # first, add the numbers, putting the sum into a variable.
    sum = x + y + z

    # now we have what we intend to return from the function, the sum
    # of the three numbers in the variable sum. now we can return sum.

    return sum

# Now, write a python statement to add 1, 2 and 3:

func_output = add_three_numbers(1, 2, 3)

# and print it:

print(f"the sum of 1, 2 and 3 is: {func_output}")

