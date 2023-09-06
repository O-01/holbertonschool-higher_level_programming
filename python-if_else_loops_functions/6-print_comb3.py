#!/usr/bin/python3
for lower in range(0, 10):
    for higher in range(lower + 1, 10):
        if lower == 8 and higher == 9:
            print("{:d}{:d}".format(lower, higher))
        else:
            print("{:d}{:d}".format(lower, higher), end=", ")
