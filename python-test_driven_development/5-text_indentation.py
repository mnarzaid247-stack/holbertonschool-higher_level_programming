#!/usr/bin/python3
"""Module that provides a function to print text with indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text:
        if new_line and char == " ":
            continue

        print(char, end="")
        if char in ".?:":
            print("\n")
            new_line = True
        else:
            new_line = False
