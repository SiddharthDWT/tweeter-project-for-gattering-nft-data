from itertools import count
import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'RumbleKongs'
limit=20000

tweets = tweepy.Cursor(api.user_timeline ,screen_name=user, count=200 ,tweet_mode='extended' ).items(limit)
# retweets=tweepy.Cursor(api.get_retweeter_ids, id=user, count=200)


# create DataFrame
columns = ['Time','User', 'Tweet' ] #,'Retweet'
data = []
retweet1=[]
# for i in retweets:
#     retweet1.append([i.id,i.count])


for tweet in tweets:
    data.append([tweet.created_at,tweet.user.screen_name, tweet.full_text])
print(retweet1)
df = pd.DataFrame(data, columns=columns)
df.to_csv('RumbleKongs.csv')
print(df)