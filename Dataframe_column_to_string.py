# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:55:33 2022

@author: ibrah
"""

import pandas as pd

############################# Cleaning common words and emojies ########################################################   

def convert_column_to_string(df_column):              #df_column like data["column name"]
    sentence = ""
    for i in df_column:
        sentence = sentence + " " + str(i)
    return(sentence)
#######################################################################################################