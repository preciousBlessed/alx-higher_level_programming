#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        len_list = len(my_list)
        while len_list > 0:
            print("{:d}".format(my_list[len_list - 1]))
            len_list -= 1
    else:
        return
