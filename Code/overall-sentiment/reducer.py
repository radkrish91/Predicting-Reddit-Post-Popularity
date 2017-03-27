#!/usr/bin/env python

import sys

(last_key, num_of_comments, total_compound, total_neg, total_neu, total_pos) = (None, 0, 0.0, 0.0, 0.0, 0.0) 
for line in sys.stdin:
    (key, com, compound, neg, neu, pos) = line.strip().split(",") 
    if last_key and last_key != key:
        print "%s,%s,%s,%s,%s,%s" % (last_key, num_of_comments, total_compound, total_neg, total_neu, total_pos)
        (last_key, num_of_comments, total_compound, total_neg, total_neu, total_pos) = (key, int(com), float(compound), float(neg), float(neu), float(pos))
    else:
        (last_key, num_of_comments, total_compound, total_neg, total_neu, total_pos) = (key, num_of_comments+int(com), total_compound+float(compound), total_neg+float(neg), total_neu+float(neu), total_pos+float(pos))

if last_key:
    print "%s,%s,%s,%s,%s,%s" % (last_key, num_of_comments, total_compound, total_neg, total_neu, total_pos)
