#!/usr/bin/python3
""" prints square with specified side length represented by '#' character """


def print_square(size):
    """ prints square with specified side length represented by '#' character -
    size input is the length of each side of the desired square to be printed -
    size must be of integer data type & with value greater than zero """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
