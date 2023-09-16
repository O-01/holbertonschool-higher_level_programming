#!/usr/bin/python3
""" prints a given text with 2 line breaks after ./?/: delimiters reached """


def text_indentation(text):
    """ prints a given text with 2 line breaks after ./?/: delimiters reached -
    text must be a string without spaces at either the beginning or end of each
    printed line """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tab = 0
    for idx, char in enumerate(text):
        if tab == 1:
            if char == " ":
                continue
            else:
                tab = 0
                continue
        elif idx > 0 and text[idx - 1] in ".?:":
            if char == " ":
                tab = 1
                char = ""
            print()
            print()
        print(char, end="")
        tab = 0
