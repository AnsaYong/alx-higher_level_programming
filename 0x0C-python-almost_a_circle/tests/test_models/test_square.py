#!/usr/bin/python3
"""
This is a test module for the ``Square``
class. It tests mutiple scenarios,
including inheritance and functionality.
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """
    This class provides test cases for the ``Square``
    class which inherits the ``Rectangle`` class. It
    tests attribute handling and methods.
    """
    def test_create_square_with_size(self):
        """
        This tests the creation of a
        square with only the size value
        provided.
        """
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_create_square_with_size_and_x(self):
        """
        This tests the creation of a
        square with the size value and x
        provided.
        """
        square = Square(5, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_create_square_with_size_x_and_y(self):
        """
        This tests the creation of a square with
        size, x, and y values provided.
        """
        square = Square(5, 2, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_create_square_with_size_x_y_and_id(self):
        """
        This tests the creation of a square with
        size, x, y, and id values provided.
        """
        square = Square(5, 2, 3, 42)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 42)

    def test_square_area(self):
        """
        This tests inheritance by assessing
        the area() method defined in the
        Rectangle class.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_display(self):
        """
        This tests inheritance by assessing
        the display() method defined in the
        Rectangle class.
        """
        square = Square(3, 1, 2)
        expected_output = "\n\n ###\n ###\n ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            square.display()
            self.assertEqual(captured_output.getvalue(), expected_output)
        finally:
            sys.stdout = sys.__stdout__  # Restore the original sys.stdout

    def test_square_str_method(self):
        """
        This tests whether the __str__ method
        in the Rectangle class is overridden
        in the Square class.
        """
        square = Square(4, 1, 2, 42)
        expected_str = "[Square] (42) 1/2 - 4"
        self.assertEqual(str(square), expected_str)

    def test_size_getter(self):
        """
        This tests the implementation for getter
        in the Square class.
        """
        square = Square(5)
        self.assertEqual(square.size, 5)
        square = Square(8)
        self.assertEqual(square.size, 8)

    def test_size_setter_valid_size(self):
        """
        This tests the validation if a valid
        size is provided as argument.
        """
        square = Square(5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_size_setter_invalid_size_type(self):
        """
        This tests the validation if an invalid
        size (type) is provided as argument.
        """
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_size_setter_invalid_size_value(self):
        """
        This tests the validation if an invalid
        size (value) is provided as argument.
        """
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -2

    def test_update_with_args(self):
        """
        Tests the update method with args.
        """
        square = Square(5)
        square.update(10, 8, 2, 3, 4)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        """
        Tests the update method with kwargs.
        """
        square = Square(5)
        square.update(id=7, x=2, y=3, width=6)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_args_and_kwargs(self):
        """
        Tests the update method with both args and
        kwargs.
        """
        square = Square(5)
        square.update(7, width=6, x=1, y=2)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_to_dictionary(self):
        """
        Tests the to_dictionary implementation for
        the Square class - Regular case.
        """
        r1 = Square(5, 2, 3, 42)
        r1_dict = r1.to_dictionary()
        expected_dict = {
            "id": 42,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(r1_dict, expected_dict)
