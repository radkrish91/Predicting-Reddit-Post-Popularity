#!/usr/bin/env python

import sys
# Input: subreddit, author, sentiment_class, comment, gilded, score, compound, neg, neu, pos
# Output: subreddit, author, sentiment_class, num_of_comments, avg_gilded, avg_score, avg_compound, avg_neg, avg_neu, avg_pos

(subreddit, author, sentiment, num_of_comments, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (None, None, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
for line in sys.stdin:
    (subr, aut, senti, com, gilded, score, compound, neg, neu, pos) = line.strip().split(",")
    if (subreddit and subreddit != subr) or (author and author != aut) or (sentiment and sentiment != senti) :
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, author, sentiment, num_of_comments, float(tot_gilded)/num_of_comments, float(tot_score)/num_of_comments, tot_compound/num_of_comments, tot_neg/num_of_comments, tot_neu/num_of_comments, tot_pos/num_of_comments)
        (subreddit, author, sentiment, num_of_comments, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (subr, aut, senti, int(com), int(gilded), int(score), float(compound), float(neg), float(neu), float(pos))
    else:
        (subreddit, author, sentiment, num_of_comments, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (subr, aut, senti, num_of_comments+int(com), tot_gilded+int(gilded), tot_score+int(score), tot_compound+float(compound), tot_neg+float(neg), tot_neu+float(neu), tot_pos+float(pos))
        
if subreddit and sentiment and author:
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, author, sentiment, num_of_comments, float(tot_gilded)/num_of_comments, float(tot_score)/num_of_comments, tot_compound/num_of_comments, tot_neg/num_of_comments, tot_neu/num_of_comments, tot_pos/num_of_comments)
