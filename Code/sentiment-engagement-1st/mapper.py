#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id, compound, neg, neu, pos, sentiment_class
    # Output : subreddit, link_id, sentiment_class, num_of_comments, score, compound, neg, neu, pos
    # Sentiment Class : {1: 'HP', 2: 'MP', 3: 'N', 4: 'MN', 5: 'HN'}

    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[3], row[16], 1, row[8], row[12], row[13], row[14], row[15])
