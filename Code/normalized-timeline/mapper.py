#!/usr/bin/env python

import sys

# Input : subreddit, bucket, sentiment_class, num_of_comments, avg_gilded, avg_score, avg_compound, avg_neg, avg_neu, avg_pos
# Output : subreddit, bucket, sentiment_class, num_of_comments, normalized_score

maxS = 1403964
minS = 535

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    score = float(row[5])*int(row[3])
    norm_score = (1.0 - (maxS - score)/(maxS - minS))
    
    print "%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], norm_score)
