#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and
then save them to a file.
"""


if __name__ == "__main__":
    import json
    import sys

    load_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    # Define the filename
    filename = "add_item.json"

    # Try to load the existing data from the JSON file
    try:
        add_data = load_json_file(filename)
    except FileNotFoundError:
        # If the file does not exist, initialize add_data as an empty list
        add_data = []

    # Append the command line arguments to the add_data list
    add_data.extend(sys.argv[1:])

    # Save the updated data to the JSON file
    save_to_json_file(add_data, filename)
