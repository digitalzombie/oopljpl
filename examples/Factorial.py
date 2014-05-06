#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

import functools
import math
import operator
import sys
import time

def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, m) :
        if n < 2 :
            return m
        return f(n - 1 , n * m)
    return f(n, 1)

def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_for_range (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_reduce_range (n) :
    assert n >= 0
    return functools.reduce(operator.mul, range(1, n + 1), 1)

def test (f) :
    print(f.__name__)
    assert f(0) ==   1
    assert f(1) ==   1
    assert f(2) ==   2
    assert f(3) ==   6
    assert f(4) ==  24
    assert f(5) == 120

    b = time.clock()
    print(f(100))
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("Factorial.py")
print()

print(sys.version)
print()

test(factorial_recursion)
test(factorial_tail_recursion)
test(factorial_while)
test(factorial_for_range)
test(factorial_reduce_range)
test(math.factorial)

print("Done.")

"""
Factorial.py

3.3.3 (default, Jan 19 2014, 09:53:07)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

factorial_recursion
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.112 milliseconds

factorial_tail_recursion
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.111 milliseconds

factorial_while
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.049 milliseconds

factorial_for_range
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.041 milliseconds

factorial_reduce_range
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.044 milliseconds

factorial
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.030 milliseconds

Done.
"""
