#!/usr/bin/python3
""" base.py unittest definitions """
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_class(unittest.TestCase):
    """ TestBase class contains unittests for Base class """
    def test_id_custom(self):
        object1 = Base(12)
        self.assertEqual(object1.id, 12)

    def test_id_sequential(self):
        object2 = Base()
        object3 = Base()
        self.assertEqual(object2.id, 1)
        self.assertEqual(object3.id, 2)

    def test_id_reassignment(self):
        object6 = Base(16)
        object6.id = 32
        self.assertEqual(32, object6.id)

    def test_id_string(self):
        self.assertEqual("test", Base("test").id)

    def test_id_float(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_id_complex(self):
        self.assertEqual(complex(36), Base(complex(36)).id)

    def test_id_dict(self):
        self.assertEqual({'a': 2, 'b': 4}, Base({'a': 2, 'b': 4}).id)

    def test_id_bool(self):
        self.assertEqual(False, Base(False).id)

    def test_id_list(self):
        self.assertEqual([1, 2, 4], Base([1, 2, 4]).id)

    def test_id_tuple(self):
        self.assertEqual((1, 2, 4), Base((1, 2, 4)).id)

    def test_id_set(self):
        self.assertEqual({1, 2, 4}, Base({1, 2, 4}).id)

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            Base(6, 9)

    def test_nb_objects_private(self):
        object5 = Base(3)
        with self.assertRaises(AttributeError):
            print(object5.nb_objects)
        with self.assertRaises(AttributeError):
            print(object5.__nb_objects)

    def test_type(self):
        self.assertEqual(type(Base), type)
        self.assertIs(Base, Base)

    def test_doc_strings(self):
        self.assertTrue(len(Base.__doc__) >= 1)
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)


class TestBase_to_json_string(unittest.TestCase):
    """ tests for to_json_string Base staticmethod """
    def test_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, "[]")

    def test_None_input(self):
        json_str = Base.to_json_string(None)
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, "[]")

    def test_list_input(self):
        dict_a = {"id": 69, "width": 6, "height": 9, "x": 6, "y": 9}
        dict_b = {"id": 420, "width": 4, "height": 20, "x": 4, "y": 20}
        json_str = Base.to_json_string([dict_a, dict_b])
        self.assertTrue(type(json_str) is str)
        dicts = json.loads(json_str)
        self.assertEqual(dicts, [dict_a, dict_b])


class TestBase_from_json_string(unittest.TestCase):
    """ tests for from_json_string Base staticmethod """
    def test_None_input(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_string_input(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_json_string_input(self):
        test_list = [
            {"id": 69, "width": 6, "height": 9, "x": 6, "y": 9},
            {"id": 420, "width": 4, "height": 2, "x": 4, "y": 2}
        ]
        self.assertEqual(type(test_list), list)
        json_str = Base.to_json_string(test_list)
        test_out = Base.from_json_string(json_str)
        self.assertTrue(type(test_out) is list)
        self.assertEqual(len(test_out), 2)
        self.assertTrue(type(test_out[0]) is dict)
        self.assertTrue(type(test_out[1]) is dict)
        self.assertEqual(test_list, test_out)


class TestBase_save_to_file(unittest.TestCase):
    """ tests for save_to_file Base classmethod """
    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
            Square.save_to_file([], 2)


if __name__ == "__main__":
    unittest.main()
