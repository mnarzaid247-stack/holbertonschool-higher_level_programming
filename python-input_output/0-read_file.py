#!/usr/bin/python3
"""module that read a file"""


def read_file(filename=""):
    """read a file and print it"""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        print(text, end="")
