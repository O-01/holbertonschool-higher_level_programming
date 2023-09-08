#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        no_c_string = my_string.translate({ord(item): None for item in "Cc"})
        return no_c_string
