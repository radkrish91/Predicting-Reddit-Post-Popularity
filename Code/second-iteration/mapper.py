#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    # Input : link_id, subreddit, num_of_comments, score, gild
    # Output : subreddit, num_of_links, num_of_comments, score, gild 
    print "%s %s %s %s %s" % (row[1], 1, row[2], row[3], row[4])
