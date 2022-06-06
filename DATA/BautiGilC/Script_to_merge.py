# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:06:15 2022

@author: ibrah
"""

import pandas as pd
import glob
import os


files = os.path.join("./", "*.csv")
files = glob.glob(files)

df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df = df.iloc[: , 1:]
df = df.drop_duplicates()

