#!/usr/bin/env python3

# Using Python as a calculator

# -------------------------------------------
# Basic Arithmetic Operations
# -------------------------------------------

# Addition: Adds two numbers together
addition = 5 + 3

# Subtraction: Subtracts the second number from the first
subtraction = 12 - 4

# Multiplication: Multiplies two numbers
multiplication = 7 * 6

# Division: Divides the first number by the second, resulting in a float
division = 48 / 6

# Modulo: Returns the remainder of the division of the two numbers
modulo = 10 % 3

# Exponentiation: Raises the first number to the power of the second number
exponentiation = 2 ** 3

print(f"5 + 3 = {addition}")
print(f"12 - 4 = {subtraction}")
print(f"7 * 6 = {multiplication}")
print(f"48 / 6 = {division}")
print(f"10 modulo 3 = {modulo}")
print(f"2 to the power of 3 = {exponentiation}")

# -------------------------------------------
# Advanced Math Functions using the `math` module
# -------------------------------------------

# The math module provides access to mathematical functions 
# that are not available in Python's basic arithmetic operations.
import math

# Square Root: Returns the square root of a number
square_root = math.sqrt(64)

# Factorial: Returns the factorial of a number (n!)
factorial = math.factorial(5)

# Logarithm: Returns the base-10 logarithm of a number
logarithm_base_10 = math.log10(100)

# Sine: Returns the sine of an angle in radians.
# Note: The math.sin() function expects the angle in radians, 
# so we first convert the angle from degrees to radians using math.radians()
sine_30_degrees = math.sin(math.radians(30))

print(f"Square root of 64 = {square_root}")
print(f"Factorial of 5 = {factorial}")
print(f"Log base 10 of 100 = {logarithm_base_10}")
print(f"Sine of 30 degrees = {sine_30_degrees:.2f}")

