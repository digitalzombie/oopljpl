#!/usr/bin/env python3

# ------------
# Exercise4.py
# ------------

"""
print("Exercise4.py")

assert(list(map(lambda x       : x + x,     []))                     == [])
assert(list(map(lambda x       : x + x,     [2, 3, 4]))              == [4, 6, 8])
assert(list(map(lambda x, y    : x + y,     (2, 3, 4), (5, 6, 7)))   == [7, 9, 11])
assert(list(map(lambda x, y, z : x + y + z, [2, 3], [4, 5], [6, 7])) == [12, 15])

print("Done.")
"""

import unittest

def map_1 (nf, *a) :
    for v in zip(*a) :
        yield nf(*v)

def map_2 (nf, *a) :
    return (nf(*v) for v in zip(*a))

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        self.assertTrue(list(map_1(lambda x       : x + x,     []))                     == [])

    def test_2 (self) :
        self.assertTrue(list(map_1(lambda x       : x + x,     [2, 3, 4]))              == [4, 6, 8])

    def test_3 (self) :
        self.assertTrue(list(map_1(lambda x, y    : x + y,     (2, 3, 4), (5, 6, 7)))   == [7, 9, 11])

    def test_4 (self) :
        self.assertTrue(list(map_1(lambda x, y, z : x + y + z, [2, 3], [4, 5], [6, 7])) == [12, 15])

unittest.main()
