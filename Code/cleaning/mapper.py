#!/usr/bin/env python

import sys

def remove_non_ascii(text):
        return ''.join([i if ord(i) < 128 else '' for i in text])

for line in sys.stdin:
        line = line.strip()
        row = line.split(",")
        id_ = row[0]
        title_ = row[1]
        url_ = row[2]
        num_points = row[3]
        num_comments = row[4]
        author = row[5]
        created_at = row[6]

        #id     title   url     num_points      num_comments    author  created_at
        if id_ and title_ and url_ and num_points and num_comments and author and created_at:
                print "%s,%s,%s,%s,%s,%s,%s" % (remove_non_ascii(id_), remove_non_ascii(title_), remove_non_ascii(url_), remove_non_ascii(num_points), remove_non_ascii(num_comments), remove_non_ascii(author), remove_non_ascii(created_at))
