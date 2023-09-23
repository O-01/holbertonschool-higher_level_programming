#!/usr/bin/python3
""" introduce area method that raises exception """


class BaseGeometry:
    """ introduce area method that raises exception """
    def area(self):
        """ raises exception due to area not yet implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ verifies that input value for name is integer above zero """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
