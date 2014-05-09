#!/usr/bin/env python3

"""
OOPL JPL: Quiz #4
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
"""

import re

print([2, 3, 4, 5, 6][-4 : -1 :  2 ])
print([2, 3, 4, 5, 6][-2 : -5 : -2 ])
print()

a = [[2], [3], [4]]
for v in a :
    v += (5,)
print(a)

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)
print(a)
print()

s = "b xaby\nzaab 123"

m = re.search("(a*)b([^a]*)(a*)b", s) # * is zero or more
print(m.group(0))
print()

m = re.search("(a+)b([^a]*)(a+)b", s) # + is one or more
print(m.group(0))
print()

m = re.search("(a?)b([^a]*)(a?)b", s) # ? is zero or one
print(m.group(0))
