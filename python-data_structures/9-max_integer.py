#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for value in my_list:
            if value > max_int:
                max_int = value
        return max_int
