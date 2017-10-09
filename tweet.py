import tweepy
from credentials2 import *
import json

def get_tweets():
    #Get the auth stuff in order
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # This function pulls some recent tweets from @codeuptown handle
    tweets = api.user_timeline(screen_name = 'codeuptown', include_rts= True, parser=tweepy.parsers.JSONParser())
    return tweets

#Does this work? Let's find out:
test = get_tweets()
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
