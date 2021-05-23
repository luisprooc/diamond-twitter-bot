from keys import auth_proccess
import tweepy

class Bot(object):

    def __init__(self):
        self.actions = {
            "a": "See Public Tweets",
            "b": "See my followers",
            "any": "Turn off bot"
        }

        self.api = tweepy.API(auth_proccess())

    def show_options(self)->str:
        print("**** BOT ACTIONS **** \n")

        for option in self.actions:
            print("Press {0} ▶▶ {1}".format(option, self.actions[option]))

        return input("\nWhat should do the bot? ")

    
    def see_public_tweets(self)->str:
        public_tweets = self.api.home_timeline()

        for tweet in public_tweets:
            print(tweet.text, end="\n")