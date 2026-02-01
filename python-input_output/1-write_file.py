#!/usr/bin/python3
"""creating a module"""


def write_file(filename="", text=""):
    """write a text to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        number = file.write(text)
        return number
