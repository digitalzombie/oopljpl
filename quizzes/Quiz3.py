#!/usr/bin/env python3

"""
OOPL JPL: Quiz #3
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?

[2, 3, 4, 5, 7]
"""

def f (x, y, z, a = 5, b = 6) :
    return [x, y, z, a, b]

t = (3,)
d = {"b" : 7}

print(f(2, z = 4, *t, **d))
