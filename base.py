import pymongo
import tweepy
import d
import psycopg2

connection = psycopg2.connect("dbname='robotorhuman_db' user='postgres' host='192.168.31.247' password='qazwsx'")

consumer_key = d.consumer_key
consumer_secret = d.consumer_secret
access_token = d.access_token
access_token_secret = d.access_token_secret

bot = d.bot
human = d.human
giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)
count = 0
human_file = open("human.txt", "a")
robot_file = open("robot.txt", "a")

with open("human.txt","r") as f:
    a = f.read()
    human_dizi = a.split()
    print(human_dizi)

connection = connection.cursor()
for i in range(len(human_dizi)):
    for j in range(len(human_dizi)):
        if i<j:
            if(human_dizi[i] == human_dizi[j]):
                human_dizi[j] = None
                count += 1
    if(human_dizi[i] is not None):
        human_dizi[i] = human_dizi[i].replace("'","")
        connection.execute("insert into human (word,count) VALUES ('{}', {}); COMMIT ;".format(human_dizi[i],count+1))
    count=0






