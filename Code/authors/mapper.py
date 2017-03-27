#!/usr/bin/env python

import sys

# Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id, compound, neg, neu, pos, sentiment_class
# Output: subreddit, author, sentiment_class, comment, gilded, score, compound, neg, neu, pos

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[7], row[16], 1, row[6], row[8], row[12], row[13], row[14], row[15])
