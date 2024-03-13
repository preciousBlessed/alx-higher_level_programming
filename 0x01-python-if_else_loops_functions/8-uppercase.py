#!/usr/bin/python3
def uppercase(str):
    for c in str:
        cc = ord(c)
        ll = chr(cc-32)
        print("{}".format(ll if cc in range(97, 123) else c), end="")
    print(end="\n")
