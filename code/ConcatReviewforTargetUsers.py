'''
Created on Jan 29, 2020

@author: ahila
'''
import pandas as pd
import json

file_path1='C:/univ/yelp_dataset/review.json'
file_path2='C:/univ/FinalProject/FinalDataSets/FriendsNotPartOfTargetUSers.csv'

df1 = pd.read_csv(file_path2)
def mylines(file_path1, _from, _to):
    with open(file_path1, encoding="utf8") as f:
        for i, line in enumerate(f):
            if i >= _from and i <= _to:
                yield json.loads(line)
                
df = pd.DataFrame([r for r in mylines(file_path1, 5500001, 6680000)])
#df2 = df.groupby("user_id")["text"].apply(','.join).reset_index()
list1 = df.groupby("user_id")["text"].apply(list).reset_index()
df2 = pd.DataFrame(list1) 
df3 = df2[df2['user_id'].isin(df1['user_id'])]

print(df3)
df3.to_csv('friendReview6')