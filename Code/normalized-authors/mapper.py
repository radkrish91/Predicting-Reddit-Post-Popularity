#!/usr/bin/env python

import sys

# Input: subreddit, author, sentiment_class, num_of_comments, avg_gilded, avg_score, avg_compound, avg_neg, avg_neu, avg_pos
# Output: subreddit, author, sentiment_class, num_of_comments, normalized_score

maxS = 8.0
midS = 0.0
minS = -200.0

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    score = float(row[5])*int(row[3])
    if(score >= maxS):
        norm_score = 1.0
    elif(score > midS):
        norm_score = (1.0 - (maxS - score)/(maxS - midS))
    elif(score > minS):
        norm_score = ((midS - score)/(midS - minS) - 1.0)
    else:
        norm_score = -1.0
    
    print "%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], norm_score)
