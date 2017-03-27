#!/usr/bin/env python

import sys
# Input : subreddit, created_utc, bucket, sentiment_class, gilded, score, compound, neg, neu, pos
# Output : subreddit, created_utc, bucket, sentiment_class, gilded, score, compound, neg, neu, pos

for line in sys.stdin:
    (subreddit, created_utc, bucket, sentiment_class, gilded, score, compound, neg, neu, pos) = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, created_utc, bucket, sentiment_class, gilded, score, compound, neg, neu, pos)
