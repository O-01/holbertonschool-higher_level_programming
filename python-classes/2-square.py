#!/usr/bin/python3
""" defines Square class by __size with instantiation """


class Square:
    """ class instantiated by __size upon meeting type/value conditions """
    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
