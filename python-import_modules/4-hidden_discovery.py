#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    print(dir(hidden_4))
    for iteration in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[iteration][0] != "_":
            print(dir(hidden_4)[iteration])
