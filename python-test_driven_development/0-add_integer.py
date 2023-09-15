#!/usr/bin/python3
""" adds 2 integers - b default value is 98 upon missing second argument """


def add_integer(a, b=98):
    """ adds 2 integers - input may be of either int or float data types """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
