#!/usr/bin/python3
def best_score(a_dictionary):
    the_best = 0
    the_key = ""
    for key, value in a_dictionary.items():
        if value > the_best:
            the_best = a_dictionary[key]
            the_key = key
    if the_key == "":
        return None
    else:
        return the_key
