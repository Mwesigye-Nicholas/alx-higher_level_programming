#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)
    if x != 0 or y != 0:
        if x == 0:
            return (tuple_b)
        if y == 0:
            return (tuple_a)
        if x > 0 and y > 0:
            if x >= 2:
                if y >= 2:
                    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
                else:
                    return (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
            else:
                if y < 2:
                    return ((tuple_a[0] + tuple_b[0]))
                else:
                    return (tuple_a[0] + tuple_b[0], tuple_b[1] + 0)
