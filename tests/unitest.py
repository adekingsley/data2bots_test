import unittest
import pytest
from ..assignment import determine_type, process_dict


class TestJsonSchemaGeneration(unittest.TestCase):

    def test_determine_type_string(self):
        value = "hello"
        result = determine_type(value)
        self.assertEqual(result, "string")

    def test_determine_type_integer(self):
        value = 42
        result = determine_type(value)
        self.assertEqual(result, "integer")

    def test_determine_type_enum(self):
        value = ["apple", "banana", "cherry"]
        result = determine_type(value)
        self.assertEqual(result, "enum")

    def test_determine_type_array(self):
        value = [{"key": "value"}, {"key2": "value2"}]
        result = determine_type(value)
        self.assertEqual(result, "array")

    def test_determine_type_object(self):
        value = {"key": "value"}
        result = determine_type(value)
        self.assertEqual(result, "object")

    def test_determine_type_unknown(self):
        value = None
        result = determine_type(value)
        self.assertEqual(result, "unknown")

    def test_process_dict_simple(self):
        input_dict = {
            "name": "John",
            "age": 30
        }
        result = process_dict(input_dict)
        expected = {
            "name": {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            },
            "age": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            }
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
