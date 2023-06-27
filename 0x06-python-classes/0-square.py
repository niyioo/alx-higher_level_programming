#!/usr/bin/python3

"""
This is a module that provides a description of the module's purpose.
"""

class Square:
    """
    This class represents a square shape.
    """

    def __init__(self):
        """
        Initializes a new instance of the Square class.
        """
        pass

def my_function():
    """
    This function performs a specific task.
    """
    pass

print(__import__("my_module").__doc__)
print(__import__("my_module").MyClass.__doc__)
print(__import__("my_module").my_function.__doc__)
print(__import__("my_module").MyClass.my_function.__doc__)
