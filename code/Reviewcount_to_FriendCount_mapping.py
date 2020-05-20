'''
Created on Jan 18, 2020

@author: ahila
'''
import pandas as pd
file_path1 ='C:/univ/FinalProject/review_count/userID_list_with_more_than_50_reviewcount.csv'

df1 = pd.read_csv(file_path1)

file_path2 ='C:/univ/FinalProject/Friends_Count/friend_Count_list.csv'

df2 = pd.read_csv(file_path2)

df3= pd.merge(df1,df2.rename(columns={'user_id':'user_id'})).rename(columns={'friendCount': 'friendCount'})
#df3 = df3[df3['friendCount' ]> 50]
print(df3)

#df3.to_csv("review_Count_to_friend_Count_list.csv")


