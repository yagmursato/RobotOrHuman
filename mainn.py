import pandas
import numpy    as np
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

deneme = []
human = []
with open("human.txt","r") as f:
    for line in f:
        human.append(line)
        deneme.append(1)
bot = []
with open("robot.txt","r") as f:
    for line in f:
        bot.append(line)
        deneme.append(0)

data = {'text': human+bot,'status': deneme}
frame = pandas.DataFrame(data)
#print(frame)
#print(len(frame[frame.human==1]))

#print(frame.head())

frame_x=frame["text"]
frame_y=frame["status"]


vect = TfidfVectorizer(min_df=1)


x_train, x_test, y_train, y_test = train_test_split(frame_x,frame_y,test_size=0.2,random_state=4)

x_trainvect = vect.fit_transform(x_train)

vect1 = TfidfVectorizer(min_df=1)

x_trainvect=vect1.fit_transform(x_train)


mnb = MultinomialNB()

y_train=y_train.astype('int')
test = []
human_test = 0
robot_test = 0
mnb.fit(x_trainvect,y_train)

with open("test.txt","r") as f:
    for line in f:
        test.append(line)

for i in range(len(test)):
    x_testvect = vect1.transform([test[i]])
    pred = mnb.predict(x_testvect)
    if (pred[0]==1):
        human_test += 1
    else:
        robot_test += 1

if (human_test>robot_test):
    print("Bu hesap insana aittir.")
else:
    print("Bu hesap bot hesaptır.")


print(human_test)
print(robot_test)