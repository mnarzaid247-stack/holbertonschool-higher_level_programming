#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = a_dictionary.keys()
    sort_key = sorted(key)
    for key, value in sort_key.items():
        print(key, ":", value)
