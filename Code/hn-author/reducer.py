#!/usr/bin/env python

import sys

for line in sys.stdin:
    (domain,sent_class,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound) = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (domain,sent_class,title_,url_,num_points,num_comments,author,created_at,neg,neu,pos,compound)
