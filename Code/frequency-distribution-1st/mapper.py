#!/usr/bin/env python

import sys
import string
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer

stop_words_english = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

# Input : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id, compound, neg, neu, pos, sentiment_class
# Output: subreddit, word, sentiment, count

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    subreddit = row[0]
    body = row[9]
    sentiment = row[16]

    tokenizer = TreebankWordTokenizer()
    word_tokens = tokenizer.tokenize(body.lower())
    
    filtered_words = [word for word in word_tokens if word not in stop_words_english]
    #print filtered_words
    for word in filtered_words:
        if word.isalnum() and not word.isdigit():
            print "%s,%s,%s,%s" % (subreddit, word, sentiment, 1)
