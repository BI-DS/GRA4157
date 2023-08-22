# Working with Python Classes

# -------------------------------------------
# Basic Class Definition and Object Creation
# -------------------------------------------

class Animal:
    """A simple Animal class."""
    
    # Constructor method
    def __init__(self, species):
        self.species = species
    
    # Instance method
    def display_info(self):
        print(f"This is a {self.species}.")

# Creating an object (instance) of the Animal class
dog = Animal("Dog")
dog.display_info()

# -------------------------------------------
# Class with Private Attributes and Methods
# -------------------------------------------

class Computer:
    """A simple Computer class with private attributes and methods."""
    
    def __init__(self, brand):
        self.__brand = brand  # Private attribute
    
    # Private method
    def __display_brand(self):
        print(f"Brand: {self.__brand}")

    # Public method that uses the private method
    def show_info(self):
        self.__display_brand()

laptop = Computer("Dell")
laptop.show_info()

# -------------------------------------------
# Inheritance
# -------------------------------------------

class Bird(Animal):  # Bird class inherits from Animal class
    """A Bird class that inherits from Animal."""
    
    def __init__(self, species, can_fly):
        super().__init__(species)  # Calling the constructor of the parent class
        self.can_fly = can_fly

    # Overriding the parent class method
    def display_info(self):
        super().display_info()  # Calling the method from the parent class
        if self.can_fly:
            print("It can fly!")
        else:
            print("It cannot fly.")

eagle = Bird("Eagle", True)
eagle.display_info()

penguin = Bird("Penguin", False)
penguin.display_info()

# -------------------------------------------
# Class Methods, Static Methods, and Properties
# -------------------------------------------

class Circle:
    """A simple Circle class."""
    
    # Class attribute
    PI = 3.14159

    def __init__(self, radius):
        self._radius = radius
    
    # Property for radius to control its setting and getting
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius should be positive.")
    
    # Class method
    @classmethod
    def get_PI(cls):
        return cls.PI

    # Static method
    @staticmethod
    def is_round():
        return True

    # Method to calculate area of the circle
    def area(self):
        return self.PI * self._radius * self._radius

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")

# Using class method
print(f"Value of PI: {Circle.get_PI()}")

# Using static method
print(f"Is circle round? {Circle.is_round()}")

# Using property
circle.radius = 10
print(f"Updated radius: {circle.radius}")
circle.radius = -5  # This will trigger the error message from the setter

