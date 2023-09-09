#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for item in sorted(set(my_list)):
        unique.append(item)
    summa = 0
    for item in range(0, len(unique)):
        summa += unique[item]
    return summa
