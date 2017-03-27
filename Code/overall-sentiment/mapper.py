#!/usr/bin/env python

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
Citation:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

sid = SentimentIntensityAnalyzer()

for line in sys.stdin:
    metrics = {}
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id
    # Output : subreddit, num_of_comments, compound, neg, neu, pos
    ss = sid.polarity_scores(row[9])
    for k in sorted(ss):
        metrics[k] = str(ss[k]) 

    print "%s,%s,%s,%s,%s,%s" % (row[0], 1, metrics['compound'], metrics['neg'], metrics['neu'], metrics['pos'])
