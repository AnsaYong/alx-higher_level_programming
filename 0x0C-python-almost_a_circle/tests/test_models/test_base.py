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
