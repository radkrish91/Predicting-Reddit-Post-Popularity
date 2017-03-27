#!/usr/bin/env python

import sys
# Input: subreddit, bucket, sentiment_class, num_of_comments, normalized_score
# Output: subreddit, bucket, sentiment_class, num_of_comments, normalized_score

maxS = 1403964
minS = 535

for line in sys.stdin:
    row = line.strip().split(",")
    norm_score = float(row[4])
    predicted_score = maxS - (1.0 - norm_score)*(maxS - minS)
    print "%s,%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4], predicted_score/int(row[3]))
