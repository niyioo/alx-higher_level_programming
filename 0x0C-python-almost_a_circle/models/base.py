#!/usr/bin/python3

"""
Module: base
"""

import csv
import json
import turtle


class Base:
    """
    Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional ID for the instance.

        Attribute:
            id (int): ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def to_csv_string(list_dictionaries):
        """
        Convert a list of dictionaries to a CSV string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: CSV string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ""

        keys = list_dictionaries[0].keys()
        csv_string = ','.join(keys) + '\n'

        for dictionary in list_dictionaries:
            values = [str(dictionary[key]) for key in keys]
            csv_string += ','.join(values) + '\n'

        return csv_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        csv_string = cls.to_csv_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(csv_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def from_csv_string(csv_string):
        """
        Convert a CSV string representation to a list of dictionaries.

        Args:
            csv_string (str): CSV string representation.

        Returns:
            list: List of dictionaries.
        """
        if csv_string is None or len(csv_string) == 0:
            return []

        lines = csv_string.strip().split('\n')
        keys = lines[0].split(',')
        dictionaries = []

        for line in lines[1:]:
            values = line.split(',')
            dictionary = dict(zip(keys, values))
            dictionaries.append(dictionary)

        return dictionaries

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instances from a CSV file and return a list of instances.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                csv_string = file.read()
                dictionaries = cls.from_csv_string(csv_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all the Rectangles and Squares using the Turtle graphics module.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        turtle.speed(2)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.done()
