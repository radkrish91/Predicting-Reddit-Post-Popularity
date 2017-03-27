#!/usr/bin/env python

import sys
import datetime

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id, compound, neg, neu, pos, sentiment_class
    # Output : subreddit, created_utc, bucket_day, bucket_hour, sentiment_class, gilded, score, compound, neg, neu, pos
    # Sentiment Class : {1: 'HP', 2: 'MP', 3: 'N', 4: 'MN', 5: 'HN'}
    
    # Bucket stores hour in NY timezone
    bucket_day = datetime.datetime.fromtimestamp(int(row[1])).strftime('%d')
    bucket_hour = datetime.datetime.fromtimestamp(int(row[1])).strftime('%H')
    
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[1], bucket_day, bucket_hour, row[16], row[6], row[8], row[12], row[13], row[14], row[15])
