#!/usr/bin/python3
""" module containing Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ defines Rectangle subclass of Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ method returns area of Rectangle object """
        return self.width * self.height

    def display(self):
        """ method prints representation of rectangle using '#' """
        [print() for coord in range(self.y)]
        for row in range(self.height):
            [print(" ", end="") for coord in range(self.x)]
            for col in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ updates attributes of Rectangle object """
        if args and len(args) > 0:
            for index, item in enumerate(args):
                if index == 0:
                    self.id = item
                if index == 1:
                    self.width = item
                if index == 2:
                    self.height = item
                if index == 3:
                    self.x = item
                if index == 4:
                    self.y = item
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        """ overrides parent class __str__ method """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )
