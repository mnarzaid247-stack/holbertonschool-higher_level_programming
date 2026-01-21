#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_set = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    total = 0
    for i in range(len(roman_string)):
        curr = roman_set[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = roman_set[roman_string[i + 1]]
            if curr < next_value:
                total = total - curr
            else:
                total = total + curr
        else:
            total = total + curr
    return total
