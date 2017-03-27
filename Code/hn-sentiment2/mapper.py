#!/usr/bin/env python

import sys

all_columns = ["domain","title_","url_","num_points","num_comments","author","created_at","neg","neu","pos","compound"]

req_columns = ["domain","title","url","num_points","num_comments","author","created_at", "neg","neu","pos","compound", "class"]

for line in sys.stdin:
    (domain,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound) = line.strip().split(",")
    if compound:
        sent_class = '0'
        if float(compound) >= -1 and float(compound) < -0.6:
                sent_class = '5'
        if float(compound) >= -0.6 and float(compound) < -0.25:
                sent_class = '4'
        if float(compound) >= -0.25 and float(compound) < 0.25:
                sent_class = '3'
        if float(compound) >= 0.25 and float(compound) < 0.6:
                sent_class = '2'
        if float(compound) >= 0.6 and float(compound) < 1.0:
                sent_class = '1'
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (domain,title_,url_,num_points,num_comments,author,created_at, neg, neu, pos, compound, sent_class)
