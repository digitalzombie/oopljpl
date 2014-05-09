#!/usr/bin/env python3

"""
% TestCollatz.py >& TestCollatz.out
"""

from io       import StringIO
from unittest import TestCase

from Collatz import collatz_solve

class TestCollatz (TestCase) :
    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

main()
