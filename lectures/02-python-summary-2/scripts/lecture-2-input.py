# Python User Input Example

# -------------------------------------------
# Basic User Input
# -------------------------------------------

# Prompting the user for their name
name = input("What is your name? ")
print(f"Hello, {name}!")

# -------------------------------------------
# Numeric Input
# -------------------------------------------

# Prompting the user for their age (and converting it to an integer)
age = int(input("How old are you? "))
print(f"You are {age} years old.")

# -------------------------------------------
# Multiple Inputs
# -------------------------------------------

# Prompting the user for multiple pieces of information
city = input("Which city do you live in? ")
country = input("Which country do you live in? ")
print(f"You live in {city}, {country}.")

# -------------------------------------------
# Confirming Choices
# -------------------------------------------

# Asking the user to confirm a choice
confirmation = input("Is the information correct? (yes/no) ")

if confirmation.lower() == 'yes':
    print("Thank you for confirming.")
else:
    print("Please double-check your information.")

# -------------------------------------------
# Advanced: Input with Type Conversion
# -------------------------------------------

# Prompting for numerical input and performing calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")