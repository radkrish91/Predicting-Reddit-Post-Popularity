#!/usr/bin/env python

import sys

for line in sys.stdin:
    
    line =  line.strip()
    row = line.split(' ', 1)
    print "%s %s" % (row[0], row[1])
