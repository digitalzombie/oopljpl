#!/usr/bin/env python3

# ------------
# Exercise3.py
# ------------

from functools import reduce
from operator  import sub

print("Exercise3.py")

assert reduce(sub, [2])       ==  2
assert reduce(sub, [2, 3])    == -1
assert reduce(sub, [2, 3, 4]) == -5

print("Done.")
