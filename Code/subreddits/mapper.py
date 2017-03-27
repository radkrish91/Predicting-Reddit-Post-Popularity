#!/usr/bin/env python

import sys

all_columns = ["created_utc", "ups", "subreddit_id", "link_id", "name", "score_hidden", "author_flair_css_class", "author_flair_text", "subreddit", "id", "removal_reason", "gilded", "downs", "archived", "author", "score", "retrieved_on", "body", "distinguished", "edited", "controversiality", "parent_id"]

subreddits = ["AskReddit", "funny", "pics", "todayilearned", "gaming", "pcmasterrace", "news", "movies", "ShowerThoughts", "nba", "mildlyinteresting", "GlobalOffensive"]

i = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    if(row[0] != all_columns[0]):
        if(row[8] in subreddits):
            # Output : subreddit, created_utc, subreddit_id, link_id, name, id, gilded, author, score, body, controversiality, parent_id
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[8], row[0], row[2], row[3], row[4], row[9], row[11], row[14], row[15], row[17], row[20], row[21])
