#!/usr/bin/env python

import sys
# Input : subreddit, sentiment_class, num_of_links, num_of_comments, score, compound, neg, neu, pos
# Output : subreddit, sentiment_class, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos, engagement

(last_key1, last_key2, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (None, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
for line in sys.stdin:
    (key1, key2, link, com, score, compound, neg, neu, pos) = line.strip().split(",") 
    if (last_key1 and last_key1 != key1) or (last_key2 and last_key2 != key2):
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (last_key1, last_key2, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos, float(num_of_comments)/num_of_links)
        (last_key1, last_key2, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (key1, key2, int(link), int(com), int(score), float(compound), float(neg), float(neu), float(pos))
    else:
        (last_key1, last_key2, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos) = (key1, key2, num_of_links+int(link), num_of_comments+int(com), total_score+int(score), total_compound+float(compound), total_neg+float(neg), total_neu+float(neu), total_pos+float(pos)) 

if last_key1 and last_key2:
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (last_key1, last_key2, num_of_links, num_of_comments, total_score, total_compound, total_neg, total_neu, total_pos, float(num_of_comments)/num_of_links)
