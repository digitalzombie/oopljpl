#!/usr/bin/env python3

"""
OOPL JPL: Quiz #2
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
"""

from functools import reduce

print(reduce(lambda x, y : x + y, [2, 3, 4], 5))
print(reduce(lambda x, y : x - y, [2, 3, 4], 5))
print()

print(reduce(lambda x, y : x + y, ["abc", "def", "ghi"], ""))
print(reduce(lambda x, y : x + y, [[2],   [3],   [4]],   []))
print(reduce(lambda x, y : x + y, [(2,),  (3,),  (4,)],  ()))

print(list(map(lambda x    : x + 5, [2, 3, 4])))
print(list(map(lambda x, y : x + y, [2, 3, 4], [5, 6, 7])))
print()

print(list(filter(lambda x : x % 2, [2, 3, 4, 5, 6])))
print()

print([x + 5 for x    in [2, 3, 4]])
print([x + y for x, y in zip([2, 3, 4], [5, 6, 7])])
