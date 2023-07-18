#!/usr/bin/python3

"""
Module: base
"""

class Base:
    """
    Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional ID for the instance.

        Attributes:
            id (int): Public instance attribute representing the ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
