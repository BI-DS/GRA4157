#!/usr/bin/env python3

# Your first Python program

# Import the sin function from the math library
from math import sin

# Import the sys library to access command line arguments
import sys

# Cast command line argument to float and assign to variable x
x = float(sys.argv[1])

# Format a string with the variable x and sin(x)
print(f"Hello world, sin({x}) = {sin(x)}")
