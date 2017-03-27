#!/usr/bin/env python

import sys
# Input: subreddit, author, sentiment_class, num_of_comments, normalized_score
# Output: subreddit, author, sentiment_class, num_of_comments, normalized_score

maxS = 8.0
midS = 0.0
mins = -200.0

for line in sys.stdin:
    row = line.strip().split(",")
    norm_score = float(row[4])
    if(norm_score > 0.0):
        predicted_score = maxS - (1.0 - norm_score)*(maxS - midS)
    else:
        predicted_score = midS - (1.0 + norm_score)*(midS - minS)
    print "%s,%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4], predicted_score/int(row[3]))
