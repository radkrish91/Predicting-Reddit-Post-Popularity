#!/usr/bin/env python

import sys

(prev_subreddit, prev_word, prev_sentiment, prev_count) = (None, None, None, 0)
for line in sys.stdin:
    (subreddit, word, sentiment, count) = line.strip().split(",")
    if (prev_subreddit and prev_subreddit != subreddit) or (prev_sentiment and prev_sentiment != sentiment) or (prev_word and prev_word != word) :
        print "%s,%s,%s,%s" % (prev_subreddit, prev_word, prev_sentiment, prev_count)
        (prev_subreddit, prev_word, prev_sentiment, prev_count) = (subreddit, word, sentiment, int(count))
    else:
        (prev_subreddit, prev_word, prev_sentiment, prev_count) = (subreddit, word, sentiment, int(count)+int(prev_count))
        
if prev_subreddit and prev_sentiment and prev_word:
    print "%s,%s,%s,%s" % (prev_subreddit, prev_word, prev_sentiment, prev_count)
