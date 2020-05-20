'''
Created on Jan 25, 2020

@author: ahila

'''
import pandas as pd
  
c_size = 6500
file_path ='C:/univ/FinalProject/Friends_Count/finalList-FriendsWithMoreThan50Reviews.csv'
 
 #file_path ='C:/Users/ahila/eclipse-workspace/TraitSpot/DataProcess/friendsList2.csv'
 
 
for df_chunk in pd.read_csv(file_path,chunksize=c_size, sep=',', error_bad_lines=False, dtype='unicode'):
    types_dict = {'friendCount': int}
    for col, col_type in types_dict.items():
        df_chunk[col] = df_chunk[col].astype(col_type)
    df = df_chunk[df_chunk['friendCount']> 100]
   
    print(df_chunk.dtypes)
    df.to_csv("list2.csv") 
    

 

 
