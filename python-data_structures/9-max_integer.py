#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maxval = my_list[0]
        for item in my_list:
            if item > maxval:
                maxval = item
        return maxval
