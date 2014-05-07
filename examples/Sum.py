#!/usr/bin/env python3

# ------
# Sum.py
# ------

from functools import reduce
from operator  import add

import sys
import time

def sum_while (a) :
    i = 0
    s = 0
    while i != len(a) :
        s += a[i]
        i += 1
    return s

def sum_for_range (a) :
    s = 0
    for i in range(len(a)) :
        s += a[i]
    return s

def sum_while_iter (a) :
    p = iter(a)
    s = 0
    try :
        while True :
            s += next(p)
    except StopIteration :
        pass
    return s

def sum_for_in (a) :
    s = 0
    for w in a :
        s += w
    return s

def sum_reduce_lambda (a) :
    return reduce(lambda x, y : x + y, a, 0)

def sum_reduce_operator (a) :
    return reduce(add, a, 0)

def test_1 (f, c) :
    assert f(c())          == 0
    assert f(c([2]))       == 2
    assert f(c([2, 3]))    == 5
    assert f(c([2, 3, 4])) == 9

def test_2 (f) :
    print(f.__name__)
    a = 500 * [1]
    b = time.clock()
    assert f(a) == 500
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("Sum.py")
print(sys.version)
print()

test_1(sum_while, list)
test_1(sum_while, tuple)
#test_1(sum_while, set) # TypeError: 'set' object does not support indexing

test_1(sum_for_range, list)
test_1(sum_for_range, tuple)
#test_1(sum_for_range, set) # TypeError: 'set' object does not support indexing

test_1(sum_while_iter, list)
test_1(sum_while_iter, tuple)
test_1(sum_while_iter, set)

test_1(sum_for_in, list)
test_1(sum_for_in, tuple)
test_1(sum_for_in, set)

test_1(sum_reduce_lambda, list)
test_1(sum_reduce_lambda, tuple)
test_1(sum_reduce_lambda, set)

test_1(sum_reduce_operator, list)
test_1(sum_reduce_operator, tuple)
test_1(sum_reduce_operator, set)

test_1(sum, list )
test_1(sum, tuple)
test_1(sum, set)

test_2(sum_while)
test_2(sum_for_range)
test_2(sum_while_iter,)
test_2(sum_for_in)
test_2(sum_reduce_lambda)
test_2(sum_reduce_operator)
test_2(sum)

print("Done.")

"""
Sum.py
3.3.3 (default, Jan 19 2014, 09:53:07)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

sum_while
0.206 milliseconds

sum_for_range
0.085 milliseconds

sum_while_iter
0.126 milliseconds

sum_for_in
0.053 milliseconds

sum_reduce_lambda
0.134 milliseconds

sum_reduce_operator
0.068 milliseconds

sum
0.013 milliseconds

Done.
"""
