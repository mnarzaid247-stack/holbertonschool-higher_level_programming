#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    number = 0
    for value in new_set:
        number = number + value
    return number
