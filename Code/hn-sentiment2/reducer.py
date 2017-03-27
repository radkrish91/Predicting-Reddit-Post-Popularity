#!/usr/bin/env python

import sys

for line in sys.stdin:
    (domain,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound,sent_class) = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (domain,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound,sent_class)
