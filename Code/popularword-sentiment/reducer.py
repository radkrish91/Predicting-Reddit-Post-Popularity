#!/usr/bin/env python

import sys

# Input: subreddit, word, sentiment, count
# Output: sentiment, count, word, subreddit

for line in sys.stdin:
    (sentiment, count, word, subreddit) = line.strip().split(",")
    print "%s,%s,%s,%s" % (sentiment, count, word, subreddit)
    
