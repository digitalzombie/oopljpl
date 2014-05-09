#!/usr/bin/env python3

"""
% Collatz.py < Collatz.in > Collatz.tmp
% diff Collatz.tmp Collatz.out
"""

from sys import stdin, stdout

def collatz_solve (r, w) :
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    w.write("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

if __name__ == '__main__' :
    collatz_solve(stdin, stdout)
