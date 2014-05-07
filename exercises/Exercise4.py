#!/usr/bin/env python3

# ------------
# Exercise4.py
# ------------

print("Exercise4.py")

assert(list(map(lambda x       : x + x,     []))                     == [])
assert(list(map(lambda x       : x + x,     [2, 3, 4]))              == [4, 6, 8])
assert(list(map(lambda x, y    : x + y,     (2, 3, 4), (5, 6, 7)))   == [7, 9, 11])
assert(list(map(lambda x, y, z : x + y + z, [2, 3], [4, 5], [6, 7])) == [12, 15])

print("Done.")
