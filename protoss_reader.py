#!/usr/bin/env python3
"""Read a file by changing the working directory"""

import os  # Importing the os module for directory operations

def main():
    """Main logic"""
    os.chdir("/tmp")  # Change the working directory to /tmp
    with open("protoss.txt", "r") as foo:
        print(foo.read())

main()

