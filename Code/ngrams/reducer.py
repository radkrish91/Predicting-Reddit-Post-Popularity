#!/usr/bin/env python

import sys

(subreddit, sentiment, sequence, tot_count, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (None, None, None, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)

for line in sys.stdin:
    (subr, senti, seq, count, gild, score, comp, neg, neu, pos) = line.strip().split(",")
    if (subreddit and subreddit != subr) or (sentiment and sentiment != senti) or (sequence and sequence != seq):
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, sentiment, sequence, tot_count, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos)
        (subreddit, sentiment, sequence, tot_count, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (subr, senti, seq, int(count), int(gild), int(score), float(comp), float(neg), float(neu), float(pos))
    else:
        (subreddit, sentiment, sequence, tot_count, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos) = (subr, senti, seq, tot_count+int(count), tot_gilded+int(gild), tot_score+int(score), tot_compound+float(comp), tot_neg+float(neg), tot_neu+float(neu), tot_pos+float(pos))

if subreddit and sentiment and sequence:
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (subreddit, sentiment, sequence, tot_count, tot_gilded, tot_score, tot_compound, tot_neg, tot_neu, tot_pos)
