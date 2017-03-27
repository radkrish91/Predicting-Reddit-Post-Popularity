#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, link_id, sentiment_class, num_of_comments, score, compound, neg, neu, pos
    # Output : subreddit, sentiment_class, num_of_links, num_of_comments, score, compound, neg, neu, pos
    # Sentiment Class : {1: 'HP', 2: 'MP', 3: 'N', 4: 'MN', 5: 'HN'}

    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[2], 1, row[3], row[4], row[5], row[6], row[7], row[8])
