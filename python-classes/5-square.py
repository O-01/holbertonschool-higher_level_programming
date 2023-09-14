#!/usr/bin/python3
""" added functionality for printing visual representation of square """


class Square:
    """ class instantiated by __size upon meeting type/value conditions """
    def __init__(self, size=0):
        """ initialize Square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ gets size attribute of Square """
        return self.__size

    @size.setter
    def size(self, value=0):
        """ sets size attribute of Square to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates area of Square """
        return self.__size ** 2

    def my_print(self):
        """ prints visual representation of Square using # character """
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end="")
            print()
