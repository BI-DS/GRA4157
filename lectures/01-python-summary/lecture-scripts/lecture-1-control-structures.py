#!/usr/bin/env python3

# Working with Python Control Structures

# -------------------------------------------
# Conditional Statements: if, elif, and else
# -------------------------------------------

age = 25

if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Conditional expression (ternary operator)
status = "minor" if age < 18 else "non-minor"
print(f"Status based on age: {status}")

# -------------------------------------------
# Loops
# -------------------------------------------

# 'for' loop with a range
print("\nUsing 'for' loop with a range:")
for i in range(5):  # prints numbers from 0 to 4
    print(i)

# 'for' loop with a list
fruits = ["apple", "banana", "cherry"]
print("\nUsing 'for' loop with a list:")
for fruit in fruits:
    print(fruit)

# 'for' loop with enumeration
print("\nUsing 'for' loop with enumeration:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 'while' loop
count = 0
print("\nUsing 'while' loop:")
while count < 5:
    print(count)
    count += 1

# -------------------------------------------
# Control Flow Tools
# -------------------------------------------

# 'break': exits the loop
print("\nUsing 'break' in a loop:")
for i in range(10):
    if i == 3:
        break
    print(i)

# 'continue': skips the current iteration and continues with the next
print("\nUsing 'continue' in a loop:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 'pass': a null operation — when it is executed, nothing happens
print("\nUsing 'pass' in a loop:")
for i in range(5):
    if i == 2:
        pass  # does nothing, just a placeholder
    print(i)
