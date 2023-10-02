import unittest
Rectangle = __import__('1-rectangle').Rectangle

class TestRectangle(unittest.TestCase):

    def test_valid_input(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_non_integer_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("5", 10)

    def test_non_integer_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "10")

    def test_properties(self):
        rect = Rectangle()
        rect.width = 5
        rect.height = 10
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    def test_string_representation(self):
        rect = Rectangle(5, 10)
        self.assertEqual(str(rect), "Rectangle(width=5, height=10)")

if __name__ == "__main__":
    unittest.main()
