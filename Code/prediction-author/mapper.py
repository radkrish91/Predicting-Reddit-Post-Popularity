#!/usr/bin/env python

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

subreddit = "todayilearned"
author = "xvvvvx"
sentiment_class = 0
body = "whos stupid ass idea was this."
metrics = {}

## Sentiment
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(body)
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


# Input: subreddit, author, sentiment_class, num_of_comments, normalized_score
# Output: subreddit, author, sentiment_class, num_of_comments, normalized_score

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    if(subreddit == row[0] and author == row[1] and sentiment_class == int(row[2])):
        print "%s,%s,%s,%s,%s" % (row[0], row[1], row[2], row[3], row[4])
