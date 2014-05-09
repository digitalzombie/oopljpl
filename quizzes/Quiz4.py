#!/usr/bin/env python3

"""
OOPL JPL: Quiz #4
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
"""

import re

s = "b xaby\nzaab 123"

m = re.search("(a*)b([^a]*)(a*)b", s) # * is zero or more
print(m.group(0))
print()

m = re.search("(a+)b([^a]*)(a+)b", s) # + is one or more
print(m.group(0))
print()

m = re.search("(a?)b([^a]*)(a?)b", s) # ? is zero or one
print(m.group(0))
