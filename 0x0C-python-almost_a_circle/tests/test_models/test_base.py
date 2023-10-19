#!/usr/bin/python3
"""
Test module for the ``base`` class.
"""
import unittest
from models.base import Base    # Import the Base class from the module
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """
    Provides test methods for the Base class
    """

    def setUp(self):
        """
        Create an instance of the Base class before each test
        """
        Base.__nb_objects = 0   # reset the __nb_objects att to 0
        self.base = Base()  # create an instance of the Base class

    def test_id_increment(self):
        """
        Test if ``id`` is incremented correctly for new instances
        """
        self.assertEqual(self.base.id, 2)   # first instance, id should be 1

        # Create another instance
        another_base = Base()
        self.assertEqual(another_base.id, 3)    # 2nd instance, id should be 2

    def test_custom_id(self):
        """
        Test if the ``id`` is set to a custom value when
        provided.
        """
        value = 42
        custom_base = Base(id=value)
        self.assertEqual(custom_base.id, value)

        new_value = -5
        new_base = Base(id=new_value)
        self.assertEqual(new_base.id, new_value)

        another_value = 0
        another_base = Base(another_value)
        self.assertEqual(another_base.id, another_value)

    def test_to_json_string_with_empty_list(self):
        """
        Test when the input list is empty
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_non_empty_list(self):
        """
        Test when the input list is non-empty
        """
        input_data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        expected_result = json.dumps(input_data)
        result = Base.to_json_string(input_data)
        self.assertEqual(result, expected_result)

    def test_to_json_string_with_none_input(self):
        """
        Test when the input list is None
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file_empty_list(self):
        """
        Test saving an empty list of objects to a JSON file.
        """
        filename = "Base.json"
        try:
            # Save an empty list
            Base.save_to_file([])
            # Check if the file exists
            self.assertTrue(os.path.exists(filename))
            # Read the file and ensure it contains '[]'
            with open(filename, 'r') as file:
                content = file.read()
                self.assertEqual(content, "[]")
        finally:
            # Clean up by removing the file
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_non_empty_list(self):
        """
        Test saving a list of objects to a JSON file.
        """
        filename = "Base.json"
        try:
            # Create a list of dictionaries
            data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
            # Save the list to a JSON file
            Base.save_to_file(data)
            # Check if the file exists
            self.assertTrue(os.path.exists(filename))
            # Read the file and ensure its content matches the input data
            with open(filename, 'r') as file:
                content = file.read()
                self.assertEqual(content, json.dumps(data))
        finally:
            # Clean up by removing the file
            if os.path.exists(filename):
                os.remove(filename)

    def test_from_json_string_empty_string(self):
        """
        Test loading an empty JSON string.
        """
        empty_json_string = ""
        result = Base.from_json_string(empty_json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_string(self):
        """
        Test loading a valid JSON string.
        """
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        valid_json_string = json.dumps(data)
        result = Base.from_json_string(valid_json_string)
        self.assertEqual(result, data)

    def test_create_instance(self):
        """
        Test creating an instance from a dictionary.
        """
        data = {"id": 1, "name": "Alice"}
        instance = Base.create(**data)
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, "Alice")

    def test_load_from_file_empty_file(self):
        """
        Test loading instances from an empty JSON file.
        """
        filename = "Base.json"
        try:
            # Create an empty JSON file
            with open(filename, 'w') as file:
                file.write("[]")
            # Load instances from the file
            result = Base.load_from_file()
            self.assertEqual(result, [])
        finally:
            # Clean up by removing the file
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_from_file_non_empty_file(self):
        """
        Test loading instances from a non-empty JSON file.
        """
        filename = "Base.json"
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        try:
            # Save data to a JSON file
            Base.save_to_file(data)
            # Load instances from the file
            result = Base.load_from_file()
            self.assertEqual(result, data)
        finally:
            # Clean up by removing the file
            if os.path.exists(filename):
                os.remove(filename)
