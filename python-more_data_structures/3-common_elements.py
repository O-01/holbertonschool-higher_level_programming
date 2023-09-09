#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for item in sorted(set(set_1)):
        for comparison in sorted(set(set_2)):
            if item == comparison:
                common.append(item)
    return common
