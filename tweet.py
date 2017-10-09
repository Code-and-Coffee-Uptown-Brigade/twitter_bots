import tweepy
from credentials import *
import json

def account_get_tweets():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # This function pulls some recent tweets from @codeuptown handle
    tweets = api.user_timeline(screen_name = 'codeuptown', include_rts= True, parser=tweepy.parsers.JSONParser())
    return tweets

def mentions():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    retweets = api.search('@codeuptown', 'en')
    return retweets

def favorite():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    favorite = api.create_favorite('917402990646046721')
    return favorite

#Does this work? Let's find out:
test = favorite()
print(test)

# def text_finder():
#     text = str(get_tweets())
#     data = json.loads(text)
#     return data
#
# test = text_finder()
# print(test)

    # trimmed_tweets = tweet_cache.cache_and_trim('tweet_ids.csv', tweets)
#
#     return trimmed_tweets
#
# print(trimmed_tweets)
