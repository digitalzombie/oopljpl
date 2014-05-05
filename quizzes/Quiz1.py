#!/usr/bin/env python3

"""
OOPL JPL: Quiz #1
"""

""" ----------------------------------------------------------------------
1. What does the following program output?

type(False): <class 'bool'>
type(bool): <class 'type'>
type(NameError()): <class 'NameError'>
type(NameError): <class 'type'>
type(type): <class 'type'>

g1
f1
f2
g2
else
finally
g3

g1
f1
NameError
finally
g3

g1
f1
finally
TypeError
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

def h (n) :
    try :
        g(n)
    except TypeError :
        print("TypeError")

h(0)
print()

h(1)
print()

h(2)
