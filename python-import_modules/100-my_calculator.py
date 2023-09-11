#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        if operator not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if operator == "+":
                func = add
            if operator == "-":
                func = sub
            if operator == "*":
                func = mul
            if operator == "/":
                func = div
            result = func(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
