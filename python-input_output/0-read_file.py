#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="UTF8") as file:
        text = file.read()
        print(text, end="")
