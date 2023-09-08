#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for item1 in range(0, len(matrix)):
            for item2 in range(0, len(matrix[item1])):
                if item2 == len(matrix[item1]) - 1:
                    print("{:d}".format(matrix[item1][item2]))
                else:
                    print("{:d}".format(matrix[item1][item2]), end=" ")
