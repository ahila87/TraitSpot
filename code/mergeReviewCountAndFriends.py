'''
Created on Jan 18, 2020

@author: ahila
'''
import pandas as pd
import json

file_path1 ='C:/univ/FinalProject/review_count/review_Count_to_friend_Count_list.csv'

df = pd.read_csv(file_path1)

file_path2 ='C:/univ/yelp_dataset/user.json'


#print(df1)

 
def mylines(file_path2, _from, _to):
    with open(file_path2, encoding="utf8") as f:
        for i, line in enumerate(f):
            if i >= _from and i <= _to:
                yield json.loads(line)
 
df1 = pd.DataFrame([r for r in mylines(file_path2, 0, 200000)])
df1 = df1.drop(['name', 'review_count', 'yelping_since','useful','funny','cool','elite','fans','average_stars','compliment_hot','compliment_more','compliment_profile','compliment_cute','compliment_list','compliment_note','compliment_plain','compliment_cool','compliment_funny','compliment_writer','compliment_photos'], axis=1)
#print(df1)

df2 = pd.DataFrame([r for r in mylines(file_path2, 200001, 600000)])
df2 = df2.drop(['name', 'review_count', 'yelping_since','useful','funny','cool','elite','fans','average_stars','compliment_hot','compliment_more','compliment_profile','compliment_cute','compliment_list','compliment_note','compliment_plain','compliment_cool','compliment_funny','compliment_writer','compliment_photos'], axis=1)
#print(df2)

df1 = pd.concat([df1,df2])
#df1.to_csv("friends.csv")


# df3 = df.assign(InDf2=df.user_id.isin(df2.user_id).astype(int))
# print(df3)
# df3.to_csv("Indf2.csv")

df3 = (df[['user_id']].merge(df1, on='user_id', how='left')
                 .rename(columns={'user_id':'user_id','friends':'friends'}))
df3.to_csv("user_reviewCount_frenCount_friends.csv")
    
