#!/usr/bin/python3
"""creating a class."""


class Square:
    """creating a class named Square."""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """creating area."""
        return self.__size * self.__size

    @property
    def size(self):
        """creating the property."""
        return self.__size

    @size.setter
    def size(self, value):
        """creating a setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
