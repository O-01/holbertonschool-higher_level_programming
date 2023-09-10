#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        mean = sum(item[0] * item[1] for item in my_list)
        weight = sum(item[1] for item in my_list)
        return mean / weight
