#!/usr/bin/python3
"""creating a module"""

import json


def save_to_json_file(my_obj, filename):
    """write an object to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
