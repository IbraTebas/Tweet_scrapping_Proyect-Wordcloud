# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 23:00:59 2022

@author: Tebas
"""
import tweepy
import config
import pandas as pd
import twitter_api
import re
import string
import pandas as pd
import sklearn
from collections import Counter
from sklearn.feature_extraction import text 
from sklearn.feature_extraction.text import CountVectorizer
from unicodedata import normalize              

trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)

df = twitter_api.df

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('@[A-Za-z0-9]+', "", text)
    text = re.sub('#[A-Za-z0-9]+', "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub('\[.*?¿\]\%', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = normalize('NFKC', normalize('NFKD', text).translate(trans_tab))
    text = text.strip()
    return text

def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…«»]', '', text)
    text = re.sub('\n', ' ', text)
    return text

backup = df[:]
#Apply cleaning. 

round1 = lambda x: clean_text_round1(x)
round2 = lambda x: clean_text_round2(x)

df = pd.DataFrame(df.text.apply(round1)) 
df = pd.DataFrame(df.text.apply(round2))



# Add new stop words
with open('Spanish.txt') as f:
    stop_words = f.read().splitlines()


# Recreate document-term matrix
cv = CountVectorizer(stop_words=stop_words)
data_cv = cv.fit_transform(df.text)
bag_of_words = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
bag_of_words.index = df.index






 


 
