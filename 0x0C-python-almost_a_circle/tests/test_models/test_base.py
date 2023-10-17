#!/usr/bin/python3
"""
Test module for the ``base`` class.
"""
import unittest
from models.base import Base    # Import the Base class from the module


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
