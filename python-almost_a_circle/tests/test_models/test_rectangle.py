#!/usr/bin/python3
""" rectangle.py unittest definitions """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle_class(unittest.TestCase):
    """ tests for Rectangle class """
    def setUp(self):
        self.instance = Rectangle(8, 16, 2, 4, 12)

    def test_width_getter(self):
        self.assertEqual(self.instance.width, 8)

    def test_height_getter(self):
        self.assertEqual(self.instance.height, 16)

    def test_x_getter(self):
        self.assertEqual(self.instance.x, 2)

    def test_y_getter(self):
        self.assertEqual(self.instance.y, 4)

    def test_id(self):
        self.assertEqual(self.instance.id, 12)

    def test_setters(self):
        self.instance.width = 12
        self.instance.height = 20
        self.instance.x = 6
        self.instance.y = 8
        self.instance.id = 16
        self.assertEqual(
            [
                self.instance.width,
                self.instance.height,
                self.instance.x,
                self.instance.y,
                self.instance.id
            ],
            [12, 20, 6, 8, 16]
        )

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_single_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(32, 64, 128, 256, 512, 1024, 2048)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__y)

    def test_width_value_exception(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_type_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("surfin", 4)

    def test_height_value_exception(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_height_type_exception(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "dude")

    def test_x_value_exception(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -8)

    def test_x_type_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "dude")

    def test_y_value_exception(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 8, -16)

    def test_y_type_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 8, "dude")

    def test_type(self):
        self.assertEqual(type(self.instance), Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIs(Rectangle, Rectangle)

    def test_doc_strings(self):
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)

    def test_str(self):
        self.assertEqual(str(self.instance), "[Rectangle] (12) 2/4 - 8/16")


class TestRectangle_area(unittest.TestCase):
    """ tests for Rectangle area method """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_area(self):
        self.assertEqual(Rectangle(4, 6).area(), 24)

    def test_area_INT_MAX_UINT_MAX(self):
        self.instance.width = 2147483647
        self.instance.height = 4294967295
        self.assertEqual(self.instance.area(), 9223372030412324865)

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.area(24)


class TestRectangle_display(unittest.TestCase):
    """ tests for Rectangle display method """
    def test_display_rectangle_2w_4h(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "##\n##\n##\n##\n"
            )

    def test_display_rectangle_as_square_6w_6h(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(6, 6).display()
            self.assertEqual(
                comp.getvalue(),
                "######\n######\n######\n######\n######\n######\n"
            )

    def test_display_rectangle_2w_4h_2x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n  ##\n  ##\n  ##\n  ##\n"
            )

    def test_display_rectangle_2w_4h_0x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 0, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n##\n##\n##\n##\n"
            )

    def test_display_rectangle_2w_4h_2x_0y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 2).display()
            self.assertEqual(
                comp.getvalue(),
                "  ##\n  ##\n  ##\n  ##\n"
            )

    def test_display_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.display()


class TestRectangle_update(unittest.TestCase):
    """ tests for Rectangle update method """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_update_id(self):
        self.instance.update(16)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 2/4")

    def test_update_width(self):
        self.instance.update(16, 6)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 6/4")

    def test_update_height(self):
        self.instance.update(16, 6, 10)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 6/10")

    def test_update_x(self):
        self.instance.update(16, 6, 10, 12)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 12/16 - 6/10")

    def test_update_y(self):
        self.instance.update(16, 6, 10, 12, 20)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 12/20 - 6/10")

    def test_update_no_arguments(self):
        self.instance.update()
        self.assertEqual(str(self.instance), "[Rectangle] (12) 8/16 - 2/4")

    def test_update_kwargs_id(self):
        self.instance.update(**{'id': 24})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 2/4")

    def test_update_kwargs_width(self):
        self.instance.update(**{'id': 24, 'width': 4})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 4/4")

    def test_update_kwargs_height(self):
        self.instance.update(**{'id': 24, 'width': 4, 'height': 8})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 4/8")

    def test_update_kwargs_x(self):
        self.instance.update(**{'id': 24, 'width': 4, 'height': 8, 'x': 16})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 16/16 - 4/8")

    def test_update_kwargs_y(self):
        self.instance.update(**{
            'id': 24,
            'width': 4,
            'height': 8,
            'x': 16,
            'y': 32
        })
        self.assertEqual(str(self.instance), "[Rectangle] (24) 16/32 - 4/8")


class TestRectangle_to_dictionary(unittest.TestCase):
    """ tests for Rectangle to_dictionary method """
    pass


if __name__ == "__main__":
    unittest.main()
