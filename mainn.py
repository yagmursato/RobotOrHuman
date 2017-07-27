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


vect = TfidfVectorizer(min_df=1, stop_words='english')


x_train, x_test, y_train, y_test = train_test_split(frame_x,frame_y,test_size=0.2,random_state=4)

x_trainvect = vect.fit_transform(["iyi ki geldin misim","zsdvb"])



x_trainvect.toarray()

vect.get_feature_names()

vect1 = TfidfVectorizer(min_df=1, stop_words='english')

x_trainvect=vect1.fit_transform(x_train)
a = x_trainvect.toarray()
vect1.inverse_transform(a[0])
print(x_train.iloc[0])

mnb = MultinomialNB()

y_train=y_train.astype('int')

print(mnb.fit(x_trainvect,y_train))

x_testvect = vect1.transform(["tüm türkiyeyi dolaşmış gibi hissediyorum ama asla çorluya gidemiyorum bilet fiyatları 25 olmuş"])
pred = mnb.predict(x_testvect)

print(pred)
actual =  np.array(y_test)
count=0
for i in range(len(pred)):
    if pred[i]==actual[i]:
        count=count+1

print(count)



"""vect.fit(data)
x = vect.transform(data["text"])
features = vect.get_feature_names()
datas = pandas.DataFrame(x.toarray(),columns=vect.get_feature_names())
print(datas["text"])
"""

