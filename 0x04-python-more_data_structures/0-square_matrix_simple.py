#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        squared_row = list(map(lambda x: x * x, row))
        n_matrix.append(squared_row)
    return n_matrix
