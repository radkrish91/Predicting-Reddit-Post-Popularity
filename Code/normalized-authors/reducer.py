#!/usr/bin/env python

import sys
# Input: subreddit, author, sentiment_class, num_of_comments, normalized_score
# Output: subreddit, author, sentiment_class, num_of_comments, normalized_score

for line in sys.stdin:
    row = line.strip().split(",")
    print "%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4])
