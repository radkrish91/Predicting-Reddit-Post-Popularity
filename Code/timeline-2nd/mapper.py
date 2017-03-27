#!/usr/bin/env python

import sys
import datetime

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, created_utc, bucket, sentiment_class, gilded, score, compound, neg, neu, pos
    # Output : subreddit, bucket, sentiment_class, num_of_comments, gilded, score, compound, neg, neu, pos
    # Sentiment Class : {1: 'HP', 2: 'MP', 3: 'N', 4: 'MN', 5: 'HN'}    
    # Bucket stores hour in NY timezone
    
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[2], row[3], 1, row[4], row[5], row[6], row[7], row[8], row[9])
