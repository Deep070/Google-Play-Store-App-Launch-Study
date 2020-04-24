# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:42:31 2019

@author: Jaynil Gaglani
"""
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import numpy as np
import statistics  
import warnings 
warnings.filterwarnings('ignore')
df = pd.read_excel('C:\\Users\\Deep\Desktop\\dataset1.xlsx',header=0)
df['Rating'] = df['Rating'].astype(float)
free = df[df['Type']=='Free']
d = free[['Rating','Installs']]
frees = {}

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result
d = normalize(d)

for i in range(len(d)):
    frees[free['App'].iloc[i]] = statistics.mean(d.iloc[i,:])
Maxfree = sorted(frees, key=frees.get, reverse=True)[:5]
#print(Maxfree)
paid = df[df['Type']=='Paid']
d1 = paid[['Rating','Installs']]
paids = {}
d1 = normalize(d1)
for i in range(len(d1)):
    paids[paid['App'].iloc[i]] = statistics.mean(d1.iloc[i,:])
Maxpaid = sorted(paids, key=paids.get, reverse=True)[:5]

review_df = pd.read_excel('C:\\Users\\Deep\\Desktop\\user.xlsx',header=0)
df2 = review_df.groupby('App')['Sentiment_Polarity','Sentiment_Subjectivity'].mean()
d3 = df2[['Sentiment_Polarity','Sentiment_Polarity']]
trends = {}
for i in range(len(d3)):
    trends[df2.index[i]] = statistics.mean(d3.iloc[i,:])
Trending = sorted(trends, key=trends.get, reverse=True)[:5]
#print(Trending)