#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else
        maxval = 0
        for item in range(0, len(my_list)):
            if my_list[item] > maxval:
                maxval = my_list[item]
        return maxval
