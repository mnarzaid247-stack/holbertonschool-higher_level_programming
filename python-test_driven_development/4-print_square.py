#!/usr/bin/python3
"""Module that provides a function to print a square using '#'."""


def print_square(size):
    """Prints a square of size x size using '#' characters."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
        return
    for _ in range(size):
        print("#" * size)
