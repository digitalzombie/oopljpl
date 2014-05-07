#!/usr/bin/env python3

# ------------
# Exercise3.py
# ------------

from functools import reduce
from operator  import sub

print("Exercise3.py")

assert reduce(sub, [2])          ==  2
assert reduce(sub, [2, 3])       == -1
assert reduce(sub, [2, 3, 4])    == -5

assert reduce(sub, [],        0) ==  0
assert reduce(sub, [2],       0) == -2
assert reduce(sub, [2, 3],    0) == -5
assert reduce(sub, [2, 3, 4], 0) == -9

print("Done.")
