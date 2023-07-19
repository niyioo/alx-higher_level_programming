import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id_assignment(self):
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_nonempty_list(self):
        b1 = Base()
        b2 = Base()
        json_string = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        expected_string = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_string, expected_string)

    def test_from_json_string_empty_string(self):
        dictionaries = Base.from_json_string("")
        self.assertEqual(dictionaries, [])

    def test_from_json_string_nonempty_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        dictionaries = Base.from_json_string(json_string)
        expected_dicts = [{"id": 1}, {"id": 2}]
        self.assertEqual(dictionaries, expected_dicts)

    def test_create_instance(self):
        dictionary = {"id": 1, "width": 10, "height": 20}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 20)

    def test_to_csv_string_empty_list(self):
        csv_string = Base.to_csv_string([])
        self.assertEqual(csv_string, "")

    def test_to_csv_string_nonempty_list(self):
        b1 = Base()
        b2 = Base()
        csv_string = Base.to_csv_string([b1.to_dictionary(), b2.to_dictionary()])
        expected_string = "id,width,height\n1,,,0\n2,,,0\n"
        self.assertEqual(csv_string, expected_string)

    def test_from_csv_string_empty_string(self):
        dictionaries = Base.from_csv_string("")
        self.assertEqual(dictionaries, [])

    def test_from_csv_string_nonempty_string(self):
        csv_string = "id,width,height\n1,10,20\n2,5,15\n"
        dictionaries = Base.from_csv_string(csv_string)
        expected_dicts = [
            {"id": "1", "width": "10", "height": "20"},
            {"id": "2", "width": "5", "height": "15"}
        ]
        self.assertEqual(dictionaries, expected_dicts)

if __name__ == '__main__':
    unittest.main()
