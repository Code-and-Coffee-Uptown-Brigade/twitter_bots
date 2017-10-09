import tweepy
from credentials import *
import json

# OAuth to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Traverse the JSON returned by search query & favorite tweets by ID
for result in api.search('@codeuptown', 'en'):
    api.create_favorite(result.id)
