#!/usr/bin/env python3

# ------------------
# Representations.py
# ------------------

import math

print("Representations.py")

i = 2
assert i        == 2
assert i        == 0b10
assert i        == 0o2
assert i        == 0x2
assert bin(i)   == "0b10"
assert oct(i)   == "0o2"
assert hex(i)   == "0x2"
assert str(i)   == "2"
assert "%o" % i == "2"
assert "%x" % i == "2"

i = 17
assert i        == 17
assert i        == 0b10001
assert i        == 0o21
assert i        == 0x11
assert bin(i)   == "0b10001"
assert oct(i)   == "0o21"
assert hex(i)   == "0x11"
assert str(i)   == "17"
assert "%o" % i == "21"
assert "%x" % i == "11"

i = -2
assert i        == -2
assert i        == -0b10
assert i        == -0o2
assert i        == -0x2
assert bin(i)   == "-0b10"
assert oct(i)   == "-0o2"
assert hex(i)   == "-0x2"
assert str(i)   == "-2"
assert "%o" % i == "-2"
assert "%x" % i == "-2"

f = 2.0
assert f       == 2.0
assert f.hex() == "0x1.0000000000000p+1"

f = -2.0
assert f       == -2.0
assert f.hex() == "-0x1.0000000000000p+1"

try :
    f = 1.0 / 0                                       # inf
    assert false
except ZeroDivisionError as e :
    assert len(e.args) == 1
    assert e.args      == ('float division by zero',)

try :
    f = math.log(0)                              # -inf
    assert false
except ValueError as e :
    assert len(e.args) == 1
    assert e.args      == ('math domain error',)

try :
    f = eval("math.sqrt(-1)")                    # nan
    assert false
except ValueError as e :
    assert len(e.args) == 1
    assert e.args      == ('math domain error',)

print("Done.")
