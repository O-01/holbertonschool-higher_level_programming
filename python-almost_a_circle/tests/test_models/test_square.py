#!/usr/bin/python3
""" square.py unittest definitions """
import unittest
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestSquare_class(unittest.TestCase):
    """ tests for Square class """
    def setUp(self):
        self.instance = Square(8, 2, 4, 12)

    def test_size_getter(self):
        self.assertEqual(self.instance.size, 8)

    def test_x_getter(self):
        self.assertEqual(self.instance.x, 2)

    def test_y_getter(self):
        self.assertEqual(self.instance.y, 4)

    def test_id(self):
        self.assertEqual(self.instance.id, 12)

    def test_setters(self):
        self.instance.size = 12
        self.instance.x = 20
        self.instance.y = 6
        self.instance.id = 16
        self.assertEqual(
            [
                self.instance.size,
                self.instance.x,
                self.instance.y,
                self.instance.id
            ],
            [12, 20, 6, 16]
        )

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            Square(32, 64, 128, 256, 512, 1024, 2048)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__size)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__y)

    def test_width_value_exception(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_width_type_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("surfin", 4)

    def test_x_value_exception(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -4)

    def test_x_type_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "dude")

    def test_y_value_exception(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 4, -8)

    def test_y_type_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, "dude")

    def test_type(self):
        self.assertEqual(type(self.instance), Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIs(Square, Square)

    def test_doc_strings(self):
        self.assertTrue(len(Square.__doc__) >= 1)
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.area.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)

    def test_str(self):
        self.assertEqual(str(self.instance), "[Square] (12) 2/4 - 8")


class TestSquare_area(unittest.TestCase):
    """ tests for Square area method """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_area_INT_MAX_UINT_MAX(self):
        self.instance.width = 2147483647
        self.instance.height = 4294967295
        self.assertEqual(self.instance.area(), 9223372030412324865)

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.area(24)


class TestSquare_display(unittest.TestCase):
    """ tests for Square display method """
    def test_display_square_2s(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2).display()
            self.assertEqual(
                comp.getvalue(),
                "##\n##\n"
            )

    def test_display_square_as_square_6s(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(6).display()
            self.assertEqual(
                comp.getvalue(),
                "######\n######\n######\n######\n######\n######\n"
            )

    def test_display_square_2s_2x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n  ##\n  ##\n"
            )

    def test_display_square_2s_0x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 0, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n##\n##\n"
            )

    def test_display_square_2s_2x_0y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 2).display()
            self.assertEqual(
                comp.getvalue(),
                "  ##\n  ##\n"
            )

    def test_display_no_arguments(self):
        with self.assertRaises(TypeError):
            Square.display()


class TestSquare_update(unittest.TestCase):
    """ tests for Square update method """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_update_id(self):
        self.instance.update(16)
        self.assertEqual(str(self.instance), "[Square] (16) 4/8 - 2")

    def test_update_size(self):
        self.instance.update(16, 6)
        self.assertEqual(str(self.instance), "[Square] (16) 4/8 - 6")

    def test_update_x(self):
        self.instance.update(16, 6, 10)
        self.assertEqual(str(self.instance), "[Square] (16) 10/8 - 6")

    def test_update_y(self):
        self.instance.update(16, 6, 10, 12)
        self.assertEqual(str(self.instance), "[Square] (16) 10/12 - 6")

    def test_update_no_arguments(self):
        self.instance.update()
        self.assertEqual(str(self.instance), "[Square] (12) 4/8 - 2")

    def test_update_kwargs_id(self):
        self.instance.update(**{'id': 24})
        self.assertEqual(str(self.instance), "[Square] (24) 4/8 - 2")

    def test_update_kwargs_size(self):
        self.instance.update(**{'id': 24, 'size': 4})
        self.assertEqual(str(self.instance), "[Square] (24) 4/8 - 4")

    def test_update_kwargs_height(self):
        self.instance.update(**{'id': 24, 'size': 4, 'x': 8})
        self.assertEqual(str(self.instance), "[Square] (24) 8/8 - 4")

    def test_update_kwargs_x(self):
        self.instance.update(**{'id': 24, 'size': 4, 'x': 8, 'y': 16})
        self.assertEqual(str(self.instance), "[Square] (24) 8/16 - 4")


class TestSquare_to_dictionary(unittest.TestCase):
    """ tests for Square to_dictionary method """
    pass


if __name__ == "__main__":
    unittest.main()
