#!/usr/bin/env python3

# Working with Python Dictionaries

# -------------------------------------------
# Creating Dictionaries
# -------------------------------------------

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {"name": "Alice", "age": 30, "city": "Wonderland"}
print(f"Person dictionary: {person}")

# Dictionary with mixed data types
mixed_dict = {
    "name": "Bob",
    42: "The Answer",
    "is_student": True,
    "courses": ["Math", "Physics"],
}
print(f"Mixed data type dictionary: {mixed_dict}")

# Dictionary created using dict constructor
constructed_dict = dict(name="Charlie", age=25, city="Cityland")
print(f"Constructed dictionary: {constructed_dict}")

# -------------------------------------------
# Accessing Dictionary Elements
# -------------------------------------------

# Accessing elements using a key
name = person["name"]
print(f"Name from dictionary: {name}")

# Using the get method (returns None if key is not found)
city = person.get("city")
print(f"City from dictionary: {city}")
unknown = person.get("unknown_key")
print(f"Unknown key value: {unknown}")

# -------------------------------------------
# Modifying Dictionaries
# -------------------------------------------

# Adding/Updating a key-value pair
person["age"] = 31  # Updating
person["country"] = "Fairyland"  # Adding
print(f"Updated person dictionary: {person}")

# Removing a key-value pair using 'del'
del person["country"]
print(f"Dictionary after removing 'country': {person}")

# Removing a key-value pair using 'pop'
popped_city = person.pop("city")
print(f"Popped city: {popped_city}, Dictionary after popping: {person}")

# -------------------------------------------
# Dictionary Functions and Methods
# -------------------------------------------

# Finding the number of key-value pairs
num_pairs = len(person)
print(f"Number of key-value pairs: {num_pairs}")

# Getting all keys and values
all_keys = person.keys()
all_values = person.values()
print(f"All keys: {list(all_keys)}, All values: {list(all_values)}")

# Checking if a key exists in the dictionary
has_name_key = "name" in person
print(f"Is 'name' a key in the dictionary? {has_name_key}")

# Merging two dictionaries using 'update'
additional_info = {"job": "Engineer", "hobby": "Reading"}
person.update(additional_info)
print(f"Person dictionary after updating: {person}")

# Clearing all key-value pairs
person.clear()
print(f"Person dictionary after clearing: {person}")
