#!/usr/bin/env python3

# ------------
# Exercise1.py
# ------------

from math import sqrt

def is_prime (n) :
    assert(n > 0)
    if (n < 2) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0:
            return False
    return True

print("Exercise1.py")

assert(not is_prime( 1));
assert(    is_prime( 3));
assert(not is_prime( 4));
assert(    is_prime( 5));

print("Done.")

"""
% coverage run --branch Exercise1.py
Exercise1.py
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Exercise1      16      2      6      3    77%
"""
