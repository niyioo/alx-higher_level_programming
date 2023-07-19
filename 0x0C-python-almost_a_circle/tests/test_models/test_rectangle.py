#!/usr/bin/python3

"""
Module: test_rectangle
"""

import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_constructor_default_values(self):
        """
        Test the constructor with default values.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, None)

    def test_constructor_custom_values(self):
        """
        Test the constructor with custom values.
        """
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_area(self):
        """
        Test the area method.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        Test the display method.
        """
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as logs:
            r.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        """
        Test the __str__ method.
        """
        r = Rectangle(4, 5, 2, 1, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 2/1 - 4/5")

    def test_update_args(self):
        """
        Test the update method with positional arguments.
        """
        r = Rectangle(5, 10)
        r.update(1, 8, 6, 4, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 1)

    def test_update_kwargs(self):
        """
        Test the update method with keyword arguments.
        """
        r = Rectangle(5, 10)
        r.update(id=1, width=8, height=6, x=4, y=2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 1)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        r = Rectangle(4, 5, 2, 1, 10)
        expected_dict = {"id": 10, "width": 4, "height": 5, "x": 2, "y": 1}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
