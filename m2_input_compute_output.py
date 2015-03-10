"""
This module lets you practice the INPUT-COMPUTE-OUTPUT pattern,
including:
  -- INPUT numbers (using input and float and int)
  -- COMPUTE (using variables and arithmetic operators)
  -- OUTPUT (using print)
  -- CALLING a function from main.

See the     m0e_input_compute_output    module for an example,
or the  m1e_input_compute_output_in_functions   module
for a more elaborate (and commented) example.

Authors: David Mutchler, Chandan Rupakheti, Claude Anderson,
         their colleagues, and Trent Punt.  September 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.

    rectangle_area()
    raise_to_power()
    cylinder_volume()

def rectangle_area():
    width = int(input('enter width of a rectangle'))
    height = int(input('enter height of a rectangle'))
    print(width * height, 'is the area of the rectangle')


    """
    Prompts for and inputs the width and height of a rectangle
    (as floating point numbers) and prints the area of the rectangle.
    """
    # TODO: 3. Implement and test this function.


def raise_to_power():

    x = float(input('enter a number'))
    n = int(input('enter an integer'))
    print(x ** n, 'is ', x, " to the ", n, " power.")





    """
    Prompts for and inputs:
      -- a floating point number X
      -- an integer N
    Prints X raised to the Nth power.
    """
    # TODO: 4. Implement and test this function.
    # Hints:
    #  -- Use  float  to convert to a floating point number
    #     but  int    to convert to an integer
    #  -- Use   **  for raising to a power


def cylinder_volume():

    diameter = float(input('enter a diameter of a cylinder'))
    heightofcylinder = float(input('enter the height of a cylinder'))

    print('The volume of the cylinder is ' , (math.pi * ((.5 * diameter) ** 2) * heightofcylinder))


    """
    Prompts for and inputs the diameter and height of a cylinder
    (as floating point numbers) and prints the volume of the cylinder.
    """

    # TODO: 5. Implement and test this function.
    # Hint: You need PI in this formula.  For PI, type:
    #    math,
    #    then a dot,
    #    then pause, then look for what to select/type.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
