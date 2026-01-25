#!/usr/bin/python3
"""creating a class."""


class Square:
    """creating class called Square."""
    def __init__(self, size=0):
        """creating a function."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
