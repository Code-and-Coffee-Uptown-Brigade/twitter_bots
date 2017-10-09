import tweepy
from credentials2 import *
import json

def get_tweets():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
