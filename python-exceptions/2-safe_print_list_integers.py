#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    number = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
            number = number + 1
        except (ValueError, TypeError):
            i = i + 1
            continue
        except IndexError:
            break
    print()
    return number
