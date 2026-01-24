#!/usr/bin/python3
"""Module that provides a function to add two integers."""
def add_integer(a, b=98):
    """Adds two integers after validating and converting inputs."""
    if type(a) != int and type(a) != float:
        raise TypeError ("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError ("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    result = a + b
    return result
