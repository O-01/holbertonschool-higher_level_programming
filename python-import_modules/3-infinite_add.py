#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summa = 0
    for iteration in range(1, len(sys.argv)):
        summa += int(sys.argv[iteration])
    print(f"{summa}")
