#!/usr/bin/python3
""" prints a given text with 2 line breaks after ./?/: delimiters reached """


def text_indentation(text):
    """ prints a given text with 2 line breaks after ./?/: delimiters reached -
    text must be a string without spaces at either the beginning or end of each
    printed line """
    if type(text) is not str:
        raise TypeError("text must be a string")
    skip = 0
    printed = 0
    for idx, char in enumerate(text):
        if printed == 0 and char == " ":
            continue
        else:
            if skip == 1:
                if char == " ":
                    continue
                else:
                    skip = 0
                    pass

            if idx > 0 and char in ".?:":
                print(char, end="\n\n")
                if idx < len(text) -1 and text[idx + 1] == " ":
                    skip = 1
            else:
                print(char, end="")
                printed = 1
