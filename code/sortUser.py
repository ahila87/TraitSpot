'''
Created on Jan 15, 2020

@author: ahila
'''


import pandas as pd
import json
filename = 'C:/univ/yelp_dataset/user.json'

def mylines(filename, _from, _to):
    with open(filename, encoding="utf8") as f:
        for i, line in enumerate(f):
            if i >= _from and i <= _to:
                yield json.loads(line)

df = pd.DataFrame([r for r in mylines(filename, 1400001, 1637138)])
df1 = df.friends.str.strip().str.split(',').apply(len).to_frame().reset_index().rename(columns={'friends':'count'})
df1 = pd.concat([df['user_id'], df1['count']],axis=1)
print(df1)
df1.to_csv("friendsCount8.csv")


