#!/usr/bin/env python

import sys

(last_key, subreddit, num_of_comments, total_score, total_gild) = (None, None, 0, 0, 0) 
for line in sys.stdin:
    (key, subreddit, com, score, gild) = line.strip().split(" ") 
    if last_key and last_key != key:
        print "%s,%s,%s,%s,%s" % (last_key, subreddit, num_of_comments, float(total_score)/num_of_comments, total_gild)
        (last_key, subreddit, num_of_comments, total_score, total_gild) = (key, subreddit, int(com), int(score), int(gild)) 
    else:
        (last_key, subreddit, num_of_comments, total_score, total_gild) = (key, subreddit, num_of_comments+int(com), total_score+int(score), total_gild+int(gild))

if last_key:
    print "%s,%s,%s,%s,%s" % (last_key, subreddit, num_of_comments, float(total_score)/num_of_comments, total_gild)
