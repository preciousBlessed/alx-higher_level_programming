#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{}: {}".format(i+1, arg))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{}: {}".format(i+1, arg))
