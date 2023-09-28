#!/usr/bin/python3
""" module containing Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines Square subclass of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates attributes of Square object """
        if args and len(args) > 0:
            for index, item in enumerate(args):
                if index == 0:
                    self.id = item
                if index == 1:
                    self.size = item
                if index == 2:
                    self.x = item
                if index == 3:
                    self.y = item
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
