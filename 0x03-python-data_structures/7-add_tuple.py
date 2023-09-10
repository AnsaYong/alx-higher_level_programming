#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        x = 0
        y = 0
    elif len(tuple_a) == 1:
        x = tuple_a[0]
        y = 0
    else:
        x, y = tuple_a

    if len(tuple_b) == 0:
        a = 0
        b = 0
    elif len(tuple_b) == 1:
        a = tuple_b[0]
        b = 0
    else:
        a, b = tuple_b

    t = (a + x, b + y)

    return (t)
