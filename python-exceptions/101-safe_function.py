#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        out = fct(*args)
    except Exception as errr:
        print("Exception: {}".format(errr), file=sys.stderr)
        out = None
    return out
