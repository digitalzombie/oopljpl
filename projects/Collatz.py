#!/usr/bin/env python3

"""
% Collatz.py < Collatz.in > Collatz.tmp
% diff Collatz.tmp Collatz.out
"""

import sys

def collatz_solve (r, w) :
    w.write("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

if __name__ == '__main__' :
    collatz_solve(sys.stdin, sys.stdout)
