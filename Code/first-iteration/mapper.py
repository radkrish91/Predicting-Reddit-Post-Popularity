#!/usr/bin/env python

import sys

all_columns = ["created_utc", "ups", "subreddit_id", "link_id", "name", "score_hidden", "author_flair_css_class", "author_flair_text", "subreddit", "id", "removal_reason", "gilded", "downs", "archived", "author", "score", "retrieved_on", "body", "distinguished", "edited", "controversiality", "parent_id"]

req_columns = ["created_utc", "ups", "subreddit_id", "link_id", "name", "score_hidden", "subreddit", "id", "removal_reason", "gilded", "downs", "author", "score", "retrieved_on", "body", "controversiality", "parent_id"]

i = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    if(row[0] != all_columns[0]):
        # Output : link_id, subreddit, num_of_comments, score, gild
        print "%s %s %s %s %s" % (row[3], row[8], 1, row[15], row[11])
