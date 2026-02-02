#!/usr/bin/python3
"""creating a module"""

import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []
items = items + sys_argv[1:]
save_to_json_file(items, filename)
