#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxint = -100000000000e1000000000000
    for number in my_list:
        if number > maxint:
            maxint = number
    return maxint
