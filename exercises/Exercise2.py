#!/usr/bin/env python3

# ------------
# Exercise2.py
# ------------

"""
print("Exercise2.py")

assert sum([])        == 0
assert sum([2])       == 2
assert sum([2, 3])    == 5
assert sum([2, 3, 4]) == 9

print("Done.")
"""

from functools import reduce
from operator  import add

import unittest

def sum_for (a) :
    s = 0
    for w in a :
        s += w
    return s

def sum_reduce (a) :
    return reduce(add, a, 0)

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        self.assertTrue(sum_for([]) == 0)

    def test_2 (self) :
        self.assertTrue(sum_for([2]) == 2)

    def test_3 (self) :
        self.assertTrue(sum_for([2, 3]) == 5)

    def test_4 (self) :
        self.assertTrue(sum_for([2, 3, 4]) == 9)

    def test_5 (self) :
        self.assertTrue(sum_reduce([]) == 0)

    def test_6 (self) :
        self.assertTrue(sum_reduce([2]) == 2)

    def test_7 (self) :
        self.assertTrue(sum_reduce([2, 3]) == 5)

    def test_8 (self) :
        self.assertTrue(sum_reduce([2, 3, 4]) == 9)

unittest.main()
