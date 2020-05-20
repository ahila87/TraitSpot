'''
Created on Feb 22, 2020

@author: ahila
'''

import pandas as pd
from sqlalchemy import create_engine
file_path1='C:/univ/FinalProject/FinalDataSets/DataSet3_200Users.csv'
csv_database = create_engine('sqlite:///dataSet3_200Users-2.db')

chunksize = 400
i = 0
j = 1
for df in pd.read_csv(file_path1, chunksize=chunksize, iterator=True):
    
   # df = df.drop(df.columns[0],axis=1)
    df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
    df.index += j
    i+=1
    df.to_sql('table', csv_database, if_exists='append')
    j = df.index[-1] + 1