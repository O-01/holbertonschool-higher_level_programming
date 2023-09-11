#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print("{:s}".format(chr(letter)), end="")
    else:
        print("{:s}".format(chr(letter - 32)), end="")
