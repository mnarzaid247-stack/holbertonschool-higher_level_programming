#!/usr/bin/python3
"""creating a module"""


def pascal_triangle(n):
    """creating a defntion"""
    new_list = []
    if n <= 0:
        return new_list
    tri = [[1]]
    for i in range(1, n):
        prev = tri[-1]
        new_row = [1]
        for j in range(len(prev) - 1):
            new_row.append(prev[j] + prev[j + 1])
        new_row.append(1)
        tri.append(new_row)
    return tri
