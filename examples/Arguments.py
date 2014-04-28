#!/usr/bin/env python3

# ------------
# Arguments.py
# ------------

def f1 (j) :
    j += 1

def f2 (t) :
    t += "def"

def f3 (b) :
    b[1] += 1

def f4 (b) :
    b += (5,)

print("Arguments.py")

i = 2
f1(i)
assert i is 2

s = "abc"
f2(s)
assert s is "abc"

a = [2, 3, 4]
f3(a)
assert a is not [2, 4, 4]
assert a ==     [2, 4, 4]

a = [2, 3, 4]
f3(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

a = [2, 3, 4]
f4(a)
assert a is not [2, 3, 4, 5]
assert a ==     [2, 3, 4, 5]

a = [2, 3, 4]
f4(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

a = (2, 3, 4)
f4(a)
assert a is not (2, 3, 4)
assert a ==     (2, 3, 4)

print("Done.")
