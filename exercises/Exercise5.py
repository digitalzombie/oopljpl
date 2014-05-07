#!/usr/bin/env python3

# ------------
# Exercise5.py
# ------------

print("Exercise5.py")

x = Integer(234)
p = iter(x)
assert iter(p) is p
assert next(p) == 4
assert next(p) == 3
assert next(p) == 2
try :
    next(p)
except StopIteration :
    pass

x = Integer(234)
assert sum(x) == 9

print("Done.")
