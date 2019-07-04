#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:41:45 2019

@author: jarnail
"""
##Prerequisites >> pip install Twython (in terminal)


#TRUDEAU

from twython import Twython  
import json
from textblob import TextBlob

# Load credentials from json file (You will need to create an app in https://developer.twitter.com/ to get access tokens to connect with Twitter API)

with open("/Users/jarnail/.spyder-py3/Creds.json", "r") as file:  
    creds = json.load(file)

python_tweets = Twython(creds['consumer_key'], creds['consumer_secret'])

# Apiquery to get top 10 tweets
query = {'q': 'Trudeau',  # OR 'q': 'Trump'
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        'tweet_mode':'extended'
        }


import pandas as pd

# Searching tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['full_text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Sorting data
df = pd.DataFrame(dict_)  
df.sort_values(by='favorite_count', inplace=True, ascending=False)  
df.head(5) 

#output printed results to a .txt 
import sys

orig_stdout = sys.stdout
f = open('/Users/jarnail/.spyder-py3/tweetsAPI-Trudeau.txt', 'w')
sys.stdout = f


for a in range (0,10):
    m = str (a)
    ##print(df['text'][a])   >> no need to print the tweets. Only need to output sentiment (That is the polarity and subjectivity value of the tweets)
    analysis = TextBlob(df['text'][a])
    print (analysis.sentiment.polarity,',',analysis.sentiment.subjectivity) 

sys.stdout = orig_stdout
f.close()


#Trudeau Graph

import matplotlib.pyplot as plt
import numpy as np


x1, y1 = np.loadtxt('/Users/jarnail/.spyder-py3/tweetsAPI-Trudeau.txt', delimiter=',', unpack=True)
plt.plot(x1,y1, label='Top 10 Tweets')

plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('#Trudeau')
plt.legend()
plt.show()




#TRUMP

from twython import Twython  
import json
from textblob import TextBlob

# Load credentials from json file
with open("/Users/jarnail/.spyder-py3/Creds.json", "r") as file:  
    creds = json.load(file)

python_tweets = Twython(creds['consumer_key'], creds['consumer_secret'])

# Apiquery to get top 10 tweets
query = {'q': 'Trump',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        'tweet_mode':'extended'
        }


import pandas as pd

# Searching tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['full_text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Sorting data
df = pd.DataFrame(dict_)  
df.sort_values(by='favorite_count', inplace=True, ascending=False)  
df.head(5) 

#output printed results to a .txt 
import sys

orig_stdout = sys.stdout
f = open('/Users/jarnail/.spyder-py3/tweetsAPI-Trump.txt', 'w')
sys.stdout = f


for a in range (0,10):
    m = str (a)
    ##print(df['text'][a])   >> only need to output sentiment (That is the polarity and subjectivity value of the tweets)
    analysis = TextBlob(df['text'][a])
    print (analysis.sentiment.polarity,',',analysis.sentiment.subjectivity) 

sys.stdout = orig_stdout
f.close()

#Trump Graph
x2, y2 = np.loadtxt('/Users/jarnail/.spyder-py3/tweetsAPI-Trump.txt', delimiter=',', unpack=True)
plt.plot(x2,y2, label='Top 10 Tweets')

plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('#Trump')
plt.legend()
plt.show()


#Trudeau VS Trump

plt.plot(x1,y1, label='#Trudeau',color='green')
plt.plot(x1, y1,'ko', markersize=7,color='green')
plt.plot(x2, y2, 'ko', markersize=7,color='red')
plt.plot(x2, y2, label='#trump',color='red')
plt.legend()



#References:
##https://developer.twitter.com/en/use-cases/analyze.html
#https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
#https://www.youtube.com/watch?v=o_OZdbCzHUA
