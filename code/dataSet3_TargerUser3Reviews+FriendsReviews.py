'''
Created on Feb 19, 2020

@author: ahila
'''
import pandas as pd
import json
import numpy as np
import csv
import dask.dataframe as dd

file_path1='C:/univ/FinalProject/extra/FinalUserToFriendsListSorted.csv'
file_path2='C:/univ/FinalProject/extra/10ReviewPerFriend.csv'
file_path3='C:/univ/FinalProject/FinalDataSets/Dataset3.csv'
#file_path4='C:/univ/FinalProject/extra/TargetUsers.csv'
# column_dtypes = {'user_id': 'category',
#                  'combinedText': 'category'}
# df1 = pd.read_csv(file_path2, dtype = column_dtypes,nrows=6000)
#,skiprows=[i for i in range(1,51)]
df = pd.read_csv(file_path1,skiprows=[i for i in range(1,1002)],low_memory=False)
df1 = pd.read_csv(file_path2)
df2 = pd.read_csv(file_path3)
#df3 = pd.read_csv(file_path4)

# def mylines(file_path2, _from, _to):
#      with open(file_path2, encoding="utf8") as f:
#          for i, line in enumerate(f):
#              if i >= _from and i <= _to:
#                  yield csv.reader(line, delimiter=',')
#  
# df1 = pd.DataFrame([r for r in mylines(file_path2, 0, 6000)])
# df1.to_csv("sample")
# print(df1)



# for i in range(1, df.shape[1]):
#     grouped = df.groupby(df.columns[[i-1, i]].tolist())
#for chunk in pd.read_csv(filename, chunksize=chunksize):    
for index,row in df.iterrows():
   # print(index)
   # print(df.loc[index,'final_friend_count'])
    for i in range(3,((df.loc[index,'final_friend_count'])+3)):
      
       # print(i)              
        x = df.iloc[index, i]
        #print(x)
        if x in df1.user_id.values:
            y = df1.loc[df1['user_id'] == x, 'combinedText'].iloc[0]
          #  df2.loc[index+51,'allReviews']  =  str(df2.loc[index+51,'allReviews']) + y
            df2.loc[index+1001,'allReviews']  =  str(df2.loc[index+1001,'allReviews']) + y
            #print(df1.loc[df1['user_id'] == x, 'combinedText'].iloc[0])
         
    print(index+1001) 
                                                                                              
  #  if index+901 > 999:
   #     break  
#print(df2)    
     
#df2.to_csv("'sample' + str(i) + '.csv'")
df2.to_csv('dataSet3_Users_1001To1053.csv')             
             
 