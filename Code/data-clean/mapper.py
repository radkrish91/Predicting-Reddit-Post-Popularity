#!/usr/bin/env python

import sys
import json
import hashlib
import itertools

all_columns = ["created_utc", "ups", "subreddit_id", "link_id", "name", "score_hidden", "author_flair_css_class", "author_flair_text", "subreddit", "id", "removal_reason", "gilded", "downs", "archived", "author", "score", "retrieved_on", "body", "distinguished", "edited", "controversiality", "parent_id"]

req_columns = ["created_utc", "ups", "subreddit_id", "link_id", "name", "score_hidden", "subreddit", "id", "removal_reason", "gilded", "downs", "author", "score", "retrieved_on", "body", "controversiality", "parent_id"]


i = 0
for line in sys.stdin:
    
    line = line.strip()
    row = line.split(",")
    all_data = dict(itertools.izip(all_columns, row))
    req_data = {}

    for key, value in all_data.iteritems():
        if key in req_columns:
            req_data[key] = value

    row_id = hashlib.sha1(
        req_data["created_utc"]+req_data["link_id"]+req_data["author"]
        ).hexdigest()
    
    req_data["comment_id"] = row_id
    i += 1

    print "%s %s" % (str(i), json.dumps(req_data))
