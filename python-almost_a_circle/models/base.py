#!/usr/bin/python3
""" module containing Base class """
import json


class Base:
    """ Base class is baseclass (based) """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of input dictionary list """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of object list to file """
        with open(cls.__name__ + ".json", "w") as outfile:
            obj_list = []
            if list_objs is not None and len(list_objs) != 0:
                for object in list_objs:
                    obj_list.append(object.to_dictionary())
            outfile.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string representation of input """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(7, 7)
        elif cls.__name__ == "Square":
            dummy = cls(7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            instance_list = []
            with open(cls.__name__ + ".json") as input_file:
                json_list = cls.from_json_string(input_file.read())
            for obj in json_list:
                instance_list.append(cls.create(**obj))
        except FileNotFoundError:
            pass
        finally:
            return instance_list
