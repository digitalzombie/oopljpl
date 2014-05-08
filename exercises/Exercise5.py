#!/usr/bin/env python3

# ------------
# Exercise5.py
# ------------

"""
print("Exercise5.py")

x = Integer_1(234)
p = iter(x)
assert iter(p) is p
assert next(p) == 4
assert next(p) == 3
assert next(p) == 2
try :
    next(p)
except StopIteration :
    pass

x = Integer_1(234)
assert sum(x) == 9

print("Done.")
"""

import unittest

class Integer_1 :
    class Iterator :
        def __init__ (self, n) :
            self.n = n

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.n == 0 :
                raise StopIteration()
            m = self.n % 10
            self.n //= 10
            return m

    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        return Integer_1.Iterator(self.n)

class Integer_2 :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        while self.n > 0 :
            yield self.n % 10
            self.n //= 10

def Integer_3 (n) :
    while n > 0 :
        yield n % 10
        n //= 10

class UnitTests (unittest.TestCase) :
    def setUp (self) :
        self.x = Integer_1(234)
        self.p = iter(self.x)

    def test_1 (self) :
        assert iter(self.p) is self.p

    def test_2 (self) :
        assert next(self.p) == 4

    def test_3 (self) :
        next(self.p)
        assert next(self.p) == 3

    def test_4 (self) :
        next(self.p)
        next(self.p)
        assert next(self.p) == 2

    def test_5 (self) :
        next(self.p)
        next(self.p)
        next(self.p)
        try :
            next(self.p)
        except StopIteration :
            pass

    def test_6 (self) :
        assert sum(self.x) == 9

    def test_7 (self) :
        assert sum(self.p) == 9

unittest.main()
