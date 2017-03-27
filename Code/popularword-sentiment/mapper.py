#!/usr/bin/env python

import sys

# Input: subreddit, word, sentiment, count
# Output: sentiment, count, word, subreddit

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    print "%s,%s,%s,%s" % (int(row[2]), int(row[3]), row[1], row[0])
