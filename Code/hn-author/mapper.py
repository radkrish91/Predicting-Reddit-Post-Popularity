#!/usr/bin/env python

import sys

all_columns = ["domain","title_","url_","num_points","num_comments","author","created_at","neg","neu","pos","compound","class"]

req_columns = ["domain","title","url","num_points","num_comments","author","created_at", "neg","neu","pos","compound", "class"]

for line in sys.stdin:
    (domain,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound,sent_class) = line.strip().split(",")
    if domain:
        domain = domain.strip()
        if domain == "medium.com" or domain == "github.com" or domain == "www.nytimes.com" or domain == "www.youtube.com" or domain == "techcrunch.com" or domain == "www.theguardian.com" or domain == "arstechnica.com" or domain == "www.bloomberg.com" or domain == "en.wikipedia.org" or domain == "www.bbc.com":
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (domain,sent_class,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound)
