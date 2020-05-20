'''
Created on Feb 22, 2020

@author: ahila
'''
'''
Created on Feb 9, 2020

@author: ahila
'''

import pandas as pd
import json
import numpy as np


file_path1='C:/univ/FinalProject/working data/review.json'
file_path2='C:/univ/FinalProject/extra/10ReviewPerFriend.csv'

df1 = pd.read_csv(file_path2)
def mylines(file_path1, _from, _to):
    with open(file_path1, encoding="utf8") as f:
        for i, line in enumerate(f):
            if i >= _from and i <= _to:
                yield json.loads(line)
                
df = pd.DataFrame([r for r in mylines(file_path1, 0, 1100000)])
#df = df.drop(['review_id','business_id','stars','useful','funny','cool','date'], axis=1)
    #df2 = df.groupby("user_id")["text"].apply(','.join).reset_index()
df2 = df[["user_id","text"]]
df3 = df2[df2['user_id'].isin(df1['user_id'])]


#df3 = data.groupby("user_id")["text"].head(3).reset_index()
#list1 = df3.groupby("user_id")["text"].apply(list).reset_index()
#data = pd.DataFrame(list1) 
#data = df3.groupby(['user_id'],as_index=False).agg(lambda x :','.join(x) )
#agg(lambda x : x.sum() if x.dtype=='float64' else ' '.join(x))
#data = df3.groupby('user_id').text.apply(lambda x:sorted(x.values,key=len)).reset_index()
data = df3.groupby('user_id').text.apply(lambda x: np.sort(x.values)[:-6:-1]).reset_index()

print(data)
    

data.to_csv('5Reviews')
