'''
Created on Jan 27, 2020

@author: ahila
'''
import pandas as pd

file_path1='C:/univ/FinalProject/FinalDataSets/NoNANValues.csv'
file_path2='C:/univ/FinalProject/review_count/userList.csv'
df = pd.read_csv(file_path1,low_memory=False)
df1 = pd.read_csv(file_path2)
#df = df.fillna(0)
print(df.dtypes)

# 
# types_dict = {'friendCount': int.
# for col, col_type in types_dict.items():
#     df[col] = df[col].astype(col_type)
list = []
for index, row in df.iterrows():
    for i in range(5,((df.loc[index,'final_friend_count'])+5)): 
#         
        if (df.iloc[index, i]) not in df1.user_id.values:
            print(df.iloc[index, i])
            dictionary_data = df.iloc[index, i]
            list.append(dictionary_data)

df_final = pd.DataFrame.from_dict(list) 
df_final.to_csv('userList2')

     
            
          #  df1.loc[x] = df.iloc[index, i]
           # x=x+1
            #df1= df1.append({'user_id': df.iloc[index, i]}, ignore_index=True)
            
            
        #print(df1)
#df1 = DataFrame.from_dict(dict, "index")
#df1.to_csv('userList2')            
        

#        if not(pd.isnull(df[index, i])):
 #           df1['userlist'] =  df.at[index, i]   
#             
            
             
     
 