#!/usr/bin/python3

"""
Module: test_square
"""

import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_constructor_default_values(self):
        """
        Test the constructor with default values.
        """
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, None)

    def test_constructor_custom_values(self):
        """
        Test the constructor with custom values.
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_area(self):
        """
        Test the area method.
        """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """
        Test the display method.
        """
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with self.assertLogs() as logs:
            s.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        """
        Test the __str__ method.
        """
        s = Square(4, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 4")

    def test_update_args(self):
        """
        Test the update method with positional arguments.
        """
        s = Square(5)
        s.update(1, 8, 4, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 1)

    def test_update_kwargs(self):
        """
        Test the update method with keyword arguments.
        """
        s = Square(5)
        s.update(id=1, size=8, x=4, y=2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 1)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        s = Square(4, 2, 1, 10)
        expected_dict = {"id": 10, "size": 4, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
