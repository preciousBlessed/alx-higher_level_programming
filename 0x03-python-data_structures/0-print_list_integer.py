#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for elem in my_list:
            print("{:d}".format(elem))
    else:
        return
