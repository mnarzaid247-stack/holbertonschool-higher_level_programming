#!/usr/bin/python3
"""creating a module with functions"""


def is_same_class(obj, a_class):
    """creating a function checs if they are the same class"""
    if type(obj) == a_class:
        return True
    else:
        return False
