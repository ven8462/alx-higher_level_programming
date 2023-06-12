#!/usr/bin/python3

def add_tuple(tuple_a(), tuple_b=()):
    result = []
    for i, (a, b) in enumerate(zip(tuple_a, tuple_b)):
        if i < 2:
            result.append(a + b)
    while len(result) < 2:
        result.append(0)
    return tuple(result)
