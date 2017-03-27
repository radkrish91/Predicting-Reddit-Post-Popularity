#!/usr/bin/env python

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from urlparse import urlparse

all_columns = ["id","title","url","num_points","num_comments","author","created_at"]

req_columns = ["id","title","url","num_points","num_comments","author","created_at", "sentiment", "subreddit"]

sid = SentimentIntensityAnalyzer()

for line in sys.stdin:
    #(id_,title_,url_,num_points,num_comments,author,created_at) = line.strip().split(",")
    (id_,title_,url_,num_points,num_comments,author,created_at) = line.strip().split(",")
    # Output : link_id, subreddit, num_of_comments, score, gil
    if url_ and title_ and urlparse(url_).hostname:
        domain = urlparse(url_).hostname.lower()
        ss = sid.polarity_scores(title_)
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (domain,title_,url_,num_points,num_comments,author,created_at, str(ss['neg']), str(ss['neu']), str(ss['pos']), str(ss['compound']))
