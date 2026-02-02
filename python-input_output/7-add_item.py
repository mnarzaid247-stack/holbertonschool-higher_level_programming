#!/usr/bin/python3
"""creating a module"""

import sys
save_to_json_file = __impoer__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __impoer__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []
items = items + sys_argv[1:]
save_to_json_file(items, filename)
