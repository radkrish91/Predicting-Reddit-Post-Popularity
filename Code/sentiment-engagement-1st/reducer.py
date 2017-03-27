#!/usr/bin/env python

import sys
# Input : subreddit, link_id, sentiment_class, num_of_comments, score, compound, neg, neu, pos
# Output : subreddit, link_id, num_of_comments, score, compound, neg, neu, pos, sentiment_class

(subreddit, last_key1, last_key2, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (None, None, None, 0, 0, 0.0, 0.0, 0.0, 0.0)
for line in sys.stdin:
    (subr, key1, key2, com, score, compound, neg, neu, pos) = line.strip().split(",") 
    if (subreddit and subreddit != subr) or (last_key1 and last_key1 != key1) or (last_key2 and last_key2 != key2):
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, last_key1, last_key2, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos)
        (subreddit, last_key1, last_key2, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, key1, key2, int(com), int(score), float(compound), float(neg), float(neu), float(pos))
    else:
        (subreddit, last_key1, last_key2, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, key1, key2, num_of_comments+int(com), total_score+int(score), total_compound+float(compound), total_neg+float(neg), total_neu+float(neu), total_pos+float(pos)) 

if subreddit and last_key1 and last_key2:
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, last_key1, last_key2, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos)
