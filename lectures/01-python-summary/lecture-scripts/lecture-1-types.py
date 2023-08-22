#!/usr/bin/env python3

# Exploring Python Data Types

# -------------------------------------------
# Numeric Types
# -------------------------------------------

# Integer
integer_num = 42
print(f"Type of {integer_num}: {type(integer_num)}")

# Float (decimal number)
float_num = 3.14
print(f"Type of {float_num}: {type(float_num)}")

# Complex number (real and imaginary parts)
complex_num = 2 + 3j
print(f"Type of {complex_num}: {type(complex_num)}")

# -------------------------------------------
# Sequence Types
# -------------------------------------------

# String (sequence of characters)
string_data = "Hello, Python!"
print(f"Type of '{string_data}': {type(string_data)}")

# List (ordered, mutable sequence)
list_data = [1, 2, 3, "Python", 3.14]
print(f"Type of {list_data}: {type(list_data)}")

# Tuple (ordered, immutable sequence)
tuple_data = (1, 2, 3, "Python")
print(f"Type of {tuple_data}: {type(tuple_data)}")

# -------------------------------------------
# Set Types
# -------------------------------------------

# Set (unordered collection with no duplicate elements)
set_data = {1, 2, 3, 4, 4, 5}
print(f"Type of {set_data}: {type(set_data)}")

# -------------------------------------------
# Mapping Types
# -------------------------------------------

# Dictionary (unordered collection of key-value pairs)
dict_data = {"name": "Alice", "age": 30, "city": "Wonderland"}
print(f"Type of {dict_data}: {type(dict_data)}")

# -------------------------------------------
# Boolean Type
# -------------------------------------------

# Represents the truth values: True and False
bool_true = True
bool_false = False
print(f"Type of {bool_true}: {type(bool_true)}")
print(f"Type of {bool_false}: {type(bool_false)}")

# -------------------------------------------
# None Type
# -------------------------------------------

# Represents the absence of a value or a null value
none_data = None
print(f"Type of {none_data}: {type(none_data)}")

