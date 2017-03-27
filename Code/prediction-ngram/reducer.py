#!/usr/bin/env python

import sys
import numpy

# Input : sequence, count, sentiment, gilded, score, compound
# Output : sequence, count, sentiment, gilded, score, compound
def median(lst):
    return numpy.median(numpy.array(lst))

l = []
for line in sys.stdin:
    (seq, count, sentiment, gild, score, comp) = line.strip().split(",")
    l.append(float(score)/int(count))
    print "%s,%s,%s,%s,%s,%s" % (seq, count, sentiment, gild, score, comp)

print "Median : %s" % (median(l))
