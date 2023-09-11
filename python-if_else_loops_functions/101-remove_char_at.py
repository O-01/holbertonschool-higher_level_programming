#!/usr/bin/python3
def remove_char_at(str, n):
    minus_n = None
    if n < 0:
        minus_n = str
    else:
        minus_n = str[:n] + str[n + 1:]
    return minus_n
