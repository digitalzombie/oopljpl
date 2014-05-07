#!/usr/bin/env python3

# ------------------
# FileInputOutput.py
# ------------------

"""
% FileInputOutput.py
"""

import sys

f = open(sys.argv[0])

for s in f :
    print(s, end = "")
