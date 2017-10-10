#!/usr/bin/env python

def count_lines(filename):
    """given a filename, this function should return a count of the number of
    lines in the file"""
    lines = 0
    with open(filename, "rb") as f:
        for line in f:
            lines += 1

    return lines

def write_file(filename):
    """given a filename, this function should write at least two lines into the file"""
    with open(filename, "w") as f:
        f.write("Hello!\n")
        f.write("Line 2\n")


