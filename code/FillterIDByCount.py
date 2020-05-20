'''
Created on Nov 22, 2019

@author: ahila
'''


#   
import pandas as pd
# 
file_path ='C:/univ/FinalProject/Friends_Count/friend_Count_list.csv'
# 
df = pd.read_csv(file_path)
# df = data.groupby(['user_id']).sum()
# 
# 
# df = df.sort_values(by ='count', ascending=False )
df = df[df['count' ]> 50]
df.to_csv("friend_Count_list_with_more_than_50.csv")
#print(df)
