#!/usr/bin/python3
def lookup(obj):
    """function that shows the methods and attrebutes"""

    my_list = list(dir(obj))
    return my_list
