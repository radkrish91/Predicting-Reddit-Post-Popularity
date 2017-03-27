#!/usr/bin/env python

import sys

for line in sys.stdin:
    row = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
