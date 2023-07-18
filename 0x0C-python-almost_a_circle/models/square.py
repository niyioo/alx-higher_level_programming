#!/usr/bin/python3

"""
Module: square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): Optional ID for the instance.

        Attributes:
            size (int): Size of the square (same as width and height in Rectangle).
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): Size value to set.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Override the __str__ method to return the Square representation.

        Returns:
            str: Square representation.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
