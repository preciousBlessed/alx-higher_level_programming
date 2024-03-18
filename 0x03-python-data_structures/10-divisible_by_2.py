#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    #new_list = []
    #for numbers in my_list:
    #   new_list.append(numbers % 2 == 0)
    return [True if i%2 == 0 else False for i in my_list]
