#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Creating a class named Square."""

    def __init__(self, size=0, position=(0, 0)):
        """creating size and position."""
        self.size = size
        self.position = position

    def area(self):
        """creating an area."""
        return self.__size * self.__size

    @property
    def size(self):
        """creating a getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """creating a setter fir size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """creating a getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """creating a setter for position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """creating a printing function."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
