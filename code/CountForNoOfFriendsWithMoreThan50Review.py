'''
Created on Jan 27, 2020

@author: ahila
'''
import pandas as pd
file_path ='C:/Users/ahila/eclipse-workspace/TraitSpot/DataProcess/list2.csv'
df = pd.read_csv(file_path)
df['final_friend_count'] = df.apply(lambda x: x.count(), axis=1)
df['final_friend_count'] = df['final_friend_count'].subtract(4)
df.to_csv("list5.csv")
df1 = df[df['final_friend_count']> 100]
df1.to_csv("list6.csv")
print(df)
print(df1)