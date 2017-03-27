#!/usr/bin/env python

import sys
from nltk.util import ngrams

# Input : subreddit, sentiment_class, gilded, score, body, compound, neg, neu, pos
# Output : subreddit, sentiment_class, sequence, count, gilded, score, compound, neg, neu, pos

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")

    sequence = row[4].split()
    for n in range(2,4):
        ngram = ngrams(sequence, n)
        for item in ngram:
            stri = ""
            for i in range(0, len(item)):
                stri += item[i]
                stri += " "
            stri = stri[:len(stri)-1]
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[0], row[1], stri, 1, row[2], row[3], row[5], row[6], row[7], row[8])
