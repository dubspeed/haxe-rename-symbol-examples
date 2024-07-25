#!/usr/bin/env python3

#
# Quickly get the byte offset of a string in a file.
# Usage: python byte_offset.py <file_path> <name>
#
import sys

def find_name_offset(file_path, name):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            name_bytes = name.encode('utf-8')
            offset = content.find(name_bytes)

            if offset != -1:
                return offset
            else:
                return None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python byte_offset.py <file_path> <name>")
        sys.exit(1)

    file_path = sys.argv[1]
    name = sys.argv[2]

    offset = find_name_offset(file_path, name)
    if offset is not None:
        print(f"{offset}")
    else:
        print(f"'{name}' not found in the file.")
        sys.exit(1)

