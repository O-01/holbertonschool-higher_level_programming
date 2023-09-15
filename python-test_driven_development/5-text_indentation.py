#!/usr/bin/python3
""" prints a given text with 2 line breaks after ./?/: delimiters reached """


def text_indentation(text):
    """ prints a given text with 2 line breaks after ./?/: delimiters reached -
    text must be a string without spaces at either the beginning or end of each
    printed line """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for idx, char in enumerate(text):
        if idx > 0 and text[idx - 1] in ".?:":
            if char == " ":
                char = ""
            print()
            print()
        print(char, end="")
