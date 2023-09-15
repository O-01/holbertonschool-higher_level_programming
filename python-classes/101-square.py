#!/usr/bin/python3
""" added functionality for printing visual representation of square """


class Square:
    """ class instantiated by __size upon meeting type/value conditions """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize Square class """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ gets size attribute of Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size attribute of Square to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ gets property attribute of Square """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets size attribute of Square to value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(item, int) for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(item >= 0 for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculates area of Square """
        return self.__size ** 2

    def my_print(self):
        """ prints visual representation of Square using # character """
        if self.__size > 0:
            for co in range(self.__position[1]):
                print()
        for row in range(self.__size):
            for ro in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """ string representation of Square class object """
        if self.__size > 0:
            for co in range(self.__position[1]):
                print()
        for row in range(self.__size):
            for ro in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            if row < self.__size - 1:
                print()
        return ""
