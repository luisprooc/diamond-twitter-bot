import tweepy

auth = tweepy.OAuthHandler(consumer_key=None, consumer_secret=None)
auth.set_access_token(access_token=None, access_token_secret=None)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)