import pandas as pd
from polyglot.text import Text
from polyglot.detect import Detector

df = pd.read_csv("data_tweets.csv")
polarity = []
sentiment = []

num = 0
for tweet in df['tweets']:
    
    react = "neutral"

    an = Text(tweet)
    polarity.append(an.polarity)

    if an.polarity > 0.0:
        react = "positive"

    elif an.polarity < 0.0:
        react = "negative"

    sentiment.append(react)

    print(tweet+" (polarity : "+str(an.polarity)+"\n")

df["polarity"] = polarity
df["sentiment"] = sentiment

df.to_csv('sentiments_data.csv')