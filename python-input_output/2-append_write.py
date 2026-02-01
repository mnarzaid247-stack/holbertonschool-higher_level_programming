#!/usr/bin/python3
"""creating a module"""


def append_write(filename="", text=""):
    """append a file"""
    with open(filename, "a", encoding="utf-8") as file:
        number = file.write(text)
        return number
