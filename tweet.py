import tweepy
from credentials import *
import json
import csv

# OAuth to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Create empty list "buffer"
buffer = []

# Traverse the JSON returned by search query & favorite tweets by ID
for result in api.search('@codeuptown', 'en'):
    buffer.append(result.id)

print(buffer)

with open('ids.csv', 'wb') as myfile:
    writer = csv.writer(myfile)
    writer.writerows(buffer)


    # for item in buffer:
    #     wr.writerow(int(buffer))


    #api.create_favorite(result.id)
