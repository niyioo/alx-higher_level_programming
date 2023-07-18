#!/usr/bin/python3

"""
Module: rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Optional ID for the instance.

        Attributes:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): Width value to set.

        Raises:
            ValueError: If width is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): Height value to set.

        Raises:
            ValueError: If height is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.

        Returns:
            int: X-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.

        Args:
            value (int): X-coordinate value to set.

        Raises:
            ValueError: If x is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("X-coordinate must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.

        Returns:
            int: Y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): Y-coordinate value to set.

        Raises:
            ValueError: If y is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Y-coordinate must be an integer")
        self.__y = value
