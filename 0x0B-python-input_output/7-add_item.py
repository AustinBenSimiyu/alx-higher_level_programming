#!/usr/bin/python3
""" This module adds all arguments to a Python list,
    and then save them to a file:

"""
import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

args_list = []
if os.path.exists("add_item.json"):
    args_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    args_list.append(arg)

save_file(args_list, "add_item.json")
