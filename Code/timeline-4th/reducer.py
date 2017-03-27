#!/usr/bin/env python

import sys
# Input : subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, gilded, score, compound, neg, neu, pos
# Output : subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, avg_gilded, avg_score, avg_compound, avg_neg, avg_neu, avg_pos

(subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (None, None, None, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)

for line in sys.stdin:
    (subr, buck1, buck2, senti, com, gilded, score, compound, neg, neu, pos) = line.strip().split(",")
    if (subreddit and subreddit != subr) or (bucket_day and bucket_day != buck1) or (bucket_hour and bucket_hour != buck2) or (sentiment_class and sentiment_class != senti):
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, float(total_gilded)/num_of_comments, float(total_score)/num_of_comments, total_compound/num_of_comments, total_neg/num_of_comments, total_neu/num_of_comments, total_pos/num_of_comments)
        (subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, buck1, buck2, senti, int(com), int(gilded), int(score), float(compound), float(neg), float(neu), float(pos))
    else:
        (subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, total_gilded, total_score, total_compound, total_neg, total_neu, total_pos) = (subr, buck1, buck2, senti, num_of_comments+int(com), total_gilded+int(gilded), total_score+int(score), total_compound+float(compound), total_neg+float(neg), total_neu+float(neu), total_pos+float(pos))
        
if subreddit and bucket_day and bucket_hour and sentiment_class:        
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, bucket_day, bucket_hour, sentiment_class, num_of_comments, float(total_gilded)/num_of_comments, float(total_score)/num_of_comments, total_compound/num_of_comments, total_neg/num_of_comments, total_neu/num_of_comments, total_pos/num_of_comments)
