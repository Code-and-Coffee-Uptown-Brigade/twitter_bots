import tweepy
from credentials import *
import json
import csv
import os

# OAuth to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Traverse the JSON returned by search query & favorite tweets by ID
buffer = []
new_buffer = []

def find_ids():
    with open("ids.csv") as ids_db:
        content = [line.rstrip() for line in ids_db] # Strip whitespace from end of Tweet ID
    for new_id in content:
        new_buffer.append(new_id)

for result in api.search('@codeuptown', 'en', 20):
    buffer.append(result.id)

# Find IDs if file exists and not empty.
if os.path.exists(ids) and os.stat(ids).st_size > 0:
    find_ids()
else
    new_buffer = buffer

if new_buffer:
    ids_db = open(ids, 'w')
    for new_id in new_buffer:
        api.create_favorite(new_id)
        # Append new_id to IDs file.
        ids.db.write("%s\n" % new_id)
    # close after writing
    ids_db.close()



    # for item in buffer:
    #     wr.writerow(int(buffer))


    #api.create_favorite(result.id)
