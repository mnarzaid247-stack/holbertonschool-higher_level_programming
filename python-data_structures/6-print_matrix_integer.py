#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for value in row:
            i = i + 1
            print("{:d}".format(value), end="")
            if i != len(row):
                print(" ", end="")
        i = 0
        print()
