#!/usr/bin/env python3

# Working with Python Functions

# -------------------------------------------
# Basic Function Definition and Calling
# -------------------------------------------


def greet():
    """This function displays a greeting."""  # This is a docstring
    print("Hello, Python!")


greet()  # Calling the function

# -------------------------------------------
# Function with Parameters
# -------------------------------------------


def display_message(message):
    """Displays the provided message."""
    print(message)


display_message("Welcome to the Python world!")

# -------------------------------------------
# Function Returning a Value
# -------------------------------------------


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


sum_result = add(5, 3)
print(f"Sum of 5 and 3: {sum_result}")

# -------------------------------------------
# Default Parameter Value
# -------------------------------------------


def greet_person(name="User"):
    """Greets the person with the provided name. If no name is given, it uses 'User'."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person()  # Uses the default value

# -------------------------------------------
# Arbitrary Number of Arguments (*args)
# -------------------------------------------


def multiply(*numbers):
    """Returns the product of all provided numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result


product = multiply(2, 3, 4)
print(f"Product of 2, 3, and 4: {product}")

# -------------------------------------------
# Keyword Arguments (**kwargs)
# -------------------------------------------


def display_info(**info):
    """Displays the provided information as key-value pairs."""
    for key, value in info.items():
        print(f"{key}: {value}")


display_info(name="Alice", age=30, city="Wonderland")

# -------------------------------------------
# Lambda (Anonymous) Functions
# -------------------------------------------

# A simple function to double a number
double = lambda x: x * 2

print(f"Double of 4: {double(4)}")

# -------------------------------------------
# Nested Functions
# -------------------------------------------


def outer_function():
    """An outer function containing a nested (inner) function."""
    print("Outer function executed.")

    def inner_function():
        """An inner function."""
        print("Inner function executed.")

    inner_function()


outer_function()
