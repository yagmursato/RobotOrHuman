import pymongo
import tweepy
import database

import d
import psycopg2

db = database.db_add()
consumer_key = d.consumer_key
consumer_secret = d.consumer_secret
access_token = d.access_token
access_token_secret = d.access_token_secret

bot = d.bot
human = d.human
giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)
human_file = open("human.txt", "a")
robot_file = open("robot.txt", "a")

def readd(dosya):
    with open(dosya,"r") as f:
        a = f.read()
        dizi = a.split()
        return dizi
def db_insert_human():
    human_dizi=readd("human.txt")
    count = 0
    for i in range(len(human_dizi)):
        for j in range(len(human_dizi)):
            if i<j:
                if(human_dizi[i] == human_dizi[j]):
                    human_dizi[j] = None
                    count += 1
        if(human_dizi[i] is not None and human_dizi[i] is not " "):
            human_dizi[i] = human_dizi[i].replace("'","")
            db.insert_human(human_dizi[i],count+1)
        count=0

def db_insert_robot():
    dizi=readd("robot.txt")
    count = 0
    for i in range(len(dizi)):
        for j in range(len(dizi)):
            if i<j:
                if(dizi[i] == dizi[j]):
                    dizi[j] = None
                    count += 1
        if(dizi[i] is not None):
            dizi[i] = dizi[i].replace("'","")
            dizi[i] = dizi[i].replace('"', "")
            dizi[i] = dizi[i].replace('?', "")
            dizi[i] = dizi[i].replace('-', "")
            dizi[i] = dizi[i].replace(',', "")
            dizi[i] = dizi[i].replace('', "")
            db.insert_robot(dizi[i],count+1)
        count=0

deneme = ["selam","iyi","ki","misim"]

print(db.human_count("RT"))
print(db.robot_count("Scam"))





