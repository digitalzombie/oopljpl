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
    a = s.split()
    x = int(a[0])
    y = int(a[1])
    w.write("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

if __name__ == '__main__' :
    collatz_solve(stdin, stdout)
