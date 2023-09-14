#!/usr/bin/python3
""" defines Square class by __size with instantiation & area method """


class Square:
    """ class instantiated by __size upon meeting type/value conditions """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
