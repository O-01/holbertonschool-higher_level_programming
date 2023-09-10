#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(item for item in sorted(set(my_list)))
