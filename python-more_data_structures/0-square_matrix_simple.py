#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for item in range(0, len(matrix)):
        square_matrix.append(list(map(lambda num: num ** 2, matrix[item])))
    return square_matrix
