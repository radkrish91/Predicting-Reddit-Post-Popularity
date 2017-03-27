#!/usr/bin/env python

import sys
import string
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stop_words_english = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

subreddit = "todayilearned"
body = "whos stupid ass idea was this."
metrics = {}
sentiment_class = 0

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

## Stopwords
tokenizer = TreebankWordTokenizer()
word_tokens = tokenizer.tokenize(body.lower())
filtered_words = [word for word in word_tokens if word not in stop_words_english]
new_comment = ''
for word in filtered_words:
    new_comment += ''.join([i if i.isalpha() or ord(i)==32 else '' for i in word])+' '


# Generate ngrams
list_of_grams = []
sequence = new_comment.split()
for n in range(2,4):
    ngram = ngrams(sequence, n)
    for item in ngram:
        stri = ""
        for i in range(0, len(item)):
            stri += item[i]
            stri += " "
        stri = stri[:len(stri)-1]
        list_of_grams.append(stri)

# Input : subreddit, sentiment_class, sequence, count, gilded, score, compound, neg, neu, pos
# Output : sequence, count, gilded, score, compound
for line in sys.stdin:
    line = line.strip()
    row = line.split(",")

    if(row[0] == subreddit and sentiment_class == int(row[1])):
        if(row[2] in list_of_grams):
            print "%s,%s,%s,%s,%s,%s" % (row[2], row[3], row[1], row[4], row[5], row[6])
