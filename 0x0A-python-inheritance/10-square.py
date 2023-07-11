#!/usr/bin/python3
"""
Module for Rectangle and Square classes.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            The square description in the format [Square] <size>/<size>.

        """
        return ("[{}] {}/{}".format("Rectangle",
                                    self.__size, self.__size))

    def __repr__(self):
        """
        Returns the string representation of the square.

        Returns:
            The square description in the format [Square] <size>/<size>.

        """
        return str(self)
