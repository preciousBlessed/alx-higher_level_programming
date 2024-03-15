#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hd_list = dir(hidden_4)
    newList = []
    for elem in hd_list:
        if elem.startswith("__"):
            continue
        else:
            newList.append(elem)
    newList.sort()
    for elem in newList:
        print("{}".format(elem))
