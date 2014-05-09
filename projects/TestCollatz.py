#!/usr/bin/env python3

"""
% TestCollatz.py >& TestCollatz.out
"""

import io
import unittest

from Collatz import collatz_solve

class TestCollatz (unittest.TestCase) :
    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

unittest.main()
