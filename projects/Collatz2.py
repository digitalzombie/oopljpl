#!/usr/bin/env python3

from sys import stdin, stdout

def collatz_read (r) :
    return ([int(v) for v in s.split()] for s in r)

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def collatz_eval (i, j) :
    v = 0
    for n in range(i, j + 1) :
        c = cycle_length(n)
        if c > v :
            v = c
    return v

def collatz_print (w, i, j, v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :
    for a in collatz_read(r) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

if __name__ == '__main__' :
    collatz_solve(stdin, stdout)
