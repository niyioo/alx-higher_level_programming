#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square shape.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the value of the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the size attribute.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares the square area with another square for equality.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares the square area with another square for inequality.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compares the square area with another square for greater than.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Compares the square area with another square for greater than or equal.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Compares the square area with another square for less than.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Compares the square area with another square for less than or equal.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
