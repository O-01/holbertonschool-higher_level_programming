#!/usr/bin/python3
""" added getter & setter for size """


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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __lt__(self, comparison):
        """ defines response to < comparison """
        return self.area() < comparison.area()

    def __le__(self, comparison):
        """ defines response to <= comparison """
        return self.area() <= comparison.area()

    def __eq__(self, comparison):
        """ defines response to == comparison """
        return self.area() == comparison.area()

    def __ne__(self, comparison):
        """ defines response to != comparison """
        return self.area() != comparison.area()

    def __gt__(self, comparison):
        """ defines response to > comparison """
        return self.area() > comparison.area()

    def __ge__(self, comparison):
        """ defines response to >= comparison """
        return self.area() >= comparison.area()
