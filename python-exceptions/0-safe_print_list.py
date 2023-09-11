#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for index in range(x):
        try:
            print(f"{my_list[index]}", end="")
            printed += 1
        except Exception:
            break
    print()
    return printed
