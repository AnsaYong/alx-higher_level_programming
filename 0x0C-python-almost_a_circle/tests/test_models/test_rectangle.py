#!/usr/bin/python3
"""
This module provides test cases for the ``Rectangle``
class.
"""
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle  # Import the Rectangle class


class TestRectangle(unittest.TestCase):
    """
    This class provides text cases for the ``Rectangle``
    class.
    """
    def setUp(self):
        """
        Create an instance of Rectangle for testing.
        """
        self.rectangle = Rectangle(5, 10, id=42)

    def test_width_property(self):
        """
        Test if the width was set to 5.
        """
        self.assertEqual(self.rectangle._Rectangle__width, 5)

    def test_height_property(self):
        """
        Test if the height was set properly.
        """
        self.assertEqual(self.rectangle._Rectangle__height, 10)

    def test_x_property(self):
        """
        Test if x was set properly to the default
        """
        self.assertEqual(self.rectangle._Rectangle__x, 0)

    def test_y_property(self):
        """
        Test if y was set to 0, since it wasn't provided
        """
        self.assertEqual(self.rectangle._Rectangle__y, 0)

    def test_width_setter(self):
        """
        Test the width property setter
        """
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

    def test_height_setter(self):
        """
        Test the height property setter
        """
        self.rectangle.height = 20
        self.assertEqual(self.rectangle.height, 20)

    def test_x_setter(self):
        """
        Test the x property setter
        """
        self.rectangle.x = 25
        self.assertEqual(self.rectangle.x, 25)

    def test_y_setter(self):
        """
        Test the y property setter
        """
        self.rectangle.y = 30
        self.assertEqual(self.rectangle.y, 30)

    def test_id_property(self):
        """
        Test the rectangle id, set by calling the parent class
        """
        self.assertEqual(self.rectangle.id, 42)

    def test_width_setter_invalid(self):
        """
        Test the width property setter with an invalid value
        """
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

    def test_height_setter_invalid(self):
        """
        Test the height property setter with an invalid value.
        """
        with self.assertRaises(ValueError):
            self.rectangle.height = -10

    def test_width_setter_string(self):
        """
        Test the width property setter with a string.
        """
        with self.assertRaises(TypeError):
            self.rectangle.width = "6"

    def test_x_setter_invalid(self):
        """
        Test the x property setter with an invalid value.
        """
        with self.assertRaises(ValueError):
            self.rectangle.x = -2

    def test_y_setter_invalid(self):
        """
        Test the y property setter with an invalid value.
        """
        with self.assertRaises(TypeError):
            self.rectangle.y = "b"

    def test_area(self):
        """
        test the area method
        """
        self.rectangle = Rectangle(3, 6)   # set an instance of rectangle
        self.assertEqual(self.rectangle.area(), 18)

    def test_area_height(self):
        """
        Test the area method when height is 10.
        """
        self.rectangle = Rectangle(3, 10)
        self.assertEqual(self.rectangle.area(), 30)

    def test_area_all_params(self):
        """
        Test the area method when all parameters are provided.
        """
        self.rectangle = Rectangle(8, 2, 0, 0, 6)
        self.assertEqual(self.rectangle.area(), 16)

    def test_display_rectangle(self):
        """
        Test the display method
        """
        self.rectangle = Rectangle(3, 4)
        expected_output = "###\n###\n###\n###\n"  # The expected output
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            self.rectangle.display()
            self.assertEqual(captured_output.getvalue(), expected_output)
        finally:
            sys.stdout = sys.__stdout__  # Restore the original sys.stdout

    def test_display_custom_dimensions(self):
        """
        Test display method
        """
        custom_rectangle = Rectangle(2, 2)
        expected_output = "##\n##\n"  # The expected output
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            custom_rectangle.display()
            self.assertEqual(captured_output.getvalue(), expected_output)
        finally:
            sys.stdout = sys.__stdout__  # Restore the original sys.stdout

    def test_str_representation(self):
        """
        Test the __str__ method.
        """
        self.rectangle = Rectangle(3, 4, 1, 2, 42)  # Instance of Rectangle
        expected_str = "[Rectangle] (42) 1/2 - 3/4"
        self.assertEqual(str(self.rectangle), expected_str)

        self.rectangle = Rectangle(4, 4, 1)  # Another instance of Rectangle
        expected_str = "[Rectangle] (9) 1/0 - 4/4"
        self.assertEqual(str(self.rectangle), expected_str)

    def test_display_x_y(self):
        """
        Test the display method taking the positioning
        (x and y) into account.
        """
        self.rectangle = Rectangle(3, 4, 1, 2, 42)
        expected_output = "\n\n ###\n ###\n ###\n ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            self.rectangle.display()
            self.assertEqual(captured_output.getvalue(), expected_output)
        finally:
            sys.stdout = sys.__stdout__  # Restore the original sys.stdout

    def test_display_custom_x_y(self):
        """
        Test the display method taking the positioning into
        account.
        """

        instance1 = Rectangle(3, 2, 1, 0)
        expected_output1 = " ###\n ###\n"
        captured_output1 = StringIO()
        sys.stdout = captured_output1

        try:
            instance1.display()
            self.assertEqual(captured_output1.getvalue(), expected_output1)
        finally:
            sys.stdout = sys.__stdout__  # Restore the original sys.stdout
