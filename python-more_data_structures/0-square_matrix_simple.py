#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        new_row = list(map(lambda x: x * x, row))
        new_mat.append(new_row)
    return new_mat
