#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            number = number + 1
            i = i + 1
        except IndexError:
            break
    print()
    return number
