#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    roman_set = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
    first_letter = roman_string[0]
    number = roman_set[first_letter]
    for i in range(1, len(roman_string)):
        for key in roman_set:
            if roman_string[i] == key:
                if roman_set[key] >= number:
                    number = number + roman_set[key]
    return number
