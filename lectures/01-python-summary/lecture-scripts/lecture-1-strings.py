#!/usr/bin/env python3

# Using Strings in Python

# -------------------------------------------
# Basic String Creation
# -------------------------------------------

# Strings can be created using single or double quotes
string1 = "Hello, World!"
string2 = "Python is fun!"

print(string1)
print(string2)

# -------------------------------------------
# String Concatenation and Repetition
# -------------------------------------------

# Joining two or more strings together
concatenated_string = string1 + " " + string2
print(concatenated_string)

# Repeating a string multiple times
repeated_string = "Echo! " * 3
print(repeated_string)

# -------------------------------------------
# String Indexing and Slicing
# -------------------------------------------

# Strings are zero-indexed in Python
# Fetching the first character
first_char = string1[0]
print(f"First character of string1: {first_char}")

# Fetching a substring (slicing)
substring = string1[7:12]  # This will fetch characters from index 7 to 11
print(f"Substring: {substring}")

# -------------------------------------------
# String Functions and Methods
# -------------------------------------------

# Getting the length of a string
length = len(string1)
print(f"Length of string1: {length}")

# Converting a string to upper and lower case
uppercase_string = string1.upper()
print(f"Uppercase: {uppercase_string}")

lowercase_string = string1.lower()
print(f"Lowercase: {lowercase_string}")

# Checking if a string starts or ends with a specific substring
starts_with_hello = string1.startswith("Hello")
print(f"Does string1 start with 'Hello'? {starts_with_hello}")

ends_with_fun = string2.endswith("fun!")
print(f"Does string2 end with 'fun!'? {ends_with_fun}")

# Finding a substring within a string
position = string1.find("World")
print(f"Position of 'World' in string1: {position}")

# Replacing a substring
replaced_string = string1.replace("Hello", "Goodbye")
print(replaced_string)

# Splitting a string into a list based on a delimiter
words = string1.split(" ")
print(words)

# -------------------------------------------
# String Interpolation and Formatting
# -------------------------------------------

# Using f-strings (formatted string literals) for string interpolation
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# Using the format method
formatted_string = "This is a {} example.".format("format method")
print(formatted_string)
