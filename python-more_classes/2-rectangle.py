#!/usr/bin/python3
""" defines Rectangle class width & height attributes """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialize Rectangle class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets width attribute of Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width to input value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets height attribute of Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height to input value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ provides area value for Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ provides perimeter value for Rectangle """
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter
