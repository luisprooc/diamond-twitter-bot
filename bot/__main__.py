import tweepy
from keys import auth_proccess


auth = auth_proccess()


api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)