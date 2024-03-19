#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) < 2:
        for i in range(len(list_a), 2):
            list_a.append(0)

    if len(list_b) < 2:
        for i in range(len(list_b), 2):
            list_b.append(0)

    tuple_a, tuple_b = tuple(list_a), tuple(list_b)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple_c)
