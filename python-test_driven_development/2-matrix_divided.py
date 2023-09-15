#!/usr/bin/python3
""" divides all elements of a matrix by div """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix by div - matrix input must be a list
    of equally-sized lists containing only int/float data - div must be a
    non-zero int or float """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for idx, row in enumerate(matrix):
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [list(map(lambda col: round(col / div, 2), row)) for row in matrix]
