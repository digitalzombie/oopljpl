#!/usr/bin/env python3

# ------------
# Exercise3.py
# ------------

from functools import reduce
from operator  import sub

"""
print("Exercise3.py")

assert reduce(sub, [2])          ==  2
assert reduce(sub, [2, 3])       == -1
assert reduce(sub, [2, 3, 4])    == -5

assert reduce(sub, [],        0) ==  0
assert reduce(sub, [2],       0) == -2
assert reduce(sub, [2, 3],    0) == -5
assert reduce(sub, [2, 3, 4], 0) == -9

print("Done.")
"""
import unittest

def reduce_1 (bf, a, v = None) :
    if not a and v is None :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_2 (bf, a, v = None) :
    if not a and v is None :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        self.assertTrue(reduce_1(sub, [2])          ==  2)

    def test_2 (self) :
        self.assertTrue(reduce_1(sub, [2, 3])       == -1)

    def test_3 (self) :
        self.assertTrue(reduce_1(sub, [2, 3, 4])    == -5)

    def test_4 (self) :
        self.assertTrue(reduce_1(sub, [],        0) ==  0)

    def test_5 (self) :
        self.assertTrue(reduce_1(sub, [2],       0) == -2)

    def test_6 (self) :
        self.assertTrue(reduce_1(sub, [2, 3],    0) == -5)

    def test_7 (self) :
        self.assertTrue(reduce_1(sub, [2, 3, 4], 0) == -9)

    def test_8 (self) :
        try :
            reduce_1(sub, [])
        except TypeError as e :
            assert type(e)      is     TypeError
            assert type(e.args) is     tuple
            assert len(e.args)  ==     1
            assert e.args       is not ("reduce() of empty sequence with no initial value",)
            assert e.args       ==     ("reduce() of empty sequence with no initial value",)
        except Exception :
            self.assertTrue(False)
        else :
            self.assertTrue(False)

unittest.main()
