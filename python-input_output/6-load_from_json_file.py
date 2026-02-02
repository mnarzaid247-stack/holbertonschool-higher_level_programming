#!/usr/bin/python3
"""creating a module"""

import json


def load_from_json_file(filename):
    """create an obj"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
