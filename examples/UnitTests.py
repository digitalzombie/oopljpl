#!/usr/bin/env python3

# ------------
# UnitTests.py
# ------------

import unittest

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        self.assertTrue(1 == 2)

    def test_2 (self) :
        self.assertTrue(2 == 2)

    def test_3 (self) :
        self.assertTrue(3 == 2)

print("UnitTests.py")
unittest.main()
print("Done.")

"""
UnitTests.py
.F.F
======================================================================
FAIL: test_2 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 16, in test_2
    self.assertTrue(False)
AssertionError

======================================================================
FAIL: test_4 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 22, in test_4
    self.assertTrue(False)
AssertionError

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=2)
"""
