#!/usr/bin/env python3

from io       import StringIO
from unittest import main, TestCase

from Collatz3 import collatz_read, collatz_eval, collatz_print, collatz_solve

class TestCollatz (TestCase) :
    def test_read (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        x = tuple(collatz_read(r))
        assert x == ([1, 10], [100, 200], [201, 210], [900, 1000])

    def test_eval (self) :
        x = tuple(collatz_eval(([1, 10], [100, 200], [201, 210], [900, 1000])))
        assert x == ([1, 10, 20], [100, 200, 125], [201, 210, 89], [900, 1000, 174])

    def test_print (self) :
        x = collatz_print(([1, 10, 20], [100, 200, 125], [201, 210, 89], [900, 1000, 174]))
        assert [v for v in x] == ['1 10 20\n', '100 200 125\n', '201 210 89\n', '900 1000 174\n']

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

main()
