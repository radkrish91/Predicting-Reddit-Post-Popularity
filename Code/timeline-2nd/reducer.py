#!/usr/bin/env python

import sys
# Input : subreddit, bucket, sentiment_class, num_of_comments, gilded, score, compound, neg, neu, pos
# Output : subreddit, bucket, sentiment_class, num_of_comments, avg_gilded, avg_score, avg_compound, avg_neg, avg_neu, avg_pos

(subreddit, bucket, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (None, None, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)

for line in sys.stdin:
    (subr, buck, senti, com, gilded, score, compound, neg, neu, pos) = line.strip().split(",")
    if (subreddit and subreddit != subr) or (bucket and bucket != buck) or (sentiment_class and sentiment_class != senti):
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, bucket, sentiment_class, num_of_comments, float(total_gilded)/num_of_comments, float(total_score)/num_of_comments, total_compound/num_of_comments, total_neg/num_of_comments, total_neu/num_of_comments, total_pos/num_of_comments)
        (subreddit, bucket, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, buck, senti, int(com), int(gilded), int(score), float(compound), float(neg), float(neu), float(pos))
    else:
        (subreddit, bucket, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, buck, senti, num_of_comments+int(com), total_gilded+int(gilded), total_score+int(score), total_compound+float(compound), total_neg+float(neg), total_neu+float(neu), total_pos+float(pos))
        
if subreddit and bucket and sentiment_class:        
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, bucket, sentiment_class, num_of_comments, float(total_gilded)/num_of_comments, float(total_score)/num_of_comments, total_compound/num_of_comments, total_neg/num_of_comments, total_neu/num_of_comments, total_pos/num_of_comments)
       
