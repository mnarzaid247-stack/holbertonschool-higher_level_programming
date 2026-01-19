#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for value in my_list:
            if value > max_int:
                max_int = value
