import pandas as pd
from polyglot.text import Text
from polyglot.detect import Detector

df = pd.read_csv("data_tweets.csv")
polarity = []
sentiment = []

positive_words={}
negative_words={}

for tweet in df['tweets']:
    
    sentences = tweet.split(" ")

    for word in sentences:
        an = Text(word)

        try:
            if an.polarity > 0.0:
                if word not in positive_words.keys():
                    positive_words[word]=1
                else:
                    positive_words[word]+=1

            elif an.polarity < 0.0:
                if word not in negative_words.keys():
                    negative_words[word]=1
                else:
                    negative_words[word]+=1

            print(word+" (polarity : "+str(an.polarity)+")\n")
        except:
            print("Ada kesalahan\n")

p=open("positive.txt", 'w+')
n=open("negative.txt", 'w+')

for key, value in positive_words.items():
    p.write(key+" "+str(value)+"\n")

for key, value in negative_words.items():
    n.write(str(value)+" "+key+"\n")

p.close()
n.close()