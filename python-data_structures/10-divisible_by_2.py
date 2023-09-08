#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_false_list = [None] * len(my_list)
    for item in range(0, len(my_list)):
        if my_list[item] % 2 == 0:
            true_false_list[item] = True
        else:
            true_false_list[item] = False
    return true_false_list
