#!/usr/bin/python3
""" defines Rectangle class width & height attributes """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize Rectangle class """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """ string representation of Rectangle class object """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for row in range(self.__height):
                for col in range(self.__width):
                    print(self.print_symbol, end="")
                if row < self.__height - 1:
                    print()
            return ""

    def __repr__(self):
        """ string representation for repr result """
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        """ defined actions upon instance deletion """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
