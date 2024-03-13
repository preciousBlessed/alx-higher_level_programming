#!/usr/bin/python3
def print_last_digit(number):
    ll = abs(number) % 10
    print("{}".format(ll), end="")
    return ll
