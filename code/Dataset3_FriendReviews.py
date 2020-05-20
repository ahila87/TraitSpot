'''
Created on Jan 29, 2020

@author: ahila
'''
import pandas as pd
import json


filename='C:/univ/FinalProject/DataSet3/dataSet3_Users_1001To1053.csv'
# 
# chunksize = 3000
# for chunk in pd.read_csv(filename, chunksize=chunksize):
#     print(chunk)
#,skiprows=[i for i in range(1,5001)]
df = pd.read_csv(filename)
#df = df[:1001]
df = df.tail(53)
print(df)
df['combinedText'] = df[['3Reviews', 'allReviews']].apply(lambda x: ''.join(x), axis=1)
df = df.drop(['3Reviews', 'allReviews'], axis=1)
print(df)

df.to_csv('C:/univ/FinalProject/DataSet3_2/dataSet3_Users_1001To1053_2')    