#!/usr/bin/env python3

"""
OOPL JPL: Quiz #1
"""

""" ----------------------------------------------------------------------
1. What does the following program do?
"""

print("type(False):",       type(False))
print("type(bool):",        type(bool))
print("type(NameError()):", type(NameError()))
print("type(NameError):",   type(NameError))
print("type(type):",        type(type))
print()

def f (n) :
    print("f1")
    if (n % 3) == 1 :
        raise NameError()
    elif (n % 3) == 2 :
        raise TypeError()
    print("f2")

def g (n) :
    try :
        try :
            print("g1")
            f(n)
            print("g2")
        except NameError :
            print("NameError")
        else :
            print("else")
        finally :
            print("finally")
        print("g3")
    except TypeError :
        print("TypeError")

g(0)
print()

g(1)
print()

g(2)
