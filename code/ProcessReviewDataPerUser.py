'''
Created on Jan 3, 2020

@author: ahila
'''

import pandas as pd
import json
filename = 'C:/univ/yelp_dataset/review.json'

def mylines(filename, _from, _to):
    with open(filename, encoding="utf8") as f:
        for i, line in enumerate(f):
            if i >= _from and i <= _to:
                yield json.loads(line)

#df = pd.DataFrame([r for r in mylines(filename, 1, 1100000)])
#df1 = df['user_id'].value_counts().to_frame().reset_index().rename(columns={'index':'user_id', 'user_id':'count'})
#print(df)
#df.to_csv("review.csv")
#df1.to_csv("count1.csv")

#df = pd.DataFrame([r for r in mylines(filename, 1100001, 2200000)])
#df1 = df['user_id'].value_counts().to_frame().reset_index().rename(columns={'index':'user_id', 'user_id':'count'})
#df1.to_csv("count2.csv")

df = pd.DataFrame([r for r in mylines(filename, 5500001, 6600000)])
df1 = df['user_id'].value_counts().to_frame().reset_index().rename(columns={'index':'user_id', 'user_id':'count'})
df1.to_csv("count6.csv")




