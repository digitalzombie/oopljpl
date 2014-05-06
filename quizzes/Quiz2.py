#!/usr/bin/env python3

"""
OOPL JPL: Quiz #2
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?

14
-4

abcdefghi
[2, 3, 4]
(2, 3, 4)
[7, 8, 9]
[7, 9, 11]

[3, 5]

[7, 8, 9]
[7, 9, 11]
"""

from functools import reduce
from operator  import add, sub

print(reduce(add, [2, 3, 4], 5))
print(reduce(lambda x, y : x - y, [2, 3, 4], 5))
print()

print(reduce(add, ["abc", "def", "ghi"], ""))
print(reduce(add, [[2],   [3],   [4]],   []))
print(reduce(add, [(2,),  (3,),  (4,)],  ()))

print(list(map(lambda x : x + 5, [2, 3, 4])))
print(list(map(add,              [2, 3, 4], [5, 6, 7])))
print()

print(list(filter(lambda x : x % 2, [2, 3, 4, 5, 6])))
print()

print([x + 5 for x    in [2, 3, 4]])
print([x + y for x, y in zip([2, 3, 4], [5, 6, 7])])
