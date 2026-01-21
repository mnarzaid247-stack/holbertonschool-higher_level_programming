#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = a_dictionary.keys()
    sort_key = sorted(key)
    for key in sort_key:
        value = a_dictionary[key]
        print(key, ": ", value, sep="")
