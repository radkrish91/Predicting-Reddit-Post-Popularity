#!/usr/bin/env python

import sys

for line in sys.stdin:
    (id_,title_,url_,num_points,num_comments,author,created_at) = line.strip().split(",")
    print "%s,%s,%s,%s,%s,%s,%s" % (id_,title_,url_,num_points,num_comments,author,created_at)

