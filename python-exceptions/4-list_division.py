#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = [0] * list_length
    while i < list_length:
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            new_list[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
        except IndexError:
            print("out of range")
            new_list[i] = 0
        finally:
            i = i + 1
    return new_list
