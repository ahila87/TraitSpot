'''
Created on Jan 21, 2020

@author: ahila
'''
import pandas as pd
import numpy as np
from io import StringIO
import re

file_path1 ='C:/univ/FinalProject/review_count/user_reviewCount_frenCount_friends.csv'

df = pd.read_csv(file_path1)
df1 = df["friends"].str.split(", ", n = -1, expand = True) 
print(df1)

for index, row in df1.iterrows():

    for i in range(0,df.loc[index,'friendCount']): 
                    
            
        if not(df[df['user_id']==row.loc[i]].index.tolist()):
            df1.at[index, i] = np.nan           
             
    print(df1)    
  
df1.to_csv("friendsList3")



