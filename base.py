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
robot_file = open("robot.txt", "w")

for i in range(len(bot)):
    twitler = api.user_timeline(screen_name = bot[i], count=100)
    for j in range(len(twitler)):
        robot_file.write(twitler[j].text+"\n")