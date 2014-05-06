#!/usr/bin/env python3

# -----------
# IsPrime2.py
# -----------

from math import sqrt

def is_prime (n) :
    assert(n > 0)
    if (n < 2) :
        return False
    for i in range(2, int(sqrt(n)) + 1) :
        if (n % i) == 0 :
            return False
    return True

print("IsPrime2.py")

assert(not is_prime( 1));
assert(    is_prime( 2));
assert(    is_prime( 3));
assert(not is_prime( 4));
assert(    is_prime( 5));
assert(not is_prime( 6));
assert(    is_prime( 7));
assert(not is_prime( 8));
assert(not is_prime( 9));
assert(not is_prime(10));
assert(    is_prime(11));

print("Done.")

"""
% coverage run --branch IsPrime2.py
IsPrime2.py
Done.

% coverage report
Name       Stmts   Miss Branch BrMiss  Cover
--------------------------------------------
IsPrime2      20      0      6      0   100%
"""
