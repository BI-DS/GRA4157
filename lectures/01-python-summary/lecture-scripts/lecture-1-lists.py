#!/usr/bin/env python3

# Working with Python Lists

# -------------------------------------------
# Creating Lists
# -------------------------------------------

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with integers
int_list = [1, 2, 3, 4, 5]
print(f"Integer list: {int_list}")

# List with mixed data types
mixed_list = [1, "Python", 3.14, True]
print(f"Mixed data type list: {mixed_list}")

# List created using list comprehension
squared_list = [x**2 for x in range(5)]
print(f"Squared list: {squared_list}")

# -------------------------------------------
# Accessing List Elements
# -------------------------------------------

# Accessing elements using index
first_element = int_list[0]
last_element = int_list[-1]
print(f"First element: {first_element}, Last element: {last_element}")

# Slicing a list
sub_list = int_list[1:4]
print(f"Sublist (from index 1 to 3): {sub_list}")

# -------------------------------------------
# Modifying Lists
# -------------------------------------------

# Appending to a list
int_list.append(6)
print(f"List after appending 6: {int_list}")

# Extending a list
int_list.extend([7, 8, 9])
print(f"List after extending with [7, 8, 9]: {int_list}")

# Inserting at a specific position
int_list.insert(1, 1.5)
print(f"List after inserting 1.5 at index 1: {int_list}")

# Removing an element
int_list.remove(1.5)
print(f"List after removing 1.5: {int_list}")

# Popping an element from a specific position
popped_element = int_list.pop(2)
print(f"Popped element: {popped_element}, List after popping: {int_list}")

# -------------------------------------------
# List Functions
# -------------------------------------------

# Finding the length of a list
list_length = len(int_list)
print(f"Length of the list: {list_length}")

# Getting the sum of all elements
list_sum = sum(int_list)
print(f"Sum of all elements: {list_sum}")

# Finding the maximum and minimum element
max_element = max(int_list)
min_element = min(int_list)
print(f"Max element: {max_element}, Min element: {min_element}")

# -------------------------------------------
# Other List Operations
# -------------------------------------------

# Reversing a list
int_list.reverse()
print(f"Reversed list: {int_list}")

# Sorting a list
int_list.sort()
print(f"Sorted list: {int_list}")

# Counting occurrences of an element
count_of_5 = int_list.count(5)
print(f"Occurrences of 5 in the list: {count_of_5}")

