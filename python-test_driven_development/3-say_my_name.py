#!/usr/bin/python3
""" prints 'My name is <first name> <last name>' """


def say_my_name(first_name, last_name=""):
    """ prints 'My name is <first name> <last name>' based upon arguments
    received - only first_name is strictly required, however both arguments
    must be of string data type """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if last_name and type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
