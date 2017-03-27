#!/usr/bin/env python

import sys

for line in sys.stdin:
    (subreddit, sentiment, gilded, score, body, compound, neg, new, pos) = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, sentiment, gilded, score, body, compound, neg, new, pos)
