'''
Created on Jan 17, 2020

@author: ahila
'''
import pandas as pd

file_path ='C:/univ/FinalProject/Friends_Count/combined_friends_csv.csv'

df = pd.read_csv(file_path)

df = df.sort_values(by ='count', ascending=False )

df['index'] = range(1, len(df) + 1)

print(df)
#df = df[df['count' ]> 50]

df.to_csv("friend_Count_list.csv")