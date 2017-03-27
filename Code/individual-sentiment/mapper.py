#!/usr/bin/env python

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

for line in sys.stdin:
    metrics = {}
    line = line.strip()
    row = line.split(",")
    # Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id
    # Output : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id, compound, neg, neu, pos, sentiment_class
    ss = sid.polarity_scores(row[9])
    for k in sorted(ss):
        metrics[k] = ss[k]
    
    # Sentiment Class : {1: 'HP', 2: 'MP', 3: 'N', 4: 'MN', 5: 'HN'}
    if(metrics['compound'] > 0.6): 
        sentiment_class = 1
    elif(metrics['compound'] > 0.25):
        sentiment_class = 2
    elif(metrics['compound'] > -0.25):
        sentiment_class = 3
    elif(metrics['compound'] > -0.6):
        sentiment_class = 4
    else:
        sentiment_class = 5
    
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], metrics['compound'], metrics['neg'], metrics['neu'], metrics['pos'], sentiment_class)
