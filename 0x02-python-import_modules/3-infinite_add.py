#!/usr/bin/python3
from sys import argv
sum = 0
if __name__ == "__main__":
    if len(argv) == 1:
        print("{}".format(sum))
    elif len(argv) > 1:
        for arg in argv[1:]:
            sum += int(arg)
        print("{}".format(sum))
