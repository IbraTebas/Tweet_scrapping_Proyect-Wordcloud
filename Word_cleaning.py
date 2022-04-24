# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:51:41 2022

@author: ibrah
"""
import pandas as pd
import re
import emoji
from Dataframe_column_to_string import *
import string
words = pd.read_csv('common words Spanish.csv')

############################# Cleaning common words and emojies ########################################################   

def clean_common_words(dictio, words):
    for i in list(dictio):
        for j in words["Words"]:
            if str(i).strip().lower() == str(j).strip().lower():
                dictio.pop(str(i).strip())
    return dictio

############emoji regex##########
emojis_iter = map(lambda y: y, emoji.UNICODE_EMOJI['en'].keys())
regex_set = re.compile('|'.join(re.escape(em) for em in emojis_iter))
##################################

def clean_emojies(dictio):
    for i in list(dictio.keys()):
        if [repr(str(i))] == regex_set.findall([i][0]):                 #needs work, is not eliminating emojis yet
            del dictio[i]
    return dictio

###################################### Word Counting ####################################################################
def count_sent(sentence):
    translate = sentence.maketrans({char: None for char in (string.punctuation + "¿""").replace("@","")})
    cleaned_words = sentence.lower().translate(translate).split()
    for i in cleaned_words:
        if i[len(i) - 1] in (string.punctuation + "¿" + '"'):
            i = i[:len(i)-1]
        elif i[0] in (string.punctuation + "¿" + '"'):
            i = i[1:]
        elif i.isdigit():
            cleaned_words.remove(i)
        
    word_counter = {}
    for word in cleaned_words:
        if word in word_counter:
            word_counter[word] += 1
        else:
                word_counter[word] = 1    
    return word_counter    

def frecuencia_palabras_columna(dataframe, column):
    dictio=count_sent(convert_column_to_string(dataframe[column]))
    return clean_common_words(dictio, words)