#!/usr/bin/python3
""" you think MyInt is equal, but is actually not equal """


class MyInt(int):
    """ MyInt, what are you doing? """
    def __eq__(self, comparison):
        return self.real != comparison

    def __ne__(self, comparison):
        return self.real == comparison
