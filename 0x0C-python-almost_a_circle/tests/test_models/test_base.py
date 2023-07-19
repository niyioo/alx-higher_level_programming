#!/usr/bin/python3

"""
Module: test_base
"""

import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test the automatic assignment of IDs.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id_assignment(self):
        """
        Test the assignment of custom IDs.
        """
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_to_json_string_empty_list(self):
        """
        Test converting an empty list of dictionaries to a JSON string.
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_nonempty_list(self):
        """
        Test converting a non-empty list of dictionaries to a JSON string.
        """
        b1 = Base()
        b2 = Base()
        json_string = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        expected_string = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_string, expected_string)

    def test_from_json_string_empty_string(self):
        """
        Test converting an empty string to a list of dictionaries.
        """
        dictionaries = Base.from_json_string("")
        self.assertEqual(dictionaries, [])

    def test_from_json_string_nonempty_string(self):
        """
        Test converting a non-empty string to a list of dictionaries.
        """
        json_string = '[{"id": 1}, {"id": 2}]'
        dictionaries = Base.from_json_string(json_string)
        expected_dicts = [{"id": 1}, {"id": 2}]
        self.assertEqual(dictionaries, expected_dicts)

    def test_create_instance(self):
        """
        Test creating an instance with attributes from a dictionary.
        """
        dictionary = {"id": 1, "width": 10, "height": 20}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 20)

    def test_to_csv_string_empty_list(self):
        """
        Test converting an empty list of dictionaries to a CSV string.
        """
        csv_string = Base.to_csv_string([])
        self.assertEqual(csv_string, "")

    def test_to_csv_string_nonempty_list(self):
        """
        Test converting a non-empty list of dictionaries to a CSV string.
        """
        b1 = Base()
        b2 = Base()
        csv_string = Base.to_csv_string([b1.to_dictionary(), b2.to_dictionary()])
        expected_string = "id,width,height\n1,,,0\n2,,,0\n"
        self.assertEqual(csv_string, expected_string)

    def test_from_csv_string_empty_string(self):
        """
        Test converting an empty string to a list of dictionaries.
        """
        dictionaries = Base.from_csv_string("")
        self.assertEqual(dictionaries, [])

    def test_from_csv_string_nonempty_string(self):
        """
        Test converting a non-empty string to a list of dictionaries.
        """
        csv_string = "id,width,height\n1,10,20\n2,5,15\n"
        dictionaries = Base.from_csv_string(csv_string)
        expected_dicts = [
            {"id": "1", "width": "10", "height": "20"},
            {"id": "2", "width": "5", "height": "15"}
        ]
        self.assertEqual(dictionaries, expected_dicts)

    def test_load_from_file_nonexistent_file(self):
        """
        Test loading instances from a nonexistent file.
        """
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_existing_file(self):
        """
        Test loading instances from an existing file.
        """
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Base)
        self.assertIsInstance(instances[1], Base)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_draw(self):
        """
        Test the draw method.
        """
        b1 = Base()
        b2 = Base()
        with self.assertRaises(turtle.Terminator):
            Base.draw([b1], [b2])


if __name__ == '__main__':
    unittest.main()
