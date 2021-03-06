#!/usr/bin/env python3

# ------------
# Exercise6.py
# ------------

"""
print("Exercise6.py")

Design, test, and implement the following methods of a queue:

back
empty
front
pop
push
size

print("Done.")
"""

import unittest

class Queue :
    def __init__ (self) :
        self.a = []

    def back (self) :
        return self.a[-1]

    def empty (self) :
        return self.size() == 0

    def front (self) :
        return self.a[0]

    def pop (self) :
        self.a.pop(0)

    def push (self, v) :
        return self.a.append(v)

    def size (self) :
        return len(self.a)

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        x = Queue()
        self.assertTrue(x.empty())
        self.assertTrue(x.size() == 0)

    def test_2 (self) :
        x = Queue()
        x.push(2)
        self.assertTrue(not x.empty())
        self.assertTrue(x.front() == 2)
        self.assertTrue(x.back()  == 2)
        self.assertTrue(x.size()  == 1)

    def test_3 (self) :
        x = Queue()
        x.push(2)
        x.push(3)
        self.assertTrue(not x.empty())
        self.assertTrue(x.front() == 2)
        self.assertTrue(x.back()  == 3)
        self.assertTrue(x.size()  == 2)

    def test_4 (self) :
        x = Queue()
        x.push(2)
        x.push(3)
        x.push(4)
        self.assertTrue(not x.empty())
        self.assertTrue(x.front() == 2)
        self.assertTrue(x.back()  == 4)
        self.assertTrue(x.size()  == 3)

    def test_4 (self) :
        x = Queue()
        x.push(2)
        x.push(3)
        x.push(4)
        x.pop()
        self.assertTrue(not x.empty())
        self.assertTrue(x.front() == 3)
        self.assertTrue(x.back()  == 4)
        self.assertTrue(x.size()  == 2)

    def test_4 (self) :
        x = Queue()
        x.push(2)
        x.push(3)
        x.push(4)
        x.pop()
        x.pop()
        self.assertTrue(not x.empty())
        self.assertTrue(x.front() == 4)
        self.assertTrue(x.back()  == 4)
        self.assertTrue(x.size()  == 1)

    def test_5 (self) :
        x = Queue()
        x.push(2)
        x.push(3)
        x.push(4)
        x.pop()
        x.pop()
        x.pop()
        self.assertTrue(x.empty())
        self.assertTrue(x.size() == 0)

unittest.main()
