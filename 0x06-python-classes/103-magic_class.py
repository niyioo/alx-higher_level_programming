#!/usr/bin/python3
import math


class MagicClass:
    """
    This class represents a magic circle.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (float, optional): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return (2 * math.pi * self.__radius)
