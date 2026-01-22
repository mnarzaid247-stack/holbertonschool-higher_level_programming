#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    i = 0
    try:
        while i < x:
            print(my_list[i], end="")
            number = number + 1
            i = i + 1
        return number
    except:
        return number
