#!/usr/bin/env python

import sys

(last_key, num_of_links, num_of_comments, total_score, total_gild) = (None, 0, 0, 0.0, 0) 
for line in sys.stdin:
    (key, link, com, score, gild) = line.strip().split(" ") 
    if last_key and last_key != key:
        print "%s,%s,%s,%s,%s" % (last_key, num_of_links, num_of_comments, total_score, total_gild)
        (last_key, num_of_links, num_of_comments, total_score, total_gild) = (key, int(link), int(com), float(score), int(gild)) 
    else:
        (last_key, num_of_links, num_of_comments, total_score, total_gild) = (key, num_of_links+int(link), num_of_comments+int(com), total_score+float(score), total_gild+int(gild))

if last_key:
    print "%s,%s,%s,%s,%s" % (last_key, num_of_links, num_of_comments, total_score, total_gild)
