#!/usr/bin/python3
""" MyList class inherited from list - sorts input """


class MyList(list):
    """ MyList class inherited from list - sorts input """
    def __init__(self):
        """ instantiates MyList object """
        super().__init__()

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
