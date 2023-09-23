#!/usr/bin/python3
""" adds new attribute to an object, if possible """


def add_attribute(obj, name, value):
    """ adds attribute with input name & desired value to input object """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
