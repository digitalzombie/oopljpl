#!/usr/bin/env python3

# ------------------
# FileInputOutput.py
# ------------------

"""
% FileInputOutput.py
"""

import sys

f = open(sys.argv[0])

for u in f :
    for v in u :
        print(v, end = "")

f = open(sys.argv[0])

for u in f :
    for v in u :
        print(v, " ", end = "")
