import csv
import tweepy
import d
consumer_key = d.consumer_key
consumer_secret = d.consumer_secret
access_token = d.access_token
access_token_secret = d.access_token_secret

bot = d.bot
human = d.human
giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)

for i in range(len(human)):
    twitler = api.user_timeline(screen_name = human[i], count=100)
    with open('deneme.csv', 'a') as f:
        writer = csv.writer(f)
        for i in range(100):
            writer.writerow([twitler[i].text,True])
