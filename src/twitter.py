import json
import tweepy

with open('../config.json') as fd:
    config = json.load(fd)
consumer_key = config['CONSUMER_KEY']
consumer_secret = config['CONSUMER_SECRET']
access_token_key = config['ACCESS_TOKEN_KEY']
access_token_secret = config['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

def reduce_tweet(tweet):
    return {
        'text': tweet.full_text,
        'user': tweet.user.screen_name,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count
    }

def get_tweets(query, count=20):
    tweets = [reduce_tweet(tweet) for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(count)]
    return tweets
