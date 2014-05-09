#!/usr/bin/env python3

from io       import StringIO
from unittest import main, TestCase

from Collatz2 import collatz_read, collatz_eval, collatz_print, collatz_solve

class TestCollatz (TestCase) :
    def test_read (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        assert tuple(collatz_read(r)) == ([1, 10], [100, 200], [201, 210], [900, 1000])

    def test_eval_1 (self) :
        self.assertTrue(collatz_eval(1, 10) == 20)

    def test_eval_2 (self) :
        self.assertTrue(collatz_eval(100, 200) == 125)

    def test_eval_3 (self) :
        self.assertTrue(collatz_eval(201, 210) == 89)

    def test_eval_4 (self) :
        self.assertTrue(collatz_eval(900, 1000) == 174)

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

main()
