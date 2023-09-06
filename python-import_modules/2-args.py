#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        arg_eng = "argument:"
    elif len(sys.argv) > 2:
        arg_eng = "arguments:"
    else:
        arg_eng = "arguments."

    print("{:d} {:s}".format(len(sys.argv) - 1, arg_eng))

    for arg in sys.argv:
        if sys.argv.index(arg) > 0:
            print("{:d}: {:s}".format(sys.argv.index(arg), arg))
